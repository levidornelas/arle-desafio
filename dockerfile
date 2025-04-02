FROM python:3.12-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto para o container
COPY . /app/

# Instalar dependências
RUN pip install --no-cache-dir django==5.1.7

# Expor a porta padrão do Django
EXPOSE 8000

# Comando para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
