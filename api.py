from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Client(BaseModel):
    id: int
    nombre: str
    email: str


clients = {}
app = FastAPI()


@app.get("/client", response_model=list[Client])
async def get_clients():
    return list(clients.values())


@app.get("/client/{id}", response_model=Client)
async def get_client(id: int):
    if id not in clients:
        raise HTTPException(status_code=404, detail="Client not found")
    return clients[id]


@app.post("/client", response_model=Client)
async def create_client(client: Client):
    client.id = len(clients) + 1
    clients[client.id] = client
    return client


@app.put("/client/{id}", response_model=Client)
async def update_client(id: int, client: Client):
    if id not in clients:
        raise HTTPException(status_code=404, detail="Client not found")
    clients[id] = client
    return client


@app.delete("/client/{id}")
async def delete_client(id: int):
    if id not in clients:
        raise HTTPException(status_code=404, detail="Client not found")
    del clients[id]
    return {"message": "Client deleted"}
