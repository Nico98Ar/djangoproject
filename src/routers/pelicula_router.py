from typing import List
from fastapi.responses import JSONResponse
from src.models.pelicula_model import Pelicula, PeliculaActualizar, PeliculaRegistrar
from fastapi import APIRouter, Path, Query # APIRouter: Lo usamos para establecer el archivo como una ruta:







peliculas: List[Pelicula] = []

pelicula_router = APIRouter()


# CONSULTAR PELICULAS
@pelicula_router.get("/ver", tags=['Peliculas'])
def get_peliculas() -> List[Pelicula]: 
    #return [pelicula.model_dump() for pelicula in peliculas] # => usando lambda function retornamos una lista, en la primera parte tomamos una pelicula y 
                                                             #    la transformamos a diccionario usando .model_dump() por cada pelicula en la lista de pelicula
                                                             # 
# podemos mejorar la documentacion de nuestro codigo usando la clase JSONRESPONSE:
    return JSONResponse(content=[pelicula.model_dump() for pelicula in peliculas])




# CONSULTAR PELICULAS POR ID
@pelicula_router.get("/ver/{id}", tags=['Peliculas'])
def get_pelicula(id: int = Path(gt=0)) -> Pelicula | dict: 
    for pelicula in peliculas:        
        if pelicula.id == id:
            #return pelicula.model_dump() # => COMO ACA RETORNAMOS UNA SOLA ENTONCES TRANSFORMAMOS DIRECTAMENTE A DICCIONARIO CON .model_dump()
            # De igual manera aca con un JsonResponse:
            return JSONResponse(content=pelicula.model_dump())
    return JSONResponse(content={})




# CONSULTAR PELICULAS POR CATEGORIA
@pelicula_router.get("/ver/categorias", tags=["Peliculas"])
def get_pelicula_por_categoria(categoria: str = Query(min_length=5, max_length=20)) -> Pelicula | dict: 
    for pelicula in peliculas:
        if pelicula.categoria == categoria:
            # return pelicula.model_dump() # => De igual manera aca
            # Otra vez usamos JSONResponse:
            return JSONResponse(content=pelicula.model_dump())
    return JSONResponse(content={})




# AGREGAR PELICULAS
@pelicula_router.post("/agregar", tags=["Peliculas"])
def crear_pelicula(pelicula: PeliculaRegistrar) -> List[Pelicula]:
    peliculas.append(pelicula) 
    # return [pelicula.model_dump() for pelicula in peliculas]
    return JSONResponse(content=[pelicula.model_dump() for pelicula in peliculas])
    # return RedirectResponse('/peliculas', status_code=303) # => Hacemos uso de RedirectResponse('ruta_redireccion', status_code=xyz), Para redirigir de una url a otra  
                                                           #    El codigo de estado 303 nos sirve para la redireccion.

# ACTUALIZAR PELICULAS
@pelicula_router.put("/actualizar/{id}", tags=["Peliculas"])
def actualizar_pelicula(id: int, pelicula: PeliculaActualizar) -> List[Pelicula]:
    for item in peliculas:
        if item.id == id:
            item.titulo = pelicula.titulo
            item.ano = pelicula.ano
            item.categoria = pelicula.categoria             
    # return [pelicula.model_dump() for pelicula in peliculas]
    # SEGUIMOS USANDO JSONRESPONSE:
    return JSONResponse(content=[pelicula.model_dump() for pelicula in peliculas])
   


# BORRAR PELICULAS
@pelicula_router.delete("/borrar/{id}", tags=["Peliculas"])
def borrar_pelicula(id: int) -> List[Pelicula]:
    for pelicula in peliculas:
        if pelicula.id == id:
            peliculas.remove(pelicula)
    # return [pelicula.model_dump() for pelicula in peliculas]
    return JSONResponse(content=[pelicula.model_dump() for pelicula in peliculas])


