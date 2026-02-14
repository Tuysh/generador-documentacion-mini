import re

from .expresiones import NOMBRE_PROGRAMA_REGEX

class ProgramaNombreRegex:
    def __init__(self):
        self.patron = NOMBRE_PROGRAMA_REGEX

    def __regex_programa_nombre(self, texto: str):
        return re.search(self.patron, texto, re.IGNORECASE)

    def encontrar_programa_nombre(self, texto: str):
        coincidencia = self.__regex_programa_nombre(texto)
        if coincidencia:
            return {"nombre": coincidencia.group(1).strip()}
        return {"nombre": "Desconocido"}