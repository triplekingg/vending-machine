from flask import Blueprint, request
from . import vending_db
from bson.json_util import dumps, loads
from bson import ObjectId
views = Blueprint('views', __name__)

collection = vending_db.vending_machines

#Returns list of vending machines along with their stock
@views.route('/')
def home():
    vending_machine = collection.find()
    list_vending = list(vending_machine)
    json_data = dumps(list_vending, indent = 2)
    return(json_data)

#Adds a new vending machine
@views.route('/addvending/', methods=['POST'])
def addVendingMachine():
    try:
        # Get the vending machine data from the request body
        vending_data = request.json

        # Insert the vending machine data into the collection
        collection.insert_one(vending_data)

        # Return the JSON object
        return "Successfully added new vending machine"

    except:
        return "Failed to add new vending machine"


#Returns vending machine that the id belongs to
@views.route('/showvending/<string:oid>', methods=['GET'])
def showVending(oid): 
    try:
        # oid = request.json["oid"]
        vending_machine = collection.find_one({"_id": ObjectId(oid)})
        json_data = dumps(vending_machine)
        return(json_data)
    except:
        return "Error"

#Deletes a vending machine
@views.route('/deletevending', methods=['POST'])
def deleteVendingMachine():
    pass

#Edits a vending machine details
@views.route('/editvending', methods=['POST'])
def editVendingMachine():
    pass
