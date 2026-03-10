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
        4,1,30,162,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,5,0,
        28,8,0,10,0,12,0,31,9,0,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,5,0,
        40,8,0,10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,51,8,1,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,65,8,2,1,3,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,82,8,5,10,5,
        12,5,85,9,5,1,5,5,5,88,8,5,10,5,12,5,91,9,5,1,5,1,5,1,5,1,6,1,6,
        1,6,5,6,99,8,6,10,6,12,6,102,9,6,1,7,1,7,1,7,3,7,107,8,7,1,8,1,8,
        1,8,5,8,112,8,8,10,8,12,8,115,9,8,1,9,1,9,1,9,5,9,120,8,9,10,9,12,
        9,123,9,9,1,10,1,10,1,10,1,10,1,10,3,10,130,8,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,
        147,8,11,1,12,1,12,1,12,1,12,5,12,153,8,12,10,12,12,12,156,9,12,
        3,12,158,8,12,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,
        22,24,0,2,1,0,3,4,1,0,5,7,173,0,41,1,0,0,0,2,50,1,0,0,0,4,64,1,0,
        0,0,6,66,1,0,0,0,8,71,1,0,0,0,10,74,1,0,0,0,12,95,1,0,0,0,14,103,
        1,0,0,0,16,108,1,0,0,0,18,116,1,0,0,0,20,129,1,0,0,0,22,146,1,0,
        0,0,24,148,1,0,0,0,26,28,5,26,0,0,27,26,1,0,0,0,28,31,1,0,0,0,29,
        27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,29,1,0,0,0,32,36,3,2,1,
        0,33,35,5,26,0,0,34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,
        1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,39,29,1,0,0,0,40,43,1,0,0,0,
        41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,
        0,0,1,45,1,1,0,0,0,46,51,3,4,2,0,47,51,3,6,3,0,48,51,3,8,4,0,49,
        51,3,10,5,0,50,46,1,0,0,0,50,47,1,0,0,0,50,48,1,0,0,0,50,49,1,0,
        0,0,51,3,1,0,0,0,52,53,5,18,0,0,53,54,5,25,0,0,54,55,5,1,0,0,55,
        56,3,12,6,0,56,57,5,26,0,0,57,65,1,0,0,0,58,59,5,19,0,0,59,60,5,
        25,0,0,60,61,5,1,0,0,61,62,3,12,6,0,62,63,5,26,0,0,63,65,1,0,0,0,
        64,52,1,0,0,0,64,58,1,0,0,0,65,5,1,0,0,0,66,67,5,25,0,0,67,68,5,
        1,0,0,68,69,3,12,6,0,69,70,5,26,0,0,70,7,1,0,0,0,71,72,3,12,6,0,
        72,73,5,26,0,0,73,9,1,0,0,0,74,75,5,15,0,0,75,76,5,25,0,0,76,77,
        5,16,0,0,77,78,3,12,6,0,78,79,5,2,0,0,79,89,5,26,0,0,80,82,5,26,
        0,0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,
        1,0,0,0,85,83,1,0,0,0,86,88,3,2,1,0,87,83,1,0,0,0,88,91,1,0,0,0,
        89,87,1,0,0,0,89,90,1,0,0,0,90,92,1,0,0,0,91,89,1,0,0,0,92,93,5,
        17,0,0,93,94,5,26,0,0,94,11,1,0,0,0,95,100,3,14,7,0,96,97,7,0,0,
        0,97,99,3,14,7,0,98,96,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,
        101,1,0,0,0,101,13,1,0,0,0,102,100,1,0,0,0,103,106,3,16,8,0,104,
        105,5,16,0,0,105,107,3,16,8,0,106,104,1,0,0,0,106,107,1,0,0,0,107,
        15,1,0,0,0,108,113,3,18,9,0,109,110,7,1,0,0,110,112,3,18,9,0,111,
        109,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,
        17,1,0,0,0,115,113,1,0,0,0,116,121,3,20,10,0,117,118,5,8,0,0,118,
        120,3,20,10,0,119,117,1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,
        122,1,0,0,0,122,19,1,0,0,0,123,121,1,0,0,0,124,130,3,22,11,0,125,
        126,3,22,11,0,126,127,5,8,0,0,127,128,3,20,10,0,128,130,1,0,0,0,
        129,124,1,0,0,0,129,125,1,0,0,0,130,21,1,0,0,0,131,147,5,20,0,0,
        132,147,5,21,0,0,133,147,5,22,0,0,134,147,5,23,0,0,135,147,5,24,
        0,0,136,147,3,24,12,0,137,147,5,25,0,0,138,139,5,9,0,0,139,140,3,
        12,6,0,140,141,5,10,0,0,141,147,1,0,0,0,142,143,5,4,0,0,143,147,
        3,22,11,0,144,145,5,11,0,0,145,147,3,22,11,0,146,131,1,0,0,0,146,
        132,1,0,0,0,146,133,1,0,0,0,146,134,1,0,0,0,146,135,1,0,0,0,146,
        136,1,0,0,0,146,137,1,0,0,0,146,138,1,0,0,0,146,142,1,0,0,0,146,
        144,1,0,0,0,147,23,1,0,0,0,148,157,5,12,0,0,149,154,3,12,6,0,150,
        151,5,13,0,0,151,153,3,12,6,0,152,150,1,0,0,0,153,156,1,0,0,0,154,
        152,1,0,0,0,154,155,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,157,
        149,1,0,0,0,157,158,1,0,0,0,158,159,1,0,0,0,159,160,5,14,0,0,160,
        25,1,0,0,0,15,29,36,41,50,64,83,89,100,106,113,121,129,146,154,157
    ]

class RISCOParser ( Parser ):

    grammarFileName = "RISCO.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "':'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'^'", "'('", "')'", "'!'", "'['", "','", "']'", 
                     "'for'", "'in'", "'end'", "'val'", "'var'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "FOR", "IN", 
                      "END", "VAL", "VAR", "NUMERO", "DECIMAL", "STRING", 
                      "BOOLEANO", "NULL", "IDENTIFICADOR", "NL", "WS", "COMENTARIO_LINEA", 
                      "COMENTARIO_BLOQUE", "COMENTARIO_DOC" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_declaracion_variable = 2
    RULE_asignacion = 3
    RULE_expresion_stmt = 4
    RULE_for_stmt = 5
    RULE_expresion = 6
    RULE_comparacion = 7
    RULE_termino = 8
    RULE_factor = 9
    RULE_potencia = 10
    RULE_primario = 11
    RULE_lista = 12

    ruleNames =  [ "programa", "sentencia", "declaracion_variable", "asignacion", 
                   "expresion_stmt", "for_stmt", "expresion", "comparacion", 
                   "termino", "factor", "potencia", "primario", "lista" ]

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
    NUMERO=20
    DECIMAL=21
    STRING=22
    BOOLEANO=23
    NULL=24
    IDENTIFICADOR=25
    NL=26
    WS=27
    COMENTARIO_LINEA=28
    COMENTARIO_BLOQUE=29
    COMENTARIO_DOC=30

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
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 133995024) != 0):
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26:
                    self.state = 26
                    self.match(RISCOParser.NL)
                    self.state = 31
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 32
                self.sentencia()
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 33
                        self.match(RISCOParser.NL) 
                    self.state = 38
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
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
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.declaracion_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.expresion_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.for_stmt()
                pass


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
        self.enterRule(localctx, 4, self.RULE_declaracion_variable)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(RISCOParser.VAL)
                self.state = 53
                self.match(RISCOParser.IDENTIFICADOR)
                self.state = 54
                self.match(RISCOParser.T__0)
                self.state = 55
                self.expresion()
                self.state = 56
                self.match(RISCOParser.NL)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(RISCOParser.VAR)
                self.state = 59
                self.match(RISCOParser.IDENTIFICADOR)
                self.state = 60
                self.match(RISCOParser.T__0)
                self.state = 61
                self.expresion()
                self.state = 62
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
        self.enterRule(localctx, 6, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(RISCOParser.IDENTIFICADOR)
            self.state = 67
            self.match(RISCOParser.T__0)
            self.state = 68
            self.expresion()
            self.state = 69
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
        self.enterRule(localctx, 8, self.RULE_expresion_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.expresion()
            self.state = 72
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
        self.enterRule(localctx, 10, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(RISCOParser.FOR)
            self.state = 75
            self.match(RISCOParser.IDENTIFICADOR)
            self.state = 76
            self.match(RISCOParser.IN)
            self.state = 77
            self.expresion()
            self.state = 78
            self.match(RISCOParser.T__1)
            self.state = 79
            self.match(RISCOParser.NL)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 133995024) != 0):
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26:
                    self.state = 80
                    self.match(RISCOParser.NL)
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 86
                self.sentencia()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(RISCOParser.END)
            self.state = 93
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
        self.enterRule(localctx, 12, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.comparacion()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 96
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 97
                self.comparacion()
                self.state = 102
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
        self.enterRule(localctx, 14, self.RULE_comparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.termino()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 104
                self.match(RISCOParser.IN)
                self.state = 105
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
        self.enterRule(localctx, 16, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.factor()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0):
                self.state = 109
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 110
                self.factor()
                self.state = 115
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
        self.enterRule(localctx, 18, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.potencia()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 117
                self.match(RISCOParser.T__7)
                self.state = 118
                self.potencia()
                self.state = 123
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
        self.enterRule(localctx, 20, self.RULE_potencia)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.primario()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.primario()
                self.state = 126
                self.match(RISCOParser.T__7)
                self.state = 127
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
        self.enterRule(localctx, 22, self.RULE_primario)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(RISCOParser.NUMERO)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(RISCOParser.DECIMAL)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.match(RISCOParser.STRING)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 134
                self.match(RISCOParser.BOOLEANO)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 135
                self.match(RISCOParser.NULL)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 136
                self.lista()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 7)
                self.state = 137
                self.match(RISCOParser.IDENTIFICADOR)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 8)
                self.state = 138
                self.match(RISCOParser.T__8)
                self.state = 139
                self.expresion()
                self.state = 140
                self.match(RISCOParser.T__9)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 9)
                self.state = 142
                self.match(RISCOParser.T__3)
                self.state = 143
                self.primario()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 10)
                self.state = 144
                self.match(RISCOParser.T__10)
                self.state = 145
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
        self.enterRule(localctx, 24, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(RISCOParser.T__11)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66066960) != 0):
                self.state = 149
                self.expresion()
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 150
                    self.match(RISCOParser.T__12)
                    self.state = 151
                    self.expresion()
                    self.state = 156
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 159
            self.match(RISCOParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





