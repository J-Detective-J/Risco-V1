
"""
visitante_evaluador.py
======================
Implementa el patrón Visitor sobre el árbol de sintaxis (AST) generado
por ANTLR para el lenguaje RISCO.

El visitor recorre el árbol nodo por nodo y ejecuta la lógica de cada
construcción del lenguaje: declaraciones, asignaciones, expresiones,
bucles, etc.

Patrón de funcionamiento:
    1. ANTLR construye el AST a partir del código fuente.
    2. VisitanteEvaluador hereda de RISCOVisitor (generado por ANTLR).
    3. Cada método visitX() corresponde a una regla X de la gramática.
    4. self.visit(nodo) delega al método correcto según el tipo del nodo.
    5. El estado del programa (variables) se mantiene en self.memoria.
"""

from antlr4 import *
from gramaticas.RISCOParser import RISCOParser     
from gramaticas.RISCOVisitor import RISCOVisitor   

class VisitanteEvaluador(RISCOVisitor):            
    """
    Visitor que evalúa el AST de un programa RISCO.

    Mantiene el estado del programa en un diccionario (memoria) que
    asocia nombres de variables con sus valores actuales.

    Atributos:
        memoria (dict): Almacena las variables del programa.
                        Clave: nombre de la variable (str).
                        Valor: cualquier valor soportado por RISCO.
        ultimo_resultado: Último valor evaluado, útil para el modo REPL.
    """
    
    def __init__(self):
        self.memoria = {}  # diccionario para variables
        self.ultimo_resultado = None
        
    # Programa
    def visitPrograma(self, ctx: RISCOParser.ProgramaContext):
        """
        Punto de entrada del visitor.

        Recorre todas las sentencias del programa en orden y las evalúa.
        Los errores en una sentencia se capturan e imprimen sin detener
        la ejecución de las sentencias siguientes.

        Args:
            ctx: Contexto del nodo 'programa' en el AST.

        Return:
            El último resultado evaluado (útil en modo interactivo).
        """

        for sentencia in ctx.sentencia():
            try:
                resultado = self.visit(sentencia)
                if resultado is not None:
                    self.ultimo_resultado = resultado
            except Exception as e:
                print(f"Error: {e}")
        return self.ultimo_resultado
    
    # Sentencias
    def visitDeclaracion_variable(self, ctx: RISCOParser.Declaracion_variableContext):
        """
        Declara una nueva variable en memoria.

        Distingue entre:
          - val: inmutable. Lanza error si se intenta declarar de nuevo.
          - var: mutable. Puede reasignarse con visitAsignacion.

        Args:
            ctx: Contexto del nodo 'declaracion_variable'.
                 Contiene el token VAL o VAR, el IDENTIFICADOR y la expresión.

        Returns:
            None (las declaraciones no producen output visible).

        Raises:
            Exception: Si se intenta redeclarar una variable val.
        """

        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        
        if ctx.VAL() is not None:  # val
            if nombre in self.memoria:
                raise Exception(f"Error: '{nombre}' ya está definida como val")
            self.memoria[nombre] = valor
        else:  # var
            self.memoria[nombre] = valor
        return None
    
    def visitAsignacion(self, ctx: RISCOParser.AsignacionContext): 
        """
        Reasigna el valor de una variable existente.

        Solo permite modificar variables previamente declaradas con var.
        Intentar asignar a una variable no declarada lanza error.

        Args:
            ctx: Contexto del nodo 'asignacion'.
                 Contiene el IDENTIFICADOR y la nueva expresión.

        Returns:
            El nuevo valor asignado.

        Raises:
            Exception: Si la variable no existe en memoria.
        """
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())  
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        
        if nombre not in self.memoria:
            raise Exception(f"Error: Variable '{nombre}' no definida")
        self.memoria[nombre] = valor
        return valor
    
    def visitExpresion_stmt(self, ctx: RISCOParser.Expresion_stmtContext):
        """
        Evalúa una expresión suelta e imprime su resultado.

        Es la forma de producir output visible en RISCO. Cualquier
        expresión escrita sola en una línea se evalúa y se muestra
        con el prefijo ">".

        Ejemplo en RISCO:
            2 + 3     →  imprime: > 5

        Args:
            ctx: Contexto del nodo 'expresion_stmt'.

        Returns:
            El valor evaluado de la expresión.
        """
        resultado = self.visit(ctx.expresion())
        print(f"> {resultado}")

    def visitPrint_stmt(self, ctx):
        valor = self.visit(ctx.expresion())

        if not isinstance(valor, str):
            raise Exception("print() solo permite strings")

        print(valor)
        return None

        return resultado
    
    def visitFor_stmt(self, ctx: RISCOParser.For_stmtContext):
        """
        Ejecuta un bucle for sobre un iterable (lista o string).

        En cada iteración:
          1. Asigna el elemento actual a la variable de iteración en memoria.
          2. Ejecuta todas las sentencias del cuerpo del bloque.

        Al terminar, la variable de iteración se elimina de memoria
        para respetar el scope del bloque.

        Ejemplo en RISCO:
            for n in [1, 2, 3]:
                n * 2
            end
            → imprime: > 2, > 4, > 6

        Args:
            ctx: Contexto del nodo 'for_stmt'.
                 Contiene IDENTIFICADOR, expresión iterable y sentencias del cuerpo.

        Returns:
            None.

        Raises:
            Exception: Si la expresión no es una lista ni un string.
        """
        nombre_var = ctx.IDENTIFICADOR().getText()
        iterable = self.visit(ctx.expresion())

        # Verificar que sea iterable (lista o string)
        if not isinstance(iterable, (list, str)):
            raise Exception(f"Error: '{iterable}' no es iterable en for")

        for elemento in iterable:
            # La variable del for existe solo dentro del bloque
            self.memoria[nombre_var] = elemento
            for sentencia in ctx.sentencia():
                try:
                    self.visit(sentencia)
                except Exception as e:
                    print(f"Error en for: {e}")
    
        # Limpiar la variable de iteración al salir
        if nombre_var in self.memoria:
            del self.memoria[nombre_var]
    
        return None
    
    # Expresiones
    def visitExpresion(self, ctx: RISCOParser.ExpresionContext):
        """
        Evalúa sumas y restas (menor precedencia).

        Si solo hay un hijo, delega directamente a comparacion.
        Si hay múltiples, evalúa de izquierda a derecha aplicando + o -.

        Args:
            ctx: Contexto del nodo 'expresion'.

        Returns:
            Resultado numérico o string (en caso de concatenación con +).
        """

        if ctx.getChildCount() == 1:
            return self.visit(ctx.comparacion(0))
        
        resultado = self.visit(ctx.comparacion(0))
        for i in range(1, len(ctx.comparacion())):
            operador = ctx.getChild(2*i - 1).getText()
            valor = self.visit(ctx.comparacion(i))
            
            if operador == '+':
                resultado += valor
            elif operador == '-':
                resultado -= valor
        return resultado
    
    def visitComparacion(self, ctx: RISCOParser.ComparacionContext):
        """
        Evalúa el operador de pertenencia 'in'.

        Si no hay operador 'in', actúa como pass-through hacia termino.
        Si hay 'in', verifica si el valor izquierdo existe en el iterable derecho.

        Ejemplo en RISCO:
            "pera" in ["manzana", "pera"]   → True
            5 in [1, 2, 3]                  → False

        Args:
            ctx: Contexto del nodo 'comparacion'.

        Returns:
            bool si hay operador 'in', o el valor del termino si no lo hay.

        Raises:
            Exception: Si el operando derecho no es lista ni string.
        """
        izquierda = self.visit(ctx.termino(0))
    
        if ctx.getChildCount() == 1:
            return izquierda
    
        # Es una expresión "x in colección"
        derecha = self.visit(ctx.termino(1))
    
        if not isinstance(derecha, (list, str)):
            raise Exception(f"Error: 'in' requiere una lista o string a la derecha")
    
        return izquierda in derecha
    
    def visitTermino(self, ctx: RISCOParser.TerminoContext):
        """
        Evalúa multiplicación, división y módulo.

        Evalúa de izquierda a derecha. La división por cero lanza error.

        Args:
            ctx: Contexto del nodo 'termino'.

        Returns:
            Resultado numérico.

        Raises:
            Exception: Si se intenta dividir por cero.
        """    
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor(0))
        
        resultado = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            operador = ctx.getChild(2*i - 1).getText()
            valor = self.visit(ctx.factor(i))
            
            if operador == '*':
                resultado *= valor
            elif operador == '/':
                if valor == 0:
                    raise Exception("Error: División por cero")
                resultado /= valor
            elif operador == '%':
                resultado %= valor
        return resultado
    
    def visitFactor(self, ctx: RISCOParser.FactorContext):
        """
        Evalúa potencias con asociatividad izquierda (nivel intermedio).

        Este nivel delega en 'potencia' para la asociatividad derecha real.

        Args:
            ctx: Contexto del nodo 'factor'.

        Returns:
            Resultado numérico.
        """         
        if ctx.getChildCount() == 1:
            return self.visit(ctx.potencia(0))
        
        resultado = self.visit(ctx.potencia(0))
        for i in range(1, len(ctx.potencia())):
            operador = ctx.getChild(2*i - 1).getText()
            valor = self.visit(ctx.potencia(i))
            
            if operador == '^':
                resultado = resultado ** valor
        return resultado
    
    def visitPotencia(self, ctx: RISCOParser.PotenciaContext):
        """
        Evalúa potencias con asociatividad derecha.

        La forma recursiva "primario ^ potencia" garantiza que
        2 ^ 3 ^ 2 se evalúe como 2 ^ (3 ^ 2) = 512.

        Args:
            ctx: Contexto del nodo 'potencia'.

        Returns:
            Resultado numérico.
        """     
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primario())
        return self.visit(ctx.primario(0)) ** self.visit(ctx.potencia())
    
    def visitPrimario(self, ctx: RISCOParser.PrimarioContext):
        """
        Evalúa valores primarios: literales, variables, expresiones agrupadas
        y operadores unarios.

        Casos manejados:
          - NUMERO      → int
          - DECIMAL     → float
          - STRING      → str (sin comillas)
          - BOOLEANO    → bool
          - NULL        → None
          - lista       → list
          - IDENTIFICADOR → valor de la variable en memoria
          - (expresion) → evalúa la expresión interna
          - -primario   → negación numérica
          - !primario   → negación lógica

        Args:
            ctx: Contexto del nodo 'primario'.

        Returns:
            El valor del literal, variable u operación unaria.

        Raises:
            Exception: Si se usa una variable no definida en memoria.
        """ 
        if ctx.NUMERO():
            return int(ctx.NUMERO().getText())
        
        if ctx.DECIMAL():
            return float(ctx.DECIMAL().getText())
        
        if ctx.STRING():
            texto = ctx.STRING().getText()
            return texto[1:-1]  # Quitar comillas
        
        if ctx.BOOLEANO():
            return ctx.BOOLEANO().getText() == 'true'
        
        if ctx.NULL():
            return None
        
        if ctx.lista():
            return self.visit(ctx.lista())
        
        if ctx.IDENTIFICADOR():
            nombre = ctx.IDENTIFICADOR().getText()
            if nombre not in self.memoria:
                raise Exception(f"Error: Variable '{nombre}' no definida")
            return self.memoria[nombre]
        
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expresion())
        
        if ctx.getChild(0).getText() == '-':
            return -self.visit(ctx.primario())
        
        if ctx.getChild(0).getText() == '!':
            valor = self.visit(ctx.primario())
            return not bool(valor)
        
        return None
    
    def visitLista(self, ctx: RISCOParser.ListaContext):
        """
        Evalúa una lista literal.

        Recorre cada expresión dentro de los corchetes y construye
        una lista Python con los valores evaluados.

        Ejemplo en RISCO:
            [1 + 1, 2 * 3, x]   → [2, 6, <valor de x>]

        Args:
            ctx: Contexto del nodo 'lista'.

        Returns:
            list con los valores evaluados de cada elemento.
        """  
        elementos = []
        for expr in ctx.expresion():
            elementos.append(self.visit(expr))
        return elementos	
    def visitPrint_stmt(self, ctx):
        valor = self.visit(ctx.expresion())

        if not isinstance(valor, str):
            raise Exception("print() solo permite strings")

        print(valor)
        return None
