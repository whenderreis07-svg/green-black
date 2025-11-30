import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn

app = FastAPI()

connections = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)

    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        connections.remove(websocket)


async def enviar_sinal(dados: dict):
    mensagem = json.dumps(dados)
    mortos = []
    for conn in connections:
        try:
            await conn.send_text(mensagem)
        except:
            mortos.append(conn)

    for morto in mortos:
        connections.remove(morto)


@app.post("/testar")
async def testar_sinal():
    dados = {
        "sala": "vip",
        "rodada": "1234",
        "cor": "verde",
        "nivel": "forte",
        "probabilidade": "87%",
        "resultado": "win",
        "hora": "04:28"
    }
    await enviar_sinal(dados)
    return {"status": "ok", "mensagem": "sinal enviado"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
