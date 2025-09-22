from uuid import UUID
from db import create_db, get_db
from employees import (
    AddEmployeeRequest,
    Employee,
    add_employee,
    delete_employee,
    get_average_salary_by_role,
    get_employee_by_id,
)
from fastapi import FastAPI
from fastapi.responses import JSONResponse


create_db()

app = FastAPI()


@app.get("/api/employees")
def get_employees() -> list[Employee]:
    employees = get_db().to_dict(orient="records")
    return [Employee(**e) for e in employees]  # type: ignore


@app.post("/api/employees")
def create_employee(employee: AddEmployeeRequest):
    id = add_employee(employee.name, employee.role, employee.salary)
    e = Employee(
        id=str(id),
        name=employee.name,
        role=employee.role,
        salary=employee.salary,
    )
    return e


@app.get("/api/employees/{employee_id}")
def get_employee(employee_id: str):
    try:
        employee_uuid = UUID(employee_id)
    except ValueError:
        return JSONResponse({"error": "Invalid employee ID"}, status_code=400)
    e = get_employee_by_id(employee_uuid)
    if not e:
        return JSONResponse({"error": "Employee not found"}, status_code=404)
    return e


@app.delete("/api/employees/{employee_id}")
def remove_employee(employee_id: str):
    df = get_db()
    if df[df["id"] == employee_id].empty:
        return JSONResponse({"error": "Employee not found"}, status_code=404)
    delete_employee(employee_id)
    return JSONResponse({"message": f"Employee with ID {employee_id} deleted."})


@app.get("/api/analytics/average-salary-by-role")
def average_salary_by_role():
    avg_salaries = get_average_salary_by_role()
    return JSONResponse(
        [
            {"role": role, "average_salary": float(salary)}
            for role, salary in avg_salaries.items()
        ]
    )
