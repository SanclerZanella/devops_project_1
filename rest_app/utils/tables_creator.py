import pymysql


class CreateTables:
    def __init__(self, app=None, db=None):
        self.connection = db
        self.table_names = ['users']

    def create_table(self):
        for table in self.table_names:
            table_name = table
            query = f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                user_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                user_name VARCHAR(50) NOT NULL,
                creation_date VARCHAR(50)
            )
            '''
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute(query)

                self.connection.commit()
                print("Table created successfully.")

            except pymysql.Error as e:
                print(f"Error creating table: {e}")
