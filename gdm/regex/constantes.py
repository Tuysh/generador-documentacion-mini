import re
from typing import Dict, List

from .expresiones import CONSTANTES_REGEX


class ConstantesRegex:
    def __init__(self):
        self.regex = re.compile(CONSTANTES_REGEX)

    def extraer_constantes(self, codigo: str) -> List[Dict[str, str]]:
        constantes: List[Dict[str, str]] = []
        for match in self.regex.finditer(codigo):
            nombre_constante = match.group(0).split("<-")[0].strip()
            valor_constante = match.group(1).strip()

            constantes.append({"nombre": nombre_constante, "valor": valor_constante})

        return constantes
