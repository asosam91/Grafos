import grafos 
from grafos.util import *
from setuptools import setup
from setuptools import find_packages


setup(name="Grafos",  # Nombre
      version="0.1",  # Versión de desarrollo
      description="Paquete para Grafos",  # Descripción del funcionamiento
      author="Adriano Sokax",  # Nombre del autor
      author_email='asosam91@gmail.com',  # Email del autor
 #     license="GPL",  # Licencia: MIT, GPL, GPL 2.0...
 #     url="http://ejemplo.com",  # Página oficial (si la hay)
      packages=find_packages(),
)