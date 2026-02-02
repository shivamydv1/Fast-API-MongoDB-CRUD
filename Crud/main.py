from fastapi import FastAPI
from Controller.user_controller import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is running"}

app.include_router(router)