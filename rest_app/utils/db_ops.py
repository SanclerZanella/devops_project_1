from flask import current_app
import datetime


class DBOps:
    def __init__(self):
        self.app = current_app
        self.db_connection = self.app.DB_CONN

    def is_user_in_db(self, id):
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

    def retrieve_user(self, id):
        with self.db_connection.cursor() as cursor:
            retrieve_query = "SELECT user_id, user_name FROM users WHERE user_id = %s"
            cursor.execute(retrieve_query, (id,))
            user = cursor.fetchone()

        return user

    def update_user(self, id, value):
        with self.db_connection.cursor() as cursor:
            update_query = "UPDATE users SET user_name = %s WHERE user_id = %s"
            cursor.execute(update_query, (value, id))
            self.db_connection.commit()

    def delete_user(self, id):
        with self.db_connection.cursor() as cursor:
            delete_query = "DELETE FROM users WHERE user_id = %s"
            cursor.execute(delete_query, (id,))
            self.db_connection.commit()
