from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('rabbit_model.pkl', 'rb'))

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    height = int(request.form['height'])
    width = int(request.form['width'])
    prediction = model.predict([[height, width]])
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text=f'A rabbit with {height} height and {width} width has a value of {output}kg')

if __name__ == "__main__":
    app.run()
