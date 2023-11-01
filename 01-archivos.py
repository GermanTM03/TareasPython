from pathlib import Path
from time import ctime

archivo = Path("archivos/archivo-prueba.txt")
# archivo.exists()
# archivo.rename()
# archivo.unlink()

# print(archivo.stat())

print("Acceso", ctime(archivo.stat().st_atime))
print("Creacion", ctime(archivo.stat().st_ctime))
print("Modificacion", ctime(archivo.stat().st_mtime))