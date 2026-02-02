from database import user_collection
from Model.entlty import User
from bson.json_util import ObjectId

def create_user(data):
    user = User(
        name=data.get("name"),
        email=data.get("email"),
    )
    result = user_collection.insert_one(user.to_dict())
    return str(result.inserted_id)

def get_all_users():
    users = []
    for user in user_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return users

def get_user(user_id):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])
    return user

def update_user(user_id, data):
    user_collection.update_one(
        {"_id": ObjectId(user_id)},
        { "$set": data}
    )
    return True


def delete_user(user_id):
    user_collection.delete_one({"_id": ObjectId(user_id)})
    return True