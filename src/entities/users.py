from sqlalchemy import Column, Integer, String, delete, update
from sqlalchemy.future import select

from ..infra.config.db_base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    password = Column(String)


def __repr__(self):
    return f"User({self.nome}, {self.email})"
