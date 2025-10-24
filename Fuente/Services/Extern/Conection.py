from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

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
            print("MongoDB connection closed.")