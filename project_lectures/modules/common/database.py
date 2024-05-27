import sqlite3

class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r"/home/carmin/Public/QA-Auto/project_lectures"+r"become_qa_auto.db")
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_query)
        record = self.cursor.fetchall()
        print(f"Success. SQLite Database version: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode FROM customers WHERE name = \"{name}\""
        self.cursor.execute(query)
        record =  self.cursor.fetchall()
        return record

    

    
#print(__name__)
