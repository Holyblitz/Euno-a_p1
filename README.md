# Euno-a_p1

# 🧠 Eunoïa - Assistante IA Linux locale (Gemma 3B)

Eunoïa est une IA locale, douce et compétente, spécialisée dans l'apprentissage de Linux. Elle fonctionne en local avec un LLM (Gemma 3B via Ollama), et dispose d'une mémoire vectorielle pour intégrer des connaissances personnalisées (guides, notes, scripts...).

## ✨ Fonctionnalités

- Réponses pédagogiques en français sur Linux
- Intégration de documents personnalisés avec vectorisation (ChromaDB + LangChain)
- Interface terminal (chat)
- Scrapers intégrés pour tldr & manpages
- Vectorisation automatique des connaissances utiles (guides, .md...)

## 🧰 Technologies

- Python
- Ollama + Gemma 3B
- LangChain
- ChromaDB
- Linux (Debian)
- [Tkinter (abandonné)]

## ▶️ Lancer Eunoïa

```bash
ollama run gemma3
python3 eunoia_chat.py
