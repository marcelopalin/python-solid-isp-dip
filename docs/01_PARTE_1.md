# 1. Introdução

Antes de tentar entender o princípio da Inversão da Dependência vamos
instalar e configurar um Logger e um gerenciador de Configurações
que considero os mais TOPs do momento.

Também vamos utilizar o SQLAlchemy 2.0, caso queira saber mais sobre o assunto assita a Live do Edu em https://www.youtube.com/hashtag/166
https://github.com/dunossauro/live-de-python

As lives que ele já falou sobre o assunto são:
- Corrotinas 152, 153, 154
- Assíncrono 59
- SQLAlchemy ORM - 139

Vamos utilizar o SQLAlchemy 2.0 Style, Async ORM, novo estilo de Queries
e Eventos.

Todas as funcionalidades de AsyncIO do SQLAlchemy são dadas pelo `greenlet`
que é o gerenciador de Threads para fazer funcionar de maneira assíncrona.

Atualmente tó temos dois banco de dados que suportam chamadas Assíncronas (dependem do driver do bd) até o momento: Postgres (psycopg2) e o SQLite (embora não seja assíncrono) ele possui uma api assíncrona `aiosqlite`.


## 1.1. Instalando o SQLAlchemy 1.4 -> 2.0

```s
poetry add aiosqlite
```

```s
poetry add sqlalchemy
Using version ^1.4.21 for SQLAlchemy

Updating dependencies
Resolving dependencies... (14.4s)

Writing lock file

Package operations: 2 installs, 0 updates, 0 removals

  • Installing greenlet (1.1.0)
  • Installing sqlalchemy (1.4.21)
```

## 1.2. Variáveis de Ambiente com Dynaconf

```s
poetry add dynaconf
poetry add jinja2
```

O Jinja é porque podemos utilizá-lo nas configurações para deixá-las mais dinâmicas.

Vamos inicializar as configurações do projeto com Dynaconf:

```s
dynaconf init -f toml
⚙️  Configuring your Dynaconf environment
------------------------------------------
🐍 The file `config.py` was generated.
  on your code now use `from config import settings`.
  (you must have `config` importable in your PYTHONPATH).

🎛️  settings.toml created to hold your settings.

🔑 .secrets.toml created to hold your secrets.

🙈 the .secrets.toml is also included in `.gitignore`
  beware to not push your secrets to a public repo
  or use dynaconf builtin support for Vault Servers.

🎉 Dynaconf is configured! read more on https://dynaconf.com
   Use `dynaconf -i config.settings list` to see your settings
```

Veja que foram criados os arquivos:
- .settings.toml
- .secrets.toml que inclusive foi incluído no .gitignore

Como este caso é de aprendizagem removerei o .secrets.toml do gitignore
para você ter ideia de como ele pode ser utilizado no projeto.

Criaremos também o arquivo `.env` com o seguinte conteúdo:

```s
export ENV_FOR_DYNACONF=development # development ou production
export MYPROGRAM_DEBUG=false
export MYPROGRAM_LOGS_DIR="logs"
export MYPROGRAM_LOG_FILENAME="program.log"
```

Onde o prefixo `MYPROGRAM` é o mesmo que foi definido no arquivo `config.py`

```py
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="MYPROGRAM",
    settings_files=['settings.toml', '.secrets.toml'],
    environments=True,
    load_dotenv=True,
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load this files in the order.
```

O arquivo `.secrets.toml` você define as senhas do projeto:

```s
[development]
HOST="127.0.0.1"
PORT="5432"
DBNAME="my_dev_db"
DBUSER="me"
DBPASSWORD="changeme"

[production]
HOST="127.0.0.1"
PORT="5432"
DBNAME="my_production_db"
DBUSER="admin"
DBPASSWORD="adminpass"
```

Por fim, configuramos as variáveis no `settings.toml`

```toml
[default]
# veja em https://dynaconf.readthedocs.io/en/docs_223/guides/environment_variables.html
CURRENT_ENV = "@jinja {{this.current_env | lower}}" # development or production
HOME_DIR = "@jinja {{env.HOME}}"
DIR_INPUT="Entrada"
DIR_OUTPUT="Saida"

[production]
DIR_OUTPUT="@jinja {{this.DIR_OUTPUT}}/production"

[development]
DIR_OUTPUT="@jinja {{this.DIR_OUTPUT}}/development"
```

## Cor no Terminal


```s
poetry add termcolor
poetry add types-termcolor
```

e também:

```s
mypy --install-types
```

Ele indicará a necessidade de instalar o termcolor types.
Porém, não consegui resolver o problema do termcolor com


## 1.3. Melhorando o Logger com Loguru

```s
poetry add loguru
```
