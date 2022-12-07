from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.engine.base import Engine
from scrapy.utils.project import get_project_settings
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def db_connect() -> Engine:
    """
    Creates database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("DATABASE"))


def create_items_table(engine: Engine):
    """
    Create the Items table
    """
    Base.metadata.create_all(engine)


class StockData(Base):
    """
    Defines the items model
    """

    __tablename__ = "stock_data"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    stock_ticker = Column("stock_ticker", String)
    stock_name = Column("stock_name", String)
    stock_price = Column("stock_price", Float)
