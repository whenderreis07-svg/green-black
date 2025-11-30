from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Response

app = FastAPI()

class Signal(BaseModel):
    mesa: str
    result: str
    conf: float
    horario: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.head("/")
def root_head():
    return Response(status_code=200)

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.post("/sinal")
def receber_sinal(data: Signal):
    print("Sinal recebido:", data.dict())
    return {"ok": True, "recebido": data.dict()}
