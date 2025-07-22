from fastapi import FastAPI, Request
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    api_version=os.getenv("AZURE_API_VERSION")
)

deployment = os.getenv("AZURE_DEPLOYMENT")

@app.post("/consultar")
async def consultar_modelo(request: Request):
    data = await request.json()
    pregunta = data.get("pregunta", "¿Qué es Azure OpenAI y para qué sirve?")

    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "Eres un asistente útil que responde de forma clara y concisa."},
            {"role": "user", "content": pregunta}
        ],
        max_tokens=500
    )

    return {"respuesta": response.choices[0].message.content}
