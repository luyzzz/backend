# 🔙 Projeto Get Stock - Backend API

API REST desenvolvida em Flask para gerenciamento de estoque de produtos automotivos.

## 🚀 Tecnologias

- **Flask** - Framework web
- **Flask-JWT-Extended** - Autenticação JWT
- **Flask-SQLAlchemy** - ORM para banco de dados
- **MySQL/PyMySQL** - Banco de dados
- **ReportLab** - Geração de PDFs
- **Flask-CORS** - Suporte a CORS

## 📁 Estrutura do Projeto

```
backend/
├── app.py                 # Ponto de entrada da aplicação
├── requirements.txt       # Dependências Python
├── setup_database.py      # Script para criar tabelas
├── src/
│   ├── routes.py         # Definição de rotas
│   ├── config/
│   │   └── data_base.py  # Configuração do banco
│   ├── Application/
│   │   ├── Controllers/  # Controladores HTTP
│   │   └── Service/      # Lógica de negócio
│   ├── Domain/           # Entidades de domínio
│   └── Infrastructure/
│       ├── Model/        # Modelos SQLAlchemy
│       └── http/         # Integrações HTTP
└── .env                  # Variáveis de ambiente (criar)
```

## ⚙️ Configuração

### 1. Instalar Dependências

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 2. Configurar Banco de Dados

Crie arquivo `.env` na raiz:

```env
# Desenvolvimento Local
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=projeto_frameworks
DB_PORT=3306

# Produção (PlanetScale/Railway)
# DB_HOST=seu-host.connect.psdb.cloud
# DB_USER=xxxxxxxxx
# DB_PASSWORD=pscale_pw_xxxxxxxxx
# DB_NAME=projeto-get-stock
# DB_PORT=3306

# Segurança
JWT_SECRET_KEY=sua-chave-secreta-forte
SECRET_KEY=outra-chave-secreta
```

### 3. Criar Tabelas

```bash
python setup_database.py
```

### 4. Executar

```bash
python app.py
```

API estará disponível em: `http://localhost:5000`

## 📡 Endpoints

### Autenticação
- `POST /verifica` - Login
- `POST /send-code` - Enviar código de verificação
- `POST /verify-code` - Verificar código e criar usuário
- `GET /me` - Dados do usuário autenticado

### Produtos
- `GET /produto` - Listar produtos
- `POST /produto` - Criar produto (Admin)
- `PUT /produto/<id>` - Atualizar produto (Admin)
- `DELETE /produto/<id>` - Deletar produto (Admin)

### Pedidos
- `POST /checkout` - Finalizar compra
- `GET /historico` - Histórico de pedidos

### Admin
- `GET /admin/stats` - Dashboard de métricas

### Health Check
- `GET /` - Status da API
- `GET /api` - Status com info do banco

## 🔐 Autenticação

Todas as rotas protegidas requerem header:
```
Authorization: Bearer <token_jwt>
```

## 🚀 Deploy (Railway Recomendado)

### Railway (Backend + MySQL incluído)

```bash
# 1. Instalar Railway CLI
npm i -g @railway/cli

# 2. Login
railway login

# 3. Criar novo projeto
railway init

# 4. Adicionar MySQL
railway add

# 5. Configurar variáveis (pegue do Railway)
railway variables set JWT_SECRET_KEY=sua-chave-aqui
railway variables set SECRET_KEY=outra-chave-aqui

# 6. Deploy
railway up

# 7. Criar tabelas (uma vez)
railway run python setup_database.py
```

## 📊 Banco de Dados

### Tabelas
- `user` - Usuários do sistema
- `produto` - Produtos cadastrados
- `order` - Pedidos realizados
- `order_item` - Itens dos pedidos

### Admin Padrão
- **Email**: `admin@admin.com`
- **Senha**: `admin123`
- **Status**: 2 (admin)

## 🤝 Integração com Frontend

Configure a URL da API no frontend:

```javascript
// Frontend: Antes das chamadas fetch
const API_URL = 'https://sua-api.railway.app';
```

Certifique-se de que o CORS está configurado para aceitar o domínio do frontend.

## 📦 Dependências

```
Flask==2.2.5
Flask-JWT-Extended==4.4.4
Flask-SQLAlchemy==3.0.5
PyMySQL==1.1.1
reportlab
python-dotenv==1.1.1
flask-cors==6.0.1
```

## 🔒 Segurança

- ✅ Senhas hasheadas com PBKDF2
- ✅ JWT com expiração de 24h
- ✅ CORS configurado
- ✅ Validação de entrada
- ✅ Upload seguro de arquivos

## 📄 Licença

Projeto acadêmico - Frameworks Web


