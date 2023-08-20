from utils.rest_factory import RestFactory


ApiFactory = RestFactory(host="0.0.0.0", port=5000)

db = ApiFactory.db_conn

ApiFactory.start_app()
