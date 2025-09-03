from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.associations import offer_executors
from src.database.models.base import TimeStampMixin, Base


class User(Base, TimeStampMixin):
    __tablename__ = "users"

    telegram_user_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    created_offers: Mapped[list["Offer"]] = relationship(back_populates="creator")
    offers_as_executor: Mapped[list["Offer"]] = relationship(secondary=offer_executors, back_populates="executors")
