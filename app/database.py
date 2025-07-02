from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings  # Assure-toi que config.py est au même niveau que database.py

# Crée le moteur SQLAlchemy avec l'URL depuis les settings
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)

# Crée une session locale configurée
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base pour les modèles ORM
Base = declarative_base()

# Dépendance FastAPI pour avoir une session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
