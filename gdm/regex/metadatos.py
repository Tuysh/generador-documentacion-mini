import re
from typing import Dict, List

from .expresiones import METADATOS_REGEX


class MetadatosRegex:
    def __init__(self):
        self.patron = METADATOS_REGEX

    def __regex_metadatos(self, texto: str):
        return re.findall(self.patron, texto, re.MULTILINE)

    def encontrar_metadatos(self, texto: str):
        conincidencias = self.__regex_metadatos(texto)

        metadatos: List[Dict[str, str]] = []

        for tipo, valor in conincidencias:
            clave, valor = tipo.strip(), valor.strip()

            metadatos.append({"clave": clave, "valor": valor})

        return metadatos
