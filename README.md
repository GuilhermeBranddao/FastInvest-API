# fast_invest

# Criando ambiente de desenvolvimento (Inicio do projeto)
    - Seguir esse tutorial: https://fastapidozero.dunossauro.com/01/



# Rodar aplicação em toda a rede
task run --host 0.0.0.0

# Add no gitignore
echo 'database.db' >> .gitignore

# Alembic
- config.set_main_option('sqlalchemy.url', Settings().DATABASE_URL)
- alembic upgrade head

# Rodar
fastapi dev fast_invest/app.py