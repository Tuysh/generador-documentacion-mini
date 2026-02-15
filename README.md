# Generador de Documentación Mini

Este programa convierte archivos de PSeInt en documentos de Word con formato profesional.

## ¿Qué hace?

Toma tu código de PSeInt y lo transforma en un documento Word bien organizado, listo para entregar o imprimir.

## ¿Qué necesitas?

- Python instalado en tu computadora
- El archivo de PSeInt que quieres convertir
- La plantilla `plantilla.docx` (debe estar en la misma carpeta donde ejecutas el programa)

## Instalación

1. Descarga o clona este proyecto en tu computadora
2. Abre una terminal o consola de comandos en la carpeta del proyecto
3. Instala las dependencias necesarias:
   ```
   pip install -r requeriments.txt
   ```

## ¿Cómo usar?

### Forma básica

```
python gmd.py tu_archivo.psc
```

Esto creará un archivo llamado `documentacion.docx` con tu código documentado.

### Personalizar el nombre del documento

```
python gmd.py tu_archivo.psc mi_documento.docx
```

Esto creará un archivo con el nombre que tú elijas.

## Importante

- La plantilla `plantilla.docx` debe estar en la carpeta raíz del proyecto
- Solo funciona con archivos de PSeInt (extensión `.psc`)
- El documento generado se guardará en la misma carpeta donde ejecutes el programa
- Revisa la sintaxis de los comentario en [SINTAXIS.md](SINTAXIS.md)

## Ejemplo

Si tienes un archivo llamado `programa.psc`:

```
python gmd.py programa.psc
```

Obtendrás un archivo `documentacion.docx` listo para usar.

## Licencia

Este proyecto está bajo la Licencia MIT - puedes usarlo libremente para tus proyectos.
