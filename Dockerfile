FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    graphviz \
    libgraphviz-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

    
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
