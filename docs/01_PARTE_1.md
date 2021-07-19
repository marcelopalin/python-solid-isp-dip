# Introdução

Vamos tentar entender o princípio da Inversão da Dependência através 
do exemplo de como devemos implementar a conexão com Banco de Dados 
de maneira que eu possa a qualquer momento trocar o BD que estou utilizando
sem muito trabalho.

O princípio da Inversão das Dependências utilizam a Interface que não existem
em Python. Mas nós iremos contornar isto através do uso de Classes Abstratas.

Primeiro vamos programar o projeto sem nos preocuparmos na troca de banco de
dados. Vamos começar criando na raiz o arquivo main.py, a pasta src.

Vamos utilizar o SQLAlchemy 2.0, caso não saiba assista a Live do Edu em https://www.youtube.com/hashtag/166

## Variáveis de Ambiente com Dynaconf

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


## Melhorando o Logger com Loguru

```s
poetry add loguru
```
