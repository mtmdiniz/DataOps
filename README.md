# Relacionamento e Agregação de Dados no MongoDB

Este é um script Python que realiza o relacionamento e agregação de dados entre as coleções "Carros" e "Montadoras" em um banco de dados MongoDB. Ele também extrai o campo "País" com base no relacionamento das coleções.

## Pré-requisitos

- Python 3.x
- Biblioteca pymongo
- Biblioteca pandas
- MongoDB instalado e em execução

## Instalação

1. Clone este repositório para o seu computador:

```bash
git clone URL_DO_REPOSITORIO

Instale as dependências necessárias:

pip install pymongo pandas

Uso
Certifique-se de que o MongoDB esteja em execução.
Execute o script Python dataFrame.py.


Este script realiza as seguintes etapas:

Cria dataframes para os carros e montadoras.
Salva os dataframes no banco de dados MongoDB.
Realiza o relacionamento entre as coleções "Carros" e "Montadoras".
Executa uma agregação para agrupar os carros por país e extrair o campo "País".
Exibe os resultados da agregação.