# Functions for model inference
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib  # Use joblib for model loading if using scikit-learn

def load_model(model_path):
    """
    Function to load a pre-trained machine learning model.
    
    Parameters:
    - model_path (str): Path to the trained model file.
    
    Returns:
    - model: Loaded machine learning model object.
    """
    model = joblib.load(model_path)  # Adjust based on your model loading approach
    return model

def evaluate_model(model, X_test, y_test):
    """
    Function to evaluate a machine learning model.
    
    Parameters:
    - model: Trained machine learning model object.
    - X_test (pd.DataFrame): Features DataFrame for testing.
    - y_test (pd.Series): Target Series for testing.
    
    Returns:
    - accuracy (float): Accuracy score of the model on the test data.
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

if __name__ == '__main__':
    # Example usage
    model_path = 'path_to_your_trained_model.pkl'  # Provide your trained model path
    data_path = 'path_to_your_data.csv'  # Provide your data path

    # Load model
    model = load_model(model_path)

    # Load data
    df = pd.read_csv(data_path)
    X, y = preprocess_data(df)  # Assuming preprocess_data function from data_processing.py

    # Split data into training and testing sets (adjust as needed)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Evaluate model
    accuracy = evaluate_model(model, X_test, y_test)
    print(f'Model accuracy on test data: {accuracy}')
