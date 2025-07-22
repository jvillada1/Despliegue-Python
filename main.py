from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Aplicación FastAPI desplegada correctamente en Azure."}

@app.get("/entorno")
def leer_variable():
    valor = os.getenv("MENSAJE_PRUEBA", "Variable de entorno no definida")
    return {"MENSAJE_PRUEBA": valor}
