from db import users_db


def add_user(id, lang='en'):
    user = {'id': id,
            'lang': lang
            }
    if users_db.find_one({"id": user['id']}) is None:
        users_db.insert_one(user)
    else:
        return False
    return True


def get_all_users():
    users_data = []
    for user in users_db.find():
        users_data.append(user)
    return users_data
