# backend/Dockerfile

FROM python:3.11-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Variáveis de ambiente para otimizar o Python no Docker
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala dependências do sistema necessárias para compilar o psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Copia e instala as dependências Python (aproveitando o cache do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Simplificado: Copia TUDO do contexto atual para /app
# Isso só funciona bem se você usar o arquivo .dockerignore (veja abaixo)
COPY . .

# Expõe a porta que o Flask vai usar
EXPOSE 5000

# Comando padrão para iniciar a aplicação
# As variáveis FLASK_APP, FLASK_RUN_HOST, etc., serão definidas no docker-compose
CMD ["flask", "run"]