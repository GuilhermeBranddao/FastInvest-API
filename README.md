# Como rodar o projeto

# 1- Passo: Realiza as instalações de dependencias 
- linux(ubuntu)
    . install.sh
- Windows
    install.bat

# 2- Passo: Ajuste no banco de dados
alembic upgrade head

# 3- Passo: rodar aplicação 
task run --host 0.0.0.0