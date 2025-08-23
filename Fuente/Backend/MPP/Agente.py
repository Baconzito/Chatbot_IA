import httpx

N8N_URL = "http://localhost:5678/webhook/Mi_Modelo"  # URL de tu webhook n8n

async def consultar_agente_ia(mensaje: str) -> str:
    async with httpx.AsyncClient() as client:
        try:
            res = await client.post(N8N_URL, json={"mensaje": mensaje})
            res.raise_for_status()
            data = res.json()
            return data.get("respuesta", "No se recibió respuesta.")
        except Exception as e:
            return f"Error al consultar IA: {e}"
