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

        def get_object(self, id=None):
            try:
                self.cursor = self.connection.cursor()
                query = "select * from employee where id=%s"
                values = (id,)
                self.cursor.execute(query, values)
                record = self.cursor.fetchone()
                return record
            except Exception as e:
                print(e)
                return None

connection_instance=DbConnect()
connection_instance.get_connection()