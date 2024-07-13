# Diagnostic decision support models (ML)
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Example function to train and save the model
def train_diagnosis_model(data_path):
    # Load your dataset
    df = pd.read_csv(data_path)  # Replace with your actual data loading logic

    # Assume 'X' contains features and 'y' contains labels (diagnoses)
    X = df.drop('diagnosis', axis=1)  # Adjust according to your dataset structure
    y = df['diagnosis']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize ExtraTreesClassifier
    model = ExtraTreesClassifier(n_estimators=100, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate model performance
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model accuracy: {accuracy}')

    # Save the trained model (optional)
    # You can save the model using joblib or pickle for later use
    # joblib.dump(model, 'diagnosis_model.joblib')

    return model

# Example function for inference with the trained model
def predict_diagnosis(patient_data):
    # Load your trained model (if not training in the same script)
    # model = joblib.load('diagnosis_model.joblib')

    # Example inference code (adjust as per your data preprocessing and model requirements)
    patient_features = pd.DataFrame([patient_data])  # Assuming patient_data is a dictionary or list
    diagnosis_prediction = model.predict(patient_features)

    return diagnosis_prediction[0]  # Return the predicted diagnosis

# Example usage (for training and testing)
if __name__ == '__main__':
    trained_model = train_diagnosis_model('path_to_your_data.csv')  # Provide your data path
