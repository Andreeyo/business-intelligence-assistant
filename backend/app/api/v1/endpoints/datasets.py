from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.dataset import ( DatasetUploadResponse, DatasetResponse, DatasetDetailResponse, DatasetColumnResponse)
from app.services.dataset_ingestion import (
    extract_column_metadata,
    extract_dataset_metadata,
    load_csv,
)
from app.services.dataset_persistence import persist_dataset
from app.services.dataset_query import (
    get_all_datasets,
    get_dataset,
    get_dataset_columns,
)

router = APIRouter()

@router.post(
    "/upload",
    response_model=DatasetUploadResponse,
)
async def upload_dataset(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
) -> DatasetUploadResponse:
    df = await load_csv(file)

    metadata = extract_dataset_metadata(
        df,
        file.filename or "unknown.csv",
    )

    columns = extract_column_metadata(df)

    dataset = persist_dataset(
        db=db,
        df=df,
        metadata=metadata,
        columns=columns,
    )

    return DatasetUploadResponse(
        dataset_id=dataset.id,
        name=dataset.name,
        row_count=dataset.row_count,
        column_count=dataset.column_count,
    )

@router.get(
    "",
    response_model=list[DatasetResponse],
)
def list_datasets(
    db: Session = Depends(get_db),
):
    return get_all_datasets(db)

@router.get(
    "/{dataset_id}",
    response_model=DatasetDetailResponse,
)
def get_dataset_details(
    dataset_id: int,
    db: Session = Depends(get_db),
):
    dataset = get_dataset(
        db=db,
        dataset_id=dataset_id,
    )

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found",
        )

    return dataset


@router.get(
    "/{dataset_id}/columns",
    response_model=list[DatasetColumnResponse],
)
def get_dataset_column_details(
    dataset_id: int,
    db: Session = Depends(get_db),
):
    dataset = get_dataset(
        db=db,
        dataset_id=dataset_id,
    )

    if dataset is None:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found",
        )

    return get_dataset_columns(
        db=db,
        dataset_id=dataset_id,
    )