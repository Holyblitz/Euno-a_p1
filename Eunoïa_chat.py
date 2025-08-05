import os
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
import subprocess

# Chargement des vecteurs
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="./chroma_index", embedding_function=embedding_model)

# Historique de la session (mémoire temporaire)
historique = []

print("🧠 Eunoïa est prête. Pose-lui tes questions (ou tape 'exit' pour quitter).\n")

while True:
    question = input("💬 Toi : ")

    if question.strip().lower() in ["exit", "quit"]:
        print("👋 À bientôt !")
        break

    # Recherche vectorielle
    docs = db.similarity_search(question, k=3)
    contexte = "\n\n".join([doc.page_content for doc in docs])

    # Historique formaté
    historique_formate = "\n".join(historique[-3:])  # limite à 3 derniers tours

    # Construction du prompt
    prompt = f"""
Tu es Eunoïa, une intelligence artificielle douce et compétente spécialisée dans Linux.

Voici le contexte extrait de ta base de connaissances :
{contexte}

---

Voici les derniers échanges :
{historique_formate}

---

Réponds maintenant à la question suivante :
{question}
"""

    # Appel à Gemma 3 via Ollama
    print("🤖 Eunoïa : ", end="", flush=True)
    process = subprocess.Popen(["ollama", "run", "gemma3"], stdin=subprocess.PIPE, text=True)
    process.communicate(prompt)

    # Ajout à l'historique
    historique.append(f"Toi : {question}")
    historique.append(f"Eunoïa : [réponse générée]")

