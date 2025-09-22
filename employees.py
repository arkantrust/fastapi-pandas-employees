from uuid import uuid4, UUID
import pandas as pd
from db import get_db


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
