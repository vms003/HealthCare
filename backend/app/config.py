# Configuration settings :In a Flask application, config.py typically stores configuration variables and settings. 
#                         These settings can include things like database connections, API keys, and other environment-specific
#                         configurations. Here’s a basic example of a config.py file for your healthcare project
import os

class Config:
    DEBUG = True  # Enable debug mode for development
    SECRET_KEY = 'your_secret_key_here'  # Replace with a secure secret key

    # Example database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Example machine learning model configuration
    MODEL_PATH = 'path_to_your_trained_model.pkl'
    DATA_PATH = 'path_to_your_data.csv'

    # Flask-CORS configuration
    CORS_HEADERS = 'Content-Type'

    # Add more configurations as needed

class ProductionConfig(Config):
    DEBUG = False
    # Add production-specific configurations

class DevelopmentConfig(Config):
    DEBUG = True
    # Add development-specific configurations

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
