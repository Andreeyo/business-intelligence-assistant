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