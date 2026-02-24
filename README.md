# Azure OpenAI Autogen Assistant

# Setup Guide

## Prerequisites

- Python 3.10+
- Azure OpenAI deployed model

---

## 1. Configure Azure OpenAI

Ensure you have:

- Azure OpenAI Resource
- Model deployment (e.g., `gpt-4.1`)
- Endpoint URL
- API Key
- API Version

---

## 2. Clone Repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

## 3. Create Virtual Environment 

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

## 4. Install Dependencies 

```bash
pip install -r requirements.txt
```

## 5. Create .env file 

Create .env file in the project root: 
```bash
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_KEY=
AZURE_OPENAI_API_VERSION=
AZURE_OPENAI_CHAT_DEPLOYMENT=
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=
```

## 6. Run the agent 

```bash
python main.py 
```
