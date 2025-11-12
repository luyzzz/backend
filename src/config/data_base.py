from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
import os

db = SQLAlchemy()

# Configuração do banco - usa variáveis de ambiente em produção
DB_CONFIG = {
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', '218101809Luiz.'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '3306'),
    'database': os.getenv('DB_NAME', 'projeto_frameworks')
}


def init_db(app):
    """
    Inicializa a base de dados com o app Flask e o SQLAlchemy usando MySQL.
    Cria o database se necessário conectando ao servidor (sem especificar database)
    e então configura a URI para o SQLAlchemy usar o database criado.
    """
    # Verifica se está em ambiente de produção (Vercel)
    is_production = os.getenv('VERCEL_ENV') == 'production' or os.getenv('FLASK_ENV') == 'production'
    
    try:
        # Em produção, não tenta criar database (assume que já existe)
        if not is_production:
            # Cria o database se não existir (apenas em desenvolvimento)
            base_uri = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/"
            engine = create_engine(base_uri)
            with engine.connect() as conn:
                conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}"))
    except Exception as e:
        print(f"Aviso: Não foi possível criar database (normal em produção): {e}")

    # Configuração MySQL para a aplicação (com database)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa a conexão do Flask-SQLAlchemy
    db.init_app(app)
