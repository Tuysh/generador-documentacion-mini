class FileReader:
    def __init__(self, path: str):
        self.path = path

    def content(self) -> str:
        try:
            with open(self.path, "r", encoding="windows-1252") as file:
                self.file = file
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"El archivo '{self.path}' no se encontró.")
        except IOError as e:
            raise IOError(f"Error al leer el archivo '{self.path}': {e}")
        except Exception as e:
            raise Exception(
                f"Ocurrió un error inesperado al leer el archivo '{self.path}': {e}"
            )

    def __exit__(
        self,
        exc_type: Exception | None,
        exc_val: Exception | None,
        exc_tb: Exception | None,
    ) -> None:
        self.file.close()
