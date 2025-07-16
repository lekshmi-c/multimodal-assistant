from ollama import Client

client = Client(host='http://localhost:11434')  # default Ollama endpoint

def get_llm_response(prompt: str) -> str:
    response = client.chat(model="llama2", messages=[
        {"role": "user", "content": prompt}
    ])
    return response['message']['content']


# from models.llm_model import get_llm_response
# from models.llm_model import get_llm_response


# def handle_text_query(text: str):
#     return get_llm_response(text)
