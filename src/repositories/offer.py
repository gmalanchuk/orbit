from src.database.models.offer import Offer
from src.repositories.base.postgres import PostgresRepository


class OfferRepository(PostgresRepository):
    model = Offer
