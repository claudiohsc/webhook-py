from fastapi import FastAPI

app = FastAPI()

clientes = {
    1: {"nome": "joao", "telefone": 5599999999999, "status": "emitido"},
    2: {"nome": "maria", "telefone": 5599999999999, "status": "emitido"},
    3: {"nome": "lisa", "telefone": 5599999999999, "status": "pago"},
    4: {"nome": "mario", "telefone": 5599999999999, "status": "emitido"}    
}

@app.get("/")
def home():
    return {"Clientes": len(clientes)}


@app.get("/clientes/{id_cliente}")
def get_cliente(id_cliente: int):
    return clientes[id_cliente]