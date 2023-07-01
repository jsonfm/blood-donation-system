from fastapi import APIRouter, Form
from database import db
from schemas.patients import PatientCreateForm



router = APIRouter(prefix="/patients")



@router.get('/')
def get_patients():
    columns = ["first_name", "last_name", "birthday"]
    sql_columns = ",".join(columns)
    response = db.execute_query(f"SELECT {sql_columns} FROM patients", columns=columns)
    return response


@router.post('/')
def create_patient(patient: PatientCreateForm):
    sql = f"""
    INSERT INTO patients (first_name, last_name, gender, email, phone_number, birthday, blood_type)
    VALUES ('{patient.first_name}', '{patient.last_name}', '{patient.gender}', '{patient.email}', '{patient.phone_number}', '{patient.birthday}', '{patient.blood_type}');
    """
    print("--> sql: ", sql)
    try:
        response = db.execute_query(sql)
        print("response: ", response)
    except Exception as e:
        print("--> error: ", e)
    return "created"


@router.put("/{patient_id}")
def update_patient(patient_id: int):
    return f"updated {patient_id}"


@router.delete("/{patient_id}")
def delete_patient(patient_id: int):
    return f"deleted {patient_id}"