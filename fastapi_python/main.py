import os
from dotenv import load_dotenv
from fastapi import FastAPI

from fastapi_python.routers import api_router

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = FastAPI()

app.include_router(api_router)

# Configuração de paginação
from fastapi_pagination import add_pagination
add_pagination(app)
