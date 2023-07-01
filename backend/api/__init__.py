from fastapi import APIRouter
from api.patients import router as patients_router


router = APIRouter()
router.include_router(patients_router)
