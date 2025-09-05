from enum import Enum

from sqlalchemy import DECIMAL, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.associations import offer_executors
from src.database.models.base import Base, TimeStampMixin


class OfferStatus(Enum):
    SUSPENDED = "на паузі"
    IN_PROGRESS = "в процесі"
    COMPLETED = "завершено"


class OfferType(Enum):
    NEWS = "новини"
    VACANCIES = "вакансії"


class Offer(Base, TimeStampMixin):
    __tablename__ = "offers"

    name: Mapped[str] = mapped_column(String(64))
    description: Mapped[str] = mapped_column(String(256), nullable=True)
    telegram_channel_url: Mapped[str] = mapped_column(String(256), nullable=True)
    # type: # Mapped[OfferType] = mapped_column(SqlEnum(OfferType), nullable=True)
    # status: Mapped[OfferStatus] = mapped_column(SqlEnum(OfferStatus), default=OfferStatus.SUSPENDED, nullable=False)
    type: Mapped[OfferType] = mapped_column(nullable=True)
    status: Mapped[OfferStatus] = mapped_column(nullable=False, default=OfferStatus.SUSPENDED)

    price_per_subscriber: Mapped[DECIMAL] = mapped_column(DECIMAL(precision=4, scale=2), default=0.0, nullable=False)
    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    creator: Mapped["User"] = relationship(back_populates="offers_as_creator")
    executors: Mapped[list["User"]] = relationship(secondary=offer_executors, back_populates="offers_as_executor")
