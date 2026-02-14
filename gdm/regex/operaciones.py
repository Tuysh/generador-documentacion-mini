import re
from typing import Dict, List

from .expresiones import (
    OPERACIONES_CON_COMENTARIO_REGEX,
    OPERACIONES_SIN_COMENTARIO_REGEX,
)


class OperacionesRegex:
    def __init__(self):
        self.patron_operaciones = (
            OPERACIONES_CON_COMENTARIO_REGEX + r"|" + OPERACIONES_SIN_COMENTARIO_REGEX
        )

    def __regex_operaciones(self, texto: str):
        return re.findall(self.patron_operaciones, texto, re.MULTILINE)

    def encontrar_operaciones(self, texto: str):
        conincidencias = self.__regex_operaciones(texto)

        lista_final: List[Dict[str, str]] = []

        for conincidencia in conincidencias:
            if conincidencia[1]:
                lista_final.append(
                    {
                        "operacion": conincidencia[0].strip(),
                        "comentario": conincidencia[1].strip(),
                    }
                )
            else:
                lista_final.append({"operacion": conincidencia[2].strip()})

        return lista_final
