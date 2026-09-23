from fastapi import FastAPI

from app.api.v1.endpoints.datasets import router as datasets_router

app = FastAPI(
    title="Business Intelligence Assistant Backend",
    version="0.1.0",
    )

app.include_router(
    datasets_router,
    prefix="/api/v1/datasets",
    tags=["datasets"],
)

@app.get("/health")
def health_check():
    return {"status": "healthy"}
