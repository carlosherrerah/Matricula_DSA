# Seccion 2. Flujos de Archivos (streams)
# Python usa la \ como un carácter de escape (como \n)
# Rutas: separador windows \, separador linux / 

# Es indistinto en windows
# name = "\\dir\\file"   # windows
# name = "dir/file"      # linux

# handles o manejadores (un tipo de puntero inteligente) o streams o flujos (una especie de canal)
# 3 modos basicos de abrir un stream:
#   Modo lectura
#   Modo escritura
#   Modo actualizar: tanto lectura como escritura
# Si deseas deshacerte del objeto, invoca el método denominado close().

#                  IOBASE
# RawIOBase   BufferedIOBase      TextIOBase  
#             binary y Text         Text
# Debido al tipo de contenido de los flujos o streams, se dividen en tipo texto y binario.
# Los streams binarios no contienen texto, sino una secuencia de bytes de cualquier valor. 
#    Esta secuencia puede ser, por ejemplo, un programa ejecutable, una imagen, un audio o un videoclip, un archivo de base de datos, etc.

# programa portable: permite la ejecucion en diferentes entornos

# stream = open(name, mode = 'r', encoding = None)
# El tercer parámetro (encoding) especifica el tipo de codificación 
#    (por ejemplo, UTF-8 cuando se trabaja con archivos de texto).

# Modos para abrir los flujos o streams: mode=open_mode
# modo de Actualizacion: se permiten ambas, lectura y escritura.
# Si no se especifica t/b  t es default
# r  t ó b  lectura
# w  t ó b  escritura
# a  t ó b  adjuntar
# r+ t ó b  lectura   y actualizacion
# w+ t ó b  escritura y actualizacion

# 4.2.7 Abriendo el flujo (stream) por primera vez
#------------------------------------------------------------------------------
try:
    stream = open("C:\\Users\\carlo\\Desktop\\File.txt", "rt")
    stream = open("\\Users\\carlo\\Desktop\\File.txt", "rt")
    stream = open("/Users/carlo/Desktop/File.txt", "rt")    
    # El procesamiento va aquí.
    stream.close()
# except IOError as exc:
#    print(exc.errno)    
except Exception as exc:
    print("No se puede abrir el archivo:", exc)

# Hay tres excepciones bien definidas en el open
# Los nombres de los streams son: 
#    sys.stdin   Entrada estandar teclado.  input() lee datos de stdin por default.
#    sys.stdout  Salida  estandar pantalla. print() envía los datos al stream stdout
#    sys.stderr  salida de error estándar.  
#------------------------------------------------------------------------------
import errno
try:
    s = open("/Users/carlo/Desktop/File.txt", "rt")  
    # El procesamiento va aquí.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("El archivo no existe.")
    elif exc.errno == errno.EMFILE:
        print("Demasiados archivos abiertos.")
    else:
        print("El numero del error es:", exc.errno)

#------------------------------------------------------------------------------
from os import strerror
try:
    s = open("/Users/carlo/Desktop/File.txt", "rt")  
    # El procesamiento va aquí.
    s.close()
except Exception as exc:
    print("El archivo no pudo ser abierto:", strerror(exc.errno))

