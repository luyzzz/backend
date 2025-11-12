"""
Script para criar tabelas no banco de dados online (PlanetScale, Railway, etc)

Execute DEPOIS de configurar as variáveis de ambiente DB_* no arquivo .env
"""

import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

print("=" * 60)
print("🔧 CRIADOR DE TABELAS - Projeto Get Stock")
print("=" * 60)

# Verifica se as variáveis estão configuradas
required_vars = ['DB_HOST', 'DB_USER', 'DB_PASSWORD', 'DB_NAME']
missing_vars = [var for var in required_vars if not os.getenv(var)]

if missing_vars:
    print("\n❌ ERRO: Variáveis de ambiente faltando!")
    print(f"   Variáveis não encontradas: {', '.join(missing_vars)}")
    print("\n📝 Solução:")
    print("   1. Crie arquivo .env na raiz do projeto")
    print("   2. Adicione as variáveis:")
    for var in required_vars:
        print(f"      {var}=seu_valor_aqui")
    print("\n   3. Execute este script novamente")
    exit(1)

print(f"\n✅ Variáveis de ambiente encontradas:")
print(f"   DB_HOST: {os.getenv('DB_HOST')}")
print(f"   DB_USER: {os.getenv('DB_USER')}")
print(f"   DB_NAME: {os.getenv('DB_NAME')}")
print(f"   DB_PORT: {os.getenv('DB_PORT', '3306')}")

print("\n📡 Conectando ao banco de dados...")

try:
    from app import create_app
    
    print("✅ Aplicação Flask carregada")
    
    # Cria aplicação Flask
    app = create_app()
    
    print("✅ Banco de dados inicializado")
    
    with app.app_context():
        from src.config.data_base import db
        from src.Infrastructure.Model.user import User
        from src.Infrastructure.Model.produto import Produto
        from src.Infrastructure.Model.order import Order
        from src.Infrastructure.Model.order_item import OrderItem
        
        print("\n🔨 Criando tabelas...")
        db.create_all()
        print("✅ Tabelas criadas com sucesso!")
        
        # Verifica tabelas criadas
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        
        print(f"\n📊 Tabelas no banco ({len(tables)}):")
        for table in tables:
            print(f"   ✓ {table}")
        
        # Cria admin
        from src.Application.Service.user_service import UserService
        print("\n👤 Criando usuário admin...")
        UserService.create_admin_if_not_exists()
        print("✅ Usuário admin verificado!")
        
        print("\n" + "=" * 60)
        print("🎉 SUCESSO! Banco de dados configurado!")
        print("=" * 60)
        print("\n📌 Próximos passos:")
        print("   1. Configure as mesmas variáveis na Vercel:")
        print("      Settings → Environment Variables")
        print("   2. Faça Redeploy na Vercel")
        print("   3. Teste: https://seu-projeto.vercel.app/api")
        print("\n✨ Tudo pronto para produção!")
        
except Exception as e:
    print(f"\n❌ ERRO ao conectar no banco:")
    print(f"   {str(e)}")
    print("\n🔍 Verifique:")
    print("   1. Credenciais estão corretas no .env")
    print("   2. Database existe no PlanetScale/Railway")
    print("   3. IP está liberado (Allow all IPs)")
    print("\n💡 Dica: Teste a conexão no MySQL Workbench primeiro")
    exit(1)
