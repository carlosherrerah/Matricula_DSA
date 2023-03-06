# Seccion 1. caracteres y cadenas vs las computadoras

# Las computadoras almacenan los caracteres como números
# ASCII (American Standard Code for Information Interchange)
# ASCII (Código Estándar Americano para Intercambio de Información)
# 256 caracteres diferentes A=65, a=97
# El código ASCII emplea ocho bits para cada signo = 256 Caracteres
# 128 alfabeto latino estandar
# Internacionalizacion = I18N
# código es un numero que compone un caracter.
# los puntos de código(128) derivados del código de páginas(128) son ambiguos
# Unicode asigna caracteres únicos
# los primeros 256 puntos de código Unicode son idénticos a la página de códigos ISO/IEC 8859-1
# UCS-4 = El nombre proviene de Universal Character Set (Conjunto de Caracteres Universales).
# UCS-4 emplea 32 bits (cuatro bytes) para almacenar cada carácter.
# BOM (byte order mark - marca de orden de bytes)
# BOM = es una combinación especial de bits que anuncia la codificación utilizada por el contenido de un archivo (por ejemplo, UCS-4 o UTF-B).
# UTF-8 = Unicode Transformation Format (Formato de Transformación Unicode).

# Python 3 es totalmente compatible con Unicode y UTF-8
# ASCII (se emplea principalmente para codificar el alfabeto latino y algunos de sus derivados) y 
# UNICODE (capaz de codificar prácticamente todos los alfabetos que utilizan los seres humanos).

# Un número correspondiente a un carácter en particular se llama punto de código.
# UNICODE utiliza diferentes formas de codificación cuando se trata de almacenar los caracteres usando archivos o memoria de computadora: 
# dos de ellas son UCS-4 y UTF-8 (esta última es la más común ya que desperdicia menos espacio de memoria).

