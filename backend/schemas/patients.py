from typing import Optional
from schemas.base import CustomBaseModel
from pydantic import Field


class Patient(CustomBaseModel):
    first_name: str
    last_name: str
    birthday: str
    email: str
    phone_number: str
    blood_type: str
    gender: str


class PatientCreateForm(Patient):
    id: Optional[int]
    created_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "birthday": "1990/01/01",
                "email": "john.doe@example.com",
                "blood_type": "AB+",
                "gender": "M",
                "phone_number": "123456789"
            }
        }
        extra = "forbid"