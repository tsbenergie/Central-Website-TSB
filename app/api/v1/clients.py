from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_clients():
    return {"message": "Liste des clients"}
