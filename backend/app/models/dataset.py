from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base

class Dataset(Base):
    __tablename__ = "datasets"

    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True,
        )
    name: Mapped[str] = mapped_column(
        String(255), 
        primary_key=False,
        )

    table_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
    )

    row_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    column_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )