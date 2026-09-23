from io import BytesIO

import pandas as pd
from fastapi import UploadFile

from app.db.database import SessionLocal
from app.services.dataset_ingestion import (
    extract_column_metadata,
    extract_dataset_metadata,
    load_csv,
)
from app.services.dataset_persistence import persist_dataset


def test_persist_dataset():
    csv_content = b"""order_id,revenue,region
1,100,West
2,250,East
3,175,West
"""

    file = UploadFile(
        filename="test.csv",
        file=BytesIO(csv_content),
    )

    db = SessionLocal()

    try:
        import asyncio

        df = asyncio.run(load_csv(file))
        metadata = extract_dataset_metadata(df, "test.csv")
        columns = extract_column_metadata(df)

        dataset = persist_dataset(
            db=db,
            df=df,
            metadata=metadata,
            columns=columns,
        )

        assert dataset.id is not None
        assert dataset.table_name == f"dataset_{dataset.id}"
        assert dataset.row_count == 3
        assert dataset.column_count == 3

    finally:
        db.close()