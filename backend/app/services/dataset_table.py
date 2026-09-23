import pandas as pd
from sqlalchemy import create_engine

from app.core.config import settings


engine = create_engine(settings.database_url)


def create_dataset_table(
    df: pd.DataFrame,
    table_name: str,
) -> None:
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="fail",
        index=False,
    )