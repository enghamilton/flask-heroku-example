"""Flask App Project."""

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    json_data = { "products":[{"pid":"1","name":"Pizza Portuguesa1","price":"23.50","description":"Queijo mussarela, presunto, ovos, ervilhas, palmito, cebola, oregano, azeitona."},{"pid":"2","name":"pizza 2","price":"23.99","description":"ingrediente 2"},{"pid":"3","name":"pizza 1","price":"23.00","description":"ingrediente 1"},{"pid":"4","name":"pizza 3","price":"12.00","description":"ingrediente da pizza 3"}],"success":1 }
    return jsonify(json_data)


if __name__ == '__main__':
    app.run()
