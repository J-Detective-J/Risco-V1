# RISCO

RISCO es un Lenguaje de Dominio Específico (DSL) orientado a operaciones de deep learning y machine learning, implementado con ANTLR4 y Python. Sigue el paradigma funcional con variables inmutables (`val`) y mutables (`var`), tipado dinámico y fuerte sin conversiones implícitas, y respeta la precedencia de operadores.

## Características

- Variables inmutables (`val`) y mutables (`var`) — ninguna puede redeclararse
- Tipado fuerte: sin conversiones implícitas entre tipos
- Validación de tipos en todos los operadores (`+` `-` `*` `/` `%` `^` `!` `&&` `||` `==` `!=` `>` `<` `>=` `<=`)
- Números enteros (`Num`), decimales (`Decimal`), texto (`Text`), booleanos (`Bool`), listas y `null`
- Concatenación de strings con `+`
- Operadores relacionales y lógicos
- Condicionales `if / elif / else`
- Bucle `for` con iteración sobre listas y strings
- Bucle `while`
- Operador `in` para verificar pertenencia
- `print()` acepta cualquier tipo de dato
- Modo interactivo (REPL) con auto-print de expresiones
- Solo acepta archivos con extensión `.rc`
- Suite de 88 pruebas automatizadas con pytest

## Limitaciones actuales (primera entrega)

- No hay input de usuario en modo archivo
- No hay indexación de listas (`lista[i]` no implementado aún)
- No hay casteo explícito (`Num()`, `Text()`, etc. — pendiente)
- No hay funciones definidas por el usuario (pendiente)
- El modo interactivo solo soporta expresiones de una línea

## Requisitos previos

Con instrucciones para instalar en Linux (Debian/Ubuntu):

- Python 3.8 o superior
```bash
sudo apt install -y python3-full python3-pip
sudo apt install python3-pip python3-venv
sudo apt install pipx
```

- antlr4
```bash
pip3 install --user antlr4-tools
```
Si no funciona:
```bash
pipx install antlr4-tools
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

- Java Runtime (para ANTLR)
```bash
sudo apt install default-jre
```

## Instalación

### 1. Clonar el repositorio y ubicarse en la carpeta
```bash
git clone <url-del-repo>
cd Risco-V1
```

### 2. Crear y activar entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requisitos.txt
```

### 4. Generar el parser
```bash
chmod +x generar.sh
./generar.sh
```

## ¿Cómo usar RISCO?

### Modo interactivo
```bash
python src/risco.py
```
El modo interactivo imprime automáticamente el resultado de cualquier expresión suelta con el prefijo `>`. Solo soporta expresiones de una línea — para bloques como `for`, `if` o `while` usar archivos `.rc`.

### Ejecutar un archivo
Crea un archivo con extensión `.rc` y ejecútalo:
```bash
python src/risco.py ejemplos/nombre_del_archivo.rc
```
RISCO rechaza archivos con cualquier otra extensión.

## Sintaxis

### Variables
```
val PI = 3.14159    // inmutable, no se puede reasignar ni redeclarar
var contador = 0    // mutable, se puede reasignar pero no redeclarar
contador = contador + 1
```

### Operadores aritméticos
| Operador | Descripción | Tipos válidos |
|----------|-------------|---------------|
| `+` | Suma / concatenación | Num+Num, Decimal+Decimal, Text+Text, Lista+Lista |
| `-` | Resta | Solo números |
| `*` | Multiplicación | Solo números |
| `/` | División | Solo números |
| `%` | Módulo | Solo números |
| `^` | Potencia (asociativo derecha) | Solo números |

### Operadores relacionales y lógicos
| Operador | Descripción | Tipos válidos |
|----------|-------------|---------------|
| `>` `<` `>=` `<=` | Comparación | Solo números |
| `==` `!=` | Igualdad | Mismo tipo |
| `&&` | AND lógico | Solo Bool |
| `\|\|` | OR lógico | Solo Bool |
| `!` | NOT lógico | Solo Bool |

### Condicionales
```
if x > 0:
    print("positivo")
elif x == 0:
    print("cero")
else:
    print("negativo")
end
```

### Bucle for
Itera sobre listas o strings:
```
val numeros = [1, 2, 3, 4, 5]
for n in numeros:
    print(n)
end

for letra in "hola":
    print(letra)
end
```

### Bucle while
```
var i = 0
while i < 5:
    print(i)
    i = i + 1
end
```

### Print
Acepta cualquier tipo de dato sin conversión implícita:
```
print("hola")
print(42)
print(3.14)
print(true)
print([1, 2, 3])
print(null)
```

### Operador in
```
val frutas = ["manzana", "pera", "uva"]
print("pera" in frutas)    // True
print("kiwi" in frutas)    // False
```

### Comentarios
```
// Comentario de línea
/- Comentario
   de bloque -/
/// Comentario de documentación
```

## Ejemplos

Los archivos de ejemplo están en la carpeta `ejemplos/`:

| Archivo | Descripción |
|---------|-------------|
| `operaciones_basicas.rc` | Suma, resta, multiplicación, división, potencia |
| `variables.rc` | Variables mutables e inmutables |
| `precedencia.rc` | Precedencia y asociatividad de operadores |
| `area_circulo.rc` | Cálculo del área de un círculo |
| `ciclofor_in.rc` | Bucle `for` y operador `in` |
| `estadisticas.rc` | Estadísticas básicas sobre una lista de datos |
| `tablas.rc` | Tablas de multiplicar con while anidado |
| `fizzbuzz.rc` | FizzBuzz del 1 al 20 con while, if/elif/else y operadores lógicos |
| `comerFrutas.rc` | Dispensadora de frutas con for e if/else |
| `prueba_completa.rc` | Demo de todas las características implementadas |

## Pruebas

El proyecto incluye 88 pruebas automatizadas con pytest:

```bash
pytest tests/ -v
```

Para correr una prueba específica:
```bash
pytest tests/test_risco.py::test_suma -v
```

Cuando agregues una feature nueva:
1. Modifica `gramaticas/RISCO.g4` si cambia la gramática
2. Regenera el parser si cambiaste el `.g4`: `./generar.sh`
3. Agrega la lógica en `src/visitante_evaluador.py`
4. Agrega sus pruebas en `tests/test_risco.py`
5. Verifica que todo sigue en orden: `pytest tests/ -v`

## Estructura del proyecto

```
Risco-V1/
  gramaticas/
    RISCO.g4              # Gramática del lenguaje (editado por el equipo)
    RISCOLexer.py         # Generado por ANTLR — no editar
    RISCOParser.py        # Generado por ANTLR — no editar
    RISCOVisitor.py       # Generado por ANTLR — no editar
  src/
    risco.py              # Punto de entrada del intérprete
    visitante_evaluador.py # Lógica de evaluación (editado por el equipo)
    manejador_errores.py  # Manejo de errores sintácticos
  ejemplos/
    *.rc                  # Archivos de ejemplo
  tests/
    test_risco.py         # Suite de pruebas
  generar.sh              # Script para regenerar el parser
  requisitos.txt          # Dependencias Python
```

## Decisiones de diseño

| Característica | Decisión | Justificación |
|---|---|---|
| Tipado | Dinámico y fuerte | Flexible pero sin conversiones silenciosas |
| Inmutabilidad | `val` — no reasignable ni redeclarable | Estilo funcional |
| `var` | Reasignable pero no redeclarable | Consistencia de scope |
| División | Devuelve el resultado de Python (`/`) | Sin símbolo de división entera — `//` es comentario |
| Extensión | `.rc` obligatoria | Identifica archivos del intérprete |
| Bool en aritmética | No permitido | `bool` es subclase de `int` en Python — validación explícita necesaria |
| Palabras reservadas | Declaradas antes de `IDENTIFICADOR` en la gramática | El lexer hace match con la primera regla que encaje |
| Operadores de dos caracteres | Declarados antes de `>` y `<` | Evita que `>=` se tokenice como `>` seguido de `=` |