from flask import Flask, redirect, render_template, render_template_string, request, jsonify, url_for
from api import fetch_inventory
app = Flask(__name__)
import sys
import barcode
from barcode.writer import ImageWriter


@app.route('/')
def home_page():
    return render_template('home/index.html')

@app.route("/itemslist")
def items_list():
    items_list = fetch_inventory.all_inventory_items()
    return render_template('listItems/items_list.html', items_list=items_list, is_edit_page=False)

@app.route("/createitem")
def create_item():
    return render_template('createItem/create_item.html')

@app.route("/itemslist/edititem")
def item_list_edit():
    items_list = fetch_inventory.all_inventory_items()
    return render_template('listItems/items_list.html', items_list=items_list, is_edit_page=True)

@app.route("/itemslist/editrow/<string:post_id>", methods=["GET"])
def edit_row(post_id):
    item = fetch_inventory.get_item(post_id)
    return render_template_string("{% import '_macros.html' as macros %}{{ macros.edit_item_row(item) }}", item=item)

@app.route("/itemslist/edit/<string:post_id>", methods=["DELETE", "PUT"])
def edit_item(post_id):
    if request.method == "DELETE":
        fetch_inventory.delete_item(post_id)
        return ""
    if request.method == "PUT":
        fetch_inventory.edit_item(request.get_json(), post_id)
        item = fetch_inventory.get_item(post_id)
        return render_template_string("{% import '_macros.html' as macros %}{{ macros.item_row(item, is_edit_page) }}", item=item, is_edit_page=True)
    return redirect(url_for('items_list'))

@app.route("/posttest", methods=['POST'])
def post_test():
    file_data = request.files["image"].read()
    form_data = request.form
    item_id = fetch_inventory.add_item_to_inventory(form_data, file_data)
    
   # EAN = barcode.get_barcode_class('ean13')
   # ean = EAN(str(item_id), writer=ImageWriter())
   # ean.save('barcode')
    return redirect(url_for("create_item"))