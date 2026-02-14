import re
from typing import List, Dict

from .expresiones import OUTPUT_REGEX

class OutputRegex:
    def __init__(self):
        self.patron = OUTPUT_REGEX

    def __regex_output(self, texto: str):
        return re.findall(self.patron, texto, re.IGNORECASE)

    def encontrar_output(self, texto: str):
        conincidencias = self.__regex_output(texto)

        lista_final: List[Dict[str, str]] = []

        for output_str in conincidencias:
            lista_final.append({
                "nombre": output_str[0].strip(),
                "tipo": output_str[1].strip(),
                "desc": "Explicita",
                "comentario": output_str[2].strip() if output_str[2] else ""
            })

        return lista_final