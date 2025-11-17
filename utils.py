import requests

OLLAMA_MODEL = "mistral"
OLLAMA_API_URL = "http://localhost:11434/api/generate"

def query_llm(prompt, max_new_tokens=400):
    """
    Queries Ollama local LLM and returns a single string.
    """
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "options": {"num_predict": max_new_tokens}
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload, stream=False)
        data = response.json()

        # If the response contains 'response', return it
        if "response" in data:
            return data["response"]
        # Sometimes it's nested in a list of chunks (older API versions)
        elif isinstance(data, list):
            return "".join(chunk.get("response", "") for chunk in data)
        else:
            return str(data)

    except Exception as e:
        return f"Error: {str(e)}"
