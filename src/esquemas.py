from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel # => Desde "pydantic" importamos BaseModel, para heredar y poder crear esquemas
from typing import Optional # => Desde "typing" libreria que viene en Python, importamos "Optional", para establecer valores opcionales en nuestros esquemas y mas..
from typing import List # => Importamos "List", desde "typing", para retornar una lista de de mejor forma


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







# Creacion del primer endpoint
@app.get("/", tags=['Inicio'])
def home():                                                                                                                   
    return "Hola mundo!"                                                                                            


# Lista de peliculas
peliculas = [
    {
        "id": 1,
        "titulo": "Avatar",
        "ano": 2009,
        "categoria": "Accion"
    },
    {
        "id" : 2,
        "titulo" : "Superman",
        "ano" : 2012,
        "categoria" : "Ficcion"
    }
]



# CONSULTAR PELICULAS
@app.get("/peliculas", tags=['Peliculas'])
def get_peliculas() -> List[Pelicula]: ###  "->": EN PYTHON SE USA PARA INDICAR QUE TIPO DE DATOS SE ESPERA QUE DEVUELVA UNA FUNCION, EN ESTE CASO USANDO List, DE "typing" 
    return peliculas                   ###        ESPERAMOS QUE DEVUELVA UNA LISTA ESTO ES MUY BUENO EN FastAPI, YA QUE NOS MUESTRA LO QUE SE ESPERA ENCONTRAR  


# CONSULTAR PELICULAS POR ID
@app.get("/peliculas/{id}", tags=['Peliculas'])
def get_pelicula(id: int) -> Pelicula: ### "->": En este caso no usaremos List de typing ya que no devolveremos una lista de peliculas, sino, una sola y hacemos referencia
    for pelicula in peliculas:         ###       a la clase.
        if pelicula['id'] == id:
            return pelicula
    return []


# CONSULTAR PELICULAS POR CATEGORIA
@app.get("/peliculas/", tags=["Peliculas"])
def get_pelicula_por_categoria(categoria: str, ano: int) -> Pelicula: 
    for pelicula in peliculas:
        if pelicula['categoria'] == categoria and pelicula['ano'] == ano:
            return pelicula
    return []



# AGREGAR PELICULAS
# => EN ESTE CASO HACER USO DEL REQUEST BODY, NO ES LO CORRECTO YA QUE AL CRECER LOS DATOS ENTONCES SE VUELVE IMPOSIBLE MANTENER EL CODIGO POR LO QUE CRECERIA MUCHO EL CODIGO, EN ESTOS CASOS SE USA MEJOR PYDANTIC
@app.post("/peliculas/", tags=["Peliculas"])
def crear_pelicula(pelicula: Pelicula) -> List[Pelicula]: # => De esta forma establecemos en los parametros a nuestro esquema previamente creado en la linea "14", a pelicula, le asignamos el esquema "Pelicula"
    peliculas.append(pelicula.model_dump()) # => a la lista "peliculas", usando ".append", agregamos nuestro parametro "pelicula", transformandolo a diccionario con ".model_dump()"
    return peliculas # => y retornamos el listado de peliculas :D


# ACTUALIZAR PELICULAS
@app.put("/peliculas/{id}", tags=["Peliculas"])
def actualizar_pelicula(id: int, pelicula: PeliculaActualizar) -> List[Pelicula]:
    for item in peliculas:
        if item["id"] == id:
            item["titulo"] = pelicula.titulo
            item["ano"] = pelicula.ano
            item["categoria"] = pelicula.categoria             
    return peliculas


# BORRAR PELICULAS
@app.delete("/peliculas/{id}", tags=["Peliculas"])
def borrar_pelicula(id: int) -> List[Pelicula]:
    for pelicula in peliculas:
        if pelicula["id"] == id:
            peliculas.remove(pelicula)
    return peliculas


