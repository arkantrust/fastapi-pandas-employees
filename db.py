import pandas as pd


def create_db():
    try:
        with open("employees.csv", "x") as file:
            file.write("id,name,role,salary\n")
    except FileExistsError:
        print("Error: The file 'employees.csv' already exists.")


def get_db() -> pd.DataFrame:
    try:
        df = pd.read_csv("employees.csv")
        return df
    except FileNotFoundError:
        print("Error: The file 'employees.csv' does not exist.")
        return pd.DataFrame(columns=["id", "name", "role", "salary"])
