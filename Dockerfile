# Imagem base do Python
FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Instala dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código para o container
COPY . /app/

# Expõe a porta
EXPOSE 8000

# Comando para rodar o Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
