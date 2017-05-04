import sqlite3

class DatabaseManager:
    
    def __init__(self, db):
        """
        Constructing a file and dictionary data structure
        :param filename:
        :param conn: The SQLite Database Connection 
        """
        self.db = db #database connection
        self.cursor = self.db.cursor()
        
    def get_db(self):
        return self.db
        
    def get_db_cursor(self):
        return self.cursor