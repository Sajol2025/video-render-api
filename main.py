from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Video Render API is running"}

@app.head("/")
def head_root():
    return {"status": "ok"}
