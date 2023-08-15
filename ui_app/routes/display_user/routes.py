from flask import (Blueprint, jsonify)


# Flask Blueprint
display_user_name = Blueprint("display_user_name", __name__)


@display_user_name.route("/", methods=["GET"])
def display_user_route():
    """
    Returns JSON
    """

    data_ui = {
        "Modules": 1,
        "Subject": "Test"
    }

    return jsonify(data_ui)
