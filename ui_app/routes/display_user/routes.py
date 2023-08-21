from flask import (Blueprint, jsonify)
import requests


# Flask Blueprint
display_user_name = Blueprint("display_user_name", __name__)


# @display_user_name.route("/users/get_user_data/<user_id>")
@display_user_name.route("/users/get_user_data/<user_id>")
def display_user_route(user_id):
    """
    Returns JSON
    """

    get_user_endpoint = f"http://rest_app:5000/users/{user_id}/"

    try:
        response = requests.get(get_user_endpoint, stream=True)
        data = response.json()
        return f"<h1 id='user'>{data['User_name']}</h1>"

    except requests.RequestException as e:
        return f"Error: {e}", 500

    except Exception as e:
        return f"<h1 id='user'>No such user: {user_id}</h1>"
