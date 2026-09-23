from sqlalchemy.orm import Session

from app.models.dataset_column import DatasetColumn

def create_dataset_columns(
        db: Session,
        dataset_id: int,
        columns: list[dict],
) -> None:

    records = [
        DatasetColumn(
            dataset_id=dataset_id,
            column_name=column["column_name"],
            data_type=column["data_type"],
            nullable=column["nullable"],
        )
        for column in columns
    ]

    db.add_all(records)
    db.flush()