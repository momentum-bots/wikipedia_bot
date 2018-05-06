from db import users_db


def add_user(id_, username=None, lang='en'):
    user = {'id': id_,
            'username': username,
            'lang': lang
            }
    if users_db.find_one({"id": user['id']}) is None and users_db.find_one({"username": user['username']}) is None:
        users_db.insert_one(user)
    else:
        return False
    return True


def set_lang(id_, lang):
    user = users_db.find_one({"id": id_})
    user['lang'] = lang
    users_db.save(user)


def get_lang(id_):
    user = users_db.find_one({"id": id_})
    return user['lang']


def get_all_users():
    users_data = []
    for user in users_db.find():
        users_data.append(user)
    return users_data


def clear_db():
    users_db.drop()
