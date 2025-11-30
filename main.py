from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.head("/")
def root_head():
    return Response(status_code=200)

@app.get("/healthz")
def healthz():
    return {"ok": True}
