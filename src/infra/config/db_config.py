from sqlalchemy.ext.asyncio import create_async_engine

from config import settings


class DBConnectionHandler:
    """Conexão com o BD SQLAlchemy"""

    def __init__(self) -> None:
        # Private
        self.__connection_string = f"sqlite//{settings.SQLITE_DBNAME}"
        self.session = None

    def get_engine(self):
        """ Comunicação do App com a Base de Dados """
        engine = create_async_engine(self.__connection_string)
        return engine
