OPERACIONES_SIN_COMENTARIO_REGEX = r"\b[a-z][a-z0-9_]*\b\s+<-(\s+.*[\w|(+*)]|\n)"
OPERACIONES_CON_COMENTARIO_REGEX = r"\b[a-z][a-z0-9_]*\b\s+<-(\s+.*[\w|(+*)]|\n).*//\s+(.*\w)"

ESTRUCTURAS_SIN_COMENTARIO_REGEX = r""  # Por el momento no se diferencian, pero se deja la opción abierta para futuras mejoras
ESTRUCTURAS_CON_COMENTARIO_REGEX = r"\bSi\s+(.*\w*) Entonces\s+//\s+(.*\w)|SiNo\s+//\s+(.*\w)"

VARIABLES_REGEX = r"Definir\s+(.*?)\s+Como\s+(\w+)"

CONSTANTES_REGEX = r"\b[A-Z][A-Z0-9_]*\b\s+<-(\s+.*[\w|(+*)]|\n)"

METADATOS_REGEX = r"//.(\w+):.(.*)"

NOMBRE_PROGRAMA_REGEX = r"\bAlgoritmo\s+(.*)"

OUTPUT_REGEX = r"//\s+Output:\s+(.*)[(+*)](.*)[(+*)][\s]-\s(.*)"