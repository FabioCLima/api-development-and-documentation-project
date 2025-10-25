# Setup com Docker - Trivia API

Este guia mostra como configurar o ambiente de desenvolvimento usando Docker.

## 📋 Pré-requisitos

- Docker instalado
- Docker Compose instalado

### Verificar instalação

```bash
docker --version
docker-compose --version
```

### Instalar Docker (se necessário)

**Ubuntu/WSL:**
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

Após instalar, faça logout e login novamente.

## 🚀 Setup com Docker

### 1. Reverter a porta no models.py

O Docker usa a porta padrão 5432. Certifique-se de que `backend/models.py` está configurado assim:

```python
database_host = 'localhost:5432'
```

### 2. Iniciar o PostgreSQL com Docker

```bash
docker-compose up -d
```

Isso irá:
- Baixar a imagem do PostgreSQL 14
- Criar o container `trivia_postgres`
- Criar o database `trivia`
- Popular automaticamente com `trivia.psql`
- Expor na porta 5432

### 3. Verificar se está rodando

```bash
docker-compose ps
```

Você deve ver algo como:
```
NAME               STATUS
trivia_postgres    Up
```

### 4. Ver logs

```bash
docker-compose logs db
```

### 5. Verificar o database

```bash
docker-compose exec db psql -U postgres -d trivia -c "SELECT COUNT(*) FROM questions;"
```

Deve retornar 19 perguntas.

## 🧪 Testar a API

### 1. Iniciar o servidor Flask

```bash
cd backend
flask run --reload
```

### 2. Testar os endpoints

Em outro terminal:

```bash
# Testar categorias
curl http://127.0.0.1:5000/categories

# Testar perguntas
curl http://127.0.0.1:5000/questions
```

## 🔧 Comandos Úteis

### Parar o Docker

```bash
docker-compose down
```

### Parar e remover volumes (resetar database)

```bash
docker-compose down -v
```

### Ver logs em tempo real

```bash
docker-compose logs -f db
```

### Acessar o banco via psql

```bash
docker-compose exec db psql -U postgres -d trivia
```

### Recriar o container

```bash
docker-compose down
docker-compose up -d
```

## 🐛 Troubleshooting

### Porta 5432 já em uso

Se você tiver outro PostgreSQL rodando localmente:

**Opção 1:** Parar o PostgreSQL local
```bash
# Identificar processo
sudo lsof -i :5432

# Parar processo
sudo kill <PID>
```

**Opção 2:** Mudar a porta no docker-compose.yml
```yaml
ports:
  - "5433:5432"  # Mude para 5433
```

E atualize `backend/models.py`:
```python
database_host = 'localhost:5433'
```

### Erro "permission denied"

```bash
sudo chown -R $USER:$USER .
```

### Container não inicia

```bash
docker-compose down -v
docker-compose up -d --force-recreate
```

### Ver todos os containers

```bash
docker ps -a
```

### Remover todos os containers e volumes

```bash
docker-compose down -v
docker system prune -a
```

## ✅ Checklist

- [ ] Docker instalado
- [ ] docker-compose.yml criado
- [ ] backend/models.py configurado para porta 5432
- [ ] Container rodando (`docker-compose ps`)
- [ ] Database populado (19 perguntas)
- [ ] API Flask respondendo

## 📝 Vantagens do Docker

✅ **Isolamento:** Não interfere com PostgreSQL local  
✅ **Reprodutibilidade:** Mesmo ambiente para todos  
✅ **Simplicidade:** Um comando para subir tudo  
✅ **Limpeza:** Remove completamente sem deixar rastro  
✅ **Portabilidade:** Funciona em Windows, Mac e Linux  

## 📚 Alternativa: Setup Manual

Se preferir não usar Docker, veja:
- `backend/SETUP.md` - Setup manual
- `VERIFICAR_AMBIENTE_LOCAL.md` - Verificação do ambiente
