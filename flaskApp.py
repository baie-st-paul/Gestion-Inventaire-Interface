from flask import Flask, redirect, render_template, render_template_string, request, jsonify, url_for
from api import fetch_inventory
app = Flask(__name__)
import sys
import barcode
from barcode.writer import ImageWriter


@app.route('/')
def home_page():
    return render_template('home/index.html')

@app.route("/itemslistpage")
def items_list_page():
    items_list = fetch_inventory.all_inventory_items()
    return render_template('listItems/items_list.html', items_list=items_list, is_edit_page=False)

@app.route("/createitempage")
def create_item_page():
    ressource_type_list = fetch_inventory.get_all_ressource_types()
    local_list = fetch_inventory.get_all_locals()
    project_list = fetch_inventory.get_all_projects()
    state_list = fetch_inventory.get_all_states()
    status_list = fetch_inventory.get_all_status()
    return render_template('createItem/create_item.html', ressource_types=ressource_type_list, locals=local_list, projects=project_list, states=state_list, status=status_list)

@app.route("/createlistingpage")
def create_listing_page():
    return render_template('createListing/create_listing.html')

@app.route("/listingform/<string:selection>")
def listing_form(selection):
    return render_template_string("{% import '_macros.html' as macros %}{{ macros.create_listing_form(listing_type) }}", listing_type=selection)

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

@app.route("/createitem", methods=['POST'])
def create_item():
    file_data = request.files["image"].read()
    form_data = request.form
    item_id = fetch_inventory.add_item_to_inventory(form_data, file_data)
    return redirect(url_for("create_item_page"))

@app.route("/create_listing/<string:listing_type>", methods=['POST'])
def create_listing(listing_type):
    form_data = request.form
    if listing_type == "ressourceType":
        fetch_inventory.add_ressource_type(form_data["name"])
    elif listing_type == "local":
        fetch_inventory.add_local(form_data["name"])
    elif listing_type == "project":
        fetch_inventory.add_project(form_data["name"])
    return redirect(url_for("create_listing_page"))