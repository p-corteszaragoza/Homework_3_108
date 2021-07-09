from flask import Flask
from data import data
import json

app = Flask(__name__)

# dictionary
me = {
    "name": "Paola",
    "last": "Cortes",
    "email": "pcorteszaragoza@gmail.com"
}

# list
products = data
#["apple", "banana", "carrot"]


@app.route("/")
@app.route("/home")
def index():
    return "Hello from python on wsl"


@app.route("/about")
def about():
    return me


@app.route("/about/me")
def name():
    return me["name"]


@app.route("/about/fullname")
def fullname():
    return me["name"] + " " + me["last"]


@app.route("/api/catalog")
def get_catalog():
    return json.dumps(products)


@app.route("/api/categories")
def get_categories():
    unique_categories = []
    for prod in products:
        category = prod["category"]
        if category not in unique_categories:
            unique_categories.append(category)
    return json.dumps(unique_categories)


@app.route("/api/test")
def test():
    # add
    products.append("strawberry")
    products.append("dragon fruit")

    # length
    # print("You have: " + str(len(products))
    print(f"You have: {len(products)} products in your catalog")

    # iterate
    for fruit in products:
        print(fruit)

    # print the name 10 times
    for i in range(0, 10, 1):
        print(me["name"])

    # remove apple from the list
    products.remove("apple")

    # print the list
    for f in products:
        print(products)
    return "Check your terminal"


if __name__ == '__main__':
    app.run(debug=True)
