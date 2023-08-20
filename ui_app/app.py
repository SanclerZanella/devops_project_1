from utils.ui_factory import UIFactory
from routes.display_user.routes import display_user_name

blueprints = [display_user_name]
ApiFactory = UIFactory(host="0.0.0.0", port=5001, blueprint_list=blueprints)
ApiFactory.start_app()
