from . import vending_db
import json

def initializeVengingMachines():
    collection = vending_db.vending_machines
    with open('website/data.json') as file:
        test_document = json.load(file)
    collection.insert_many(test_document)