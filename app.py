from flask import Flask, render_template, request,jsonify

from chat import chatbot
from chat import get_response


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('base.html')


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # check if message is valid
    response = get_response(text)
    if(response):
        message = {"answer":response}
    else:
        response = chatbot(text)
        message = {"answer":response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)