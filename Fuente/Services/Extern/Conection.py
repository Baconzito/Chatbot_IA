from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, PyMongoError

class MongoDBConnection:
    def __init__(self, connection_string):
        """Initialize MongoDB connection with connection string."""
        self.connection_string = connection_string
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

    def insert_document(self, db_name: str, collection_name: str, document: dict, close_after: bool = False):
        """
        Insert a single document into the specified collection.
        Returns inserted_id on success, or None on failure.
        """
        if not self.client:
            if not self.connect():
                return None
        try:
            db = self.get_database(db_name)
            if db is None:
                print("No database available.")
                return None
            result = db[collection_name].insert_one(document)
            return result.inserted_id
        except PyMongoError as e:
            print(f"Error inserting document: {e}")
            return None
        finally:
            if close_after:
                self.close()

    def find_documents(self, db_name: str, collection_name: str, query: dict = None, projection: dict = None, limit: int = 0, close_after: bool = False):
        """
        Find documents in a collection.
        Returns a list of documents (may be empty) or None on connection failure.
        """
        if query is None:
            query = {}
        if not self.client:
            if not self.connect():
                return None
        try:
            db = self.get_database(db_name)
            if db is None:
                print("No database available.")
                return []
            cursor = db[collection_name].find(query, projection)
            if limit and isinstance(limit, int) and limit > 0:
                cursor = cursor.limit(limit)
            return list(cursor)
        except PyMongoError as e:
            print(f"Error finding documents: {e}")
            return []
        finally:
            if close_after:
                self.close()