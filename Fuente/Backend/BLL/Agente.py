from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from BLL.chat_logic import procesar_mensaje

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Limitar a tu dominio si querés
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatInput(BaseModel):
    message: str

@app.post("/chat")
async def chat(input: ChatInput):
    respuesta = await procesar_mensaje(input.message)
    return {"reply": respuesta}
