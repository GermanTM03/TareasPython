from pathlib import Path
archivo = Path("INE.txt")
texto = archivo.read_text("utf-8").split("\n")

#modificar texto
texto.insert(0, "!HOLA MUNDO!")
archivo.write_text("\n".join(texto),"utf-8")