from flask import Blueprint

from .extensions import mongo

main = Blueprint("main", __name__)

@main.route("/")
def index():
  user_collection = mongo.db.users.insert_one({"name": "vijay"})
  return user_collection