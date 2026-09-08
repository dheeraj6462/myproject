import mysql.connector

class DbConnect:

    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Dheeraj@2004",
                database="company_db"
                )
            return self.connection
        except Exception as e:
            return None

class Employee_manager(DbConnect):
    pass

connection_instance=DbConnect()
connection_instance.get_connection()