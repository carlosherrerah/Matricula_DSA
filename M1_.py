# 2.5
import platform 
from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple
print(platform())
print(platform(1))
print(platform(0, 1))
print(machine())
print(processor())
print(system())
print(version())
print(python_implementation())
print(python_version_tuple())

# https://docs.python.org/3/py-modindex.html
import os
print(dir(os))
