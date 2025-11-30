from fastapi import FastAPI

app = FastAPI()

@app.get("/")
@app.head("/")
def root():
    return {"status": "ok"}

@app.get("/healthz")
@app.head("/healthz")
def health():
    return {"status": "healthy"}
