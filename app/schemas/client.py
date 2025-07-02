from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date
import enum

class ClientStatus(str, enum.Enum):
    """Enum for client status, matching the model."""
    ACTIF = "Actif"
    PROSPECT = "Prospect"
    INACTIF = "Inactif"

# --- Base Schema ---
# Contains fields that are common to other schemas.
class ClientBase(BaseModel):
    nom: str = Field(..., min_length=3, max_length=100, description="Nom de l'entreprise cliente")
    contact: Optional[str] = Field(None, max_length=100, description="Nom de la personne de contact")
    email: Optional[EmailStr] = Field(None, description="Email de contact")
    telephone: Optional[str] = Field(None, max_length=20, description="Numéro de téléphone")
    adresse: Optional[str] = Field(None, max_length=255, description="Adresse postale du client")
    secteur: Optional[str] = Field(None, max_length=50, description="Secteur d'activité (BTP, Démolition, etc.)")
    commercial: Optional[str] = Field(None, max_length=100, description="Commercial assigné")

# --- Create Schema ---
# Used when creating a new client via the API. Inherits from Base.
class ClientCreate(ClientBase):
    statut: ClientStatus = Field(ClientStatus.PROSPECT, description="Statut initial du client")

# --- Update Schema ---
# Used when updating an existing client. All fields are optional.
class ClientUpdate(BaseModel):
    nom: Optional[str] = Field(None, min_length=3, max_length=100)
    contact: Optional[str] = Field(None, max_length=100)
    email: Optional[EmailStr] = None
    telephone: Optional[str] = Field(None, max_length=20)
    adresse: Optional[str] = Field(None, max_length=255)
    secteur: Optional[str] = Field(None, max_length=50)
    commercial: Optional[str] = Field(None, max_length=100)
    statut: Optional[ClientStatus] = None
    chiffre_affaires: Optional[float] = Field(None, ge=0)
    nb_projets: Optional[int] = Field(None, ge=0)
    dernier_contact: Optional[date] = None

# --- Read Schema ---
# This is the main schema for returning client data from the API.
# It includes the 'id' and other fields from the database model.
class Client(ClientBase):
    id: int
    statut: ClientStatus
    chiffre_affaires: float = 0.0
    nb_projets: int = 0
    dernier_contact: Optional[date] = None

    class Config:
        # This tells Pydantic to read the data even if it is not a dict,
        # but an ORM model (or any other arbitrary object with attributes).
        from_attributes = True
