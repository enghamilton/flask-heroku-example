"""Flask App Project."""

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    json_data = {'products':[{'pid':1,'username':'user 01'},{'pid':2,'username':'user 02'},{'pid':3,'username':'user 03'}],'success':1}
    return jsonify(json_data)


if __name__ == '__main__':
    app.run()
