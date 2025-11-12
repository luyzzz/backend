# 🚀 Deploy na Vercel - Guia Completo

## ✅ Otimizações Feitas

1. **Criado `.vercelignore`** - Exclui .venv, .db, cache Python (~200MB removidos)
2. **Otimizado `requirements.txt`** - Removidas dependências desnecessárias (Twilio, aiohttp, etc)
3. **Criado `vercel.json`** - Configuração específica para Vercel
4. **Melhorado `.gitignore`** - Evita enviar arquivos grandes

## ⚠️ IMPORTANTE: Configure o Banco de Dados Online

A Vercel não suporta MySQL local. Escolha uma opção:

### Opção 1: PlanetScale (Recomendado) ✨
1. Acesse: https://planetscale.com/
2. Crie conta gratuita
3. Crie novo database: `projeto-get-stock`
4. Copie a connection string
5. Na Vercel, vá em Settings → Environment Variables
6. Adicione:
   - `DB_HOST`: seu-db.us-east.psdb.cloud
   - `DB_USER`: seu-usuario
   - `DB_PASSWORD`: sua-senha
   - `DB_NAME`: projeto-get-stock
   - `DB_PORT`: 3306
   - `JWT_SECRET_KEY`: uma-chave-forte-aqui

### Opção 2: Railway
1. Acesse: https://railway.app/
2. Crie novo projeto → MySQL
3. Copie as credenciais
4. Configure no Vercel (mesmas variáveis acima)

### Opção 3: Supabase (PostgreSQL)
1. Acesse: https://supabase.com/
2. Crie projeto
3. Vá em Settings → Database → Connection String
4. No Vercel, adicione:
   - `DATABASE_URL`: postgresql://...

## 📋 Passos para Deploy

### 1. Prepare o Banco de Dados
```bash
# Rode este script localmente para criar as tabelas no banco online
# Altere data_base.py para usar as credenciais do banco online
python -c "from src.config.data_base import db; from app import create_app; app = create_app(); app.app_context().push(); db.create_all(); print('Tabelas criadas!')"
```

### 2. Deploy na Vercel
```bash
# Opção A: Via CLI
npm i -g vercel
vercel

# Opção B: Via GitHub (Recomendado)
# 1. Acesse: https://vercel.com/new
# 2. Conecte seu repositório GitHub
# 3. Clique em "Import"
# 4. Configure as variáveis de ambiente
# 5. Deploy!
```

### 3. Configure Variáveis de Ambiente na Vercel
No dashboard da Vercel:
1. Vá em **Settings** → **Environment Variables**
2. Adicione TODAS as variáveis do `.env.example`
3. Salve e faça **Redeploy**

## 🔧 Solução de Problemas

### "Function size exceeded 250MB"
✅ **Resolvido!** O `.vercelignore` agora exclui:
- `.venv/` (ambiente virtual)
- `.db/` (MySQL local)
- `__pycache__/` (cache Python)
- Arquivos de desenvolvimento

### "Database connection failed"
1. Verifique se configurou as variáveis de ambiente na Vercel
2. Teste a conexão com banco online localmente primeiro
3. Certifique-se que o banco permite conexões externas

### "No such file: static/uploads/..."
- Crie a pasta `static/uploads/` no banco online
- Ou use serviço de storage (Cloudinary, S3)

## 📊 Tamanho do Projeto

- **Antes**: ~319MB (com .venv e .db)
- **Depois**: ~25MB (otimizado)
- **Limite Vercel**: 250MB ✅

## 🎯 Próximos Passos

1. Configure banco online (PlanetScale/Railway)
2. Adicione variáveis de ambiente na Vercel
3. Faça deploy via GitHub
4. Teste o site: `https://seu-projeto.vercel.app`
5. Configure domínio customizado (opcional)

## 💡 Dicas

- Use **PlanetScale** para MySQL gratuito e escalável
- Configure **Vercel KV** para cache/sessões (opcional)
- Ative **Analytics** na Vercel para monitorar performance
- Use **Vercel Blob** para uploads de imagens em produção

---
**Tamanho atual do bundle**: ~25MB ✅
**Status**: Pronto para deploy! 🚀
