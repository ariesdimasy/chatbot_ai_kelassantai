import os 
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

X_API_KEY = os.getenv("X_API_KEY")