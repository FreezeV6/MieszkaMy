import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Paths
TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(os.path.join(__file__, '..'))), r'templates')
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(os.path.join(__file__, '..'))), r'static')

# Database path
DB_PATH = os.getenv('DB_PATH')

# App secret key
KEY = os.getenv('APP_KEY')

# Mail
MAIL_API_KEY = os.getenv('MAIL_API_KEY')
MAIL_API_SECRET = os.getenv('MAIL_API_SECRET')

EMAIL = os.getenv('EMAIL')
