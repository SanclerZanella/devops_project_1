# from flask import Flask, render_template
# import pymysql

# app = Flask(__name__)

# # Replace with your MySQL connection details
# connection = pymysql.connect(
#     host='db4free.net',
#     user='sanclerzanella',
#     password='projetodevopsone',
#     db='projectonedevops',
# )

# @app.route('/')
# def index():
#     try:
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT 1")
#             data = cursor.fetchall()
#         return f'<h1>HELLO WORLD - {data}!!!</h1>'
#     except pymysql.Error as e:
#         return f"Error accessing database: {e}"

# if __name__ == '__main__':
#     app.run(debug=True)
