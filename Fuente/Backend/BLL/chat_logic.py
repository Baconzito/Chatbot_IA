from MPP.Agente import consultar_agente_ia

async def procesar_mensaje(mensaje: str) -> str:
    # Lógica de negocio: validaciones, control, filtros
    if not mensaje.strip():
        return "Mensaje vacío."

    # Enviar al MPP para procesar con la IA
    respuesta = await consultar_agente_ia(mensaje)
    return respuesta
