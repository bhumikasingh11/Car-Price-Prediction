from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        present_price = float(request.form['present_price'])
        kms_driven = int(request.form['kms_driven'])
        owner = int(request.form['owner'])
        years_used = int(request.form['years_used'])

        fuel_type = request.form['fuel_type']
        seller_type = request.form['seller_type']
        transmission = request.form['transmission']

        fuel_diesel = 1 if fuel_type == 'Diesel' else 0
        fuel_petrol = 1 if fuel_type == 'Petrol' else 0
        seller_individual = 1 if seller_type == 'Individual' else 0
        transmission_manual = 1 if transmission == 'Manual' else 0

        features = np.array([[present_price,
                               kms_driven,
                               owner,
                               years_used,
                               fuel_diesel,
                               fuel_petrol,
                               seller_individual,
                               transmission_manual]])

        prediction = model.predict(features)
        output = round(prediction[0], 2)

        return render_template(
            "index.html",
            prediction_text=f"Predicted Price: ₹ {output} Lakhs"
        )

    except Exception as e:
        print(e)
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)