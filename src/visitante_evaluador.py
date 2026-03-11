
"""
Visitante evaluador para RISCO
"""

from antlr4 import *
from gramaticas.RISCOParser import RISCOParser     
from gramaticas.RISCOVisitor import RISCOVisitor   

class VisitanteEvaluador(RISCOVisitor):            
    """
    Visitante que evalúa expresiones y mantiene estado de variables
    """
    
    def __init__(self):
        self.memoria = {}  # diccionario para variables
        self.ultimo_resultado = None
        
    # Programa
    def visitPrograma(self, ctx: RISCOParser.ProgramaContext):       
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
        nombre = ctx.IDENTIFICADOR().getText()
        valor = self.visit(ctx.expresion())
        
        if nombre not in self.memoria:
            raise Exception(f"Error: Variable '{nombre}' no definida")
        self.memoria[nombre] = valor
        return valor
    
    def visitExpresion_stmt(self, ctx: RISCOParser.Expresion_stmtContext):
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
        izquierda = self.visit(ctx.termino(0))
    
        if ctx.getChildCount() == 1:
            return izquierda
    
        # Es una expresión "x in colección"
        derecha = self.visit(ctx.termino(1))
    
        if not isinstance(derecha, (list, str)):
            raise Exception(f"Error: 'in' requiere una lista o string a la derecha")
    
        return izquierda in derecha
    
    def visitTermino(self, ctx: RISCOParser.TerminoContext):     
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
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primario())
        return self.visit(ctx.primario(0)) ** self.visit(ctx.potencia())
    
    def visitPrimario(self, ctx: RISCOParser.PrimarioContext):  
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
