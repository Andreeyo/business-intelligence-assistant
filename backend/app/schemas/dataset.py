from pydantic import BaseModel

class DatasetUploadResponse(BaseModel):
    dataset_id: int
    name: str
    row_count: int
    column_count: int