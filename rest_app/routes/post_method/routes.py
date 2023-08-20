from flask import (Blueprint, jsonify, current_app)
import pymysql

# Flask Blueprint
post_method = Blueprint("post_method", __name__)


@post_method.route("/", methods=["GET"])
def post_route():
    """
    Returns JSON
    """

    app = current_app
    DB_connection = app.DB_CONN

    try:
        with DB_connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            data = cursor.fetchall()
        return f'<h1>HELLO WORLD - {data}!!!</h1>'
    except pymysql.Error as e:
        return f"Error accessing database: {e}"
