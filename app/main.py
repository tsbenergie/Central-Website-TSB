from fastapi import FastAPI
from app.database import engine, Base
from app.api.v1 import clients  # <-- import absolu ici

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GestionPro API",
    description="API pour l'application de gestion de projets et de flotte.",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "clients",
            "description": "Opérations concernant les clients.",
        },
        {
            "name": "Root",
            "description": "Point d'entrée de l'API.",
        },
    ]
)

app.include_router(clients.router, prefix="/api/v1/clients", tags=["clients"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bienvenue sur l'API GestionPro"}
