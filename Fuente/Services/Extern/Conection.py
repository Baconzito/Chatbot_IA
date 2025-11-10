from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, PyMongoError
import os
from typing import Optional
from dotenv import load_dotenv
from pathlib import Path
from bson.objectid import ObjectId

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

class MongoDBConnection:
    def __init__(self, connection_string: Optional[str] = None):
        """
        Initialize MongoDB connection with connection string from environment variable.
        Falls back to provided connection_string if env var is not set.
        """
        self.connection_string = os.getenv('MONGODB_URI')
        self.client = None
        
    def connect(self):
        """Establish connection to MongoDB cluster."""
        try:
            self.client = MongoClient(self.connection_string)
            # Ping the server to verify connection
            self.client.admin.command('ping')
            print("Successfully connected to MongoDB!")
            return True
        except ConnectionFailure as e:
            print(f"Failed to connect to MongoDB: {e}")
            return False
            
    def get_database(self, db_name):
        """Get database instance."""
        if self.client:
            return self.client[db_name]
        return None
        
    def close(self):
        """Close MongoDB connection."""
        if self.client:
            self.client.close()
            self.client = None
            print("MongoDB connection closed.")

    # def insert_document(self, db_name: str, collection_name: str, document: dict, close_after: bool = False):
    #     """
    #     Insert a single document into the specified collection.
    #     Returns inserted_id on success, or None on failure.
    #     """
    #     if not self.client:
    #         if not self.connect():
    #             return None
    #     try:
    #         db = self.get_database(db_name)
    #         if db is None:
    #             print("No database available.")
    #             return None
    #         result = db[collection_name].insert_one(document)
    #         return result.inserted_id
    #     except PyMongoError as e:
    #         print(f"Error inserting document: {e}")
    #         return None
    #     finally:
    #         if close_after:
    #             self.close()
    
    def find_documents(self, db_name: str, collection_name: str, query: dict = None, projection: dict = None, limit: int = 0, close_after: bool = False):
        if query is None:
            query = {}

        # Intentar convertir _id si viene como string (caso común)
        if "_id" in query and isinstance(query["_id"], str):
            try:
                query["_id"] = ObjectId(query["_id"])
            except Exception:
                # no convertir si no es un ObjectId válido
                pass

        if not self.client:
            if not self.connect():
                return None

        try:
            print(f"[DEBUG] find_documents -> db: {db_name}, collection: {collection_name}, query: {query}, projection: {projection}, limit: {limit}")
            db = self.get_database(db_name)
            if db is None:
                print("No database available.")
                return []
            # Verificar cantidad antes de convertir a lista (útil para debug)
            count = db[collection_name].count_documents(query)
            print(f"[DEBUG] documents matching: {count}")
            cursor = db[collection_name].find(query, projection)
            if limit and isinstance(limit, int) and limit > 0:
                cursor = cursor.limit(limit)
            results = list(cursor)
            print(f"[DEBUG] returning {len(results)} documents")
            return results
        except PyMongoError as e:
            print(f"Error finding documents: {e}")
            return []
        finally:
            if close_after:
                self.close()
        

    def get_menu_by_id(self, menu_id: str, db_name: str = "chatbot_ia", collection_name: str = "Menus", close_after: bool = False) -> dict:
        """
        Retrieve a specific menu document by its ID.
        
        Args:
            menu_id (str): The ID of the menu to find
            db_name (str): Database name, defaults to AppDB
            collection_name (str): Collection name, defaults to Menus
            close_after (bool): Whether to close the connection after operation
            
        Returns:
            dict: The menu document if found, None otherwise
        """
        try:
            docs = self.find_documents(
                db_name=db_name,
                collection_name=collection_name,
                query={"_id": menu_id},
                limit=1,
                close_after=False
            )
            
            if docs and len(docs) > 0:
                return docs[0]
            return None
            
        except PyMongoError as e:
            print(f"Error retrieving menu: {e}")
            return None
        finally:
            if close_after:
                self.close()