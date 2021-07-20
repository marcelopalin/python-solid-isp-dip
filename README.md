# Projeto python-solid-isp-dip

Vamos abordar dois princípios SOLID:

- Interface Segregation Principle (ISP)
- Dependency Inversion Principle (DIP)

# Passos iniciais da Criação do Projeto

Para as pessoas que estã iniciando na programação em python, irei descrever os passos que utilizo para criar um projeto python.

1. Abra a sua conta no Github e crie o projeto já escolhendo a criação do
.gitignore e do README e da LICENÇA. Clone seu projeto e abra o editor na
pasta.

2. Irei utilizar o VSCode. Na pasta do projeto eu abro o vscode `code .`;
3. Vamos iniciar escolhendo o gerenciador de pacotes POETRY pois as vantagens de usarmos o POETRY são:
   - em geral, ao instalarmos os pacotes eles também instalam suas dependências.
  Com o Poetry conseguiremos remover o pacote e junto serão removidas suas dependências.
  - O Poetry também divide dependências de produção e dependências de desenvolvimento igual ao `npm`.
  - Com Poetry você pode rodar o projeto sem ativar o ambiente virtual. Ex: `poetry run python main.py`
  - Isto é ótimo quando temos que colocar os comandos no crontab!
  - Para saber as últimas versões disponíveis dos pacotes faça: `poetry show --latest`

Ref: um artigo que mostra como usar Poetry com FastAPI é: https://levelup.gitconnected.com/creating-an-api-with-fastapi-and-docker-809429d778e6

3.1 - Configurando para o projeto ter seu ambiente virtual dentro dele:

```s
poetry config --local virtualenvs.in-project true
```
Caso queira este comportamento para todos os outro projetos execute o comando acima sem o `--local`

1. Inicialize o projeto:

```s
poetry init
```

Ativando o ambiente virtual:

```s
poetry shell
```

5. Adicionando os pacotes de desenvolvimento

```s
poetry add -D black --allow-prereleases
poetry add -D pytest
poetry add -D flake8
poetry add -D pylint
poetry add -D autoflake
poetry add -D isort
poetry add -D mypy
```

A sinalização `--allow-prereleases`  em nossa adição de black é necessária porque, tecnicamente, ela não foi lançada.

Obs:

Caso queira exportar os pacotes de dependência faça:

```s
poetry export --dev --without-hashes -f requirements.txt > requirements.txt
```

6. Criando os arquivos de Lint e Makefile

   .editorconfig
   .flake8
   .isoft.cfg
   .mypy.ini
   ```s
      pylint --generate-rcfile > .pylintrc
   ```

7. Instalando o Pre-commit

```s
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

8. Enviando para o Git a primeria vez

```s
pre-commit run --all-files
```

Rode 2x, até aparecer tudo OK e novamente `git add .`
e por fim o `git commit`

## Como iniciar o projeto logo após ter baixado ele neste ponto?

Ou melhor, como inicializar um projeto que usa Poetry após sua Clonagem?

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

# Parte 01

Utilizaremos o Loguru, Dynaconf e SQLAlchemy.
Criaremos uma pasta `app` com o projeto inicial.

https://www.dynaconf.com/

> Leia: [Parte 01](docs/01_PARTE_1.md)

# Parte 02

Para visualizar o BD Sqlite instale: `sudo apt install sqlite3`
`sudo apt install sqlitebrowser`
Um visualizador mais sofisticado é o `DBeaver` mas é trabalhoso de instalar.
Outros são os plug-ins do vscode.


# Referências:

Pré-commit: https://waylonwalker.com/pre-commit-is-awesome/

https://campuscode.com.br/conteudos/s-o-l-i-d-principio-de-segregacao-de-interface

https://campuscode.com.br/conteudos/s-o-l-i-d-principio-de-inversao-de-dependencia

https://medium.com/desenvolvendo-com-paixao/o-que-%C3%A9-solid-o-guia-completo-para-voc%C3%AA-entender-os-5-princ%C3%ADpios-da-poo-2b937b3fc530

Sobre pre-commit e estilos:
https://levelup.gitconnected.com/raise-the-bar-of-code-quality-in-python-projects-7c49743f004f

https://www.youtube.com/watch?v=yBNHKAF-XdE&t=1439s

https://github.com/programadorLhama/backend_project_python-lab-
