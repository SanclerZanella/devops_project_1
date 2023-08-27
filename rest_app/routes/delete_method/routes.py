from flask import (Blueprint, jsonify, request)
import pymysql
from utils.db_ops import DBOps

# Flask Blueprint
delete_method = Blueprint("delete_method", __name__)


@delete_method.route("/users/<user_id>", methods=["DELETE"])
def delete_route(user_id):
    """
    Display user from the database
    """

    db_ops = DBOps()

    try:
        user_exist = db_ops.is_user_in_db(user_id)
        if user_exist is False:
            response = {"Status": "ERROR", "reason": "No such ID"}
            return jsonify(response), 500
        else:
            db_ops.delete_user(user_id)

            response = {"Status": "OK", "User_deleted": f"{user_id}"}
            return jsonify(response), 200

    except pymysql.Error as e:
        response = {"Status": "ERROR", "reason": f'{e}'}
        return jsonify(response), 500
