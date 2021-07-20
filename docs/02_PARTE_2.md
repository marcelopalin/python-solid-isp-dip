# 1. SOLID - Princípio da Inversão de Dependência

Vamos tentar entender o princípio da Inversão da Dependência. Utilizarei
o exemplo de como devemos implementar a conexão com Banco de Dados.

O objetivo é não implementarmos de forma DIRETA a conexão e sim através de uma INTERFACE (classe Abstract).

O princípio da Inversão das Dependências utilizam a Interface que não existem
em Python. Mas nós iremos contornar isto através do uso de Classes Abstratas.

Vamos utilizar o SQLAlchemy 2.0, caso não saiba assista a Live em https://www.youtube.com/hashtag/166


# 2. Como criamos a conexão?

Vamos criar as pastas `src/interfaces` e a pasta `src/infra`.
Sempre que quisermos criar uma conexão com algum Banco de Dados colocaremos
dentro da pasta de `infra` e sempre obedecerá as regras definidas na interface
que estarão na pasta `interfaces`.

1. instale o SQLAlchemy:

```s
poetry add sqlalchemy
```

2. Crie o arquivo `src/infra/config/db_config.py`

Veja que estamos utilizando a sintaxe Async/IO do SQLAlchemy 2.0
para acessar o sqlite utilizando a api aiosqlite.

```py
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

```

e o arquivo `src/infra/config/db_base.py`

```py
from sqlalchemy.orm import declarative_base

Base = declarative_base()
```

No arquivo `src/infra/config/__init__.py` nós colocamos:

```py
from .db_base import Base
from .db_config import DBConnectionHandler
```
O que seria uma espécie de filtro do que podemos importar do pacote `infra/config`

Vamos criar as Entities (Models) na pasta `src/entities`:

```py
from sqlalchemy import Column, Integer, String
from sqlalchemy.future import select

from ..infra.config.db_base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)


def __repr__(self):
    return f"User({self.nome}, {self.email})"

```
