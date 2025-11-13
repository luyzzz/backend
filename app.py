from flask import Flask
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_cors import CORS
from src.config.data_base import init_db, db
from src.routes import init_routes
from src.Infrastructure.Model.user import User
import os

def create_app():
    """
    Cria e configura a aplicação Flask.
    """
    app = Flask(__name__)
    
    # Usa variáveis de ambiente em produção
    app.secret_key = os.getenv('SECRET_KEY', 'sua_chave_secreta_aqui')
    
    CORS(app)
    
    # JWT Configuration com variável de ambiente
    app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY', 'flaroque')
    # Expiração de 24 horas para o token de acesso
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)
    jwt = JWTManager(app)

    # Inicializa banco de dados
    try:
        init_db(app)
        print("✅ Banco de dados inicializado")
    except Exception as e:
        print(f"❌ Erro ao inicializar banco: {e}")
        # Em produção, não falha se banco não conectar (pode precisar de configuração)
        is_production = os.getenv('VERCEL_ENV') == 'production' or os.getenv('RENDER') == 'true'
        if not is_production:
            raise

    # Inicializa rotas
    init_routes(app)

    # Detecta ambiente de produção
    is_production = os.getenv('VERCEL_ENV') == 'production' or os.getenv('RENDER') == 'true'
    
    with app.app_context():
        try:
            # Importe TODOS os modelos antes do create_all
            from src.Infrastructure.Model.user import User  # noqa: F401
            from src.Infrastructure.Model.produto import Produto  # noqa: F401
            from src.Infrastructure.Model.order import Order  # noqa: F401
            from src.Infrastructure.Model.order_item import OrderItem  # noqa: F401
            
            # Só tenta criar tabelas em desenvolvimento
            if not is_production:
                db.create_all()
                print("✅ Tabelas criadas/verificadas")
                
                # Criar usuário admin se não existir (só em dev)
                from src.Application.Service.user_service import UserService
                UserService.create_admin_if_not_exists()
                print("✅ Usuário admin verificado")
            else:
                print("ℹ️ Modo produção: assumindo que tabelas já existem")
            
        except Exception as e:
            print(f"❌ Erro na inicialização: {e}")
            # Log do erro mas não falha em produção
            if not is_production:
                raise

    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)