from utils.app_factory import AppFactory
from routes.display_user.routes import display_user_name

blueprints = [display_user_name]
ApiFactory = AppFactory(host="0.0.0.0", port=5001, blueprint_list=blueprints)
ApiFactory.start_app()
