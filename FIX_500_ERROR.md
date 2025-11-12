# 🔧 Guia Rápido - Fix Error 500 Vercel

## ✅ Mudanças Feitas

1. **data_base.py** - Agora usa variáveis de ambiente (`DB_HOST`, `DB_USER`, `DB_PASSWORD`, etc)
2. **app.py** - Melhor tratamento de erros e usa `JWT_SECRET_KEY` do ambiente
3. **routes.py** - Adicionado health check em `/` e `/api` para debug
4. **vercel.json** - Otimizado para servir arquivos estáticos

---

## 🚨 ERRO 500: CAUSA PROVÁVEL

**O banco de dados não está configurado!** A Vercel está tentando conectar no `localhost` que não existe.

---

## 🎯 SOLUÇÃO RÁPIDA (2 minutos)

### Passo 1: Configure Banco Online (PlanetScale - Grátis)

1. **Cadastre-se**: https://planetscale.com/
2. **Crie database**: 
   - Nome: `projeto-get-stock`
   - Região: `US East` (mais rápido)
3. **Copie credenciais**: Dashboard → Connect → General

### Passo 2: Configure Variáveis na Vercel

1. Acesse: https://vercel.com/[seu-usuario]/[seu-projeto]/settings/environment-variables
2. Adicione estas variáveis (**TODAS são obrigatórias**):

```
DB_HOST=aws.connect.psdb.cloud
DB_USER=xxxxxxxxx
DB_PASSWORD=pscale_pw_xxxxxxxxx
DB_NAME=projeto-get-stock
DB_PORT=3306
JWT_SECRET_KEY=cole-uma-chave-forte-aqui
SECRET_KEY=cole-outra-chave-forte-aqui
```

**Gerar chaves fortes**:
```bash
# No PowerShell:
python -c "import secrets; print(secrets.token_hex(32))"
```

### Passo 3: Criar Tabelas no Banco

**Localmente, rode UMA VEZ**:

1. Crie arquivo `.env` na raiz do projeto:
```env
DB_HOST=aws.connect.psdb.cloud
DB_USER=xxxxxxxxx
DB_PASSWORD=pscale_pw_xxxxxxxxx
DB_NAME=projeto-get-stock
DB_PORT=3306
```

2. Execute:
```bash
python -c "from app import create_app; app = create_app(); print('Tabelas criadas!')"
```

### Passo 4: Redeploy na Vercel

1. Vá em: Deployments → [...] → Redeploy
2. Ou faça commit e push:
```bash
git add .
git commit -m "Fix database configuration for production"
git push
```

---

## 🧪 Testar se Funcionou

Acesse: `https://seu-projeto.vercel.app/`

**Deve retornar**:
```json
{
  "status": "ok",
  "message": "API Projeto Get Stock - Running",
  "environment": "production"
}
```

Acesse: `https://seu-projeto.vercel.app/api`

**Deve retornar**:
```json
{
  "mensagem": "API - OK; Docker - Up",
  "database": "connected",
  "environment": "production"
}
```

Se `"database": "connected"` → **Sucesso!** ✅  
Se `"database": "error: ..."` → Veja a mensagem de erro abaixo.

---

## 🐛 Problemas Comuns

### Erro: "Access denied for user"
- **Causa**: Credenciais erradas
- **Solução**: Copie novamente as credenciais do PlanetScale

### Erro: "Unknown database"
- **Causa**: Database não existe no PlanetScale
- **Solução**: Crie o database com o nome exato: `projeto-get-stock`

### Erro: "Can't connect to MySQL server"
- **Causa**: Host incorreto ou firewall
- **Solução**: 
  1. Verifique se o host no PlanetScale é `aws.connect.psdb.cloud` (ou similar)
  2. No PlanetScale, vá em Settings → Allow all IPs

### Database: "connected" mas site não abre
- **Causa**: Tabelas não foram criadas
- **Solução**: Rode o Passo 3 (Criar Tabelas) localmente

### Erro: "JWT_SECRET_KEY not set"
- **Causa**: Variável não configurada na Vercel
- **Solução**: Adicione `JWT_SECRET_KEY` nas Environment Variables

---

## 📋 Checklist Final

- [ ] Criei conta no PlanetScale
- [ ] Criei database `projeto-get-stock`
- [ ] Copiei credenciais (host, user, password)
- [ ] Configurei 7 variáveis de ambiente na Vercel:
  - [ ] `DB_HOST`
  - [ ] `DB_USER`
  - [ ] `DB_PASSWORD`
  - [ ] `DB_NAME`
  - [ ] `DB_PORT`
  - [ ] `JWT_SECRET_KEY`
  - [ ] `SECRET_KEY`
- [ ] Criei tabelas rodando o script localmente
- [ ] Fiz redeploy na Vercel
- [ ] Testei `/` e `/api` - database connected ✅

---

## 🆘 Ainda com Erro?

1. **Veja os logs da Vercel**:
   - Dashboard → Deployments → [último deploy] → View Function Logs
   - Procure por erros em vermelho

2. **Compartilhe o erro**:
   - Copie a mensagem de erro completa
   - Compartilhe a resposta de `https://seu-projeto.vercel.app/api`

3. **Alternativa rápida** (se PlanetScale não funcionar):
   - Use **Railway**: https://railway.app/
   - New Project → Add MySQL → Copie credenciais
   - Configure na Vercel e redeploy

---

**Tempo estimado**: 5 minutos com PlanetScale configurado ⚡
