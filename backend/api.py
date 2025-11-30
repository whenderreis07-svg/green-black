from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sinais")
def pegar_sinais():
    return {
        "sinais": [
            {"horario": "10:32", "valor": "R$ 1.350", "tendencia": "Alta"},
            {"horario": "10:35", "valor": "R$ 1.410", "tendencia": "Baixa"},
            {"horario": "10:40", "valor": "R$ 1.500", "tendencia": "Alta"},
        ]
    }
