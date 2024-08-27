import os

class Config:
    # Use an environment variable for the secret key, fallback to a random key for security
    SECRET_KEY = os.environ.get('qwui') or os.urandom(24)
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///employees.db'  # You can change this to your preferred DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Uploads configuration
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'UPLOAD_FOLDER')  # Folder for saving uploaded CSV files
    
    # Allowed file extensions for uploads
    ALLOWED_EXTENSIONS = {'csv'}  # We are allowing only CSV files for this project
