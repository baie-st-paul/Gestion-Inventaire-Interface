import urllib3, json



def all_inventory_items():
    response = urllib3.request("GET", "http://localhost:8081/api/v1/inventory/getAll")
    data = json.loads(response.data)
    return data