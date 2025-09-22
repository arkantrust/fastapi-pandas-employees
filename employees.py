from uuid import uuid4, UUID
import pandas as pd
from db import get_db
from pydantic import BaseModel


class AddEmployeeRequest(BaseModel):
    name: str
    role: str
    salary: float


class Employee(AddEmployeeRequest):
    id: str


def get_employee_by_id(employee_id: UUID) -> Employee | None:
    df = get_db()
    employee = df[df["id"] == str(employee_id)]
    if employee.empty:
        print(employee)
        return None
    return Employee(**employee.iloc[0].to_dict())


def add_employee(name: str, role: str, salary: float) -> UUID:
    df = get_db()
    new_id = uuid4()
    new_employee = pd.DataFrame(
        [[new_id, name, role, salary]], columns=["id", "name", "role", "salary"]
    )
    df = pd.concat([df, new_employee], ignore_index=True)
    df.to_csv("employees.csv", index=False)
    return new_id


def delete_employee(id: str):
    df = get_db()
    df = df[df["id"] != id]
    df.to_csv("employees.csv", index=False)


def get_average_salary_by_role():
    df = get_db()
    roles = df.groupby("role")
    return roles["salary"].mean()
