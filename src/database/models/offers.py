from enum import Enum

from sqlalchemy import ForeignKey, DECIMAL, String, Column, Table
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Enum as SqlEnum

from src.database.models.associations import offer_executors
from src.database.models.base import TimeStampMixin, Base


class OfferType(Enum): # todo переименовать енамы
    UNDEFINED = "не визначено"
    NEWS = "новини"
    VACANCIES = "вакансії"


class OfferStatus(Enum): # todo переименовать енамы
    IN_PROGRESS = "в процесі"
    SUSPENDED = "призупинено"
    COMPLETED = "завершено"



class Offer(Base, TimeStampMixin):
    __tablename__ = "offers"

    creator: Mapped["User"] = relationship(back_populates="created_offers")
    name: Mapped[str] = mapped_column(String(64))
    description: Mapped[str] = mapped_column(String(256), nullable=True)
    telegram_channel_url: Mapped[str] = mapped_column(String(256), nullable=True)
    type: Mapped[OfferType] = mapped_column(SqlEnum(OfferType), default=OfferType.UNDEFINED, nullable=False)
    status: Mapped[OfferStatus] = mapped_column(SqlEnum(OfferStatus), default=OfferStatus.SUSPENDED, nullable=False)
    price_per_subscriber: Mapped[DECIMAL] = mapped_column(DECIMAL(precision=4, scale=2), default=0.0, nullable=False)
    executors: Mapped[list["User"]] = relationship(secondary=offer_executors, back_populates="offers_as_executor")
