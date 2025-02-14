""" Program for loading a file """

import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    """ def load(path: str) -> pd.core.frame.DataFrame:
    Function who load the csv file """
    csv = ""
    try:
        csv = pd.read_csv(path)
        print("Loading dataset of dimensions", csv.shape)
    except FileNotFoundError:
        print("File not found.")
    except pd.errors.EmptyDataError:
        print("No data")
    except pd.errors.ParserError:
        print("Parse error")
    except Exception:
        print("Some other exception")
    return csv
