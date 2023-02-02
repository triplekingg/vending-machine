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
    print(data)

    machine_id = data['_id']['$oid']
    get_vending_response = get_vending(machine_id)
    assert get_vending_response.status_code == 200

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
    

def test_can_show_vending():
    #Add a vending machines
    payload = new_vending_payload()
    add_vending_response = create_vending(payload)
    assert add_vending_response.status_code == 200
    machine_id = add_vending_response.json()['_id']['$oid']
    
    show_vending_response = get_vending(machine_id)
    assert show_vending_response.status_code == 200

def test_can_delete_vending():
   #Add a vending machine
    payload = new_vending_payload()
    add_vending_response = create_vending(payload)
    assert add_vending_response.status_code == 200
    machine_id = add_vending_response.json()['_id']['$oid']
    
    #Delete the vending machine
    show_vending_response = delete_vending(machine_id)
    assert show_vending_response.status_code == 200 




def create_vending(payload):
    return requests.post(ENDPOINT +'addvending/', json=payload)

def get_vending(machine_id):
    return requests.get(ENDPOINT + f"showvending/{machine_id}") 

def update_vending(payload):
    return requests.post(ENDPOINT +'updatevending/', json=payload)

def delete_vending(machine_id):
    payload = {"oid": machine_id}
    return requests.post(ENDPOINT +'deletevending/', json=payload)  

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