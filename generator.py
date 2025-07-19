# generator.py
import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

def generate_questions(resume_text):
    api_key = os.getenv("MISTRAL_API_KEY")

    if not api_key:
        raise Exception("MISTRAL_API_KEY not found in environment variables.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are a technical HR interviewer. Based on the following resume, generate 5 smart technical interview questions relevant to the candidate’s experience, projects, and skills. Be concise.

Resume:
\"\"\"
{resume_text}
\"\"\"
"""

    data = {
        "model": "mistral-small",  # You can also use mistral-medium or mistral-large
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers=headers,
        json=data
    )

    if response.status_code != 200:
        raise Exception(f"Mistral API Error: {response.status_code} - {response.text}")

    result = response.json()
    return result["choices"][0]["message"]["content"]