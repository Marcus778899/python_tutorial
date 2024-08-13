import json
from flask import Flask,make_response
import requests

app = Flask(__name__)

@app.route("/cafe_taipei", methods=['GET'])
def get_cafe_info_taipei():
    url = "https://cafenomad.tw/api/v1.2/cafes/taipei"
    response = requests.get(url)

    response = make_response(json.dumps(response.json(), ensure_ascii=False))

    response.headers["Content-Type"] = "application/json"
    response.headers["Access-Control-Allow-Origin"] = "*"

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)