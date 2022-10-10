from __main__ import app, db, request
from bson.json_util import dumps
from bson import ObjectId

col = db["users"]

@app.route("/<name>")
def user(name):
    try:
        user = dumps(list(col.find({"_id" : ObjectId(name)})))
        return user
    except:
        return []

#GET
@app.route("/", methods=["GET"])
def AllUsers():
    try:
        user = dumps(list(col.find({})))
        return user
    except:
        return []

#POST
@app.route("/", methods=["POST"])
def CreateUser():
    data = request.json
    col.insert_one( {
        "name" : data["name"],
        "email" : data["email"],
        "password" : data["password"],
        "admin" : data["admin"]

    } )

    return dumps({"Success" : 1})

#DELETE
@app.route("/<id>", methods=["DELETE"])
def DeleteUser(id):

    col.delete_one( {"_id" : ObjectId(id)} )

    return dumps({"Success" : 1})

#GET
@app.route("/<id>/<password>", methods=["GET"])
def LogIn(id, password):
    try:
        user = dumps(list(col.find({"_id" : ObjectId(id), "password" : password})))
        if user == "NULL":
            return []
        return user
    except:
        return []



    
