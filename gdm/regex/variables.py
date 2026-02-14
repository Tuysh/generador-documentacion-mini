import re
from typing import Dict, List

from .expresiones import VARIABLES_REGEX


class VariablesRegex:
    def __init__(self):
        self.patron = VARIABLES_REGEX

    def __regex_variables(self, texto: str):
        return re.findall(self.patron, texto, re.IGNORECASE)

    def encontrar_variables(self, texto: str):
        conincidencias = self.__regex_variables(texto)

        lista_final: List[Dict[str, str]] = []

        for variables_str, tipo in conincidencias:
            nombres: List[str] = variables_str.split(",")

            for nombre in nombres:
                lista_final.append(
                    {
                        "nombre": nombre.strip(),
                        "tipo": tipo,
                        "constante": "Si" if nombre.strip().isupper() else "No",
                    }
                )

        return lista_final
