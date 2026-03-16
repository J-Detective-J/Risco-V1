// Generated from /home/lina/Risco-V1/gramaticas/RISCO.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class RISCOParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, FOR=15, IN=16, END=17, 
		VAL=18, VAR=19, PRINT=20, NUMERO=21, DECIMAL=22, STRING=23, BOOLEANO=24, 
		NULL=25, IDENTIFICADOR=26, NL=27, WS=28, COMENTARIO_LINEA=29, COMENTARIO_BLOQUE=30, 
		COMENTARIO_DOC=31;
	public static final int
		RULE_programa = 0, RULE_sentencia = 1, RULE_print_stmt = 2, RULE_declaracion_variable = 3, 
		RULE_asignacion = 4, RULE_expresion_stmt = 5, RULE_for_stmt = 6, RULE_expresion = 7, 
		RULE_comparacion = 8, RULE_termino = 9, RULE_factor = 10, RULE_potencia = 11, 
		RULE_primario = 12, RULE_lista = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "sentencia", "print_stmt", "declaracion_variable", "asignacion", 
			"expresion_stmt", "for_stmt", "expresion", "comparacion", "termino", 
			"factor", "potencia", "primario", "lista"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'='", "':'", "'+'", "'-'", "'*'", "'/'", "'%'", 
			"'^'", "'!'", "'['", "','", "']'", "'for'", "'in'", "'end'", "'val'", 
			"'var'", "'print'", null, null, null, null, "'null'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "FOR", "IN", "END", "VAL", "VAR", "PRINT", "NUMERO", 
			"DECIMAL", "STRING", "BOOLEANO", "NULL", "IDENTIFICADOR", "NL", "WS", 
			"COMENTARIO_LINEA", "COMENTARIO_BLOQUE", "COMENTARIO_DOC"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "RISCO.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }


	    # Memoria para variables
	    memoria = {}

	public RISCOParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(RISCOParser.EOF, 0); }
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public List<TerminalNode> NL() { return getTokens(RISCOParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(RISCOParser.NL, i);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).enterPrograma(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).exitPrograma(this);
		}
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 268212290L) != 0)) {
				{
				{
				setState(31);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==NL) {
					{
					{
					setState(28);
					match(NL);
					}
					}
					setState(33);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(34);
				sentencia();
				setState(38);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(35);
						match(NL);
						}
						} 
					}
					setState(40);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
				}
				}
				}
				setState(45);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(46);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenciaContext extends ParserRuleContext {
		public Declaracion_variableContext declaracion_variable() {
			return getRuleContext(Declaracion_variableContext.class,0);
		}
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public Expresion_stmtContext expresion_stmt() {
			return getRuleContext(Expresion_stmtContext.class,0);
		}
		public For_stmtContext for_stmt() {
			return getRuleContext(For_stmtContext.class,0);
		}
		public Print_stmtContext print_stmt() {
			return getRuleContext(Print_stmtContext.class,0);
		}
		public SentenciaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentencia; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).enterSentencia(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).exitSentencia(this);
		}
	}

	public final SentenciaContext sentencia() throws RecognitionException {
		SentenciaContext _localctx = new SentenciaContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_sentencia);
		try {
			setState(53);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(48);
				declaracion_variable();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(49);
				asignacion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(50);
				expresion_stmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(51);
				for_stmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(52);
				print_stmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Print_stmtContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(RISCOParser.PRINT, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode NL() { return getToken(RISCOParser.NL, 0); }
		public Print_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).enterPrint_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).exitPrint_stmt(this);
		}
	}

	public final Print_stmtContext print_stmt() throws RecognitionException {
		Print_stmtContext _localctx = new Print_stmtContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_print_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			match(PRINT);
			setState(56);
			match(T__0);
			setState(57);
			expresion();
			setState(58);
			match(T__1);
			setState(59);
			match(NL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Declaracion_variableContext extends ParserRuleContext {
		public TerminalNode VAL() { return getToken(RISCOParser.VAL, 0); }
		public TerminalNode IDENTIFICADOR() { return getToken(RISCOParser.IDENTIFICADOR, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode NL() { return getToken(RISCOParser.NL, 0); }
		public TerminalNode VAR() { return getToken(RISCOParser.VAR, 0); }
		public Declaracion_variableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracion_variable; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).enterDeclaracion_variable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).exitDeclaracion_variable(this);
		}
	}

	public final Declaracion_variableContext declaracion_variable() throws RecognitionException {
		Declaracion_variableContext _localctx = new Declaracion_variableContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_declaracion_variable);
		try {
			setState(73);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(61);
				match(VAL);
				setState(62);
				match(IDENTIFICADOR);
				setState(63);
				match(T__2);
				setState(64);
				expresion();
				setState(65);
				match(NL);
				}
				break;
			case VAR:
				enterOuterAlt(_localctx, 2);
				{
				setState(67);
				match(VAR);
				setState(68);
				match(IDENTIFICADOR);
				setState(69);
				match(T__2);
				setState(70);
				expresion();
				setState(71);
				match(NL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionContext extends ParserRuleContext {
		public TerminalNode IDENTIFICADOR() { return getToken(RISCOParser.IDENTIFICADOR, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode NL() { return getToken(RISCOParser.NL, 0); }
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).enterAsignacion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).exitAsignacion(this);
		}
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(IDENTIFICADOR);
			setState(76);
			match(T__2);
			setState(77);
			expresion();
			setState(78);
			match(NL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expresion_stmtContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode NL() { return getToken(RISCOParser.NL, 0); }
		public Expresion_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).enterExpresion_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).exitExpresion_stmt(this);
		}
	}

	public final Expresion_stmtContext expresion_stmt() throws RecognitionException {
		Expresion_stmtContext _localctx = new Expresion_stmtContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_expresion_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			expresion();
			setState(81);
			match(NL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_stmtContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(RISCOParser.FOR, 0); }
		public TerminalNode IDENTIFICADOR() { return getToken(RISCOParser.IDENTIFICADOR, 0); }
		public TerminalNode IN() { return getToken(RISCOParser.IN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public List<TerminalNode> NL() { return getTokens(RISCOParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(RISCOParser.NL, i);
		}
		public TerminalNode END() { return getToken(RISCOParser.END, 0); }
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public For_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).enterFor_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).exitFor_stmt(this);
		}
	}

	public final For_stmtContext for_stmt() throws RecognitionException {
		For_stmtContext _localctx = new For_stmtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_for_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			match(FOR);
			setState(84);
			match(IDENTIFICADOR);
			setState(85);
			match(IN);
			setState(86);
			expresion();
			setState(87);
			match(T__3);
			setState(88);
			match(NL);
			setState(98);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 268212290L) != 0)) {
				{
				{
				setState(92);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==NL) {
					{
					{
					setState(89);
					match(NL);
					}
					}
					setState(94);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(95);
				sentencia();
				}
				}
				setState(100);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(101);
			match(END);
			setState(102);
			match(NL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionContext extends ParserRuleContext {
		public List<ComparacionContext> comparacion() {
			return getRuleContexts(ComparacionContext.class);
		}
		public ComparacionContext comparacion(int i) {
			return getRuleContext(ComparacionContext.class,i);
		}
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).enterExpresion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).exitExpresion(this);
		}
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_expresion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			comparacion();
			setState(109);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__4 || _la==T__5) {
				{
				{
				setState(105);
				_la = _input.LA(1);
				if ( !(_la==T__4 || _la==T__5) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(106);
				comparacion();
				}
				}
				setState(111);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComparacionContext extends ParserRuleContext {
		public List<TerminoContext> termino() {
			return getRuleContexts(TerminoContext.class);
		}
		public TerminoContext termino(int i) {
			return getRuleContext(TerminoContext.class,i);
		}
		public TerminalNode IN() { return getToken(RISCOParser.IN, 0); }
		public ComparacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparacion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).enterComparacion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).exitComparacion(this);
		}
	}

	public final ComparacionContext comparacion() throws RecognitionException {
		ComparacionContext _localctx = new ComparacionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_comparacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			termino();
			setState(115);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IN) {
				{
				setState(113);
				match(IN);
				setState(114);
				termino();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TerminoContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).enterTermino(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).exitTermino(this);
		}
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_termino);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			factor();
			setState(122);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 896L) != 0)) {
				{
				{
				setState(118);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 896L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(119);
				factor();
				}
				}
				setState(124);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public List<PotenciaContext> potencia() {
			return getRuleContexts(PotenciaContext.class);
		}
		public PotenciaContext potencia(int i) {
			return getRuleContext(PotenciaContext.class,i);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).enterFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).exitFactor(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_factor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			potencia();
			setState(130);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__9) {
				{
				{
				setState(126);
				match(T__9);
				setState(127);
				potencia();
				}
				}
				setState(132);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PotenciaContext extends ParserRuleContext {
		public PrimarioContext primario() {
			return getRuleContext(PrimarioContext.class,0);
		}
		public PotenciaContext potencia() {
			return getRuleContext(PotenciaContext.class,0);
		}
		public PotenciaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_potencia; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).enterPotencia(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).exitPotencia(this);
		}
	}

	public final PotenciaContext potencia() throws RecognitionException {
		PotenciaContext _localctx = new PotenciaContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_potencia);
		try {
			setState(138);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(133);
				primario();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(134);
				primario();
				setState(135);
				match(T__9);
				setState(136);
				potencia();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimarioContext extends ParserRuleContext {
		public TerminalNode NUMERO() { return getToken(RISCOParser.NUMERO, 0); }
		public TerminalNode DECIMAL() { return getToken(RISCOParser.DECIMAL, 0); }
		public TerminalNode STRING() { return getToken(RISCOParser.STRING, 0); }
		public TerminalNode BOOLEANO() { return getToken(RISCOParser.BOOLEANO, 0); }
		public TerminalNode NULL() { return getToken(RISCOParser.NULL, 0); }
		public ListaContext lista() {
			return getRuleContext(ListaContext.class,0);
		}
		public TerminalNode IDENTIFICADOR() { return getToken(RISCOParser.IDENTIFICADOR, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public PrimarioContext primario() {
			return getRuleContext(PrimarioContext.class,0);
		}
		public PrimarioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primario; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).enterPrimario(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).exitPrimario(this);
		}
	}

	public final PrimarioContext primario() throws RecognitionException {
		PrimarioContext _localctx = new PrimarioContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_primario);
		try {
			setState(155);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMERO:
				enterOuterAlt(_localctx, 1);
				{
				setState(140);
				match(NUMERO);
				}
				break;
			case DECIMAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(141);
				match(DECIMAL);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 3);
				{
				setState(142);
				match(STRING);
				}
				break;
			case BOOLEANO:
				enterOuterAlt(_localctx, 4);
				{
				setState(143);
				match(BOOLEANO);
				}
				break;
			case NULL:
				enterOuterAlt(_localctx, 5);
				{
				setState(144);
				match(NULL);
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 6);
				{
				setState(145);
				lista();
				}
				break;
			case IDENTIFICADOR:
				enterOuterAlt(_localctx, 7);
				{
				setState(146);
				match(IDENTIFICADOR);
				}
				break;
			case T__0:
				enterOuterAlt(_localctx, 8);
				{
				setState(147);
				match(T__0);
				setState(148);
				expresion();
				setState(149);
				match(T__1);
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 9);
				{
				setState(151);
				match(T__5);
				setState(152);
				primario();
				}
				break;
			case T__10:
				enterOuterAlt(_localctx, 10);
				{
				setState(153);
				match(T__10);
				setState(154);
				primario();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListaContext extends ParserRuleContext {
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public ListaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).enterLista(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof RISCOListener ) ((RISCOListener)listener).exitLista(this);
		}
	}

	public final ListaContext lista() throws RecognitionException {
		ListaContext _localctx = new ListaContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_lista);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			match(T__11);
			setState(166);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 132126786L) != 0)) {
				{
				setState(158);
				expresion();
				setState(163);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__12) {
					{
					{
					setState(159);
					match(T__12);
					setState(160);
					expresion();
					}
					}
					setState(165);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(168);
			match(T__13);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001f\u00ab\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0001\u0000\u0005\u0000\u001e\b\u0000"+
		"\n\u0000\f\u0000!\t\u0000\u0001\u0000\u0001\u0000\u0005\u0000%\b\u0000"+
		"\n\u0000\f\u0000(\t\u0000\u0005\u0000*\b\u0000\n\u0000\f\u0000-\t\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u00016\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003J\b\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0005\u0006[\b\u0006\n\u0006\f\u0006^\t\u0006"+
		"\u0001\u0006\u0005\u0006a\b\u0006\n\u0006\f\u0006d\t\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u0007"+
		"l\b\u0007\n\u0007\f\u0007o\t\u0007\u0001\b\u0001\b\u0001\b\u0003\bt\b"+
		"\b\u0001\t\u0001\t\u0001\t\u0005\ty\b\t\n\t\f\t|\t\t\u0001\n\u0001\n\u0001"+
		"\n\u0005\n\u0081\b\n\n\n\f\n\u0084\t\n\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0003\u000b\u008b\b\u000b\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0003\f\u009c\b\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0005\r\u00a2\b\r\n\r\f\r\u00a5\t\r\u0003\r\u00a7\b\r\u0001\r\u0001"+
		"\r\u0001\r\u0000\u0000\u000e\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u0000\u0002\u0001\u0000\u0005\u0006\u0001"+
		"\u0000\u0007\t\u00b6\u0000+\u0001\u0000\u0000\u0000\u00025\u0001\u0000"+
		"\u0000\u0000\u00047\u0001\u0000\u0000\u0000\u0006I\u0001\u0000\u0000\u0000"+
		"\bK\u0001\u0000\u0000\u0000\nP\u0001\u0000\u0000\u0000\fS\u0001\u0000"+
		"\u0000\u0000\u000eh\u0001\u0000\u0000\u0000\u0010p\u0001\u0000\u0000\u0000"+
		"\u0012u\u0001\u0000\u0000\u0000\u0014}\u0001\u0000\u0000\u0000\u0016\u008a"+
		"\u0001\u0000\u0000\u0000\u0018\u009b\u0001\u0000\u0000\u0000\u001a\u009d"+
		"\u0001\u0000\u0000\u0000\u001c\u001e\u0005\u001b\u0000\u0000\u001d\u001c"+
		"\u0001\u0000\u0000\u0000\u001e!\u0001\u0000\u0000\u0000\u001f\u001d\u0001"+
		"\u0000\u0000\u0000\u001f \u0001\u0000\u0000\u0000 \"\u0001\u0000\u0000"+
		"\u0000!\u001f\u0001\u0000\u0000\u0000\"&\u0003\u0002\u0001\u0000#%\u0005"+
		"\u001b\u0000\u0000$#\u0001\u0000\u0000\u0000%(\u0001\u0000\u0000\u0000"+
		"&$\u0001\u0000\u0000\u0000&\'\u0001\u0000\u0000\u0000\'*\u0001\u0000\u0000"+
		"\u0000(&\u0001\u0000\u0000\u0000)\u001f\u0001\u0000\u0000\u0000*-\u0001"+
		"\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000+,\u0001\u0000\u0000\u0000"+
		",.\u0001\u0000\u0000\u0000-+\u0001\u0000\u0000\u0000./\u0005\u0000\u0000"+
		"\u0001/\u0001\u0001\u0000\u0000\u000006\u0003\u0006\u0003\u000016\u0003"+
		"\b\u0004\u000026\u0003\n\u0005\u000036\u0003\f\u0006\u000046\u0003\u0004"+
		"\u0002\u000050\u0001\u0000\u0000\u000051\u0001\u0000\u0000\u000052\u0001"+
		"\u0000\u0000\u000053\u0001\u0000\u0000\u000054\u0001\u0000\u0000\u0000"+
		"6\u0003\u0001\u0000\u0000\u000078\u0005\u0014\u0000\u000089\u0005\u0001"+
		"\u0000\u00009:\u0003\u000e\u0007\u0000:;\u0005\u0002\u0000\u0000;<\u0005"+
		"\u001b\u0000\u0000<\u0005\u0001\u0000\u0000\u0000=>\u0005\u0012\u0000"+
		"\u0000>?\u0005\u001a\u0000\u0000?@\u0005\u0003\u0000\u0000@A\u0003\u000e"+
		"\u0007\u0000AB\u0005\u001b\u0000\u0000BJ\u0001\u0000\u0000\u0000CD\u0005"+
		"\u0013\u0000\u0000DE\u0005\u001a\u0000\u0000EF\u0005\u0003\u0000\u0000"+
		"FG\u0003\u000e\u0007\u0000GH\u0005\u001b\u0000\u0000HJ\u0001\u0000\u0000"+
		"\u0000I=\u0001\u0000\u0000\u0000IC\u0001\u0000\u0000\u0000J\u0007\u0001"+
		"\u0000\u0000\u0000KL\u0005\u001a\u0000\u0000LM\u0005\u0003\u0000\u0000"+
		"MN\u0003\u000e\u0007\u0000NO\u0005\u001b\u0000\u0000O\t\u0001\u0000\u0000"+
		"\u0000PQ\u0003\u000e\u0007\u0000QR\u0005\u001b\u0000\u0000R\u000b\u0001"+
		"\u0000\u0000\u0000ST\u0005\u000f\u0000\u0000TU\u0005\u001a\u0000\u0000"+
		"UV\u0005\u0010\u0000\u0000VW\u0003\u000e\u0007\u0000WX\u0005\u0004\u0000"+
		"\u0000Xb\u0005\u001b\u0000\u0000Y[\u0005\u001b\u0000\u0000ZY\u0001\u0000"+
		"\u0000\u0000[^\u0001\u0000\u0000\u0000\\Z\u0001\u0000\u0000\u0000\\]\u0001"+
		"\u0000\u0000\u0000]_\u0001\u0000\u0000\u0000^\\\u0001\u0000\u0000\u0000"+
		"_a\u0003\u0002\u0001\u0000`\\\u0001\u0000\u0000\u0000ad\u0001\u0000\u0000"+
		"\u0000b`\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000ce\u0001\u0000"+
		"\u0000\u0000db\u0001\u0000\u0000\u0000ef\u0005\u0011\u0000\u0000fg\u0005"+
		"\u001b\u0000\u0000g\r\u0001\u0000\u0000\u0000hm\u0003\u0010\b\u0000ij"+
		"\u0007\u0000\u0000\u0000jl\u0003\u0010\b\u0000ki\u0001\u0000\u0000\u0000"+
		"lo\u0001\u0000\u0000\u0000mk\u0001\u0000\u0000\u0000mn\u0001\u0000\u0000"+
		"\u0000n\u000f\u0001\u0000\u0000\u0000om\u0001\u0000\u0000\u0000ps\u0003"+
		"\u0012\t\u0000qr\u0005\u0010\u0000\u0000rt\u0003\u0012\t\u0000sq\u0001"+
		"\u0000\u0000\u0000st\u0001\u0000\u0000\u0000t\u0011\u0001\u0000\u0000"+
		"\u0000uz\u0003\u0014\n\u0000vw\u0007\u0001\u0000\u0000wy\u0003\u0014\n"+
		"\u0000xv\u0001\u0000\u0000\u0000y|\u0001\u0000\u0000\u0000zx\u0001\u0000"+
		"\u0000\u0000z{\u0001\u0000\u0000\u0000{\u0013\u0001\u0000\u0000\u0000"+
		"|z\u0001\u0000\u0000\u0000}\u0082\u0003\u0016\u000b\u0000~\u007f\u0005"+
		"\n\u0000\u0000\u007f\u0081\u0003\u0016\u000b\u0000\u0080~\u0001\u0000"+
		"\u0000\u0000\u0081\u0084\u0001\u0000\u0000\u0000\u0082\u0080\u0001\u0000"+
		"\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u0015\u0001\u0000"+
		"\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0085\u008b\u0003\u0018"+
		"\f\u0000\u0086\u0087\u0003\u0018\f\u0000\u0087\u0088\u0005\n\u0000\u0000"+
		"\u0088\u0089\u0003\u0016\u000b\u0000\u0089\u008b\u0001\u0000\u0000\u0000"+
		"\u008a\u0085\u0001\u0000\u0000\u0000\u008a\u0086\u0001\u0000\u0000\u0000"+
		"\u008b\u0017\u0001\u0000\u0000\u0000\u008c\u009c\u0005\u0015\u0000\u0000"+
		"\u008d\u009c\u0005\u0016\u0000\u0000\u008e\u009c\u0005\u0017\u0000\u0000"+
		"\u008f\u009c\u0005\u0018\u0000\u0000\u0090\u009c\u0005\u0019\u0000\u0000"+
		"\u0091\u009c\u0003\u001a\r\u0000\u0092\u009c\u0005\u001a\u0000\u0000\u0093"+
		"\u0094\u0005\u0001\u0000\u0000\u0094\u0095\u0003\u000e\u0007\u0000\u0095"+
		"\u0096\u0005\u0002\u0000\u0000\u0096\u009c\u0001\u0000\u0000\u0000\u0097"+
		"\u0098\u0005\u0006\u0000\u0000\u0098\u009c\u0003\u0018\f\u0000\u0099\u009a"+
		"\u0005\u000b\u0000\u0000\u009a\u009c\u0003\u0018\f\u0000\u009b\u008c\u0001"+
		"\u0000\u0000\u0000\u009b\u008d\u0001\u0000\u0000\u0000\u009b\u008e\u0001"+
		"\u0000\u0000\u0000\u009b\u008f\u0001\u0000\u0000\u0000\u009b\u0090\u0001"+
		"\u0000\u0000\u0000\u009b\u0091\u0001\u0000\u0000\u0000\u009b\u0092\u0001"+
		"\u0000\u0000\u0000\u009b\u0093\u0001\u0000\u0000\u0000\u009b\u0097\u0001"+
		"\u0000\u0000\u0000\u009b\u0099\u0001\u0000\u0000\u0000\u009c\u0019\u0001"+
		"\u0000\u0000\u0000\u009d\u00a6\u0005\f\u0000\u0000\u009e\u00a3\u0003\u000e"+
		"\u0007\u0000\u009f\u00a0\u0005\r\u0000\u0000\u00a0\u00a2\u0003\u000e\u0007"+
		"\u0000\u00a1\u009f\u0001\u0000\u0000\u0000\u00a2\u00a5\u0001\u0000\u0000"+
		"\u0000\u00a3\u00a1\u0001\u0000\u0000\u0000\u00a3\u00a4\u0001\u0000\u0000"+
		"\u0000\u00a4\u00a7\u0001\u0000\u0000\u0000\u00a5\u00a3\u0001\u0000\u0000"+
		"\u0000\u00a6\u009e\u0001\u0000\u0000\u0000\u00a6\u00a7\u0001\u0000\u0000"+
		"\u0000\u00a7\u00a8\u0001\u0000\u0000\u0000\u00a8\u00a9\u0005\u000e\u0000"+
		"\u0000\u00a9\u001b\u0001\u0000\u0000\u0000\u000f\u001f&+5I\\bmsz\u0082"+
		"\u008a\u009b\u00a3\u00a6";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}