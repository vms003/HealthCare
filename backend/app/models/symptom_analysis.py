import nltk
import string
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

nltk.download('punkt')
nltk.download('stopwords')

# Example function to train and save the symptom analysis model
def train_symptom_analysis_model(data_path):
    # Load your dataset
    df = pd.read_csv(data_path)  # Replace with your actual data loading logic

    # Example dataset columns: 'text' for symptoms and 'label' for categories
    X = df['text']
    y = df['label']

    # Preprocessing function for text data
    def preprocess_text(text):
        text = text.lower()  # Convert text to lowercase
        text = re.sub(r'\d+', '', text)  # Remove numbers
        text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
        return text

    # Initialize TF-IDF vectorizer and Random Forest classifier pipeline
    model = Pipeline([
        ('tfidf', TfidfVectorizer(preprocessor=preprocess_text, stop_words='english')),
        ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate model performance
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model accuracy: {accuracy}')

    # Save the trained model (optional)
    # joblib.dump(model, 'symptom_analysis_model.joblib')

    return model

# Example function for inference with the trained model
def analyze_symptoms(symptoms_data, model):
    # Example symptom analysis code using the trained model
    symptoms_text = pd.Series(symptoms_data)
    predictions = model.predict(symptoms_text)
    return predictions.tolist()

# Example usage (for training and testing)
if __name__ == '__main__':
    trained_model = train_symptom_analysis_model('path_to_your_data.csv')  # Provide your data path
