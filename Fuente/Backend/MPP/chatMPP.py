from dataclasses import dataclass, asdict
from Services.Extern.Conection import MongoDBConnection
from typing import Optional, List, Dict, Any
from datetime import datetime

class ChatMPP:
    def __init__(self):
        # Initialize MongoDB connection
        self.db_conection = MongoDBConnection("mongodb+srv://farellijavier_db_user:farellijavier_db_user@cluster0.b5uiirf.mongodb.net/")
        # No need for _ensure_db() since we're using MongoDB

    def get_menu_by_id(self, menu_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves a menu by its ID using the MongoDB connection.
        
        Args:
            menu_id (str): The ID of the menu to retrieve
            
        Returns:
            Optional[Dict[str, Any]]: The menu document if found, None otherwise
        """
        try:
            menu = self.db_conection.get_menu_by_id(
                menu_id=menu_id,
                close_after=True
            )
            return menu
        except Exception as e:
            print(f"Error retrieving menu from database: {e}")
            return None

