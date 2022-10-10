from __main__ import app, db, request
from bson.json_util import dumps
from bson import ObjectId

col = db["pc_parts"]

@app.route("/parts/<name>")
def Find_Pc_Part(name):
    try:
        part = dumps(list(col.find({"_id" : ObjectId(name)})))
        return part
    except:
        return []

@app.route("/", methods=["GET"])
def AllPcParts():
    try:
        pc_part = dumps(list(col.find({})))
        return pc_part
    except:
        return []

@app.route("/", methods=["POST"])
def CreatePcPart():
    data = request.json
    col.insert_one( {
        "name" : data["name"],
        "category" : data["category"],
        "price" : data["price"]

    } )

    return dumps({"Success" : 1})
    
@app.route("/<id>", methods=["DELETE"])
def DeletePcPart(id):

    col.delete_one( {"_id" : ObjectId(id)} )

    return dumps({"Success" : 1})