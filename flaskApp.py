from flask import Flask, render_template
from api import fetch_inventory
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home/index.html')

@app.route("/itemslist")
def items_list():
    items_list = fetch_inventory.all_inventory_items()
    return render_template('listItems/items_list.html', items_list=items_list)
