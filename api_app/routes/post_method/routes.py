from flask import (Blueprint, jsonify)


# Flask Blueprint
post_method = Blueprint("post_method", __name__)


@post_method.route("/", methods=["GET"])
def post_route():
    """
    Returns JSON
    """

    data = {
        "Modules": 15,
        "Subject": "Data Structures and Algorithms"
    }

    return jsonify(data)
