import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    DEBUG = os.getenv("DEBUG", False)
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///fastsam.db")
    # Add other config settings as needed
