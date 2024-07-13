# Unit tests for data processingimport pandas as pd
from sklearn.model_selection import train_test_split

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
    - X_train, X_test, y_train, y_test (tuple): Split data into train and test sets.
    """
    # Example: Assuming 'X' contains features and 'y' contains labels
    X = df.drop('label', axis=1)  # Adjust based on your dataset structure
    y = df['label']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    # Example usage
    data_path = 'path_to_your_data.csv'  # Provide your data path
    df = load_data(data_path)
    X_train, X_test, y_train, y_test = preprocess_data(df)

    # Print some information about the processed data
    print(f'Train data shape: {X_train.shape}, Test data shape: {X_test.shape}')
    print(f'Example features: {X_train.head()}')
    print(f'Example labels: {y_train.head()}')
