# Projeto API BIG AGRICULTURE

Este projeto é uma API desenvolvida em Django REST Framework com suporte a Docker e Docker Compose, focada na gestão de produtores, propriedades, safras e culturas.

## Requisitos

- Docker
- Docker Compose

## Como iniciar o projeto

### 1. Clonar o repositório

```bash
git clone https://seu-repo-url.git
cd nome-do-projeto
```

### 2. Subir a aplicação com Docker

```bash
docker-compose up --build
```

A API estará disponível em: [http://0.0.0.0:8000](http://0.0.0.0:8000)

A documentação Swagger estará disponível em: [http://0.0.0.0:8000/api/docs](http://0.0.0.0:8000/api/docs)

## Comandos úteis

### Criar e aplicar migrações

Criação de migrações:

```bash
docker-compose run web python manage.py makemigrations
```

Aplicação das migrações:

```bash
docker-compose run web python manage.py migrate
```

### Executar os testes da aplicação (Unitários e Integração)

```bash
docker-compose exec web ./manage.py test
```

### Gerar o diagrama de modelos

```bash
docker-compose exec web python manage.py graph_models -a -o /code/diagram.png
```

O diagrama será salvo na raiz do projeto com o nome `diagram.png`.

## Estrutura da API

A API possui os seguintes recursos principais:

- Produtores
- Propriedades
- Safras
- Culturas

Cada recurso possui endpoints completos (CRUD) e documentação acessível via Swagger.

## Configuração de Ambiente

O arquivo `.env` deve conter a variável `DATABASE_URL`, por exemplo:

```
DATABASE_URL=postgres://postgres:postgres@db:5432/bigagriculture
```

## Logs

A pasta `logs/` armazena os arquivos de log da aplicação. Os logs seguem o padrão configurado no `settings.py` e são úteis para auditoria e diagnóstico de erros. Certifique-se de que esta pasta existe para evitar falhas na escrita dos arquivos de log.

## Utils

A pasta `utils/` contém utilitários globais do projeto, como:

- `exception_handler.py`: gerencia e registra exceções de forma personalizada, integrando-se ao sistema de logging do Django REST Framework.
- Outros módulos auxiliares reutilizáveis podem ser adicionados aqui.

## Observações

- Certifique-se de que a porta `8000` está disponível localmente.
- Em caso de alterações no modelo, lembre-se de executar `makemigrations` e `migrate`.
