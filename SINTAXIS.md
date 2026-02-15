# Sintaxis de Documentación para PSeInt

Este documento explica cómo debes escribir los comentarios especiales en tu código de PSeInt para que el generador pueda crear la documentación correctamente.

## Información General del Programa

### Nombre del Programa
```
Algoritmo NombreDelPrograma
```
El nombre que pongas después de `Algoritmo` será el título de tu documento.

### Metadatos (Información del autor y descripción)

Usa comentarios especiales al inicio de tu código:

```
// Author: Tu Nombre
// Description: Descripción breve de lo que hace el programa
```

**Importante:** Usa exactamente `Author` y `Description` (con mayúscula inicial).

## Variables

### Declarar Variables
```
Definir nombreVariable Como Entero
Definir edad, altura Como Real
Definir nombre, apellido Como Cadena
```

Las variables se documentarán automáticamente. Si la variable está en MAYÚSCULAS, se considerará una constante.

### Constantes
Las constantes deben escribirse completamente en MAYÚSCULAS y asignarles un valor:

```
Definir PI Como Real
PI <- 3.1416

Definir IVA Como Real
IVA <- 0.16
```

## Fórmulas y Operaciones

Para documentar una operación o cálculo, agrega un comentario explicativo usando `//`:

```
resultado <- (base * altura) / 2 // Calcula el área del triángulo
precio_final <- precio + (precio * IVA) // Aplica el IVA al precio
total <- cantidad * precio // Calcula el total de la compra
```

**Sin comentario:**
```
suma <- a + b
```
Se documentará solo la fórmula sin descripción.

**Con comentario:**
```
suma <- a + b // Suma dos números
```
Se documentará la fórmula con su descripción.

## Estructuras Condicionales (Situaciones)

### Condición Si
Para documentar una condición `Si`, agrega un comentario en la misma línea:

```
Si edad >= 18 Entonces // Verifica si es mayor de edad
    Escribir "Eres mayor de edad"
FinSi
```

### Condición SiNo
Para documentar el `SiNo`, agrega un comentario:

```
Si nota >= 70 Entonces // Verifica si aprobó
    Escribir "Aprobado"
SiNo // El estudiante reprobó
    Escribir "Reprobado"
FinSi
```

## Salidas (Outputs)

Para documentar las salidas o resultados del programa, usa esta sintaxis especial:

```
// Output: nombre_variable*Tipo* - Descripción de la salida
```

**Ejemplos:**
```
// Output: total*Real* - Total de la compra con IVA incluido
// Output: aprobado*Logico* - Indica si el estudiante aprobó o no
// Output: mensaje*Cadena* - Mensaje final para el usuario
```

**Formato:**
- Escribe `// Output:` seguido de un espacio
- Nombre de la variable
- Entre asteriscos el tipo (`*Entero*`, `*Real*`, `*Cadena*`, `*Logico*`)
- Un guión y espacio `- `
- La descripción de qué representa esa salida

## Ejemplo Completo

```
// Author: Juan Pérez
// Description: Programa que calcula el área de un triángulo

Algoritmo CalcularAreaTriangulo
    Definir base, altura, area Como Real
    
    Escribir "Ingrese la base del triángulo:"
    Leer base
    
    Escribir "Ingrese la altura del triángulo:"
    Leer altura
    
    area <- (base * altura) / 2 // Calcula el área usando la fórmula base por altura entre dos
    
    Si area > 0 Entonces // Verifica que el área sea válida
        Escribir "El área del triángulo es: ", area
    SiNo // El área no puede ser cero o negativa
        Escribir "Error: Los valores deben ser positivos"
    FinSi
    
    // Output: area*Real* - Área calculada del triángulo en unidades cuadradas
FinAlgoritmo
```

## Reglas Importantes

1. **Los comentarios de documentación deben ir en la misma línea** que la instrucción (operaciones, condicionales)
2. **Use `//` para los comentarios**, no `///` ni otros formatos
3. **Las constantes deben estar en MAYÚSCULAS** para ser reconocidas
4. **Los metadatos deben ir al inicio del archivo** antes del algoritmo
5. **El formato de Output es estricto**: respeta los asteriscos y el guión
6. **No uses tildes ni caracteres especiales** en los nombres de variables

## Tipos de Datos Válidos

- `Entero` - Números enteros
- `Real` - Números decimales
- `Cadena` - Texto
- `Logico` - Verdadero/Falso
- `Caracter` - Un solo carácter

## Consejos

- Escribe comentarios claros y descriptivos
- No uses abreviaturas difíciles de entender
- Documenta todas las fórmulas importantes
- Explica la lógica de tus condiciones
- Lista todas las salidas importantes de tu programa
