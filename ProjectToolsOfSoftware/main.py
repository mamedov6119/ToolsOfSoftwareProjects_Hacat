import pymongo 
from flask import Flask, request
from bson.json_util import dumps
from bson import ObjectId
from flask_cors import CORS
//


client = pymongo.MongoClient("mongodb+srv://Murad:hSkrqm1JZZmXVxVv@project.xtsgpdq.mongodb.net/?retryWrites=true&w=majority")
db = client["mamedov6119"]
col = db["users"]


app = Flask(__name__)
CORS(app, support_credentials=True)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response


import users, pc_parts # function from users @app.route("/<name>") def user(name):



if __name__ == "__main__":
    app.run(host="192.168.0.217", port=5000)



