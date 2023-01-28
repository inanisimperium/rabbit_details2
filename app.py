#import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    height = float(request.form['height'])
    width = float(request.form['width'])
    prediction = model.predict([[height, width]])
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text=f'{output}')

if __name__ == "__main__":
    app.run()
