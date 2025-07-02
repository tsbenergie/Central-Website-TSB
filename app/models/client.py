from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.models.base import BaseModel


class ClientStatus(str, enum.Enum):
    ACTIF = "Actif"
    PROSPECT = "Prospect" 
    INACTIF = "Inactif"


class ClientSector(str, enum.Enum):
    BTP = "BTP"
    TRAVAUX_PUBLICS = "Travaux Publics"
    DEMOLITION = "Démolition"
    TERRASSEMENT = "Terrassement"
    AUTRE = "Autre"


class Client(BaseModel):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(200), nullable=False, index=True)
    contact = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    telephone = Column(String(20), nullable=False)
    adresse = Column(Text, nullable=False)
    
    # Informations commerciales
    statut = Column(Enum(ClientStatus), default=ClientStatus.PROSPECT, nullable=False)
    secteur = Column(Enum(ClientSector), default=ClientSector.AUTRE, nullable=False)
    chiffre_affaires = Column(Float, default=0.0)
    nb_projets = Column(Integer, default=0)
    
    # Suivi commercial
    commercial = Column(String(100))
    dernier_contact = Column(DateTime(timezone=True), server_default=func.now())
    
    # Informations complémentaires
    siret = Column(String(14), unique=True)
    tva_intracommunautaire = Column(String(20))
    notes = Column(Text)
    
    # Relations
    quotes = relationship("Quote", back_populates="client", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Client(nom='{self.nom}', email='{self.email}', statut='{self.statut}')>"
    
    @property
    def statut_color(self):
        """Retourne la couleur associée au statut du client."""
        colors = {
            ClientStatus.ACTIF: "success",
            ClientStatus.PROSPECT: "warning", 
            ClientStatus.INACTIF: "secondary"
        }
        return colors.get(self.statut, "secondary")
    
    def to_dict(self):
        """Convertit l'objet en dictionnaire."""
        return {
            "id": self.id,
            "nom": self.nom,
            "contact": self.contact,
            "email": self.email,
            "telephone": self.telephone,
            "adresse": self.adresse,
            "statut": self.statut.value,
            "secteur": self.secteur.value,
            "chiffre_affaires": self.chiffre_affaires,
            "nb_projets": self.nb_projets,
            "commercial": self.commercial,
            "dernier_contact": self.dernier_contact.isoformat() if self.dernier_contact else None,
            "siret": self.siret,
            "tva_intracommunautaire": self.tva_intracommunautaire,
            "notes": self.notes,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }