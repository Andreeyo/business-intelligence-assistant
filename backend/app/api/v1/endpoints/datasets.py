from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.dataset import DatasetUploadResponse
from app.services.dataset_ingestion import (
    extract_column_metadata,
    extract_dataset_metadata,
    load_csv,
)
from app.services.dataset_persistence import persist_dataset

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