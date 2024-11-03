from http import HTTPStatus

from fastapi import FastAPI

from fast_invest.schemas import Message

from fast_invest.routers import auth, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)



@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
