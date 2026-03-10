# RISCO

RISCO es un Lenguaje de Dominio Específico (DSL) para realizar operaciones matemáticas y de control de flujo, implementado con ANTLR4 y Python. Sigue un estilo funcional con variables inmutables (`val`) y mutables (`var`), y respeta la precedencia de operadores.

## Características

- Variables inmutables (`val`) y mutables (`var`)
- Null y valores nulos
- Listas y operaciones
- Booleanos y operaciones lógicas
- Strings y concatenación
- Bucle `for` con iteración sobre listas y strings
- Operador `in` para verificar pertenencia
- Suite de pruebas automatizadas con pytest

## Requisitos previos

Con instrucciones para instalar en Linux (Debian):

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
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
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
> ⚠️ El modo interactivo solo soporta expresiones de una línea. Para bloques como `for`, usar archivos `.rc`.

### Ejecutar un archivo
Crea un archivo con extensión `.rc` y ejecútalo:
```bash
python src/risco.py ejemplos/nombre_del_archivo.rc
```

## Sintaxis

### Variables
```
val PI = 3.14159    // inmutable, no se puede reasignar
var contador = 0    // mutable
contador = contador + 1
```

### Operadores
| Operador | Descripción |
|----------|-------------|
| `+` `-` `*` `/` `%` | Aritméticos |
| `^` | Potencia |
| `!` | Not lógico |
| `in` | Pertenencia (devuelve booleano) |

### Listas
```
val numeros = [1, 2, 3, 4, 5]
val frutas = ["manzana", "pera", "uva"]
```

### Bucle for
Itera sobre listas o strings:
```
for n in numeros:
    n * 2
end

for letra in "hola":
    letra
end
```

### Operador in
```
"pera" in frutas    // > True
2 in numeros        // > True
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
| `ciclofor_in.rc` | Bucle `for` e operador `in` |

## Pruebas

El proyecto incluye una suite de pruebas automatizadas con pytest:

```bash
pytest tests/ -v
```

Para correr una prueba específica:
```bash
pytest tests/test_risco.py::test_for_lista -v
```

Cuando agregues una feature nueva:
1. Agrega sus tests en `tests/test_risco.py`
2. Regenera el parser si cambiaste el `.g4`: `./generar.sh`
3. Verifica que todo sigue en orden: `pytest tests/ -v`

## Estructura del proyecto

```
Risco-V1/
  gramaticas/
    RISCO.g4              # Gramática del lenguaje
    RISCOLexer.py         # Generado por ANTLR
    RISCOParser.py        # Generado por ANTLR
    RISCOVisitor.py       # Generado por ANTLR
  src/
    risco.py              # Intérprete principal
    visitante_evaluador.py # Lógica de evaluación
    manejador_errores.py  # Manejo de errores de sintaxis
  ejemplos/
    *.rc                  # Archivos de ejemplo
  tests/
    test_risco.py         # Suite de pruebas
  generar.sh              # Script para regenerar el parser
  requisitos.txt          # Dependencias Python
```