# POETRY

Referências:
https://medium.com/analytics-vidhya/poetry-finally-an-all-in-one-tool-to-manage-python-packages-3c4d2538e828

## Como instalar o Poetry?

```s
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
```

Saída:

```s
Poetry (1.1.7) is installed now. Great!

To get started you need Poetry's bin directory ($HOME/.poetry/bin) in your `PATH`
environment variable. Next time you log in this will be done
automatically.

To configure your current shell run `source $HOME/.poetry/env`
```


Nota: você pode ter que adicionar Poetry ao seu PATH.
Se você está usando o Bash, basta adicionar a seguinte linha
no final do arquivo `~/.bashrc`

```s
export PATH=$PATH:$HOME/.poetry/bin
```

E se for o zsh estará no arquivo `~/.zshrc`.

Abra uma nova aba e verifique se funcionou:

```s
poetry --version
Poetry version 1.1.7
```

Poesia cria um `ambiente virtual` para o seu projeto, que corresponde à sua versão especificada do Python. Isso é mantido **fora da raiz do projeto** por padrão para não criar confusão. Se optar por colocar o ambiente virtual de volta no diretório do projeto basta mudarmos as configurações.

Vejamos antes quais são as configurações atuais com o comando `poetry config --list`

```s
cache-dir = "/home/mpi/.cache/pypoetry"
experimental.new-installer = true
installer.parallel = true
virtualenvs.create = true
virtualenvs.in-project = null
virtualenvs.path = "{cache-dir}/virtualenvs"  # /home/mpi/.cache/pypoetry/virtualenvs
```

Executando este comando estaremos dizendo que o Poetry deve criar o ambiente
virtual dentro dos novos projetos (padrão pasta .venv):

```s
poetry config virtualenvs.in-project true
```

Obs: caso queira uma configuração específica LOCAL apenas para o Projeto você deve passar a opção: `--local`

```s
poetry config --local virtualenvs.in-project true
```

Daí ele criará dentro do projeto o arquivo `poetry.toml` com o conteúdo:

```toml
[virtualenvs]
in-project = true
```

Obs: para usá-lo no Docker devemos desativar o comportamento padrão da poesia para criar ambientes virtuais para cada um de nossos projetos porque tudo já está isolado no contêiner docker.

Se você não quiser que o Poetry gerencie seus ambientes virtuais, pode desativar esse comportamento com este comando:

```s
poetry config virtualenvs.create false
```

Seguindo os princípios de código:

https://realpython.com/python-code-quality/
https://alexvanzyl.com/posts/2020-05-19-fastapi-simple-application-structure-from-scratch/
WorkFlow usando pre-commits
https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/


## Como atualizar Poetry?

Exemplo:

```s
poetry self update --preview
Updating to 1.1.6
 - Downloading poetry-1.1.6-linux.tar.gz 100%

Poetry (1.1.6) is installed now. Great!
```


## Como criar um Projeto do Zero com Poetry?

Vamos supor que deseja criar o projeto dentro do diretório `backend`
e definir o nome dele diferente do nome do diretório passe a opção `--name`:

```s
poetry new backend --name app
```

Saída:

```s
tree -L 2 .
.
├── app
│   └── __init__.py
├── pyproject.toml
├── README.rst
└── tests
    ├── __init__.py
    └── test_app.py

2 directories, 5 files
```


# Comandos Básicos do Poetry

## Inicializando o Poetry em um projeto existente:

```s
poetry init
```

será gerado o arquvio `pyproject.toml`

Veja um exemplo das perguntas que tem que responder:

```s
poetry init

This command will guide you through creating your pyproject.toml config.

Package name [python-solid-isp-dip]:
Version [0.1.0]:
Description []:  SOLID - interface and dependence injection
Author [Marcelo Facio Palin <mail@gmail.com>, n to skip]:  n
License []:  MIT
Compatible Python versions [^3.9]:

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file

[tool.poetry]
name = "python-solid-isp-dip"
version = "0.1.0"
description = "SOLID - interface and dependence injection"
authors = ["Your Name <you@example.com>"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.9"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes]
```


Como adicionar um pacote para Produção?

```s
poetry add requests
```

## Como adicionar um pacote que serve apenas para o Ambiente de Desenvolvimento?

```s
poetry add -D pytest
```

Exemplo:

```s
poetry add -D pytest
Creating virtualenv python-solid-isp-dip in /home/mpi/github.com/python-solid-isp-dip/.venv
Using version ^6.2.4 for pytest

Updating dependencies
Resolving dependencies... (1.9s)

Writing lock file

Package operations: 8 installs, 0 updates, 0 removals

  • Installing pyparsing (2.4.7)
  • Installing attrs (21.2.0)
  • Installing iniconfig (1.1.1)
  • Installing packaging (21.0)
  • Installing pluggy (0.13.1)
  • Installing py (1.10.0)
  • Installing toml (0.10.2)
  • Installing pytest (6.2.4)
```

Veja que ele criou o ambiente virtual na pasta `.venv` e alterou o arquivo
`pyproject.toml`:

```toml
[tool.poetry.dev-dependencies]
pytest = "^6.2.4"
```
E as dependências do pacote `pytest` não aparecem! Elas ficam armazenadas
no arquivo `poetry.lock`.

Qual é a vantagem? Quando fizermos a remoção do pacote `pytest` todos os outros pacotes dependentes também serão removidos.

Para mostrarmos a lista de dependências dos pacotes basta utilizarmos o comando:

```s
poetry show --tree
```

Saída:

```s
poetry show --tree

pytest 6.2.4 pytest: simple powerful testing with Python
├── atomicwrites >=1.0
├── attrs >=19.2.0
├── colorama *
├── iniconfig *
├── packaging *
│   └── pyparsing >=2.0.2
├── pluggy >=0.12,<1.0.0a1
├── py >=1.8.2
└── toml *
```

Veja que ele mostra os pacotes que foram instalados com o `pytest`.
E se removermos o `pytest` e dermos o comando novamente, veja:

https://python-poetry.org/docs/cli/#remove

```s
poetry remove -D pytest
```


## Saber as últimas versões dos Pacotes

Se você não tem certeza que tem a última versão dos pacotes:

```s
poetry show --latest
```

- Baixou o projeto do Git e quer instalar os pacotes:

```s
poetry install
```

- Habilitando o ambiente virtual:

```s
poetry shell
```

- Verifica erros no pyproject.toml:

```s
poetry check
```


- Rodando os testes:

```s
poetry install
poetry shell
poetry run pytest
```


Exportando os pacotes instalados com Poetry para o arquivo requirements.txt:


```s
poetry export -f requirements.txt > requirements.txt
```


# Informação do Ambiente Virtual

```s
poetry env info

Virtualenv
Python:         3.9.5
Implementation: CPython
Path:           /home/mpi/github.com/python-solid-isp-dip/.venv
Valid:          True

System
Platform: linux
OS:       posix
Python:   /usr
```

## Como remover um pacote?

Se o pacote for de desenvolvimento devemos executar:

```s
poetry remove -D pytest
```

```s
 poetry remove -D pytest
Updating dependencies
Resolving dependencies... (0.1s)

Writing lock file

Package operations: 0 installs, 0 updates, 8 removals

  • Removing attrs (21.2.0)
  • Removing iniconfig (1.1.1)
  • Removing packaging (21.0)
  • Removing pluggy (0.13.1)
  • Removing py (1.10.0)
  • Removing pyparsing (2.4.7)
  • Removing pytest (6.2.4)
  • Removing toml (0.10.2)
```

Veja que o `poetry.lock` foi modificado.


Senão faremos:

```s
poetry remove requests
```
