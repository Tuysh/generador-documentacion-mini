import re
from typing import Dict, List

from .expresiones import ESTRUCTURAS_CON_COMENTARIO_REGEX


class EstructurasRegex:
    def __init__(self):
        self.patron_condicionales = ESTRUCTURAS_CON_COMENTARIO_REGEX

    def __regex_estructuras(self, texto: str, patron: str):
        return re.findall(patron, texto, re.IGNORECASE | re.MULTILINE)

    def encontrar_estructuras(self, texto: str):

        lista_final: List[Dict[str, str]] = []

        condicionales = self.__regex_estructuras(texto, self.patron_condicionales)

        lista_final: List[Dict[str, str]] = []

        for condicional in condicionales:
            if condicional[0]:  # Si es un "Si"
                lista_final.append(
                    {
                        "tipo": "Si",
                        "condicion": condicional[0].strip(),
                        "comentario": condicional[1].strip(),
                    }
                )
            elif condicional[2]:  # Si es un "SiNo"
                lista_final.append({"tipo": "SiNo", "comentario": condicional[2].strip()})

        return lista_final
