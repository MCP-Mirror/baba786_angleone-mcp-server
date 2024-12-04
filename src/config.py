import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # AngleOne Credentials
    API_KEY = os.getenv('ANGLEONE_API_KEY')
    CLIENT_ID = os.getenv('ANGLEONE_CLIENT_ID')
    PASSWORD = os.getenv('ANGLEONE_PASSWORD')
    TOKEN = os.getenv('ANGLEONE_TOKEN')
    
    # Server Configuration
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', '8000'))
    
    # Validate configuration
    @classmethod
    def validate(cls):
        required_vars = ['API_KEY', 'CLIENT_ID', 'PASSWORD', 'TOKEN']
        missing = [var for var in required_vars if not getattr(cls, var)]
        if missing:
            raise ValueError(f'Missing required environment variables: {missing}')
