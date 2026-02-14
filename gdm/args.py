from sys import argv
from typing import TypedDict

class Args(TypedDict):
    archivo: str
    salida: str

def get_args() -> Args:
    if len(argv) < 2:
        raise ValueError("Se requiere al menos un argumento: el nombre del archivo a procesar y salida opcional.")
    
    return {"archivo": argv[1], "salida": argv[2] if len(argv) > 2 else "documentacion.docx"}