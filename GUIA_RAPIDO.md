# 🚀 SOLUÇÃO RÁPIDA - Erro 500 Vercel

## 🎯 Problema
Seu site deu erro 500 porque está tentando conectar em `localhost` (que não existe na Vercel).

## ✅ Solução em 3 Passos (5 minutos)

---

### 📦 PASSO 1: Criar Banco Online (PlanetScale - Grátis)

1. Acesse: **https://planetscale.com/**
2. Clique em **"Sign up"** (pode usar conta GitHub)
3. Clique em **"Create database"**
   - Name: `projeto-get-stock`
   - Region: `US East`
4. Clique em **"Create database"**
5. Vá em **"Connect"** → **"Create password"**
6. **COPIE ESTAS 4 LINHAS** (vamos usar no próximo passo):
   ```
   Host: aws.connect.psdb.cloud
   Username: xxxxxxx
   Password: pscale_pw_xxxxxxx
   Database: projeto-get-stock
   ```

---

### ⚙️ PASSO 2: Configurar Variáveis na Vercel

1. Vá em: **https://vercel.com/dashboard**
2. Clique no seu projeto
3. Vá em **Settings** (menu esquerdo) → **Environment Variables**
4. Adicione **7 variáveis** (clique em "+ Add New"):

| Nome | Valor | Onde pegar |
|------|-------|------------|
| `DB_HOST` | `aws.connect.psdb.cloud` | PlanetScale → Connect |
| `DB_USER` | `xxxxxxx` | PlanetScale → Connect |
| `DB_PASSWORD` | `pscale_pw_xxxxxxx` | PlanetScale → Connect |
| `DB_NAME` | `projeto-get-stock` | Nome do seu database |
| `DB_PORT` | `3306` | Digite: 3306 |
| `JWT_SECRET_KEY` | `[gerar abaixo]` | Veja como gerar ⬇️ |
| `SECRET_KEY` | `[gerar abaixo]` | Veja como gerar ⬇️ |

**Gerar chaves secretas** (no PowerShell):
```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```
Rode 2 vezes para gerar 2 chaves diferentes.

5. Clique em **"Save"**

---

### 🗄️ PASSO 3: Criar Tabelas no Banco

**No seu computador:**

1. Crie arquivo `.env` na raiz do projeto:
```env
DB_HOST=aws.connect.psdb.cloud
DB_USER=xxxxxxx
DB_PASSWORD=pscale_pw_xxxxxxx
DB_NAME=projeto-get-stock
DB_PORT=3306
```
(Cole os mesmos valores do PlanetScale)

2. Execute no PowerShell:
```powershell
python setup_database.py
```

Deve aparecer:
```
✅ Tabelas criadas com sucesso!
✅ Usuário admin verificado!
🎉 SUCESSO! Banco de dados configurado!
```

---

### 🔄 PASSO 4: Redeploy

1. Vá em Vercel: **Deployments**
2. Clique nos **3 pontinhos** (...) do último deploy
3. Clique em **"Redeploy"**
4. Aguarde 30 segundos

---

## ✅ Testar se Funcionou

Acesse: **`https://seu-projeto.vercel.app/api`**

Deve mostrar:
```json
{
  "mensagem": "API - OK; Docker - Up",
  "database": "connected",  ← Se aparecer "connected" = SUCESSO! ✅
  "environment": "production"
}
```

Se aparecer `"database": "connected"` → **PRONTO! Site no ar!** 🎉

---

## 🐛 Erros Comuns

### ❌ "database": "error: Access denied"
**Solução**: Credenciais erradas. Copie novamente do PlanetScale.

### ❌ "database": "error: Unknown database"
**Solução**: Database não existe. Certifique-se que criou no PlanetScale.

### ❌ "database": "error: Can't connect"
**Solução**: 
1. PlanetScale → Settings → IP Addresses → Allow all
2. Aguarde 2 minutos e tente novamente

### ❌ Script setup_database.py dá erro
**Solução**: 
```powershell
pip install python-dotenv
python setup_database.py
```

---

## 📌 Login Admin Padrão

Depois que tudo funcionar:

- **Email**: `admin@admin.com`
- **Senha**: `admin123`

---

## 🆘 Ainda Não Funcionou?

1. **Veja os logs da Vercel**:
   - Deployments → [último] → View Function Logs
   - Copie o erro em vermelho

2. **Teste a conexão local**:
   ```powershell
   python setup_database.py
   ```
   Se funcionar local mas não na Vercel = variáveis erradas na Vercel

3. **Alternativa rápida**: Use **Railway** (mais fácil)
   - https://railway.app/
   - New Project → MySQL
   - Copie credenciais → Cole na Vercel

---

**Tempo total**: ⏱️ 5-10 minutos  
**Custo**: 🆓 100% Grátis (PlanetScale + Vercel free tier)
