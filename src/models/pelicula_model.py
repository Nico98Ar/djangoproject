import datetime
from pydantic import BaseModel, Field





class Pelicula(BaseModel):                                    
    id: int                                                   
    titulo: str                                                
    ano: int                                                                
    categoria: str                                               



class PeliculaActualizar(BaseModel):
    titulo: str
    ano: int
    categoria: str

 


class PeliculaRegistrar(BaseModel):
    id: int = Field(gt=0)
    titulo: str = Field(min_length=4, max_length=15, default="Nombre de pelicula...")
    ano: int = Field(le=datetime.date.today().year, ge=1896, default=datetime.date.today().year)
    categoria: str = Field(min_length=5, max_length=15, default="Categoria de pelicula...")


