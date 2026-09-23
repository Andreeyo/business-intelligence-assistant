from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, JSON, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base

class DatasetProfile(Base):
    __tablename__ = "dataset_profiles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    dataset_id: Mapped[int] = mapped_column(
        ForeignKey("datasets.id"),
        nullable=False,
        unique=True,
    )

    profile_json: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )