import urllib3, json, base64

#ADDRESS = "http://localhost:8083" #dev
ADDRESS = "http://server:8081" #docker

def get_item(post_id):
    response = urllib3.request("GET", ADDRESS + "/api/v1/inventory/get/"+post_id)
    data = json.loads(response.data)
    return data

def all_inventory_items():
    response = urllib3.request("GET", ADDRESS + "/api/v1/inventory/getAll")
    data = json.loads(response.data)
    return data

def add_item_to_inventory(form_json, data):
    consumable = False
    if "consumable" in form_json:
        consumable = True
    
    encoded_body = json.dumps({
        "name": form_json["name"],
        "description": form_json["description"],
        "category": form_json["category"],
        "image": {
            "data": base64.b64encode(bytes(bytearray(data))).decode("utf-8"),
        },
        "quantity": form_json["quantity"],
        "location": form_json["location"],
        "ressourceType": form_json["ressourceType"],
        "local": form_json["local"],
        "status": form_json["status"],
        "consumable": consumable,
        "state": form_json["state"],
        "project": form_json["project"]
    })
    response = urllib3.request("POST", ADDRESS + "/api/v1/inventory/create",
                               headers={'Content-Type': 'application/json'},
                               body=encoded_body)
    data = json.loads(response.data)
    return data["id"]

def delete_item(post_id):
    response = urllib3.request("DELETE", ADDRESS + "/api/v1/inventory/delete/"+post_id)
    return response.data

def edit_item(form_json, post_id):
    encoded_body = json.dumps({
        "name": form_json["name"],
        "description": form_json["description"],
        "category": form_json["category"],
        "totalQuantity": form_json["totalQuantity"],
        "currentQuantity": form_json["currentQuantity"],
        "location": form_json["location"],
        "ressourceType": form_json["ressourceType"],
        "local": form_json["local"],
        "status": form_json["status"],
        "consumable": form_json["consumable"],
        "state": form_json["state"],
        "project": form_json["project"]
    })
    response = urllib3.request("PUT", ADDRESS + "/api/v1/inventory/update/"+post_id,
                               headers={'Content-Type': 'application/json'},
                               body=encoded_body)
    return response.data

def get_all_ressource_types():
    response = urllib3.request("GET", ADDRESS + "/api/v1/ressourcetype/getAll")
    return json.loads(response.data)

def get_all_locals():
    response = urllib3.request("GET", ADDRESS + "/api/v1/local/getAll")
    return json.loads(response.data)

def get_all_projects():
    response = urllib3.request("GET", ADDRESS + "/api/v1/project/getAll")
    return json.loads(response.data)

def get_all_states():
    response = urllib3.request("GET", ADDRESS + "/api/v1/state/getAll")
    return json.loads(response.data)

def get_all_status():
    response = urllib3.request("GET", ADDRESS + "/api/v1/status/getAll")
    return json.loads(response.data)

def add_ressource_type(name):
    encoded_body = json.dumps({
        "name": name
    })
    response = urllib3.request("POST", ADDRESS + "/api/v1/ressourcetype/create",
                               headers={'Content-Type': 'application/json'},
                               body=encoded_body)
    return response.data

def add_local(name):
    encoded_body = json.dumps({
        "name": name
    })
    response = urllib3.request("POST", ADDRESS + "/api/v1/local/create",
                               headers={'Content-Type': 'application/json'},
                               body=encoded_body)
    return response.data

def add_project(name):
    encoded_body = json.dumps({
        "name": name
    })
    response = urllib3.request("POST", ADDRESS + "/api/v1/project/create",
                               headers={'Content-Type': 'application/json'},
                               body=encoded_body)
    return response.data