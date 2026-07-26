from fastapi import FastAPI

# Uvicorn এই "app" নামটিকেই খুঁজছে
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Video Render API is running successfully!"}
