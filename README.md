# 🤖💱 AI-Powered Currency Converter Chatbot

This is a simple **Currency Converter Chatbot** built to demonstrate how AI tools (like local LLMs via Ollama) can be integrated with external APIs to understand and respond to natural language queries like:

> 💬 "Convert 100 INR to USD"  
> 💬 "What is 75 EUR in JPY?"

---

## 🎯 Project Goal

The goal of this project is to learn how to use LLMs to interpret human language, extract useful data (amounts and currencies), and integrate that with a real-world service (ExchangeRate API) to get meaningful results.

---

## 🔧 Tech stack

- **Ollama** — To run a local Large Language Model (like LLaMA 3)
- **LLM (LLaMA 3.2)** — To extract structured data (amount, from_currency, to_currency) from human input
- **ExchangeRate-API** — To fetch real-time exchange rates
- **Streaming Response** — Simulate a natural chat experience using LLM streaming responses

---

## 🚀 Features

- Understands queries like “How much is 100 INR in USD?”
- Uses LLM to extract structured info from user input
- Fetches real-time currency exchange data
- Streams AI responses like a real-time chatbot
- Clean environment-variable-based config for API keys

---

## 🧱 Prerequisites

Make sure you have:

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running (model: `llama3.2`)
- A free account + API key from [ExchangeRate-API](https://www.exchangerate-api.com/)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/abipriya-rajendran/ai-tools.git
cd currency-converter
```

### 2. Install Required Python Packages
```bash
pip install requests python-dotenv
```

### 3. Configure Environment Variables
Create a .env file in the project root:
```bash
touch .env
```
Add the key
```bash
EXCHANGE_RATE_API_KEY=your_api_key_here
```
🔒 Important: Make sure .env is added to your .gitignore to avoid accidentally pushing it to GitHub.

### 4. Run Ollama (LLM) Locally
```bash
ollama run llama3.2
```

### 5. Run the Chatbot
```bash
python3 currencyconverter.py
```

### 6. Result
<img width="1314" alt="image" src="https://github.com/user-attachments/assets/690e0e84-fb61-42ee-8340-a5dcb1ce3833" />


## 📚 Learnings from this Project
How to use LLMs to extract structured info from free-form text

How to integrate LLMs with real-world tools (like currency APIs)

How to work with streamed responses from a local AI model

Best practices for secure API key handling
