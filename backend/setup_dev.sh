#!/bin/bash

# Script de setup do ambiente de desenvolvimento
# Backend - Trivia API

set -e

echo "🚀 Configurando ambiente de desenvolvimento..."

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Verificar se o PostgreSQL está instalado
if ! command -v psql &> /dev/null; then
    echo -e "${RED}❌ PostgreSQL não está instalado.${NC}"
    echo "Por favor, instale com: sudo apt-get install postgresql postgresql-contrib"
    exit 1
fi

# Verificar se o PostgreSQL está rodando
if ! pg_isready &> /dev/null; then
    echo -e "${YELLOW}⚠️  PostgreSQL não está rodando.${NC}"
    echo "Iniciando PostgreSQL..."
    sudo service postgresql start || echo "Por favor, inicie manualmente: sudo service postgresql start"
fi

# Criar database se não existir
echo -e "${GREEN}📦 Criando database 'trivia'...${NC}"
if createdb trivia 2>/dev/null; then
    echo -e "${GREEN}✅ Database criado com sucesso!${NC}"
else
    echo -e "${YELLOW}⚠️  Database 'trivia' já existe ou não foi possível criar.${NC}"
fi

# Popular database
echo -e "${GREEN}📊 Populando database...${NC}"
if psql trivia < trivia.psql &>/dev/null; then
    echo -e "${GREEN}✅ Database populado com sucesso!${NC}"
else
    echo -e "${YELLOW}⚠️  Database já populado ou erro ao popular.${NC}"
fi

# Instalar dependências com uv (se estiver no diretório raiz)
if [ -f "../pyproject.toml" ]; then
    echo -e "${GREEN}📚 Instalando dependências com uv...${NC}"
    cd ..
    uv sync
    echo -e "${GREEN}✅ Dependências instaladas!${NC}"
    cd backend
fi

echo -e "${GREEN}✅ Ambiente configurado com sucesso!${NC}"
echo ""
echo "Para rodar o servidor:"
echo "  flask run --reload"
echo ""
echo "Para rodar os testes:"
echo "  python test_flaskr.py"
