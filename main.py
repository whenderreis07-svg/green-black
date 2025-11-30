from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Signal(BaseModel):
    mesa: str
    result: str
    conf: float
    horario: str


@app.get("/")
def home():
    return {"status": "API funcionando", "versao": "green-black"}


@app.post("/sinal")
def receber_sinal(data: Signal):
    print("Sinal recebido:")
    print(data.dict())
    return {"ok": True, "recebido": data.dict()}

