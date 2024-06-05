from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Imagen(BaseModel): 
    url : HttpUrl
    nombre : str


class Tipo(BaseModel): 
    id : int
    nombre : str

class Categoria(BaseModel): 
    nombre : str
    tipo : Tipo

class Etiqueta(BaseModel): 
    nombre : str
    descripcion : str
    categoria : Categoria

class Item(BaseModel): 
    id : int
    nombre : str
    descripcion : Union[str, None] = None
    precio : float
    impuesto : Union[float, None] = None
    imagen : Union[List[Imagen], None] = None
    etiquetas : List[Etiqueta]

class Oferta(BaseModel): 
    nombre : str
    descripcion : Union[str, None] = None
    precio : float 
    items : List[Item]

@app.post('/items')
async def actualizar(item : Item): 
    resultados = {'item': item}
    return resultados

@app.post('/ofertas')
async def crear(oferta : Oferta): 
    resultados = {'oferta': oferta}
    return resultados