from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:int

def patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)

patient_info = {"name":"kalpesh", "age":25}

patient1 = Patient(**patient_info)
