from typing import TypedDict

import docxtpl  # pyright: ignore[reportMissingTypeStubs]


class Entrada(TypedDict):
    tipo: str
    nombre: str
    init: str


class Salida(TypedDict):
    tipo: str
    nombre: str
    desc: str

class Formulas(TypedDict):
    formula: str
    descripcion: str

class Situaciones(TypedDict):
    situacion: str
    descripcion: str

class Datos(TypedDict):
    nombre_programa: str
    nombre_programador: str
    descripcion_modulo: str
    entradas: list[Entrada]
    salidas: list[Salida]
    formulas: list[Formulas]
    situaciones: list[Situaciones]
    observaciones: str


class GenerateDocumentacion:
    def __init__(self, plantilla: str, datos: Datos, salida: str = "documentacion.docx"):
        self.plantilla = plantilla
        self.datos = datos
        self.salida = salida
        self.doc = docxtpl.DocxTemplate(self.plantilla)

    def generar_documento(self):
        # Aquí iría la lógica para generar el documento usando los datos
        self.doc.render(dict(self.datos))
        self.doc.save(self.salida)  # pyright: ignore[reportUnknownMemberType]
