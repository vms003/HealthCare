from flask import Flask, request, jsonify
from flask_cors import CORS
from models.symptom_analysis import analyze_symptoms
from models.image_analysis import analyze_image
from models.diagnostic_support import predict_diagnosis
from services.data_processing import preprocess_data

app = Flask(__name__)
CORS(app)

# Example endpoint for symptom analysis
@app.route('/api/analyze_symptoms', methods=['POST'])
def analyze_symptoms_endpoint():
    data = request.get_json()
    symptoms = data['symptoms']

    # Analyze symptoms using the trained model
    results = analyze_symptoms(symptoms, trained_model)

    return jsonify({'results': results})

# Example endpoint for image analysis
@app.route('/api/analyze_image', methods=['POST'])
def analyze_image_endpoint():
    # Assuming image file is sent as multipart form-data
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the uploaded image to a temporary location
    image_path = '/tmp/uploaded_image.png'  # Adjust as needed
    file.save(image_path)

    # Analyze the image using the trained model
    result = analyze_image(image_path, trained_model)

    return jsonify({'result': result})

# Example endpoint for diagnostic support
@app.route('/api/predict_diagnosis', methods=['POST'])
def predict_diagnosis_endpoint():
    data = request.get_json()
    patient_data = data['patient_data']
    processed_data = preprocess_data(patient_data)
    diagnosis = predict_diagnosis(processed_data)
    return jsonify({'diagnosis': diagnosis})

if __name__ == '__main__':
    app.run(debug=True)
