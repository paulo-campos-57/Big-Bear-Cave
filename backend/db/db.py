from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
print("Banco conectado em:", DATABASE_URL)

db = SQLAlchemy()