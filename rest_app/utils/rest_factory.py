import os
from flask import Flask
from .db_connector import ConnectDB
from .tables_creator import CreateTables
if os.path.exists('env.py'):
    pass


db = ConnectDB()


class RestFactory:
    def __init__(self, app=__name__, host="", port=0, isDebug=True):
        self.app = Flask(app)
        self.host = host
        self.port = port
        self.isDebug = isDebug

        self.db = ConnectDB(self.app)
        self.db_conn = self.db.connect_db()

    def __create_app(self):
        app = self.app

        
        create_tables = CreateTables(app, self.db_conn)
        create_tables.create_table()

        self.__register_blueprints()

        app.DB_CONN = self.db_conn

        return app
    
    def __register_blueprints(self):
        from routes.post_method.routes import post_method

        blueprints = [post_method]

        if blueprints is None or len(blueprints) == 0:
            pass
        else:
            for bp in blueprints:
                self.app.register_blueprint(bp)

    def start_app(self):
        app = self.__create_app()

        app.run(host=self.host,
                port=self.port,
                debug=self.isDebug)