from flask import Flask


class AppFactory:
    def __init__(self, app=__name__, host="", port=0, isDebug=True, blueprint_list=None):
        self.app = Flask(app)
        self.host = host
        self.port = port
        self.isDebug = isDebug
        self.blueprint_list = blueprint_list

    def __create_app(self):
        self.__register_blueprints()
        return self.app

    def __register_blueprints(self):
        if self.blueprint_list is None or len(self.blueprint_list) == 0:
            pass
        else:
            for bp in self.blueprint_list:
                self.app.register_blueprint(bp)

    def start_app(self):
        app = self.__create_app()
        app.run(host=self.host,
                port=self.port,
                debug=self.isDebug)
