from gdm import FileReader, Datos, get_args

def main():
    try:
        print("Generador de Documentación Mini - Procesando archivo...")
        args = get_args()
        fileReader = FileReader(args['archivo'])
        contenido = fileReader.content()

        datos = Datos(contenido)
        datos.limpiar_datos()
        datos.generar_documentacion(salida=args['salida'])

        print(f"Documentación generada exitosamente en: {args['salida']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()