import json
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

def parse_user_input(user_input):
    prompt = f"""
Extract the amount, from currency, and to currency from this sentence:
"{user_input}"

Return it as JSON with keys: amount, from_currency, to_currency.
Use 3-letter ISO currency codes like USD, INR, EUR.
The response should only contain the json and nothing else.
"""
    try:
        response = requests.post("http://localhost:11434/api/chat", json={
            "model": "llama3.2",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "stream": False
        })

        data = response.json()

        reply = data.get("message", {}).get("content", "")
        parsed = json.loads(reply.strip())

        return float(parsed['amount']), parsed['from_currency'], parsed['to_currency']

    except Exception as e:
        print("⚠️ Error parsing with LLM:", e)
        return None, None, None

def ask_ollama(prompt):
    response = requests.post("http://localhost:11434/api/chat", json={
        "model": "llama3.2",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": True
    })
    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            content = data.get("message", {}).get("content", "")
            if content:
                print(content, end="", flush=True)
                time.sleep(0.05)

    print()

def get_conversion_rate(from_currency, to_currency, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    res = requests.get(url).json()
    return res['conversion_rates'].get(to_currency)

def run_bot():
    print("💬 Currency Converter Bot (type 'exit' to quit)")
    
    exchange_rate_api_key = os.getenv("EXCHANGE_RATE_API_KEY")
    if not exchange_rate_api_key:
        raise ValueError("⚠️ Missing EXCHANGE_RATE_API_KEY in environment variables.")

    while True:
        user_input = input("\n🧑 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Bye!")
            break

        amount, from_curr, to_curr = parse_user_input(user_input)
        if not all([amount, from_curr, to_curr]):
            print("❌ Sorry, I couldn't understand. Try something like 'Convert 5 USD to INR', 'What’s 50 EUR in INR?'.")
            continue

        from_curr = from_curr.upper()
        to_curr = to_curr.upper()
        
        rate = get_conversion_rate(from_curr, to_curr, exchange_rate_api_key)

        converted = amount * rate
        prompt = f"""Converted {amount} {from_curr} to {converted:.2f} {to_curr} using an exchange rate of {rate:.4f}. 
        Can you explain this nicely to a user? Just return the final message text only. No extra commentary. 
        Behave like you've converted the currency."""

        print("\n🤖 Bot says:")
        print(ask_ollama(prompt))

if __name__ == "__main__":
    run_bot()
