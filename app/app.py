from flask import Flask, jsonify, request
import joblib

app = Flask(__name__)

# Load the machine learning model
model = joblib.load('F:\My Projects\LPrediction\pklFiles\RandomForestClassifier_loan_prediction_model.pkl')

@app.route('/api/predict_loan', methods=['POST'])
def predict_loan():
    # Get the input data from the request
    data = request.json
    gender = data.get('gender')
    married = data.get('married')
    dependents = data.get('dependents')
    education = data.get('education')
    self_employed = data.get('self_employed')
    applicant_income = data.get('applicant_income')
    coapplicant_income = data.get('coapplicant_income')
    loan_amount = data.get('loan_amount')
    loan_term = data.get('loan_term')
    credit_history = data.get('credit_history')
    property_area = data.get('property_area')

    # Make the loan prediction
    prediction = model.predict([[gender, married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_term, credit_history, property_area]])

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
