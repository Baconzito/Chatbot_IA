from dataclasses import dataclass, asdict
from Services.extern import connection as MongoDBConnection
import sqlite3
import json
from typing import Optional, List, Dict, Any
from datetime import datetime
import os

# chatMPP.py
# Módulo de acceso a datos para "Chat" (similar a UserMPP.py)
# Implementación simple basada en sqlite3 + JSON para mensajes.
# Diseñado para usarse como proveedor de persistencia (MPP = Mapper / Persistence Provider).



@dataclass
class Chat:
    id: Optional[int]
    user_id: int
    title: Optional[str]
    messages: List[Dict[str, Any]]  # lista de mensajes como diccionarios
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class ChatMPP:
    def __init__(self, db_path: str):
        """
        db_path: ruta al fichero sqlite (ej: "./data.db")
        """
        self.db_conection = MongoDBConnection(db_path)
        self._ensure_db()

