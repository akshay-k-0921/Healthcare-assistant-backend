import requests
from django.conf import settings

HF_API_URL = "https://api-inference.huggingface.co/models/gpt2"

headers = {
    "Authorization": f"Bearer {settings.HUGGINGFACE_API_KEY}"
}

def get_ai_response(prompt: str):
    payload = {"inputs": prompt}
    response = requests.post(HF_API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        try:
            # Extract generated text
            return data[0]["generated_text"]
        except (KeyError, IndexError):
            return "Sorry, I couldn't generate a response."
    else:
        return f"Error: {response.status_code}, {response.text}"
