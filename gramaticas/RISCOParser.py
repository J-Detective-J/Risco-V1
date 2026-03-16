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
        4,1,43,287,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,5,0,49,8,0,10,0,12,0,52,9,0,
        5,0,54,8,0,10,0,12,0,57,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,68,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,3,3,88,8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,5,6,105,8,6,10,6,12,6,108,9,6,1,6,5,6,111,
        8,6,10,6,12,6,114,9,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,5,7,124,8,
        7,10,7,12,7,127,9,7,1,7,5,7,130,8,7,10,7,12,7,133,9,7,1,7,1,7,1,
        7,1,7,1,7,5,7,140,8,7,10,7,12,7,143,9,7,1,7,5,7,146,8,7,10,7,12,
        7,149,9,7,5,7,151,8,7,10,7,12,7,154,9,7,1,7,1,7,1,7,1,7,5,7,160,
        8,7,10,7,12,7,163,9,7,1,7,5,7,166,8,7,10,7,12,7,169,9,7,3,7,171,
        8,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,5,8,181,8,8,10,8,12,8,184,9,
        8,1,8,5,8,187,8,8,10,8,12,8,190,9,8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,
        1,10,5,10,200,8,10,10,10,12,10,203,9,10,1,11,1,11,1,11,5,11,208,
        8,11,10,11,12,11,211,9,11,1,12,1,12,1,12,5,12,216,8,12,10,12,12,
        12,219,9,12,1,13,1,13,1,13,5,13,224,8,13,10,13,12,13,227,9,13,1,
        14,1,14,1,14,5,14,232,8,14,10,14,12,14,235,9,14,1,15,1,15,1,15,3,
        15,240,8,15,1,16,1,16,1,16,5,16,245,8,16,10,16,12,16,248,9,16,1,
        17,1,17,1,17,1,17,1,17,3,17,255,8,17,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,272,8,18,1,
        19,1,19,1,19,1,19,5,19,278,8,19,10,19,12,19,281,9,19,3,19,283,8,
        19,1,19,1,19,1,19,0,0,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,0,4,1,0,29,30,2,0,5,6,31,32,1,0,7,8,1,0,9,11,307,
        0,55,1,0,0,0,2,67,1,0,0,0,4,69,1,0,0,0,6,87,1,0,0,0,8,89,1,0,0,0,
        10,94,1,0,0,0,12,97,1,0,0,0,14,118,1,0,0,0,16,175,1,0,0,0,18,194,
        1,0,0,0,20,196,1,0,0,0,22,204,1,0,0,0,24,212,1,0,0,0,26,220,1,0,
        0,0,28,228,1,0,0,0,30,236,1,0,0,0,32,241,1,0,0,0,34,254,1,0,0,0,
        36,271,1,0,0,0,38,273,1,0,0,0,40,42,5,39,0,0,41,40,1,0,0,0,42,45,
        1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,
        46,50,3,2,1,0,47,49,5,39,0,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,
        0,0,0,50,51,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,53,43,1,0,0,0,54,
        57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,55,1,0,0,
        0,58,59,5,0,0,1,59,1,1,0,0,0,60,68,3,6,3,0,61,68,3,8,4,0,62,68,3,
        10,5,0,63,68,3,12,6,0,64,68,3,4,2,0,65,68,3,14,7,0,66,68,3,16,8,
        0,67,60,1,0,0,0,67,61,1,0,0,0,67,62,1,0,0,0,67,63,1,0,0,0,67,64,
        1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,3,1,0,0,0,69,70,5,22,0,0,
        70,71,5,1,0,0,71,72,3,18,9,0,72,73,5,2,0,0,73,74,5,39,0,0,74,5,1,
        0,0,0,75,76,5,20,0,0,76,77,5,38,0,0,77,78,5,3,0,0,78,79,3,18,9,0,
        79,80,5,39,0,0,80,88,1,0,0,0,81,82,5,21,0,0,82,83,5,38,0,0,83,84,
        5,3,0,0,84,85,3,18,9,0,85,86,5,39,0,0,86,88,1,0,0,0,87,75,1,0,0,
        0,87,81,1,0,0,0,88,7,1,0,0,0,89,90,5,38,0,0,90,91,5,3,0,0,91,92,
        3,18,9,0,92,93,5,39,0,0,93,9,1,0,0,0,94,95,3,18,9,0,95,96,5,39,0,
        0,96,11,1,0,0,0,97,98,5,17,0,0,98,99,5,38,0,0,99,100,5,18,0,0,100,
        101,3,18,9,0,101,102,5,4,0,0,102,112,5,39,0,0,103,105,5,39,0,0,104,
        103,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,
        109,1,0,0,0,108,106,1,0,0,0,109,111,3,2,1,0,110,106,1,0,0,0,111,
        114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,
        112,1,0,0,0,115,116,5,19,0,0,116,117,5,39,0,0,117,13,1,0,0,0,118,
        119,5,23,0,0,119,120,3,18,9,0,120,121,5,4,0,0,121,131,5,39,0,0,122,
        124,5,39,0,0,123,122,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,
        126,1,0,0,0,126,128,1,0,0,0,127,125,1,0,0,0,128,130,3,2,1,0,129,
        125,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,
        152,1,0,0,0,133,131,1,0,0,0,134,135,5,24,0,0,135,136,3,18,9,0,136,
        137,5,4,0,0,137,147,5,39,0,0,138,140,5,39,0,0,139,138,1,0,0,0,140,
        143,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,144,1,0,0,0,143,
        141,1,0,0,0,144,146,3,2,1,0,145,141,1,0,0,0,146,149,1,0,0,0,147,
        145,1,0,0,0,147,148,1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,150,
        134,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,
        170,1,0,0,0,154,152,1,0,0,0,155,156,5,25,0,0,156,157,5,4,0,0,157,
        167,5,39,0,0,158,160,5,39,0,0,159,158,1,0,0,0,160,163,1,0,0,0,161,
        159,1,0,0,0,161,162,1,0,0,0,162,164,1,0,0,0,163,161,1,0,0,0,164,
        166,3,2,1,0,165,161,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,
        168,1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,170,155,1,0,0,0,170,
        171,1,0,0,0,171,172,1,0,0,0,172,173,5,19,0,0,173,174,5,39,0,0,174,
        15,1,0,0,0,175,176,5,26,0,0,176,177,3,18,9,0,177,178,5,4,0,0,178,
        188,5,39,0,0,179,181,5,39,0,0,180,179,1,0,0,0,181,184,1,0,0,0,182,
        180,1,0,0,0,182,183,1,0,0,0,183,185,1,0,0,0,184,182,1,0,0,0,185,
        187,3,2,1,0,186,182,1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,0,188,
        189,1,0,0,0,189,191,1,0,0,0,190,188,1,0,0,0,191,192,5,19,0,0,192,
        193,5,39,0,0,193,17,1,0,0,0,194,195,3,20,10,0,195,19,1,0,0,0,196,
        201,3,22,11,0,197,198,5,28,0,0,198,200,3,22,11,0,199,197,1,0,0,0,
        200,203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,21,1,0,0,0,203,
        201,1,0,0,0,204,209,3,24,12,0,205,206,5,27,0,0,206,208,3,24,12,0,
        207,205,1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,
        210,23,1,0,0,0,211,209,1,0,0,0,212,217,3,26,13,0,213,214,7,0,0,0,
        214,216,3,26,13,0,215,213,1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,
        0,217,218,1,0,0,0,218,25,1,0,0,0,219,217,1,0,0,0,220,225,3,28,14,
        0,221,222,7,1,0,0,222,224,3,28,14,0,223,221,1,0,0,0,224,227,1,0,
        0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,27,1,0,0,0,227,225,1,0,0,
        0,228,233,3,30,15,0,229,230,7,2,0,0,230,232,3,30,15,0,231,229,1,
        0,0,0,232,235,1,0,0,0,233,231,1,0,0,0,233,234,1,0,0,0,234,29,1,0,
        0,0,235,233,1,0,0,0,236,239,3,32,16,0,237,238,5,18,0,0,238,240,3,
        32,16,0,239,237,1,0,0,0,239,240,1,0,0,0,240,31,1,0,0,0,241,246,3,
        34,17,0,242,243,7,3,0,0,243,245,3,34,17,0,244,242,1,0,0,0,245,248,
        1,0,0,0,246,244,1,0,0,0,246,247,1,0,0,0,247,33,1,0,0,0,248,246,1,
        0,0,0,249,255,3,36,18,0,250,251,3,36,18,0,251,252,5,12,0,0,252,253,
        3,34,17,0,253,255,1,0,0,0,254,249,1,0,0,0,254,250,1,0,0,0,255,35,
        1,0,0,0,256,272,5,33,0,0,257,272,5,34,0,0,258,272,5,35,0,0,259,272,
        5,36,0,0,260,272,5,37,0,0,261,272,3,38,19,0,262,272,5,38,0,0,263,
        264,5,1,0,0,264,265,3,18,9,0,265,266,5,2,0,0,266,272,1,0,0,0,267,
        268,5,8,0,0,268,272,3,36,18,0,269,270,5,13,0,0,270,272,3,36,18,0,
        271,256,1,0,0,0,271,257,1,0,0,0,271,258,1,0,0,0,271,259,1,0,0,0,
        271,260,1,0,0,0,271,261,1,0,0,0,271,262,1,0,0,0,271,263,1,0,0,0,
        271,267,1,0,0,0,271,269,1,0,0,0,272,37,1,0,0,0,273,282,5,14,0,0,
        274,279,3,18,9,0,275,276,5,15,0,0,276,278,3,18,9,0,277,275,1,0,0,
        0,278,281,1,0,0,0,279,277,1,0,0,0,279,280,1,0,0,0,280,283,1,0,0,
        0,281,279,1,0,0,0,282,274,1,0,0,0,282,283,1,0,0,0,283,284,1,0,0,
        0,284,285,5,16,0,0,285,39,1,0,0,0,28,43,50,55,67,87,106,112,125,
        131,141,147,152,161,167,170,182,188,201,209,217,225,233,239,246,
        254,271,279,282
    ]

class RISCOParser ( Parser ):

    grammarFileName = "RISCO.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'='", "':'", "'>'", "'<'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'!'", "'['", 
                     "','", "']'", "'for'", "'in'", "'end'", "'val'", "'var'", 
                     "'print'", "'if'", "'elif'", "'else'", "'while'", "'&&'", 
                     "'||'", "'=='", "'!='", "'>='", "'<='", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "FOR", "IN", "END", "VAL", "VAR", "PRINT", 
                      "IF", "ELIF", "ELSE", "WHILE", "AND", "OR", "EQ", 
                      "NEQ", "GTE", "LTE", "NUMERO", "DECIMAL", "STRING", 
                      "BOOLEANO", "NULL", "IDENTIFICADOR", "NL", "WS", "COMENTARIO_LINEA", 
                      "COMENTARIO_BLOQUE", "COMENTARIO_DOC" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_print_stmt = 2
    RULE_declaracion_variable = 3
    RULE_asignacion = 4
    RULE_expresion_stmt = 5
    RULE_for_stmt = 6
    RULE_if_stmt = 7
    RULE_while_stmt = 8
    RULE_expresion = 9
    RULE_or_logico = 10
    RULE_and_logico = 11
    RULE_igualdad = 12
    RULE_relacional = 13
    RULE_suma = 14
    RULE_comparacion = 15
    RULE_termino = 16
    RULE_potencia = 17
    RULE_primario = 18
    RULE_lista = 19

    ruleNames =  [ "programa", "sentencia", "print_stmt", "declaracion_variable", 
                   "asignacion", "expresion_stmt", "for_stmt", "if_stmt", 
                   "while_stmt", "expresion", "or_logico", "and_logico", 
                   "igualdad", "relacional", "suma", "comparacion", "termino", 
                   "potencia", "primario", "lista" ]

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
    IF=23
    ELIF=24
    ELSE=25
    WHILE=26
    AND=27
    OR=28
    EQ=29
    NEQ=30
    GTE=31
    LTE=32
    NUMERO=33
    DECIMAL=34
    STRING=35
    BOOLEANO=36
    NULL=37
    IDENTIFICADOR=38
    NL=39
    WS=40
    COMENTARIO_LINEA=41
    COMENTARIO_BLOQUE=42
    COMENTARIO_DOC=43

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
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1091004686594) != 0):
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==39:
                    self.state = 40
                    self.match(RISCOParser.NL)
                    self.state = 45
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 46
                self.sentencia()
                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 47
                        self.match(RISCOParser.NL) 
                    self.state = 52
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
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


        def if_stmt(self):
            return self.getTypedRuleContext(RISCOParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(RISCOParser.While_stmtContext,0)


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
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.declaracion_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.expresion_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.print_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 65
                self.if_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 66
                self.while_stmt()
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
            self.state = 69
            self.match(RISCOParser.PRINT)
            self.state = 70
            self.match(RISCOParser.T__0)
            self.state = 71
            self.expresion()
            self.state = 72
            self.match(RISCOParser.T__1)
            self.state = 73
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
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(RISCOParser.VAL)
                self.state = 76
                self.match(RISCOParser.IDENTIFICADOR)
                self.state = 77
                self.match(RISCOParser.T__2)
                self.state = 78
                self.expresion()
                self.state = 79
                self.match(RISCOParser.NL)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.match(RISCOParser.VAR)
                self.state = 82
                self.match(RISCOParser.IDENTIFICADOR)
                self.state = 83
                self.match(RISCOParser.T__2)
                self.state = 84
                self.expresion()
                self.state = 85
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
            self.state = 89
            self.match(RISCOParser.IDENTIFICADOR)
            self.state = 90
            self.match(RISCOParser.T__2)
            self.state = 91
            self.expresion()
            self.state = 92
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
            self.state = 94
            self.expresion()
            self.state = 95
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
            self.state = 97
            self.match(RISCOParser.FOR)
            self.state = 98
            self.match(RISCOParser.IDENTIFICADOR)
            self.state = 99
            self.match(RISCOParser.IN)
            self.state = 100
            self.expresion()
            self.state = 101
            self.match(RISCOParser.T__3)
            self.state = 102
            self.match(RISCOParser.NL)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1091004686594) != 0):
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==39:
                    self.state = 103
                    self.match(RISCOParser.NL)
                    self.state = 108
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 109
                self.sentencia()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
            self.match(RISCOParser.END)
            self.state = 116
            self.match(RISCOParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(RISCOParser.IF, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RISCOParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(RISCOParser.ExpresionContext,i)


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


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(RISCOParser.ELIF)
            else:
                return self.getToken(RISCOParser.ELIF, i)

        def ELSE(self):
            return self.getToken(RISCOParser.ELSE, 0)

        def getRuleIndex(self):
            return RISCOParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = RISCOParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(RISCOParser.IF)
            self.state = 119
            self.expresion()
            self.state = 120
            self.match(RISCOParser.T__3)
            self.state = 121
            self.match(RISCOParser.NL)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1091004686594) != 0):
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==39:
                    self.state = 122
                    self.match(RISCOParser.NL)
                    self.state = 127
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 128
                self.sentencia()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 134
                self.match(RISCOParser.ELIF)
                self.state = 135
                self.expresion()
                self.state = 136
                self.match(RISCOParser.T__3)
                self.state = 137
                self.match(RISCOParser.NL)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1091004686594) != 0):
                    self.state = 141
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==39:
                        self.state = 138
                        self.match(RISCOParser.NL)
                        self.state = 143
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 144
                    self.sentencia()
                    self.state = 149
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 155
                self.match(RISCOParser.ELSE)
                self.state = 156
                self.match(RISCOParser.T__3)
                self.state = 157
                self.match(RISCOParser.NL)
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1091004686594) != 0):
                    self.state = 161
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==39:
                        self.state = 158
                        self.match(RISCOParser.NL)
                        self.state = 163
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 164
                    self.sentencia()
                    self.state = 169
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 172
            self.match(RISCOParser.END)
            self.state = 173
            self.match(RISCOParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(RISCOParser.WHILE, 0)

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
            return RISCOParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = RISCOParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_while_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(RISCOParser.WHILE)
            self.state = 176
            self.expresion()
            self.state = 177
            self.match(RISCOParser.T__3)
            self.state = 178
            self.match(RISCOParser.NL)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1091004686594) != 0):
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==39:
                    self.state = 179
                    self.match(RISCOParser.NL)
                    self.state = 184
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 185
                self.sentencia()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 191
            self.match(RISCOParser.END)
            self.state = 192
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
        self.enterRule(localctx, 18, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
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
        self.enterRule(localctx, 20, self.RULE_or_logico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.and_logico()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 197
                self.match(RISCOParser.OR)
                self.state = 198
                self.and_logico()
                self.state = 203
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
        self.enterRule(localctx, 22, self.RULE_and_logico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.igualdad()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 205
                self.match(RISCOParser.AND)
                self.state = 206
                self.igualdad()
                self.state = 211
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
        self.enterRule(localctx, 24, self.RULE_igualdad)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.relacional()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29 or _la==30:
                self.state = 213
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 214
                self.relacional()
                self.state = 219
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
        self.enterRule(localctx, 26, self.RULE_relacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.suma()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6442451040) != 0):
                self.state = 221
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6442451040) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 222
                self.suma()
                self.state = 227
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
        self.enterRule(localctx, 28, self.RULE_suma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.comparacion()
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 229
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 230
                self.comparacion()
                self.state = 235
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
        self.enterRule(localctx, 30, self.RULE_comparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.termino()
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 237
                self.match(RISCOParser.IN)
                self.state = 238
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
        self.enterRule(localctx, 32, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.potencia()
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0):
                self.state = 242
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 243
                self.potencia()
                self.state = 248
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
        self.enterRule(localctx, 34, self.RULE_potencia)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.primario()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.primario()
                self.state = 251
                self.match(RISCOParser.T__11)
                self.state = 252
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
        self.enterRule(localctx, 36, self.RULE_primario)
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(RISCOParser.NUMERO)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.match(RISCOParser.DECIMAL)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.match(RISCOParser.STRING)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.match(RISCOParser.BOOLEANO)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 5)
                self.state = 260
                self.match(RISCOParser.NULL)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 6)
                self.state = 261
                self.lista()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 7)
                self.state = 262
                self.match(RISCOParser.IDENTIFICADOR)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 8)
                self.state = 263
                self.match(RISCOParser.T__0)
                self.state = 264
                self.expresion()
                self.state = 265
                self.match(RISCOParser.T__1)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 9)
                self.state = 267
                self.match(RISCOParser.T__7)
                self.state = 268
                self.primario()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 10)
                self.state = 269
                self.match(RISCOParser.T__12)
                self.state = 270
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
        self.enterRule(localctx, 38, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(RISCOParser.T__13)
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 541165904130) != 0):
                self.state = 274
                self.expresion()
                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 275
                    self.match(RISCOParser.T__14)
                    self.state = 276
                    self.expresion()
                    self.state = 281
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 284
            self.match(RISCOParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





