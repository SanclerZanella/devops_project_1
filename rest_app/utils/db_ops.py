from flask import current_app
import pymysql
import datetime


class DBOps:
    def __init__(self):
        self.app = current_app
        self.db_connection = self.app.DB_CONN

    def is_user_in_db(self, id):
        user_exists = None
        with self.db_connection.cursor() as cursor:
            select_query = "SELECT user_id FROM users WHERE user_id = %s"
            cursor.execute(select_query, (id,))
            user_exists = cursor.fetchone()

        if user_exists:
            return True
        else:
            return False

    def insert_user(self, id, user_name):
        with self.db_connection.cursor() as cursor:
            insert_query = "INSERT INTO users (user_id, user_name, creation_date) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (id, user_name, datetime.datetime.now()))
            self.db_connection.commit()
