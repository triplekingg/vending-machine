from flask import Blueprint

views = Blueprint('views', __name__)


#Returns list of vending machines, list of stock products
@views.route('/')
def home():
    return 'hello'

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
