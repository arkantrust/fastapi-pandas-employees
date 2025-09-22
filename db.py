import pandas as pd


def create_db():
    # check if file exists, if not create it
    try:
        pd.read_csv("employees.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["id", "name", "role", "salary"])
        df.to_csv("employees.csv", index=False)


def get_db() -> pd.DataFrame:
    try:
        df = pd.read_csv("employees.csv")
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["id", "name", "role", "salary"])
