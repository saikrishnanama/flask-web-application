from .database import get_pyMongoDb
from datetime import datetime

# User Activity
def create_user(email, password, username):
    mongo = get_pyMongoDb()
    user = {'username': username, 'email': email, 'password': password}
    mongo.db.users.insert_one(user)

def get_user(username):
    mongo = get_pyMongoDb()
    return mongo.db.users.find_one({'username': username})


# Post Activity
def create_post(data):
    mongo = get_pyMongoDb()
    post = {
        'posted_by': data['posted_by'],
        'posted_content': data['posted_content'],
        'likes': [{},{}],
        'comments': [{}, {}],
        "created_at": datetime.utcnow()
    }
    mongo.db.posts.insert_one(post)

def get_posts():
    mongo = get_pyMongoDb()
    return list(mongo.db.posts.find().sort('created_at', -1))

def update_posts(data):
    print("hello world")
    # mongo = get_pyMongoDb()
    # collection = mongo['posts']
    # result = collection.update_one(
    # { "_id": "ObjectId('66bda1370cdef30b55fac4a7')" },            # Filter: Find user with username "johndoe"
    # { "$set": { 'posted_content': {'content':'hi this is an update'},"updated_at": datetime.utcnow()}})

    # print('result',result)
    




