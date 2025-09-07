from enum import Enum

from sqlalchemy import DECIMAL, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

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

    name: Mapped[str] = mapped_column(String(64), nullable=False)
    description: Mapped[str] = mapped_column(String(256), nullable=True)
    telegram_channel_url: Mapped[str] = mapped_column(String(256), nullable=False)
    offer_type: Mapped[OfferType] = mapped_column(nullable=False)
    offer_status: Mapped[OfferStatus] = mapped_column(default=OfferStatus.SUSPENDED, nullable=False)
    price_per_subscriber: Mapped[DECIMAL] = mapped_column(DECIMAL(precision=4, scale=2), default=0.0, nullable=False)
    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    # m2m на юзера (поле исполнители)
