# Generated from gramaticas/RISCO.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,171,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,1,0,5,0,37,8,0,10,0,12,0,40,
        9,0,5,0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,
        54,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,3,3,74,8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,5,6,91,8,6,10,6,12,6,94,9,6,1,6,5,6,97,8,6,10,
        6,12,6,100,9,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,108,8,7,10,7,12,7,111,
        9,7,1,8,1,8,1,8,3,8,116,8,8,1,9,1,9,1,9,5,9,121,8,9,10,9,12,9,124,
        9,9,1,10,1,10,1,10,5,10,129,8,10,10,10,12,10,132,9,10,1,11,1,11,
        1,11,1,11,1,11,3,11,139,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,156,8,12,1,13,1,13,
        1,13,1,13,5,13,162,8,13,10,13,12,13,165,9,13,3,13,167,8,13,1,13,
        1,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,2,1,0,5,
        6,1,0,7,9,182,0,43,1,0,0,0,2,53,1,0,0,0,4,55,1,0,0,0,6,73,1,0,0,
        0,8,75,1,0,0,0,10,80,1,0,0,0,12,83,1,0,0,0,14,104,1,0,0,0,16,112,
        1,0,0,0,18,117,1,0,0,0,20,125,1,0,0,0,22,138,1,0,0,0,24,155,1,0,
        0,0,26,157,1,0,0,0,28,30,5,27,0,0,29,28,1,0,0,0,30,33,1,0,0,0,31,
        29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,31,1,0,0,0,34,38,3,2,1,
        0,35,37,5,27,0,0,36,35,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,
        1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,41,31,1,0,0,0,42,45,1,0,0,0,
        43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,46,47,5,
        0,0,1,47,1,1,0,0,0,48,54,3,6,3,0,49,54,3,8,4,0,50,54,3,10,5,0,51,
        54,3,12,6,0,52,54,3,4,2,0,53,48,1,0,0,0,53,49,1,0,0,0,53,50,1,0,
        0,0,53,51,1,0,0,0,53,52,1,0,0,0,54,3,1,0,0,0,55,56,5,20,0,0,56,57,
        5,1,0,0,57,58,3,14,7,0,58,59,5,2,0,0,59,60,5,27,0,0,60,5,1,0,0,0,
        61,62,5,18,0,0,62,63,5,26,0,0,63,64,5,3,0,0,64,65,3,14,7,0,65,66,
        5,27,0,0,66,74,1,0,0,0,67,68,5,19,0,0,68,69,5,26,0,0,69,70,5,3,0,
        0,70,71,3,14,7,0,71,72,5,27,0,0,72,74,1,0,0,0,73,61,1,0,0,0,73,67,
        1,0,0,0,74,7,1,0,0,0,75,76,5,26,0,0,76,77,5,3,0,0,77,78,3,14,7,0,
        78,79,5,27,0,0,79,9,1,0,0,0,80,81,3,14,7,0,81,82,5,27,0,0,82,11,
        1,0,0,0,83,84,5,15,0,0,84,85,5,26,0,0,85,86,5,16,0,0,86,87,3,14,
        7,0,87,88,5,4,0,0,88,98,5,27,0,0,89,91,5,27,0,0,90,89,1,0,0,0,91,
        94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,92,1,0,0,
        0,95,97,3,2,1,0,96,92,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,
        1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,0,101,102,5,17,0,0,102,103,5,
        27,0,0,103,13,1,0,0,0,104,109,3,16,8,0,105,106,7,0,0,0,106,108,3,
        16,8,0,107,105,1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,
        0,0,0,110,15,1,0,0,0,111,109,1,0,0,0,112,115,3,18,9,0,113,114,5,
        16,0,0,114,116,3,18,9,0,115,113,1,0,0,0,115,116,1,0,0,0,116,17,1,
        0,0,0,117,122,3,20,10,0,118,119,7,1,0,0,119,121,3,20,10,0,120,118,
        1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,19,1,
        0,0,0,124,122,1,0,0,0,125,130,3,22,11,0,126,127,5,10,0,0,127,129,
        3,22,11,0,128,126,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,
        1,0,0,0,131,21,1,0,0,0,132,130,1,0,0,0,133,139,3,24,12,0,134,135,
        3,24,12,0,135,136,5,10,0,0,136,137,3,22,11,0,137,139,1,0,0,0,138,
        133,1,0,0,0,138,134,1,0,0,0,139,23,1,0,0,0,140,156,5,21,0,0,141,
        156,5,22,0,0,142,156,5,23,0,0,143,156,5,24,0,0,144,156,5,25,0,0,
        145,156,3,26,13,0,146,156,5,26,0,0,147,148,5,1,0,0,148,149,3,14,
        7,0,149,150,5,2,0,0,150,156,1,0,0,0,151,152,5,6,0,0,152,156,3,24,
        12,0,153,154,5,11,0,0,154,156,3,24,12,0,155,140,1,0,0,0,155,141,
        1,0,0,0,155,142,1,0,0,0,155,143,1,0,0,0,155,144,1,0,0,0,155,145,
        1,0,0,0,155,146,1,0,0,0,155,147,1,0,0,0,155,151,1,0,0,0,155,153,
        1,0,0,0,156,25,1,0,0,0,157,166,5,12,0,0,158,163,3,14,7,0,159,160,
        5,13,0,0,160,162,3,14,7,0,161,159,1,0,0,0,162,165,1,0,0,0,163,161,
        1,0,0,0,163,164,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,166,158,
        1,0,0,0,166,167,1,0,0,0,167,168,1,0,0,0,168,169,5,14,0,0,169,27,
        1,0,0,0,15,31,38,43,53,73,92,98,109,115,122,130,138,155,163,166
    ]

class RISCOParser ( Parser ):

    grammarFileName = "RISCO.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'='", "':'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'^'", "'!'", "'['", "','", "']'", 
                     "'for'", "'in'", "'end'", "'val'", "'var'", "'print'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "FOR", "IN", 
                      "END", "VAL", "VAR", "PRINT", "NUMERO", "DECIMAL", 
                      "STRING", "BOOLEANO", "NULL", "IDENTIFICADOR", "NL", 
                      "WS", "COMENTARIO_LINEA", "COMENTARIO_BLOQUE", "COMENTARIO_DOC" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_print_stmt = 2
    RULE_declaracion_variable = 3
    RULE_asignacion = 4
    RULE_expresion_stmt = 5
    RULE_for_stmt = 6
    RULE_expresion = 7
    RULE_comparacion = 8
    RULE_termino = 9
    RULE_factor = 10
    RULE_potencia = 11
    RULE_primario = 12
    RULE_lista = 13

    ruleNames =  [ "programa", "sentencia", "print_stmt", "declaracion_variable", 
                   "asignacion", "expresion_stmt", "for_stmt", "expresion", 
                   "comparacion", "termino", "factor", "potencia", "primario", 
                   "lista" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    FOR=15
    IN=16
    END=17
    VAL=18
    VAR=19
    PRINT=20
    NUMERO=21
    DECIMAL=22
    STRING=23
    BOOLEANO=24
    NULL=25
    IDENTIFICADOR=26
    NL=27
    WS=28
    COMENTARIO_LINEA=29
    COMENTARIO_BLOQUE=30
    COMENTARIO_DOC=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



        # Memoria para variables
        memoria = {}



    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(RISCOParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RISCOParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(RISCOParser.SentenciaContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RISCOParser.NL)
            else:
                return self.getToken(RISCOParser.NL, i)

        def getRuleIndex(self):
            return RISCOParser.RULE_programa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = RISCOParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268212290) != 0):
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27:
                    self.state = 28
                    self.match(RISCOParser.NL)
                    self.state = 33
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 34
                self.sentencia()
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 35
                        self.match(RISCOParser.NL) 
                    self.state = 40
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(RISCOParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion_variable(self):
            return self.getTypedRuleContext(RISCOParser.Declaracion_variableContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(RISCOParser.AsignacionContext,0)


        def expresion_stmt(self):
            return self.getTypedRuleContext(RISCOParser.Expresion_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(RISCOParser.For_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(RISCOParser.Print_stmtContext,0)


        def getRuleIndex(self):
            return RISCOParser.RULE_sentencia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = RISCOParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.declaracion_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.expresion_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.print_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(RISCOParser.PRINT, 0)

        def expresion(self):
            return self.getTypedRuleContext(RISCOParser.ExpresionContext,0)


        def NL(self):
            return self.getToken(RISCOParser.NL, 0)

        def getRuleIndex(self):
            return RISCOParser.RULE_print_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_stmt" ):
                return visitor.visitPrint_stmt(self)
            else:
                return visitor.visitChildren(self)




    def print_stmt(self):

        localctx = RISCOParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(RISCOParser.PRINT)
            self.state = 56
            self.match(RISCOParser.T__0)
            self.state = 57
            self.expresion()
            self.state = 58
            self.match(RISCOParser.T__1)
            self.state = 59
            self.match(RISCOParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracion_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(RISCOParser.VAL, 0)

        def IDENTIFICADOR(self):
            return self.getToken(RISCOParser.IDENTIFICADOR, 0)

        def expresion(self):
            return self.getTypedRuleContext(RISCOParser.ExpresionContext,0)


        def NL(self):
            return self.getToken(RISCOParser.NL, 0)

        def VAR(self):
            return self.getToken(RISCOParser.VAR, 0)

        def getRuleIndex(self):
            return RISCOParser.RULE_declaracion_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion_variable" ):
                return visitor.visitDeclaracion_variable(self)
            else:
                return visitor.visitChildren(self)




    def declaracion_variable(self):

        localctx = RISCOParser.Declaracion_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracion_variable)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(RISCOParser.VAL)
                self.state = 62
                self.match(RISCOParser.IDENTIFICADOR)
                self.state = 63
                self.match(RISCOParser.T__2)
                self.state = 64
                self.expresion()
                self.state = 65
                self.match(RISCOParser.NL)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(RISCOParser.VAR)
                self.state = 68
                self.match(RISCOParser.IDENTIFICADOR)
                self.state = 69
                self.match(RISCOParser.T__2)
                self.state = 70
                self.expresion()
                self.state = 71
                self.match(RISCOParser.NL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(RISCOParser.IDENTIFICADOR, 0)

        def expresion(self):
            return self.getTypedRuleContext(RISCOParser.ExpresionContext,0)


        def NL(self):
            return self.getToken(RISCOParser.NL, 0)

        def getRuleIndex(self):
            return RISCOParser.RULE_asignacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = RISCOParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(RISCOParser.IDENTIFICADOR)
            self.state = 76
            self.match(RISCOParser.T__2)
            self.state = 77
            self.expresion()
            self.state = 78
            self.match(RISCOParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expresion_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(RISCOParser.ExpresionContext,0)


        def NL(self):
            return self.getToken(RISCOParser.NL, 0)

        def getRuleIndex(self):
            return RISCOParser.RULE_expresion_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion_stmt" ):
                return visitor.visitExpresion_stmt(self)
            else:
                return visitor.visitChildren(self)




    def expresion_stmt(self):

        localctx = RISCOParser.Expresion_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expresion_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.expresion()
            self.state = 81
            self.match(RISCOParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(RISCOParser.FOR, 0)

        def IDENTIFICADOR(self):
            return self.getToken(RISCOParser.IDENTIFICADOR, 0)

        def IN(self):
            return self.getToken(RISCOParser.IN, 0)

        def expresion(self):
            return self.getTypedRuleContext(RISCOParser.ExpresionContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RISCOParser.NL)
            else:
                return self.getToken(RISCOParser.NL, i)

        def END(self):
            return self.getToken(RISCOParser.END, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RISCOParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(RISCOParser.SentenciaContext,i)


        def getRuleIndex(self):
            return RISCOParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = RISCOParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(RISCOParser.FOR)
            self.state = 84
            self.match(RISCOParser.IDENTIFICADOR)
            self.state = 85
            self.match(RISCOParser.IN)
            self.state = 86
            self.expresion()
            self.state = 87
            self.match(RISCOParser.T__3)
            self.state = 88
            self.match(RISCOParser.NL)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268212290) != 0):
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27:
                    self.state = 89
                    self.match(RISCOParser.NL)
                    self.state = 94
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 95
                self.sentencia()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self.match(RISCOParser.END)
            self.state = 102
            self.match(RISCOParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RISCOParser.ComparacionContext)
            else:
                return self.getTypedRuleContext(RISCOParser.ComparacionContext,i)


        def getRuleIndex(self):
            return RISCOParser.RULE_expresion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)




    def expresion(self):

        localctx = RISCOParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.comparacion()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 105
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 106
                self.comparacion()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RISCOParser.TerminoContext)
            else:
                return self.getTypedRuleContext(RISCOParser.TerminoContext,i)


        def IN(self):
            return self.getToken(RISCOParser.IN, 0)

        def getRuleIndex(self):
            return RISCOParser.RULE_comparacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacion" ):
                return visitor.visitComparacion(self)
            else:
                return visitor.visitChildren(self)




    def comparacion(self):

        localctx = RISCOParser.ComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.termino()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 113
                self.match(RISCOParser.IN)
                self.state = 114
                self.termino()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RISCOParser.FactorContext)
            else:
                return self.getTypedRuleContext(RISCOParser.FactorContext,i)


        def getRuleIndex(self):
            return RISCOParser.RULE_termino

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)




    def termino(self):

        localctx = RISCOParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.factor()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0):
                self.state = 118
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 119
                self.factor()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def potencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RISCOParser.PotenciaContext)
            else:
                return self.getTypedRuleContext(RISCOParser.PotenciaContext,i)


        def getRuleIndex(self):
            return RISCOParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = RISCOParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.potencia()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 126
                self.match(RISCOParser.T__9)
                self.state = 127
                self.potencia()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PotenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primario(self):
            return self.getTypedRuleContext(RISCOParser.PrimarioContext,0)


        def potencia(self):
            return self.getTypedRuleContext(RISCOParser.PotenciaContext,0)


        def getRuleIndex(self):
            return RISCOParser.RULE_potencia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPotencia" ):
                return visitor.visitPotencia(self)
            else:
                return visitor.visitChildren(self)




    def potencia(self):

        localctx = RISCOParser.PotenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_potencia)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.primario()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.primario()
                self.state = 135
                self.match(RISCOParser.T__9)
                self.state = 136
                self.potencia()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(RISCOParser.NUMERO, 0)

        def DECIMAL(self):
            return self.getToken(RISCOParser.DECIMAL, 0)

        def STRING(self):
            return self.getToken(RISCOParser.STRING, 0)

        def BOOLEANO(self):
            return self.getToken(RISCOParser.BOOLEANO, 0)

        def NULL(self):
            return self.getToken(RISCOParser.NULL, 0)

        def lista(self):
            return self.getTypedRuleContext(RISCOParser.ListaContext,0)


        def IDENTIFICADOR(self):
            return self.getToken(RISCOParser.IDENTIFICADOR, 0)

        def expresion(self):
            return self.getTypedRuleContext(RISCOParser.ExpresionContext,0)


        def primario(self):
            return self.getTypedRuleContext(RISCOParser.PrimarioContext,0)


        def getRuleIndex(self):
            return RISCOParser.RULE_primario

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimario" ):
                return visitor.visitPrimario(self)
            else:
                return visitor.visitChildren(self)




    def primario(self):

        localctx = RISCOParser.PrimarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_primario)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(RISCOParser.NUMERO)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(RISCOParser.DECIMAL)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.match(RISCOParser.STRING)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
                self.match(RISCOParser.BOOLEANO)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 5)
                self.state = 144
                self.match(RISCOParser.NULL)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 145
                self.lista()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 7)
                self.state = 146
                self.match(RISCOParser.IDENTIFICADOR)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 8)
                self.state = 147
                self.match(RISCOParser.T__0)
                self.state = 148
                self.expresion()
                self.state = 149
                self.match(RISCOParser.T__1)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 9)
                self.state = 151
                self.match(RISCOParser.T__5)
                self.state = 152
                self.primario()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 10)
                self.state = 153
                self.match(RISCOParser.T__10)
                self.state = 154
                self.primario()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RISCOParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(RISCOParser.ExpresionContext,i)


        def getRuleIndex(self):
            return RISCOParser.RULE_lista

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista" ):
                return visitor.visitLista(self)
            else:
                return visitor.visitChildren(self)




    def lista(self):

        localctx = RISCOParser.ListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(RISCOParser.T__11)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 132126786) != 0):
                self.state = 158
                self.expresion()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 159
                    self.match(RISCOParser.T__12)
                    self.state = 160
                    self.expresion()
                    self.state = 165
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 168
            self.match(RISCOParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





