from flask import Blueprint
from . import vending_db
from bson.json_util import dumps, loads
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
@views.route('/addvending', methods=['POST'])
def addVendingMachine():
    pass

#Deletes a vending machine
@views.route('/deletevending', methods=['POST'])
def deleteVendingMachine():
    pass

#Edits a vending machine details
@views.route('/editvending', methods=['POST'])
def editVendingMachine():
    pass
