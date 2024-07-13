# API endpoints for data handling
from flask import Flask, request, jsonify
from flask_cors import CORS
from models.data_processing import load_data, preprocess_data
from models.model_inference import load_model, evaluate_model
import pandas as pd

app = Flask(__name__)
CORS(app)

# Example endpoint for loading and preprocessing data
@app.route('/api/load_data', methods=['GET'])
def load_and_process_data():
    data_path = 'path_to_your_data.csv'  # Provide your data path
    df = load_data(data_path)
    X, y = preprocess_data(df)
    return jsonify({'message': 'Data loaded and processed successfully'})

# Example endpoint for model evaluation
@app.route('/api/evaluate_model', methods=['POST'])
def evaluate_trained_model():
    # Provide your trained model path
    model_path = 'path_to_your_trained_model.pkl'  
    # Provide your data path
    data_path = 'path_to_your_data.csv' 

    # Load model
    model = load_model(model_path)

    # Load data
    df = pd.read_csv(data_path)
    X, y = preprocess_data(df)

    # Split data into training and testing sets (adjust as needed)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Evaluate model
    accuracy = evaluate_model(model, X_test, y_test)
    return jsonify({'accuracy': accuracy})

if __name__ == '__main__':
    app.run(debug=True)
