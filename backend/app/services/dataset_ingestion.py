import pandas as pd
from fastapi import UploadFile

async def load_csv(file: UploadFile) -> pd.DataFrame:
    if not file.filename:
        raise ValueError("A file name is required.")
    
    if not file.filename.lower().endswith(".csv"):
        raise ValueError("Only CSV files are supported")

    contents = await file.read()

    if not contents:
        raise ValueError("The uploaded files are empty.")

    from io import BytesIO

    return pd.read_csv(BytesIO(contents))


def extract_dataset_metadata(df: pd.DataFrame, filename: str) -> dict:
    return{
        "name": filename,
        "row_count": len(df),
        "column_count": len(df.columns),
    }


def extract_column_metadata(df):
    columns = []

    for column in df.columns:
        columns.append(
            {
                "column_name": column,
                "data_type": str(df[column].dtype),
                "nullable": bool(df[column].isnull().any(),)
            }
        )

    return columns

