import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def responder(pergunta):

    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": pergunta}]
    )

    return resposta.choices[0].message.content

if __name__ == "__main__":
    pergunta = input("Você: ")
    resposta = responder(pergunta)
    print("Groq:", resposta)
