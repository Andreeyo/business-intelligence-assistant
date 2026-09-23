from fastapi import APIRouter, File, UploadFile

from app.schemas.dataset import DatasetUploadResponse

router = APIRouter()

@router.post(
    "/upload",
    response_model=DatasetUploadResponse,
)

async def upload_dataset(
    file: UploadFile = File(...),
) -> DatasetUploadResponse:
    return DatasetUploadResponse(
        dataset_id=0,
        name=file.filename or "unknown.csv",
        row_count=0,
        column_count=0
    )