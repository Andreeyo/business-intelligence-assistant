import pandas as pd
from fastapi import UploadFile, HTTPException
from pandas.errors import EmptyDataError, ParserError

async def load_csv(file: UploadFile) -> pd.DataFrame:
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="A file name is required.",
            )
    
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are supported",
            )

    contents = await file.read()

    if not contents:
        raise HTTPException(
            status_code=400,
            detail="The uploaded file is empty.",
            )


    from io import BytesIO

    try:
        df = pd.read_csv(BytesIO(contents))

        if df.empty:
            raise HTTPException(
                status_code=400,
                detail="The uploaded CSV file contains no data rows"
            )
        return df
    except EmptyDataError:
        raise HTTPException(
            status_code=400,
            detail="The uploaded CSV file is empty"
        )
    except ParserError:
        raise HTTPException(
            status_code=400,
            detail="The uploaded CSV file is invalid"
        )
    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="The uploaded CSV file could not be decoded"
        )



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

