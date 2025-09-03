from sqlalchemy import Table, ForeignKey, Column

from src.database.models.base import Base

offer_executors = Table(
    "offer_executors",
    Base.metadata,
    Column("offer_id", ForeignKey("offers.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True),
)
