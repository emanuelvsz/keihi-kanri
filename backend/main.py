from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à minha API FastAPI"}

@app.get("/keihi")
def read_item():
    return {"message": "Rota que irá retornar todas as despesas do usuário"}
