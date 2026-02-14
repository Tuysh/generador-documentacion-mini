from gdm import FileReader, Datos, get_args

if __name__ == "__main__":
    args = get_args()
    fileReader = FileReader(args['archivo'])
    contenido = fileReader.content()

    datos = Datos(contenido)
    datos.limpiar_datos()
    datos.generar_documentacion(salida=args['salida'])
