# Use a imagem oficial do Python
FROM python:3.10

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo de requerimentos e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante da aplicação
COPY . .

# Exponha a porta da aplicação
EXPOSE 8000

# Comando para rodar as migrações e iniciar o servidor
CMD ["sh", "-c", "sudo daphne bookswap.asgi:application --port 80 --bind 0.0.0.0 -v2 --reload && sudo python manage.py runworker -v2"]
