from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base model class from which other models inherit"""

    id: Mapped[int] = mapped_column(primary_key=True, index=True)


class TimeStampMixin:
    """Mixin class for adding timestamps to a model"""

    created_at: Mapped[datetime] = mapped_column(index=True, server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), server_onupdate=func.now(), nullable=False)
