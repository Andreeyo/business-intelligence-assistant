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

def get_columns_by_dataset_id(
    db: Session,
    dataset_id: int,
) -> list[DatasetColumn]:
    return (
        db.query(DatasetColumn)
        .filter(DatasetColumn.dataset_id == dataset_id)
        .order_by(DatasetColumn.id)
        .all()
    )