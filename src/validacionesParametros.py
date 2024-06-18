from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel # => Desde "pydantic" importamos BaseModel, para heredar y poder crear esquemas
from typing import Optional # => Desde "typing" libreria que viene en Python, importamos "Optional", para establecer valores opcionales en nuestros esquemas y mas..
from typing import List # => Importamos "List", desde "typing", para retornar una lista de de mejor forma

# VALIDACIONES:
from pydantic import Field # => Importamos "Fiel", para poder hacer las validaciones
from fastapi import Path # => Hacemos esta importacion "Path", desde "fastapi", para la validacion de parametros de ruta
from fastapi import Query # => Hacemos esta importacion "Query" desde "fastapi" para la validacion de query's
import datetime


app = FastAPI()
app.title = "Mi proyecto"





################# CREACION DE ESQUEMAS/MODELOS CON LIBRERIA pydantic ######################

# pydantic: Es una libreria que se encarga con todo lo relacionado al manejo de datos y del las validacion, con esta crearemos nuestros primeros esquemas
# ______________________________________________________________
class Pelicula(BaseModel):                                      # 
    id: int                                                     #
    titulo: str                                                 # => ESTO ES UN ESQUEMA, (CON LA CREACION DE ESQUEMAS VAMOS A EVITAR LA DUPLICIDAD DE CODIGO EN ESTE CASO ESTE ESQUEMA APLICA
    ano: int                                                    #                         PARA AGREGAR PELICULAS COMO PARA CONSULTARLAS)
    categoria: str                                              # 
#_______________________________________________________________#


# CREACION DE ESQUEMA PARA ACTUALIZAR PELICULA:
class PeliculaActualizar(BaseModel):
    titulo: str
    ano: int
    categoria: str





################################# VALIDACIONES ###############################################


# CREACION DE ESQUEMA PARA REGISTRAR PELICULAS (CON VALIDACION)
class PeliculaRegistrar(BaseModel):
    id: int
    titulo: str = Field(min_length=4, max_length=15, default="Nombre de pelicula...")
    ano: int = Field(le=datetime.date.today().year, ge=1896, default=datetime.date.today().year)
    categoria: str = Field(min_length=5, max_length=15, default="Categoria de pelicula...")

# gt: greater than (Mayor que)
# ge: greater than or equal (Mayor o igual que)

# lt: less than (Menor que)
# le: less than or equal (Menor o igual que)





#*************************************************************************************************************************************************************************#
# Creacion del primer endpoint
@app.get("/", tags=['Inicio'])
def home():                                                                                                                   
    return "Hola mundo!"                                                                                            


# Lista de peliculas
peliculas: List[Pelicula] = []



# CONSULTAR PELICULAS
@app.get("/peliculas", tags=['Peliculas'])
def get_peliculas() -> List[Pelicula]: 
    return [pelicula.model_dump() for pelicula in peliculas] # => usando lambda function retornamos una lista, en la primera parte tomamos una pelicula y 
                                                             #    la transformamos a diccionario usando .model_dump() por cada pelicula en la lista de peliculas.   

# CONSULTAR PELICULAS POR ID
@app.get("/peliculas/{id}", tags=['Peliculas'])
def get_pelicula(id: int = Path(gt=0)) -> Pelicula | dict: 
    for pelicula in peliculas:        
        if pelicula.id == id:
            return pelicula.model_dump() # => COMO ACA RETORNAMOS UNA SOLA ENTONCES TRANSFORMAMOS DIRECTAMENTE A DICCIONARIO CON .model_dump()
    return {}


# CONSULTAR PELICULAS POR CATEGORIA
@app.get("/peliculas/", tags=["Peliculas"])
def get_pelicula_por_categoria(categoria: str = Query(min_length=5, max_length=20)) -> Pelicula | dict: 
    for pelicula in peliculas:
        if pelicula.categoria == categoria:
            return pelicula.model_dump() # => De igual manera aca
    return {}



# AGREGAR PELICULAS
@app.post("/peliculas/", tags=["Peliculas"])
def crear_pelicula(pelicula: PeliculaRegistrar) -> List[Pelicula]:
    peliculas.append(pelicula) 
    return [pelicula.model_dump() for pelicula in peliculas]


# ACTUALIZAR PELICULAS
@app.put("/peliculas/{id}", tags=["Peliculas"])
def actualizar_pelicula(id: int, pelicula: PeliculaActualizar) -> List[Pelicula]:
    for item in peliculas:
        if item.id == id:
            item.titulo = pelicula.titulo
            item.ano = pelicula.ano
            item.categoria = pelicula.categoria             
    return [pelicula.model_dump() for pelicula in peliculas]


# BORRAR PELICULAS
@app.delete("/peliculas/{id}", tags=["Peliculas"])
def borrar_pelicula(id: int) -> List[Pelicula]:
    for pelicula in peliculas:
        if pelicula.id == id:
            peliculas.remove(pelicula)
    return [pelicula.model_dump() for pelicula in peliculas]


