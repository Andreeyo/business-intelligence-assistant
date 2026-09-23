from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class DatasetColumn(Base):
    __tablename__ = "dataset_columns"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key="True",
    )

    dataset_id: Mapped[int] = mapped_column(
        ForeignKey("datasets.id"),
        nullable=False,
    )

    column_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    data_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    semantic_role: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    nullable: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )