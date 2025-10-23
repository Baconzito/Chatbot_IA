from dataclasses import dataclass, asdict
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
        self.db_path = db_path
        self._ensure_db()

    def _get_conn(self):
        conn = sqlite3.connect(self.db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        conn.row_factory = sqlite3.Row
        return conn

    def _ensure_db(self):
        """Crea la tabla si no existe."""
        if not os.path.exists(os.path.dirname(self.db_path)) and os.path.dirname(self.db_path) != "":
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        with self._get_conn() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS chats (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    title TEXT,
                    messages TEXT NOT NULL,
                    created_at TEXT DEFAULT (datetime('now')),
                    updated_at TEXT DEFAULT (datetime('now'))
                )
                """
            )
            conn.commit()

    def _row_to_chat(self, row: sqlite3.Row) -> Chat:
        messages = json.loads(row["messages"]) if row["messages"] else []
        return Chat(
            id=row["id"],
            user_id=row["user_id"],
            title=row["title"],
            messages=messages,
            created_at=row["created_at"],
            updated_at=row["updated_at"],
        )

    def create_chat(self, user_id: int, title: Optional[str], messages: Optional[List[Dict[str, Any]]] = None) -> Chat:
        """Inserta un nuevo chat y devuelve la entidad creada."""
        messages = messages or []
        messages_json = json.dumps(messages, ensure_ascii=False)
        with self._get_conn() as conn:
            cur = conn.execute(
                """
                INSERT INTO chats (user_id, title, messages, created_at, updated_at)
                VALUES (?, ?, ?, datetime('now'), datetime('now'))
                """,
                (user_id, title, messages_json),
            )
            chat_id = cur.lastrowid
            row = conn.execute("SELECT * FROM chats WHERE id = ?", (chat_id,)).fetchone()
            return self._row_to_chat(row)

    def get_chat_by_id(self, chat_id: int) -> Optional[Chat]:
        """Devuelve un Chat por su id o None si no existe."""
        with self._get_conn() as conn:
            row = conn.execute("SELECT * FROM chats WHERE id = ?", (chat_id,)).fetchone()
            return self._row_to_chat(row) if row else None

    def list_chats_by_user(self, user_id: int, limit: int = 50, offset: int = 0) -> List[Chat]:
        """Lista chats de un usuario con paginación simple."""
        with self._get_conn() as conn:
            rows = conn.execute(
                "SELECT * FROM chats WHERE user_id = ? ORDER BY updated_at DESC LIMIT ? OFFSET ?",
                (user_id, limit, offset),
            ).fetchall()
            return [self._row_to_chat(r) for r in rows]

    def update_chat(self, chat_id: int, title: Optional[str] = None, messages: Optional[List[Dict[str, Any]]] = None) -> Optional[Chat]:
        """Actualiza título y/o mensajes de un chat. Devuelve el chat actualizado o None."""
        # Obtener chat actual
        existing = self.get_chat_by_id(chat_id)
        if not existing:
            return None

        new_title = title if title is not None else existing.title
        new_messages = messages if messages is not None else existing.messages
        messages_json = json.dumps(new_messages, ensure_ascii=False)

        with self._get_conn() as conn:
            conn.execute(
                """
                UPDATE chats
                SET title = ?, messages = ?, updated_at = datetime('now')
                WHERE id = ?
                """,
                (new_title, messages_json, chat_id),
            )
            row = conn.execute("SELECT * FROM chats WHERE id = ?", (chat_id,)).fetchone()
            return self._row_to_chat(row)

    def delete_chat(self, chat_id: int) -> bool:
        """Elimina un chat; devuelve True si se eliminó alguna fila."""
        with self._get_conn() as conn:
            cur = conn.execute("DELETE FROM chats WHERE id = ?", (chat_id,))
            return cur.rowcount > 0

    def count_chats_for_user(self, user_id: int) -> int:
        """Cuenta los chats de un usuario."""
        with self._get_conn() as conn:
            row = conn.execute("SELECT COUNT(1) as cnt FROM chats WHERE user_id = ?", (user_id,)).fetchone()
            return int(row["cnt"] or 0)

# Ejemplo de uso (se puede quitar en producción)
if __name__ == "__main__":
    mpp = ChatMPP("./data/chat_db.sqlite")
    chat = mpp.create_chat(user_id=1, title="Prueba", messages=[{"role": "user", "text": "Hola"}])
    print("Creado:", asdict(chat))
    fetched = mpp.get_chat_by_id(chat.id)
    print("Recuperado:", asdict(fetched) if fetched else None)