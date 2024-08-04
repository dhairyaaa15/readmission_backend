from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model (replace 'model.sav' with your actual model filename)
model = joblib.load('logisticmodel.sav')

@app.route('/')
def welcome():
    return "Welcome to the Patient Readmission Prediction Application!"

# Define the predict endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = request.json

        # Convert JSON data to DataFrame
        df = pd.DataFrame([data])

        # Ensure the columns match the features used during training
        expected_features = ['age', 'time_in_hospital', 'num_procedures', 'num_medications', 
                             'number_outpatient_log1p', 'number_emergency_log1p', 
                             'number_inpatient_log1p', 'number_diagnoses', 'metformin', 
                             'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 
                             'glipizide', 'glyburide', 'pioglitazone', 'rosiglitazone', 
                             'acarbose', 'tolazamide', 'insulin', 'glyburide-metformin', 
                             'AfricanAmerican', 'Asian', 'Caucasian', 'Hispanic', 'Other', 
                             'gender_1', 'admission_type_id_3', 'admission_type_id_5', 
                             'discharge_disposition_id_2', 'discharge_disposition_id_7', 
                             'discharge_disposition_id_10', 'discharge_disposition_id_18', 
                             'admission_source_id_4', 'admission_source_id_7', 
                             'admission_source_id_9', 
                             'A1Cresult_1', 'num_medications|time_in_hospital', 
                             'num_medications|num_procedures', 'time_in_hospital|num_lab_procedures', 
                             'num_medications|num_lab_procedures', 'num_medications|number_diagnoses', 
                             'age|number_diagnoses', 'change|num_medications', 
                             'number_diagnoses|time_in_hospital', 'num_medications|numchange', 
                             'level1_diag1_1.0', 'level1_diag1_2.0', 'level1_diag1_3.0', 
                             'level1_diag1_4.0', 'level1_diag1_5.0', 'level1_diag1_6.0', 
                             'level1_diag1_7.0', 'level1_diag1_8.0']

        # Ensure the input data has all required features
        df = df.reindex(columns=expected_features, fill_value=0)

        # Make prediction
        prediction = model.predict(df)
        prediction_proba = model.predict_proba(df)

        # Return the prediction as JSON
        return jsonify({
            'prediction': int(prediction[0]), 
            'probability': prediction_proba[0].tolist()
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
