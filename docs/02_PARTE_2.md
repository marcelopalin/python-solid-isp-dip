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
