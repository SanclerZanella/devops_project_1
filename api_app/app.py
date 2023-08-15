from utils.app_factory import AppFactory
from routes.post_method.routes import post_method


blueprints = [post_method]
ApiFactory = AppFactory(host="0.0.0.0", port=5000, blueprint_list=blueprints)
ApiFactory.start_app()
