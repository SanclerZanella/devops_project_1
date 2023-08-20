import os
import pymysql
if os.path.exists('env.py'):
    import env


class ConnectDB:
    def __init__(self, app=None):
        self.app = app
        self.db_host = os.environ.get("DB_HOST")
        self.db_user = os.environ.get("DB_USER")
        self.db_password = os.environ.get("DB_PASSWORD")
        self.db_name = os.environ.get("DB_NAME")

    def connect_db(self):
        return pymysql.connect(
                    host=self.db_host,
                    user=self.db_user,
                    password=self.db_password,
                    db=self.db_name,
                )

    def test_DB_conn(self):
        try:
            conn = self.connect_db()
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1")  # Execute a simple query to check connection

            return True

        except pymysql.Error as e:
            return f"Database connection failed: {e}"
