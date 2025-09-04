from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.associations import offer_executors
from src.database.models.base import Base, TimeStampMixin


class User(Base, TimeStampMixin):
    __tablename__ = "users"

    telegram_user_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    offers_as_creator: Mapped[list["Offer"]] = relationship(back_populates="creator", cascade="all, delete-orphan")
    offers_as_executor: Mapped[list["Offer"]] = relationship(secondary=offer_executors, back_populates="executors")
