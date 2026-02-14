from typing import Any

from .file import GenerateDocumentacion
from .regex import (
    ConstantesRegex,
    EstructurasRegex,
    MetadatosRegex,
    OperacionesRegex,
    VariablesRegex,
    ProgramaNombreRegex,
    OutputRegex,
)


class Datos:
    def __init__(self, codigo: str):
        self.codigo = codigo
        self.variables = VariablesRegex().encontrar_variables(codigo)
        self.metadatos = MetadatosRegex().encontrar_metadatos(codigo)
        self.estructuras = EstructurasRegex().encontrar_estructuras(codigo)
        self.operaciones = OperacionesRegex().encontrar_operaciones(codigo)
        self.constantes = ConstantesRegex().extraer_constantes(codigo)
        self.nombre_programa = ProgramaNombreRegex().encontrar_programa_nombre(codigo)
        self.output = OutputRegex().encontrar_output(codigo)

        self.plantilla = "plantilla.docx"

    def obtener_datos(self) -> dict[str, Any]:
        return {
            "variables": self.variables,
            "metadatos": self.metadatos,
            "estructuras": self.estructuras,
            "operaciones": self.operaciones,
            "constantes": self.constantes,
            "programa_nombre": self.nombre_programa.get('nombre', 'DEFINIR'),
            "output": self.output,
        }

    def limpiar_datos(self):
        metadatos = self.obtener_datos().get('metadatos', [])

        variables: list[dict[str, str]] = []
        formulas: list[dict[str, str]] = []
        situaciones: list[dict[str, str]] = []

        for variable in self.obtener_datos().get('variables', []):
            valor = "Si "
            
            if variable['constante'] == 'Si':
                indice = next((i for i, m in enumerate(self.obtener_datos().get('constantes', [])) if m['nombre'] == variable['nombre']), None)
                
                valor += f"({self.obtener_datos().get('constantes', [])[indice]['valor']})" if indice is not None else ""
            
            variables.append({
                "nombre": variable['nombre'],
                "tipo": variable['tipo'],
                "init": 'No' if variable['constante'] != 'Si' else valor,
            })

        for formula in self.obtener_datos().get('operaciones', []):
            formulas.append({
                "formula": formula['operacion'],
                "descripcion": formula.get('comentario', ''),
            })
        
        for situacion in self.obtener_datos().get('estructuras', []):
            if situacion['tipo'] == 'Si':
                situaciones.append({
                    "situacion": situacion.get('condicion', ''),
                    "descripcion": situacion.get('comentario', ''),
                })
            elif situacion['tipo'] == 'SiNo':
                situaciones.append({
                    "situacion": 'SiNo',
                    "descripcion": situacion.get('comentario', ''),
                })

        datos: dict[str, Any] = {
            'nombre_programador': next((m['valor'] for m in metadatos if m['clave'] == 'Author'), ''),
            'descripcion_modulo': next((m['valor'] for m in metadatos if m['clave'] == 'Description'), ''),
            'programa_nombre': self.nombre_programa.get('nombre', 'DEFINIR'),
            'entradas': variables,
            'salidas': self.output,
            'formulas': formulas,
            'situaciones': situaciones,
        }

        return datos

    def generar_documentacion(self, salida: str = "documentacion.docx"):
        try:
            generate_doc = GenerateDocumentacion(self.plantilla, datos=self.limpiar_datos(), salida=salida) # type: ignore
            generate_doc.generar_documento()
        except Exception as e:
            print(f"Error al generar la documentación: {e}")