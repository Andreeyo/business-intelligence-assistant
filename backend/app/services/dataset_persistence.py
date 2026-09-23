import pandas as pd
from sqlalchemy.orm import Session

from app.repositories.dataset_column_repository import (
    create_dataset_columns,
)
from app.repositories.dataset_repository import create_dataset
from app.services.dataset_table import create_dataset_table


def persist_dataset(
    db: Session,
    df: pd.DataFrame,
    metadata: dict,
    columns: list[dict],
):
    dataset = create_dataset(
        db=db,
        name=metadata["name"],
        table_name=None,
        row_count=metadata["row_count"],
        column_count=metadata["column_count"],
    )

    dataset.table_name = f"dataset_{dataset.id}"
    db.flush()

    create_dataset_table(
        df=df,
        table_name=dataset.table_name,
    )

    create_dataset_columns(
        db=db,
        dataset_id=dataset.id,
        columns=columns,
    )

    db.commit()

    return dataset