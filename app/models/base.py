from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from app.database import Base


class BaseModel(Base):
    """Modèle de base avec les champs communs."""
    __abstract__ = True
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    def save(self, db_session):
        """Sauvegarde l'objet en base de données."""
        db_session.add(self)
        db_session.commit()
        db_session.refresh(self)
        return self
    
    def delete(self, db_session):
        """Supprime l'objet de la base de données."""
        db_session.delete(self)
        db_session.commit()
        return True