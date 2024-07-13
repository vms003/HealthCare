# Unit tests for model inference
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib  # Use joblib for model loading if using scikit-learn

def load_data(file_path):
    """
    Function to load data from a CSV file.
    
    Parameters:
    - file_path (str): Path to the CSV file.
    
    Returns:
    - df (pd.DataFrame): Loaded DataFrame containing the data.
    """
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    """
    Function to preprocess data for machine learning models.
    This function can be customized based on your specific data preprocessing needs.
    
    Parameters:
    - df (pd.DataFrame): DataFrame containing the loaded data.
    
    Returns:
    - X (pd.DataFrame): Features DataFrame.
    - y (pd.Series): Target Series.
    """
    # Example: Assuming 'X' contains features and 'y' contains labels
    X = df.drop('label', axis=1)  # Adjust based on your dataset structure
    y = df['label']
    return X, y

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
    data_path = 'path_to_your_data.csv'  # Provide your data path
    model_path = 'path_to_your_trained_model.pkl'  # Provide your trained model path

    # Load data
    df = load_data(data_path)
    X, y = preprocess_data(df)

    # Split data into training and testing sets (adjust as needed)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Load trained model
    model = joblib.load(model_path)  # Adjust based on your model loading approach

    # Evaluate model
    accuracy = evaluate_model(model, X_test, y_test)
    print(f'Model accuracy on test data: {accuracy}')

