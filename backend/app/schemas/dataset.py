from pydantic import BaseModel

class DatasetUploadResponse(BaseModel):
    dataset_id: int
    name: str
    row_count: int
    column_count: int

class DatasetResponse(BaseModel):
    id: int
    name: str
    table_name: str | None
    row_count: int
    column_count: int

    class Config:
        from_attributes = True

class DatasetColumnResponse(BaseModel):
    id: int
    column_name: str
    data_type: str
    nullable: bool

    class Config:
        from_attributes = True

class DatasetDetailResponse(BaseModel):
    id: int
    name: str
    table_name: str | None
    row_count: int
    column_count: int

    class Config:
        from_attributes = True