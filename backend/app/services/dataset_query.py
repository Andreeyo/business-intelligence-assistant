from sqlalchemy.orm import Session

from app.models.dataset import Dataset
from app.models.dataset_column import DatasetColumn

from app.repositories.dataset_repository import (
    get_datasets,
    get_dataset_by_id,
)

from app.repositories.dataset_column_repository import (
    get_columns_by_dataset_id,
)


def get_all_datasets(
    db: Session,
) -> list[Dataset]:
    return get_datasets(db)


def get_dataset(
    db: Session,
    dataset_id: int,
) -> Dataset | None:
    return get_dataset_by_id(
        db=db,
        dataset_id=dataset_id,
    )


def get_dataset_columns(
    db: Session,
    dataset_id: int,
) -> list[DatasetColumn]:
    return get_columns_by_dataset_id(
        db=db,
        dataset_id=dataset_id,
    )