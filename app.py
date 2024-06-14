from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the Lasso Regression model
with open('lasso_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract form data
    data = {
        'Year': int(request.form['Year']),
        'Present_Price': float(request.form['Present_Price']),
        'Kms_Driven': int(request.form['Kms_Driven']),
        'Fuel_Type': int(request.form['Fuel_Type']),
        'Seller_Type': int(request.form['Seller_Type']),
        'Transmission': int(request.form['Transmission']),
        'Owner': int(request.form['Owner'])
    }
    
    # Convert data to DataFrame
    input_data = pd.DataFrame([data])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Return predicted price as JSON response
    return jsonify({'price': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
