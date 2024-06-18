# Desde fastapi importamos FastAPI
from fastapi import FastAPI
                                                                                                                                   # se usa para recargar la pagina automaticamente
# Para desplegar la aplicacion escribimos en consola "uvicorn nombre_deL_archivo:nombre_de_la_aplicacion --host x.y.z.z   --port xyzc     --reload"
# en mi caso:                                         uvicorn       main        :          app           --host 0.0.0.0   --port 5000     --reload


# PARA TRAER LOS ROUTERS CREADOS A NUESTRO MAIN USAMOS:
from src.routers.pelicula_router import pelicula_router


# TRAER EL MIDDLEWARE (MANEJO DE ERRORES)
from src.utils.http_error_handler import HTTPErrorHandler






app = FastAPI()  # => Crear aplicacion


# LLAMAMOS AL MIDDILWARE:
app.add_middleware(HTTPErrorHandler)


# DEFINIR CONFIGURACION DE DOCUMENTACION DE FASTAPI
app.title = "Mi proyecto"  # => Para cambiar el titulo
# app.version = 2.0.0      # => Para cambiar la version 


#____________________________________________________________________________________________________________________
# RUTA BASICA:                                                                                                       #
# Con esta linea creamos una ruta para mostrar usando un decorador "@" y .get("x")                                   #                                                                    #   
@app.get("/", tags=['Inicio']) # => Usamos tags = ['Nombre_del_conjunto'] lo usamos para mantener un orden de endpoint #           
                                                                                                                     # => ESTO ES UN "endpoint" (basicamente son rutas xd)   
# Definimos nuestra primera funcion llamada home(): la cual nos devuelve un hola mundo                               #
def home():                                                                                                          #           
    return "Hola mundo!"                                                                                             # 
#____________________________________________________________________________________________________________________#



# PARA AÑADIR LOS ROUTERS A NUESTRA APLICACION DESPUES DE LA RUTA HOME:
app.include_router(prefix="/peliculas", router=pelicula_router) 







