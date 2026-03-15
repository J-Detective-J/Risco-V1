
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
    
    def __init__(self,modo_interactivo=False):
        self.memoria = {}  # diccionario para variables
        self.vals = set() # variables inmutables (val)
        self.ultimo_resultado = None
        self.modo_interactivo = modo_interactivo
        
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
        
        if nombre in self.memoria:
            raise Exception(f"Error: '{nombre}' ya está definida y no puede redeclararse")
    
        if ctx.VAL() is not None:
            self.memoria[nombre] = valor
            self.vals.add(nombre)
        else:
            self.memoria[nombre] = valor
        return None
    
    def visitAsignacion(self, ctx: RISCOParser.AsignacionContext): 
        """
        Reasigna el valor de una variable existente.

        Solo permite modificar variables previamente declaradas con var.
        Intentar asignar a una variable no declarada lanza error.
        Intentar asignar a una variable val lanza error de inmutabilidad.

        Args:
            ctx: Contexto del nodo 'asignacion'.
                Contiene el IDENTIFICADOR y la nueva expresión.

        Returns:
            El nuevo valor asignado.

        Raises:
            Exception: Si la variable no existe en memoria.
            Exception: Si la variable es inmutable (val).
        """
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        
        if nombre not in self.memoria:
            raise Exception(f"Error: Variable '{nombre}' no definida")
        if nombre in self.vals:
            raise Exception(f"Error: '{nombre}' es inmutable, no se puede reasignar")
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
        if self.modo_interactivo:
            print(f"> {resultado}")
        return resultado

    def visitPrint_stmt(self, ctx):
        valor = self.visit(ctx.expresion())
        print(valor) # Imprime cualquier tipo de dato, sin conversiones implicitas
        return None

    
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
    
    def visitIf_stmt(self, ctx: RISCOParser.If_stmtContext):
        """
        Evalúa un condicional if/elif/else.

        Evalúa la condición del if. Si es verdadera ejecuta su bloque
        y termina. Si no, evalúa cada elif en orden. Si ninguno es
        verdadero y hay un else, ejecuta su bloque.

        Args:
            ctx: Contexto del nodo 'if_stmt'.

        Returns:
            None.

        Raises:
            Exception: Si la condición no evalúa a Bool.
        """
        # Recoger todas las expresiones (if + cada elif)
        expresiones = ctx.expresion()
        # Recoger todos los bloques de sentencias
        # ANTLR agrupa las sentencias en orden: bloque if, bloque elif1, bloque elif2, bloque else
        bloques = self._obtener_bloques_if(ctx)

        # Evaluar if
        condicion = self.visit(expresiones[0])
        if not isinstance(condicion, bool):
            raise Exception(
                f"Error de tipos: la condición del 'if' debe ser Bool, "
                f"no '{type(condicion).__name__}'"
            )
        if condicion:
            for sentencia in bloques[0]:
                self.visit(sentencia)
            return None

        # Evaluar elif(s)
        num_elif = len(expresiones) - 1
        for i in range(num_elif):
            condicion = self.visit(expresiones[i + 1])
            if not isinstance(condicion, bool):
                raise Exception(
                    f"Error de tipos: la condición del 'elif' debe ser Bool, "
                    f"no '{type(condicion).__name__}'"
                )
            if condicion:
                for sentencia in bloques[i + 1]:
                    self.visit(sentencia)
                return None

        # Evaluar else si existe
        tiene_else = ctx.ELSE() is not None
        if tiene_else:
            for sentencia in bloques[-1]:
                self.visit(sentencia)

        return None

    def _obtener_bloques_if(self, ctx: RISCOParser.If_stmtContext):
        """
        Separa las sentencias del if_stmt en bloques según los tokens
        IF, ELIF, ELSE y END.

        Returns:
            Lista de listas de sentencias. El índice 0 es el bloque if,
            los siguientes son los bloques elif, y el último es el else
            si existe.
        """
        bloques = []
        bloque_actual = []

        for i in range(ctx.getChildCount()):
            hijo = ctx.getChild(i)
            texto = hijo.getText()

            if texto in ('if', 'elif', 'else', 'end'):
                if texto in ('elif', 'else', 'end') and bloque_actual is not None:
                    bloques.append(bloque_actual)
                    bloque_actual = []
                if texto == 'end':
                    bloque_actual = None
            elif hasattr(hijo, 'getRuleIndex'):
                # Es una sentencia (nodo del árbol, no token)
                if bloque_actual is not None:
                    bloque_actual.append(hijo)

        return bloques

    def visitWhile_stmt(self, ctx: RISCOParser.While_stmtContext):
        """
        Evalúa un bucle while.

        Evalúa la condición antes de cada iteración. Si es verdadera
        ejecuta el bloque. Si es falsa desde el inicio, no ejecuta nada.

        Args:
            ctx: Contexto del nodo 'while_stmt'.

        Returns:
            None.

        Raises:
            Exception: Si la condición no evalúa a Bool.
        """
        while True:
            condicion = self.visit(ctx.expresion())
            if not isinstance(condicion, bool):
                raise Exception(
                    f"Error de tipos: la condición del 'while' debe ser Bool, "
                    f"no '{type(condicion).__name__}'"
                )
            if not condicion:
                break
            for sentencia in ctx.sentencia():
                self.visit(sentencia)
        return None
    
    # Expresiones
    def visitExpresion(self, ctx: RISCOParser.ExpresionContext):
        """
        Punto de entrada de la jerarquía de expresiones.

        Delega directamente a or_logico, que es el nivel de menor
        precedencia en la jerarquía de operadores de RISCO.

        Args:
            ctx: Contexto del nodo 'expresion'.

        Returns:
            El valor evaluado por or_logico.
        """
        return self.visit(ctx.or_logico())
    
    def visitOr_logico(self, ctx: RISCOParser.Or_logicoContext):
        """
        Evalúa el operador lógico OR (||).

        Si solo hay un hijo, delega a and_logico.
        Si hay múltiples, evalúa de izquierda a derecha.
        Solo opera sobre valores Bool — lanza error si algún operando
        no es booleano.

        Ejemplo en RISCO:
            true || false   → True
            false || false  → False

        Args:
            ctx: Contexto del nodo 'or_logico'.

        Returns:
            bool resultado de aplicar OR entre los operandos.

        Raises:
            Exception: Si algún operando no es Bool.
        """
        resultado = self.visit(ctx.and_logico(0))
        for i in range(1, len(ctx.and_logico())):
            valor = self.visit(ctx.and_logico(i))
            if not isinstance(resultado, bool) or not isinstance(valor, bool):
                raise Exception(
                    f"Error de tipos: '||' solo opera sobre Bool, "
                    f"no sobre '{type(resultado).__name__}' y '{type(valor).__name__}'"
                )
            resultado = resultado or valor
        return resultado

    def visitAnd_logico(self, ctx: RISCOParser.And_logicoContext):
        """
        Evalúa el operador lógico AND (&&).

        Si solo hay un hijo, delega a igualdad.
        Si hay múltiples, evalúa de izquierda a derecha.
        Solo opera sobre valores Bool — lanza error si algún operando
        no es booleano.

        Ejemplo en RISCO:
            true && false   → False
            true && true    → True

        Args:
            ctx: Contexto del nodo 'and_logico'.

        Returns:
            bool resultado de aplicar AND entre los operandos.

        Raises:
            Exception: Si algún operando no es Bool.
        """
        resultado = self.visit(ctx.igualdad(0))
        for i in range(1, len(ctx.igualdad())):
            valor = self.visit(ctx.igualdad(i))
            if not isinstance(resultado, bool) or not isinstance(valor, bool):
                raise Exception(
                    f"Error de tipos: '&&' solo opera sobre Bool, "
                    f"no sobre '{type(resultado).__name__}' y '{type(valor).__name__}'"
                )
            resultado = resultado and valor
        return resultado
    
    def visitIgualdad(self, ctx: RISCOParser.IgualdadContext):
        """
        Evalúa los operadores de igualdad (== y !=).

        Si no hay operador, delega a relacional.
        Si hay operador, verifica que ambos operandos sean del mismo tipo
        antes de comparar — RISCO no permite comparar tipos distintos.

        Ejemplo en RISCO:
            5 == 5        → True
            "a" != "b"    → True
            5 == "hola"   → Error de tipos

        Args:
            ctx: Contexto del nodo 'igualdad'.

        Returns:
            bool resultado de la comparación, o el valor de relacional
            si no hay operador.

        Raises:
            Exception: Si los operandos son de tipos distintos.
        """
        if ctx.getChildCount() == 1:
            return self.visit(ctx.relacional(0))
        izq = self.visit(ctx.relacional(0))
        op  = ctx.getChild(1).getText()
        der = self.visit(ctx.relacional(1))
        if type(izq) != type(der):
            raise Exception(
                f"Error de tipos: '{op}' no puede comparar "
                f"'{type(izq).__name__}' y '{type(der).__name__}'"
            )
        if op == '==': return izq == der
        if op == '!=': return izq != der

    def visitRelacional(self, ctx: RISCOParser.RelacionalContext):
        """
        Evalúa los operadores relacionales (>, <, >=, <=).

        Si no hay operador, delega a suma.
        Si hay operador, verifica que ambos operandos sean números
        (Num o Decimal) — no permite comparar Bool ni otros tipos.
        La comprobación explícita de bool es necesaria porque en Python
        bool es subclase de int y pasaría la validación sin ella.

        Ejemplo en RISCO:
            5 > 3         → True
            3.14 <= 3.14  → True
            true > false  → Error de tipos

        Args:
            ctx: Contexto del nodo 'relacional'.

        Returns:
            bool resultado de la comparación, o el valor de suma
            si no hay operador.

        Raises:
            Exception: Si algún operando no es número o es Bool.
        """
        if ctx.getChildCount() == 1:
            return self.visit(ctx.suma(0))
        izq = self.visit(ctx.suma(0))
        op  = ctx.getChild(1).getText()
        der = self.visit(ctx.suma(1))
        
        if isinstance(izq, bool) or isinstance(der, bool) or \
        not isinstance(izq, (int, float)) or not isinstance(der, (int, float)):
            raise Exception(
                f"Error de tipos: '{op}' solo opera sobre números, "
                f"no sobre '{type(izq).__name__}' y '{type(der).__name__}'"
            )
        if op == '>':  return izq > der
        if op == '<':  return izq < der
        if op == '>=': return izq >= der
        if op == '<=': return izq <= der

    def visitSuma(self, ctx: RISCOParser.ExpresionContext):
        """
        Evalúa sumas y restas.

        Si solo hay un hijo, delega a comparacion.
        Si hay múltiples, evalúa de izquierda a derecha aplicando + o -.
        El operador + valida que ambos operandos sean del mismo tipo.
        El operador - valida que ambos sean números y no Bool.

        Ejemplo en RISCO:
            5 + 3           → 8
            "hola" + " RC"  → "hola RC"
            [1] + [2]       → [1, 2]
            "a" - "b"       → Error de tipos
            True + False    → Error de tipos

        Args:
            ctx: Contexto del nodo 'suma'.

        Returns:
            Resultado de la suma/resta entre los operandos.

        Raises:
            Exception: Si los tipos son incompatibles con el operador.
        """

        if ctx.getChildCount() == 1:
            return self.visit(ctx.comparacion(0))
        
        resultado = self.visit(ctx.comparacion(0))
        for i in range(1, len(ctx.comparacion())):
            operador = ctx.getChild(2*i - 1).getText()
            valor = self.visit(ctx.comparacion(i))
            
            # Operaciones suma y resta con validaciones de tipo
            if operador == '+':
                if isinstance(resultado, bool):
                    raise Exception(
                        f"Error de tipos: '+' no está definido para Bool"
                    )
                if type(resultado) != type(valor):
                    raise Exception(
                        f"Error de tipos: '+' no puede operar "
                        f"'{type(resultado).__name__}' y '{type(valor).__name__}'"
                    )
                resultado += valor
            elif operador == '-':
                if isinstance(resultado, bool) or isinstance(valor, bool) or \
                    not isinstance(resultado, (int, float)) or not isinstance(valor, (int, float)):
                    raise Exception(
                        f"Error de tipos: '-' solo opera sobre números"
                    )
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
            return self.visit(ctx.potencia(0))
        
        resultado = self.visit(ctx.potencia(0))
        for i in range(1, len(ctx.potencia())):
            operador = ctx.getChild(2*i - 1).getText()
            valor = self.visit(ctx.potencia(i))
            
            # Operaciones multiplicación, división y módulo con validaciones de tipo
            if operador == '*':
                if isinstance(resultado, bool) or isinstance(valor, bool) or \
                    not isinstance(resultado, (int, float)) or not isinstance(valor, (int, float)):
                    raise Exception("Error de tipos: '*' solo opera sobre números")
                resultado *= valor
            elif operador == '/':
                if isinstance(resultado, bool) or isinstance(valor, bool) or \
                    not isinstance(resultado, (int, float)) or not isinstance(valor, (int, float)):
                    raise Exception("Error de tipos: '/' solo opera sobre números")
                if valor == 0:
                    raise Exception("Error: División por cero")
                resultado /= valor
            elif operador == '%':
                if isinstance(resultado, bool) or isinstance(valor, bool) or \
                    not isinstance(resultado, (int, float)) or not isinstance(valor, (int, float)):
                    raise Exception("Error de tipos: '%' solo opera sobre números")
                resultado %= valor
        return resultado
    
    def visitPotencia(self, ctx: RISCOParser.PotenciaContext):
        """
        Evalúa potencias con asociatividad derecha.
        2 ^ 3 ^ 2 se evalúa como 2 ^ (3 ^ 2) = 512.
        Solo opera sobre números, no sobre Bool ni otros tipos.
        """
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primario())
        
        base = self.visit(ctx.primario()) 
        exp  = self.visit(ctx.potencia())
        
        if isinstance(base, bool) or isinstance(exp, bool) or \
        not isinstance(base, (int, float)) or not isinstance(exp, (int, float)):
            raise Exception("Error de tipos: '^' solo opera sobre números")
        
        return base ** exp
    
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
            if not isinstance(valor, bool):
                raise Exception(
                    f"Error de tipos: '!' solo opera sobre Bool, "
                    f"no sobre '{type(valor).__name__}'"
                )
            return not valor
        
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
    
