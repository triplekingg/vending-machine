import requests

ENDPOINT = 'http://127.0.0.1:8000/'

def test_can_connect():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_add_vending_machine():
    payload = new_vending_payload()
    add_vending_response = create_vending(payload)
    assert add_vending_response.status_code == 200

    data = add_vending_response.json()

    machine_id = data['_id']['$oid']
    get_vending_response = get_vending(machine_id)
    assert get_vending_response.status_code == 200

    #Delete the vending machine so the database will not be affected
    delete_vending(machine_id)

def test_can_update_vending():
    #add a vending machine
    payload = new_vending_payload()
    add_vending_response = create_vending(payload)
    assert add_vending_response.status_code == 200
    machine_id = add_vending_response.json()['_id']['$oid'] 
    

    #update the vending machine
    new_payload = {
    "oid": machine_id,
    "name": "Cold Drinks Test Update",
    "location": "Updated Floor"
    }
    update_vending_response = update_vending(new_payload)
    assert update_vending_response.status_code == 200

   #Delete the vending machine so the database will not be affected
    delete_vending(machine_id) 

def test_can_show_vending():
    #Add a vending machines
    payload = new_vending_payload()
    add_vending_response = create_vending(payload)
    assert add_vending_response.status_code == 200
    machine_id = add_vending_response.json()['_id']['$oid']
    
    show_vending_response = get_vending(machine_id)
    assert show_vending_response.status_code == 200

    #Delete the vending machine so the database will not be affected
    delete_vending(machine_id)

def test_can_delete_vending():
   #Add a vending machine
    payload = new_vending_payload()
    add_vending_response = create_vending(payload)
    assert add_vending_response.status_code == 200
    machine_id = add_vending_response.json()['_id']['$oid']
    
    #Delete the vending machine
    show_vending_response = delete_vending(machine_id)
    assert show_vending_response.status_code == 200 

def test_can_show_stock():
   #Add a vending machine
    payload = new_vending_payload()
    add_vending_response = create_vending(payload)
    assert add_vending_response.status_code == 200
    machine_id = add_vending_response.json()['_id']['$oid']
    
    #Show stock
    show_stock_response = get_stock(machine_id)
    assert show_stock_response.status_code == 200

    #Delete the vending machine so the database will not be affected
    delete_vending(machine_id)

def test_can_update_stock():
   #Add a vending machine
    payload = new_vending_payload()
    add_vending_response = create_vending(payload)
    assert add_vending_response.status_code == 200
    machine_id = add_vending_response.json()['_id']['$oid']
    
    #Show stock
    stock_payload = new_stock_payload(machine_id)
    update_stock_response = update_stock(stock_payload)
    assert update_stock_response.status_code == 200

    #Delete the vending machine so the database will not be affected
    delete_vending(machine_id)

def test_can_delete_stock():
   #Add a vending machine
    payload = new_vending_payload()
    add_vending_response = create_vending(payload)
    assert add_vending_response.status_code == 200
    machine_id = add_vending_response.json()['_id']['$oid']
    
    #Show stock
    stock_payload = new_stock_payload(machine_id)
    update_stock_response = update_stock(stock_payload)
    assert update_stock_response.status_code == 200
    item_name = 'Coke'
    #Delete stock
    delete_payload = get_delete_payload(machine_id,item_name)
    delete_stock_response = delete_stock(delete_payload)
    assert delete_stock_response.status_code == 200
    #Delete the vending machine so the database will not be affected
    delete_vending(machine_id)  


def create_vending(payload):
    return requests.post(ENDPOINT +'addvending/', json=payload)

def get_vending(machine_id):
    return requests.get(ENDPOINT + f"showvending/{machine_id}") 

def update_vending(payload):
    return requests.post(ENDPOINT +'updatevending/', json=payload)

def delete_vending(machine_id):
    payload = {"oid": machine_id}
    return requests.post(ENDPOINT +'deletevending/', json=payload)  

def get_stock(machine_id):
    return requests.get(ENDPOINT + f"showstock/{machine_id}") 

def update_stock(payload):
    return requests.post(ENDPOINT + f"updatestock/", json=payload)   

def delete_stock(payload):
    return requests.post(ENDPOINT + f"deletestock/", json=payload) 

def new_vending_payload():
    return {"name": "Cold Drinks Test",
    "location": "Old building 34th Floor Test",
    "stock": {
        "Coke": 12,
        "Sprite": 32,
        "Aura Water": 23,
        "Singha Water": 12,
        "Fanta (Orange)": 21,
        "Fanta (Red)": 4,
        "Mountain Dew": 11,
        "Yakult": 12,
        "Meiji Milk (Chocolate)": 11
    }} 

def new_stock_payload(machine_id):
    return {
    "oid": machine_id,
    "stock": {
        "Coke": 1,
        "Sprite": 2,
        "Milshake": 3
    }
}

def get_delete_payload(machine_id, item_name):
    return {
    "oid": machine_id,
    "item_name":item_name
}