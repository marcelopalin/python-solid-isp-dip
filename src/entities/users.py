from sqlalchemy import Column, Integer, String
from sqlalchemy.future import select

from ..infra.config.db_base import Base


class User(Base):
    """Model User

    Args:
        Base ([type]): [description]
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)


def __repr__(self):
    return f"User({self.nome}, {self.email})"
