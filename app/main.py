from fastapi import FastAPI
from .routers import tickets
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://asofe-rifa.web.app"],  # Cambia esto a tu URL de frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(tickets.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project"}
