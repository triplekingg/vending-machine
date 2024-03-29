from flask import Blueprint, request
from . import vending_db
from bson.json_util import dumps, loads
from bson import ObjectId
import datetime

views = Blueprint("views", __name__)

collection = vending_db.vending_machines

# Returns list of vending machines along with their stock
@views.route("/")
def home():
    vending_machine = collection.find()
    list_vending = list(vending_machine)
    json_data = dumps(list_vending, indent=2)
    return json_data


# Adds a new vending machine
@views.route("/addvending/", methods=["POST"])
def addVendingMachine():
    try:
        # Get the vending machine data from the request body
        vending_data = request.json

        # # Get the current time
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")

        # # Add the current time as an attribute in the vending machine data
        vending_data["latest_time"] = current_time

        # Insert the vending machine data into the collection
        id = collection.insert_one(vending_data).inserted_id

        vending_machine = collection.find_one({"_id": ObjectId(id)})
        json_data = dumps(vending_machine)
        return json_data
    except:
        return "Failed to add new vending machine"


# Returns vending machine that the id belongs to
@views.route("/showvending/<string:oid>", methods=["GET"])
def showVending(oid):
    try:
        vending_machine = collection.find_one({"_id": ObjectId(oid)})
        json_data = dumps(vending_machine)
        return json_data
    except:
        return "Error"


# Returns stock of vending machine that the id belongs to
@views.route("/showstock/<string:oid>", methods=["GET"])
def showStock(oid):
    vending_machine = collection.find_one({"_id": ObjectId(oid)})
    json_data = dumps(vending_machine["stock"])
    return json_data


# Deletes a vending machine
@views.route("/deletevending/", methods=["POST"])
def deleteVendingMachine():
    try:
        oid = request.json["oid"]
        collection.delete_one({"_id": ObjectId(oid)})
        return "Successfully deleted"
    except:
        return "Error"


# Updates a vending machine name and location
@views.route("/updatevending/", methods=["POST"])
def editVendingMachineById():
    try:
        oid = request.json["oid"]
        name = request.json["name"]
        location = request.json["location"]
        current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        # Check if the history document exists
        vending_machine = collection.find_one({"_id": ObjectId(oid)})
        old_name = vending_machine["name"]
        old_location = vending_machine["location"]
        old_time = vending_machine["latest_time"]
        print(old_time)
        # Update the details of the vending machine
        collection.update_one(
            {"_id": ObjectId(oid)},
            {
                "$set": {
                    "name": name,
                    "location": location,
                    "latest_time": current_time,
                    "history": {
                        f"{old_time}": {"name": old_name, "location": old_location}
                    },
                }
            },
        )
        # collection.insert_one(
        #     {"_id": ObjectId(oid)},
        #     {'history': {f"{old_time}" :{"name": old_name, "location": old_location}}}
        # )
        # Return success message
        return "Successfully updated"
    except:
        return "Error"


# Updates or Adds stock of the vending machine of which the id belongs to
@views.route("/updatestock/", methods=["POST"])
def updateStock():
    try:
        # Get the oid and stock data from the request body
        oid = request.json["oid"]
        stock = request.json["stock"]

        # iterate through the stock dictionary
        for key, value in stock.items():
            # update the vending machine stock
            collection.update_one(
                {"_id": ObjectId(oid)}, {"$set": {"stock." + key: value}}
            )

        # Uncomment below to return json
        # Find the vending machine with the matching _id
        vending_machine = collection.find_one({"_id": ObjectId(oid)})

        # Convert the vending machine to a JSON object
        json_data = dumps(vending_machine)

        # Return the JSON object
        return json_data
        # return "Success"
    except:
        return "Failed"


# Removes stock of the vending machine of which the id belongs to
@views.route("/deletestock/", methods=["POST"])
def deleteStock():
    try:
        # Get the oid and stock data from the request body
        oid = request.json["oid"]
        item_name = request.json["item_name"]
        # Delete item
        collection.update_one(
            {"_id": ObjectId(oid)}, {"$unset": {"stock." + item_name: ""}}
        )
        return "Success"
    except:
        return "Failed"
