# Generated from gramaticas/RISCO.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RISCOParser import RISCOParser
else:
    from RISCOParser import RISCOParser

# This class defines a complete generic visitor for a parse tree produced by RISCOParser.

class RISCOVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RISCOParser#programa.
    def visitPrograma(self, ctx:RISCOParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RISCOParser#sentencia.
    def visitSentencia(self, ctx:RISCOParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RISCOParser#declaracion_variable.
    def visitDeclaracion_variable(self, ctx:RISCOParser.Declaracion_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RISCOParser#asignacion.
    def visitAsignacion(self, ctx:RISCOParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RISCOParser#expresion_stmt.
    def visitExpresion_stmt(self, ctx:RISCOParser.Expresion_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RISCOParser#for_stmt.
    def visitFor_stmt(self, ctx:RISCOParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RISCOParser#expresion.
    def visitExpresion(self, ctx:RISCOParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RISCOParser#comparacion.
    def visitComparacion(self, ctx:RISCOParser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RISCOParser#termino.
    def visitTermino(self, ctx:RISCOParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RISCOParser#factor.
    def visitFactor(self, ctx:RISCOParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RISCOParser#potencia.
    def visitPotencia(self, ctx:RISCOParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RISCOParser#primario.
    def visitPrimario(self, ctx:RISCOParser.PrimarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RISCOParser#lista.
    def visitLista(self, ctx:RISCOParser.ListaContext):
        return self.visitChildren(ctx)



del RISCOParser