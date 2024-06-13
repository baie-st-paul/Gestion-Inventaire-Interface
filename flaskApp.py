from flask import Flask, render_template, request, jsonify
from api import fetch_inventory
app = Flask(__name__)
import sys


@app.route('/')
def home_page():
    return render_template('home/index.html')

@app.route("/itemslist")
def items_list():
    items_list = fetch_inventory.all_inventory_items()
    return render_template('listItems/items_list.html', items_list=items_list)

@app.route("/createitem")
def create_item():
    return render_template('createItem/create_item.html')

@app.route("/posttest", methods=['POST'])
def post_test():
    file_data = request.files["image"].read()
    form_data = request.form
    item_id = fetch_inventory.add_item_to_inventory(form_data, file_data)
    print(item_id, file=sys.stderr)
    return render_template('createItem/create_item.html')