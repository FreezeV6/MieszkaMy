import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Paths
TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(os.path.join(__file__, '..'))), r'templates')
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(os.path.join(__file__, '..'))), r'static')

# Database path
DB_PATH = os.getenv('DB_PATH', 'sqlite:///default.db')  # Default to SQLite if DB_PATH is not set

# App secret key
KEY = os.getenv('APP_KEY', 'default-secret-key')  # Default to a placeholder key
