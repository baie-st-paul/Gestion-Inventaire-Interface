import urllib3, json, base64



def all_inventory_items():
    response = urllib3.request("GET", "http://localhost:8081/api/v1/inventory/getAll")
    data = json.loads(response.data)
    return data

def add_item_to_inventory(form_json, data):
    encoded_body = json.dumps({
        "name": form_json["name"],
        "description": form_json["description"],
        "category": form_json["category"],
        "image": {
            "data": base64.b64encode(bytes(bytearray(data))).decode("utf-8"),
        },
        "quantity": form_json["quantity"],
        "location": form_json["location"]
    })
    response = urllib3.request("POST", "http://localhost:8081/api/v1/inventory/create",
                               headers={'Content-Type': 'application/json'},
                               body=encoded_body
                            )
    
    data = json.loads(response.data)
    return data["id"]

def delete_item(post_id):
    response = urllib3.request("DELETE", "http://localhost:8081/api/v1/inventory/delete/"+post_id)
    return response.data