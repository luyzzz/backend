from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
import os

db = SQLAlchemy()

def init_db(app):
    """
    Inicializa a base de dados com o app Flask e o SQLAlchemy usando MySQL.
    Suporta DATABASE_URL completa (Render/Heroku) ou variáveis individuais.
    """
    # Verifica se existe DATABASE_URL (padrão em Render, Heroku, etc)
    database_url = os.getenv('DATABASE_URL')
    
    if database_url:
        # Se DATABASE_URL existe, usa diretamente
        # Render/Heroku fornecem no formato: mysql://user:pass@host:port/dbname
        # Converte mysql:// para mysql+pymysql://
        if database_url.startswith('mysql://'):
            database_url = database_url.replace('mysql://', 'mysql+pymysql://', 1)
        elif database_url.startswith('postgres://'):
            # Render pode usar PostgreSQL
            database_url = database_url.replace('postgres://', 'postgresql+psycopg2://', 1)
        
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
        print(f"✓ Usando DATABASE_URL do ambiente")
    else:
        # Configuração do banco usando variáveis individuais (desenvolvimento)
        DB_CONFIG = {
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASSWORD', '218101809Luiz.'),
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': os.getenv('DB_PORT', '3306'),
            'database': os.getenv('DB_NAME', 'projeto_frameworks')
        }
        
        # Verifica se está em ambiente de produção
        is_production = os.getenv('VERCEL_ENV') == 'production' or os.getenv('FLASK_ENV') == 'production'
        
        try:
            # Em produção, não tenta criar database (assume que já existe)
            if not is_production:
                # Cria o database se não existir (apenas em desenvolvimento)
                base_uri = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/"
                engine = create_engine(base_uri)
                with engine.connect() as conn:
                    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}"))
                print(f"✓ Database '{DB_CONFIG['database']}' verificado/criado")
        except Exception as e:
            print(f"Aviso: Não foi possível criar database (normal em produção): {e}")

        # Configuração MySQL para a aplicação (com database)
        app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa a conexão do Flask-SQLAlchemy
    try:
        db.init_app(app)
        print("✓ Banco de dados inicializado com sucesso")
    except Exception as e:
        print(f"❌ Erro ao inicializar banco: {e}")
        raise
