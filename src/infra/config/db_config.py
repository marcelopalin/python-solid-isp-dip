from sqlalchemy.ext.asyncio import create_async_engine

from src.config import settings


class DBConnectionHandler:
    """Conexão com o BD SQLAlchemy"""

    def __init__(self) -> None:
        # Private
        str_conn = f"sqlite+aiosqlite:///./{settings.SQLITE_DBNAME}"
        print(f"{str_conn}")
        self.__connection_string = str_conn
        self.session = None

    def get_engine(self):
        """ Comunicação do App com a Base de Dados """
        engine = create_async_engine(self.__connection_string)
        return engine
