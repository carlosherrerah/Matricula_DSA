# Seccion 4. Instalador de paquetes (PIP)

# Python se ha convertido en líder en investigación sobre: 
#    inteligencia artificial, La minería de datos
# No empezar desde Cero

# Repositorio PyPI = Python Package Index = La Tienda de Quesos = Gratuito = pip
# https://wiki.python.org/psf/PackagingWG.
# https://pypi.org/

# -----------------------------------------------------------------------------
# pip en MS Windows
import os
os.system("pip --version")

# Terminal
# PS C:\Dev> pip --version

# Path = C:\Program Files\Python3\Scripts\;C:\Program Files\Python3\;

# -----------------------------------------------------------------------------
# pip en Linux

# Terminal
# $ pip  --version
# $ pip3 --version

# En caso de instalacion
# $ sudo apt install python3-pip
# $ pacman si usas Arch Linux
# $ yum    si usas Red Hat

# Cómo usar pip
# PS C:\Dev> pip help
# PS C:\Dev> pip help install

# Paquetes instalado hasta el momento
# c:\> pip list

# [notice] To update, run: python.exe -m pip install --upgrade pip

# Informacion sobre algun paquete
# c:\> pip show package_name
# Qué paquetes son necesarios para utilizar con éxito el paquete (Requires:)
# Qué paquetes necesitan que el paquete se utilice con éxito (Required-by:)

# https://pypi.org/search/
# Framework, Programming Language, etc

# https://www.pygame.org
# c:\> pip install pygame
# c:\> pip install --user pygame

# pip install --user pygame
# pip uninstall pygame

# pip install -U nombre    # actualiza un paquete previamente instalado
# pip install nombre_del_paquete==versión_del_paquete






