
import os
import json
from pathlib import Path
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 📁 Chemin vers le dossier contenant les fichiers à vectoriser
data_folder = "../data"

# 📦 Modèle d'embeddings local
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 📚 Fonction de chargement de documents
def charger_documents():
    documents = []

    for filename in os.listdir(data_folder):
        path = os.path.join(data_folder, filename)

        if filename.endswith(".md"):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                documents.append(Document(page_content=content, metadata={"source": filename}))

        elif filename.endswith(".json"):
            with open(path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        for item in data:
                            text = json.dumps(item, ensure_ascii=False, indent=2)
                            documents.append(Document(page_content=text, metadata={"source": filename}))
                except Exception as e:
                    print(f"Erreur de lecture {filename} : {e}")

    return documents

# 🔍 Découpe des documents pour vectorisation
def splitter(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(documents)

# 🧠 Construction de l'index vectoriel
def construire_index():
    print("[🔍] Chargement des documents...")
    docs = charger_documents()
    print(f"[✔] {len(docs)} documents chargés.")

    print("[✂️] Découpage des documents...")
    chunks = splitter(docs)
    print(f"[✔] {len(chunks)} morceaux prêts à être vectorisés.")

    print("[📦] Création de l'index vectoriel local (Chroma)...")
    vectordb = Chroma.from_documents(chunks, embedding_model, persist_directory="./chroma_index")
    vectordb.persist()

    print("[✅] Index construit et sauvegardé dans ./chroma_index")

if __name__ == "__main__":
    construire_index()
