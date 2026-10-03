from sqlalchemy.orm import Session

from app.models.dataset import Dataset

def create_dataset(
        db: Session,
        name: str,
        table_name: str | None,
        row_count: int,
        column_count: int,
) -> Dataset:

    dataset = Dataset(
        name=name,
        table_name=table_name,
        row_count=row_count,
        column_count=column_count,
    )

    db.add(dataset)
    db.flush()

    return dataset

def get_datasets(
    db: Session,
) -> list[Dataset]:
    return (
        db.query(Dataset)
        .order_by(Dataset.id)
        .all()
    )


def get_dataset_by_id(
    db: Session,
    dataset_id: int,
) -> Dataset | None:
    return (
        db.query(Dataset)
        .filter(Dataset.id == dataset_id)
        .first()
    )