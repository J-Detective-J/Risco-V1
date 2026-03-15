import pytest
import sys
import os
from io import StringIO

# Para que encuentre los módulos de src y gramaticas
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.risco import RISCO

def ejecutar(codigo):
    """Ejecuta código RISCO y captura lo que imprime"""
    captura = StringIO()
    sys.stdout = captura
    interprete = RISCO(modo_interactivo=True)
    interprete._ejecutar_codigo(codigo)
    sys.stdout = sys.__stdout__
    return [l.strip() for l in captura.getvalue().strip().splitlines() if l.strip()]


# Operaciones básicas 

def test_suma():
    assert ejecutar("val x = 5\nval y = 3\nx + y\n") == ["> 8"]

def test_resta():
    assert ejecutar("val x = 5\nval y = 3\nx - y\n") == ["> 2"]

def test_multiplicacion():
    assert ejecutar("val x = 5\nval y = 3\nx * y\n") == ["> 15"]

def test_division():
    resultado = ejecutar("val x = 5\nval y = 3\nx / y\n")
    assert resultado == ["> 1.6666666666666667"]

def test_division_por_cero():
    resultado = ejecutar("1 / 0\n")
    assert any("División por cero" in r for r in resultado)

def test_modulo():
    assert ejecutar("10 % 3\n") == ["> 1"]

def test_potencia():
    assert ejecutar("2 ^ 3\n") == ["> 8"]


# Precedencia

def test_precedencia_suma_multiplicacion():
    assert ejecutar("2 + 3 * 4\n") == ["> 14"]

def test_precedencia_parentesis():
    assert ejecutar("(2 + 3) * 4\n") == ["> 20"]

def test_negativo_unario():
    assert ejecutar("-5\n") == ["> -5"]


# Variables 

def test_val_inmutable():
    resultado = ejecutar("val x = 10\nx\n")
    assert resultado == ["> 10"]

def test_val_no_reasignable():
    # Intentar redefinir un val debe lanzar error, no imprimir valor
    resultado = ejecutar("val x = 1\nval x = 2\n")
    assert "> 2" not in resultado

def test_var_mutable():
    assert ejecutar("var x = 0\nx = x + 1\nx = x + 1\nx\n") == ["> 2"]

def test_variable_no_definida():
    resultado = ejecutar("z\n")
    assert any("no definida" in r for r in resultado)


# Strings 

def test_string():
    assert ejecutar('"hola"\n') == ['> hola']

def test_string_concatenacion():
    assert ejecutar('"hola" + " risco"\n') == ['> hola risco']


#  Booleanos

def test_booleano_true():
    assert ejecutar("true\n") == ["> True"]

def test_booleano_false():
    assert ejecutar("false\n") == ["> False"]

def test_not_logico():
    assert ejecutar("!true\n") == ["> False"]


# Listas

def test_lista():
    assert ejecutar("[1, 2, 3]\n") == ["> [1, 2, 3]"]

def test_lista_vacia():
    assert ejecutar("[]\n") == ["> []"]


# For

def test_for_lista():
    codigo = "val nums = [1, 2, 3]\nfor n in nums:\n    n\nend\n"
    assert ejecutar(codigo) == ["> 1", "> 2", "> 3"]

def test_for_string():
    codigo = 'val p = "ab"\nfor c in p:\n    c\nend\n'
    assert ejecutar(codigo) == ["> a", "> b"]

def test_for_variable_no_existe_fuera():
    # Después del for, n no debe existir
    codigo = "val nums = [1]\nfor n in nums:\n    n\nend\nn\n"
    lineas = ejecutar(codigo)
    assert "> 1" in lineas       # dentro del for sí imprime
    assert lineas[-1] != "> 1"   # fuera del for no vuelve a imprimir


# In como expresión de comparacion

def test_in_verdadero():
    codigo = 'val frutas = ["pera", "uva"]\n"pera" in frutas\n'
    assert ejecutar(codigo) == ["> True"]

def test_in_falso():
    codigo = 'val frutas = ["pera", "uva"]\n"mango" in frutas\n'
    assert ejecutar(codigo) == ["> False"]

def test_in_numero():
    codigo = "val nums = [1, 2, 3]\n2 in nums\n"
    assert ejecutar(codigo) == ["> True"]

# print acepta cualquier tipo
def test_print_string():
    assert ejecutar('print("hola")\n') == ["hola"]

def test_print_numero():
    assert ejecutar('print(42)\n') == ["42"]

def test_print_decimal():
    assert ejecutar('print(3.14)\n') == ["3.14"]

def test_print_booleano():
    assert ejecutar('print(true)\n') == ["True"]

def test_print_lista():
    assert ejecutar('print([1, 2, 3])\n') == ["[1, 2, 3]"]

def test_print_null():
    assert ejecutar('print(null)\n') == ["None"]

def test_print_expresion():
    assert ejecutar('print(2 + 3)\n') == ["5"]

def test_print_variable():
    assert ejecutar('val x = 10\nprint(x)\n') == ["10"]

# Validación de tipos con errores

def test_suma_string_numero_error():
    resultado = ejecutar('"hola" + 3\n')
    assert any("Error de tipos" in r for r in resultado)

def test_suma_numero_string_error():
    resultado = ejecutar('3 + "hola"\n')
    assert any("Error de tipos" in r for r in resultado)

def test_resta_strings_error():
    resultado = ejecutar('"hola" - "h"\n')
    assert any("Error de tipos" in r for r in resultado)

def test_multiplicacion_string_numero_error():
    resultado = ejecutar('"hola" * 3\n')
    assert any("Error de tipos" in r for r in resultado)

def test_division_string_error():
    resultado = ejecutar('"hola" / 2\n')
    assert any("Error de tipos" in r for r in resultado)

def test_modulo_string_error():
    resultado = ejecutar('"hola" % 2\n')
    assert any("Error de tipos" in r for r in resultado)

def test_not_sobre_numero_error():
    resultado = ejecutar('!5\n')
    assert any("Error de tipos" in r for r in resultado)

def test_not_sobre_string_error():
    resultado = ejecutar('!"hola"\n')
    assert any("Error de tipos" in r for r in resultado)

# Operaciones válidas con tipos correctos

def test_suma_strings_valida():
    assert ejecutar('"hola" + " mundo"\n') == ["> hola mundo"]

def test_suma_numeros_valida():
    assert ejecutar('3 + 4\n') == ["> 7"]

def test_suma_listas_valida():
    assert ejecutar('[1, 2] + [3, 4]\n') == ["> [1, 2, 3, 4]"]

def test_not_booleano_valido():
    assert ejecutar('!false\n') == ["> True"]

# Operadores lógicos — solo booleanos
def test_and_no_booleano_error():
    resultado = ejecutar('5 && true\n')
    assert any("Error de tipos" in r for r in resultado)

def test_or_no_booleano_error():
    resultado = ejecutar('5 || true\n')
    assert any("Error de tipos" in r for r in resultado)

# Igualdad — tipos distintos
def test_igualdad_tipos_distintos_error():
    resultado = ejecutar('5 == "hola"\n')
    assert any("Error de tipos" in r for r in resultado)

# Relacionales — solo números
def test_relacional_string_error():
    resultado = ejecutar('"hola" > "mundo"\n')
    assert any("Error de tipos" in r for r in resultado)

def test_relacional_booleano_error():
    resultado = ejecutar('true > false\n')
    assert any("Error de tipos" in r for r in resultado)

# Casos válidos
def test_and_valido():
    assert ejecutar('true && false\n') == ["> False"]

def test_or_valido():
    assert ejecutar('true || false\n') == ["> True"]

def test_igualdad_numeros():
    assert ejecutar('5 == 5\n') == ["> True"]

def test_igualdad_strings():
    assert ejecutar('"hola" == "hola"\n') == ["> True"]

def test_relacional_valido():
    assert ejecutar('5 > 3\n') == ["> True"]