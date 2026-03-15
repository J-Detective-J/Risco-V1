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
        4,1,39,205,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,0,
        41,9,0,1,0,1,0,5,0,45,8,0,10,0,12,0,48,9,0,5,0,50,8,0,10,0,12,0,
        53,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,82,8,3,
        1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,
        99,8,6,10,6,12,6,102,9,6,1,6,5,6,105,8,6,10,6,12,6,108,9,6,1,6,1,
        6,1,6,1,7,1,7,1,8,1,8,1,8,5,8,118,8,8,10,8,12,8,121,9,8,1,9,1,9,
        1,9,5,9,126,8,9,10,9,12,9,129,9,9,1,10,1,10,1,10,5,10,134,8,10,10,
        10,12,10,137,9,10,1,11,1,11,1,11,5,11,142,8,11,10,11,12,11,145,9,
        11,1,12,1,12,1,12,5,12,150,8,12,10,12,12,12,153,9,12,1,13,1,13,1,
        13,3,13,158,8,13,1,14,1,14,1,14,5,14,163,8,14,10,14,12,14,166,9,
        14,1,15,1,15,1,15,1,15,1,15,3,15,173,8,15,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,190,8,
        16,1,17,1,17,1,17,1,17,5,17,196,8,17,10,17,12,17,199,9,17,3,17,201,
        8,17,1,17,1,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,0,4,1,0,25,26,2,0,5,6,27,28,1,0,7,8,1,0,9,11,215,0,51,
        1,0,0,0,2,61,1,0,0,0,4,63,1,0,0,0,6,81,1,0,0,0,8,83,1,0,0,0,10,88,
        1,0,0,0,12,91,1,0,0,0,14,112,1,0,0,0,16,114,1,0,0,0,18,122,1,0,0,
        0,20,130,1,0,0,0,22,138,1,0,0,0,24,146,1,0,0,0,26,154,1,0,0,0,28,
        159,1,0,0,0,30,172,1,0,0,0,32,189,1,0,0,0,34,191,1,0,0,0,36,38,5,
        35,0,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,
        42,1,0,0,0,41,39,1,0,0,0,42,46,3,2,1,0,43,45,5,35,0,0,44,43,1,0,
        0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,50,1,0,0,0,48,46,
        1,0,0,0,49,39,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,
        52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,0,0,1,55,1,1,0,0,0,56,62,3,6,
        3,0,57,62,3,8,4,0,58,62,3,10,5,0,59,62,3,12,6,0,60,62,3,4,2,0,61,
        56,1,0,0,0,61,57,1,0,0,0,61,58,1,0,0,0,61,59,1,0,0,0,61,60,1,0,0,
        0,62,3,1,0,0,0,63,64,5,22,0,0,64,65,5,1,0,0,65,66,3,14,7,0,66,67,
        5,2,0,0,67,68,5,35,0,0,68,5,1,0,0,0,69,70,5,20,0,0,70,71,5,34,0,
        0,71,72,5,3,0,0,72,73,3,14,7,0,73,74,5,35,0,0,74,82,1,0,0,0,75,76,
        5,21,0,0,76,77,5,34,0,0,77,78,5,3,0,0,78,79,3,14,7,0,79,80,5,35,
        0,0,80,82,1,0,0,0,81,69,1,0,0,0,81,75,1,0,0,0,82,7,1,0,0,0,83,84,
        5,34,0,0,84,85,5,3,0,0,85,86,3,14,7,0,86,87,5,35,0,0,87,9,1,0,0,
        0,88,89,3,14,7,0,89,90,5,35,0,0,90,11,1,0,0,0,91,92,5,17,0,0,92,
        93,5,34,0,0,93,94,5,18,0,0,94,95,3,14,7,0,95,96,5,4,0,0,96,106,5,
        35,0,0,97,99,5,35,0,0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,
        0,100,101,1,0,0,0,101,103,1,0,0,0,102,100,1,0,0,0,103,105,3,2,1,
        0,104,100,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,
        0,107,109,1,0,0,0,108,106,1,0,0,0,109,110,5,19,0,0,110,111,5,35,
        0,0,111,13,1,0,0,0,112,113,3,16,8,0,113,15,1,0,0,0,114,119,3,18,
        9,0,115,116,5,24,0,0,116,118,3,18,9,0,117,115,1,0,0,0,118,121,1,
        0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,17,1,0,0,0,121,119,1,0,
        0,0,122,127,3,20,10,0,123,124,5,23,0,0,124,126,3,20,10,0,125,123,
        1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,19,1,
        0,0,0,129,127,1,0,0,0,130,135,3,22,11,0,131,132,7,0,0,0,132,134,
        3,22,11,0,133,131,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,
        1,0,0,0,136,21,1,0,0,0,137,135,1,0,0,0,138,143,3,24,12,0,139,140,
        7,1,0,0,140,142,3,24,12,0,141,139,1,0,0,0,142,145,1,0,0,0,143,141,
        1,0,0,0,143,144,1,0,0,0,144,23,1,0,0,0,145,143,1,0,0,0,146,151,3,
        26,13,0,147,148,7,2,0,0,148,150,3,26,13,0,149,147,1,0,0,0,150,153,
        1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,25,1,0,0,0,153,151,1,
        0,0,0,154,157,3,28,14,0,155,156,5,18,0,0,156,158,3,28,14,0,157,155,
        1,0,0,0,157,158,1,0,0,0,158,27,1,0,0,0,159,164,3,30,15,0,160,161,
        7,3,0,0,161,163,3,30,15,0,162,160,1,0,0,0,163,166,1,0,0,0,164,162,
        1,0,0,0,164,165,1,0,0,0,165,29,1,0,0,0,166,164,1,0,0,0,167,173,3,
        32,16,0,168,169,3,32,16,0,169,170,5,12,0,0,170,171,3,30,15,0,171,
        173,1,0,0,0,172,167,1,0,0,0,172,168,1,0,0,0,173,31,1,0,0,0,174,190,
        5,29,0,0,175,190,5,30,0,0,176,190,5,31,0,0,177,190,5,32,0,0,178,
        190,5,33,0,0,179,190,3,34,17,0,180,190,5,34,0,0,181,182,5,1,0,0,
        182,183,3,14,7,0,183,184,5,2,0,0,184,190,1,0,0,0,185,186,5,8,0,0,
        186,190,3,32,16,0,187,188,5,13,0,0,188,190,3,32,16,0,189,174,1,0,
        0,0,189,175,1,0,0,0,189,176,1,0,0,0,189,177,1,0,0,0,189,178,1,0,
        0,0,189,179,1,0,0,0,189,180,1,0,0,0,189,181,1,0,0,0,189,185,1,0,
        0,0,189,187,1,0,0,0,190,33,1,0,0,0,191,200,5,14,0,0,192,197,3,14,
        7,0,193,194,5,15,0,0,194,196,3,14,7,0,195,193,1,0,0,0,196,199,1,
        0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,201,1,0,0,0,199,197,1,
        0,0,0,200,192,1,0,0,0,200,201,1,0,0,0,201,202,1,0,0,0,202,203,5,
        16,0,0,203,35,1,0,0,0,18,39,46,51,61,81,100,106,119,127,135,143,
        151,157,164,172,189,197,200
    ]

class RISCOParser ( Parser ):

    grammarFileName = "RISCO.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'='", "':'", "'>'", "'<'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'!'", "'['", 
                     "','", "']'", "'for'", "'in'", "'end'", "'val'", "'var'", 
                     "'print'", "'&&'", "'||'", "'=='", "'!='", "'>='", 
                     "'<='", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "FOR", "IN", "END", "VAL", "VAR", "PRINT", 
                      "AND", "OR", "EQ", "NEQ", "GTE", "LTE", "NUMERO", 
                      "DECIMAL", "STRING", "BOOLEANO", "NULL", "IDENTIFICADOR", 
                      "NL", "WS", "COMENTARIO_LINEA", "COMENTARIO_BLOQUE", 
                      "COMENTARIO_DOC" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_print_stmt = 2
    RULE_declaracion_variable = 3
    RULE_asignacion = 4
    RULE_expresion_stmt = 5
    RULE_for_stmt = 6
    RULE_expresion = 7
    RULE_or_logico = 8
    RULE_and_logico = 9
    RULE_igualdad = 10
    RULE_relacional = 11
    RULE_suma = 12
    RULE_comparacion = 13
    RULE_termino = 14
    RULE_potencia = 15
    RULE_primario = 16
    RULE_lista = 17

    ruleNames =  [ "programa", "sentencia", "print_stmt", "declaracion_variable", 
                   "asignacion", "expresion_stmt", "for_stmt", "expresion", 
                   "or_logico", "and_logico", "igualdad", "relacional", 
                   "suma", "comparacion", "termino", "potencia", "primario", 
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
    T__14=15
    T__15=16
    FOR=17
    IN=18
    END=19
    VAL=20
    VAR=21
    PRINT=22
    AND=23
    OR=24
    EQ=25
    NEQ=26
    GTE=27
    LTE=28
    NUMERO=29
    DECIMAL=30
    STRING=31
    BOOLEANO=32
    NULL=33
    IDENTIFICADOR=34
    NL=35
    WS=36
    COMENTARIO_LINEA=37
    COMENTARIO_BLOQUE=38
    COMENTARIO_DOC=39

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
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68190101762) != 0):
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==35:
                    self.state = 36
                    self.match(RISCOParser.NL)
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 42
                self.sentencia()
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 43
                        self.match(RISCOParser.NL) 
                    self.state = 48
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
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
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.declaracion_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.expresion_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 60
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
            self.state = 63
            self.match(RISCOParser.PRINT)
            self.state = 64
            self.match(RISCOParser.T__0)
            self.state = 65
            self.expresion()
            self.state = 66
            self.match(RISCOParser.T__1)
            self.state = 67
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
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.match(RISCOParser.VAL)
                self.state = 70
                self.match(RISCOParser.IDENTIFICADOR)
                self.state = 71
                self.match(RISCOParser.T__2)
                self.state = 72
                self.expresion()
                self.state = 73
                self.match(RISCOParser.NL)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(RISCOParser.VAR)
                self.state = 76
                self.match(RISCOParser.IDENTIFICADOR)
                self.state = 77
                self.match(RISCOParser.T__2)
                self.state = 78
                self.expresion()
                self.state = 79
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
            self.state = 83
            self.match(RISCOParser.IDENTIFICADOR)
            self.state = 84
            self.match(RISCOParser.T__2)
            self.state = 85
            self.expresion()
            self.state = 86
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
            self.state = 88
            self.expresion()
            self.state = 89
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
            self.state = 91
            self.match(RISCOParser.FOR)
            self.state = 92
            self.match(RISCOParser.IDENTIFICADOR)
            self.state = 93
            self.match(RISCOParser.IN)
            self.state = 94
            self.expresion()
            self.state = 95
            self.match(RISCOParser.T__3)
            self.state = 96
            self.match(RISCOParser.NL)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68190101762) != 0):
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==35:
                    self.state = 97
                    self.match(RISCOParser.NL)
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 103
                self.sentencia()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
            self.match(RISCOParser.END)
            self.state = 110
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

        def or_logico(self):
            return self.getTypedRuleContext(RISCOParser.Or_logicoContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.or_logico()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_logicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_logico(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RISCOParser.And_logicoContext)
            else:
                return self.getTypedRuleContext(RISCOParser.And_logicoContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(RISCOParser.OR)
            else:
                return self.getToken(RISCOParser.OR, i)

        def getRuleIndex(self):
            return RISCOParser.RULE_or_logico

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr_logico" ):
                return visitor.visitOr_logico(self)
            else:
                return visitor.visitChildren(self)




    def or_logico(self):

        localctx = RISCOParser.Or_logicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_or_logico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.and_logico()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 115
                self.match(RISCOParser.OR)
                self.state = 116
                self.and_logico()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_logicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def igualdad(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RISCOParser.IgualdadContext)
            else:
                return self.getTypedRuleContext(RISCOParser.IgualdadContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(RISCOParser.AND)
            else:
                return self.getToken(RISCOParser.AND, i)

        def getRuleIndex(self):
            return RISCOParser.RULE_and_logico

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_logico" ):
                return visitor.visitAnd_logico(self)
            else:
                return visitor.visitChildren(self)




    def and_logico(self):

        localctx = RISCOParser.And_logicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_and_logico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.igualdad()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 123
                self.match(RISCOParser.AND)
                self.state = 124
                self.igualdad()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgualdadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relacional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RISCOParser.RelacionalContext)
            else:
                return self.getTypedRuleContext(RISCOParser.RelacionalContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(RISCOParser.EQ)
            else:
                return self.getToken(RISCOParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(RISCOParser.NEQ)
            else:
                return self.getToken(RISCOParser.NEQ, i)

        def getRuleIndex(self):
            return RISCOParser.RULE_igualdad

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgualdad" ):
                return visitor.visitIgualdad(self)
            else:
                return visitor.visitChildren(self)




    def igualdad(self):

        localctx = RISCOParser.IgualdadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_igualdad)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.relacional()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25 or _la==26:
                self.state = 131
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 132
                self.relacional()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def suma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RISCOParser.SumaContext)
            else:
                return self.getTypedRuleContext(RISCOParser.SumaContext,i)


        def GTE(self, i:int=None):
            if i is None:
                return self.getTokens(RISCOParser.GTE)
            else:
                return self.getToken(RISCOParser.GTE, i)

        def LTE(self, i:int=None):
            if i is None:
                return self.getTokens(RISCOParser.LTE)
            else:
                return self.getToken(RISCOParser.LTE, i)

        def getRuleIndex(self):
            return RISCOParser.RULE_relacional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelacional" ):
                return visitor.visitRelacional(self)
            else:
                return visitor.visitChildren(self)




    def relacional(self):

        localctx = RISCOParser.RelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_relacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.suma()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 402653280) != 0):
                self.state = 139
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 402653280) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 140
                self.suma()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumaContext(ParserRuleContext):
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
            return RISCOParser.RULE_suma

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)




    def suma(self):

        localctx = RISCOParser.SumaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_suma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.comparacion()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 147
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 148
                self.comparacion()
                self.state = 153
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
        self.enterRule(localctx, 26, self.RULE_comparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.termino()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 155
                self.match(RISCOParser.IN)
                self.state = 156
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

        def potencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RISCOParser.PotenciaContext)
            else:
                return self.getTypedRuleContext(RISCOParser.PotenciaContext,i)


        def getRuleIndex(self):
            return RISCOParser.RULE_termino

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)




    def termino(self):

        localctx = RISCOParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.potencia()
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0):
                self.state = 160
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 161
                self.potencia()
                self.state = 166
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
        self.enterRule(localctx, 30, self.RULE_potencia)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.primario()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.primario()
                self.state = 169
                self.match(RISCOParser.T__11)
                self.state = 170
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
        self.enterRule(localctx, 32, self.RULE_primario)
        try:
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(RISCOParser.NUMERO)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(RISCOParser.DECIMAL)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.match(RISCOParser.STRING)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
                self.match(RISCOParser.BOOLEANO)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 5)
                self.state = 178
                self.match(RISCOParser.NULL)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 6)
                self.state = 179
                self.lista()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 7)
                self.state = 180
                self.match(RISCOParser.IDENTIFICADOR)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 8)
                self.state = 181
                self.match(RISCOParser.T__0)
                self.state = 182
                self.expresion()
                self.state = 183
                self.match(RISCOParser.T__1)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 9)
                self.state = 185
                self.match(RISCOParser.T__7)
                self.state = 186
                self.primario()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 10)
                self.state = 187
                self.match(RISCOParser.T__12)
                self.state = 188
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
        self.enterRule(localctx, 34, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(RISCOParser.T__13)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 33822892290) != 0):
                self.state = 192
                self.expresion()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 193
                    self.match(RISCOParser.T__14)
                    self.state = 194
                    self.expresion()
                    self.state = 199
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 202
            self.match(RISCOParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





