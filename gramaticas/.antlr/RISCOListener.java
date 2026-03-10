// Generated from /home/lina/Risco-V1/gramaticas/RISCO.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link RISCOParser}.
 */
public interface RISCOListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link RISCOParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(RISCOParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link RISCOParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(RISCOParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link RISCOParser#sentencia}.
	 * @param ctx the parse tree
	 */
	void enterSentencia(RISCOParser.SentenciaContext ctx);
	/**
	 * Exit a parse tree produced by {@link RISCOParser#sentencia}.
	 * @param ctx the parse tree
	 */
	void exitSentencia(RISCOParser.SentenciaContext ctx);
	/**
	 * Enter a parse tree produced by {@link RISCOParser#declaracion_variable}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracion_variable(RISCOParser.Declaracion_variableContext ctx);
	/**
	 * Exit a parse tree produced by {@link RISCOParser#declaracion_variable}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracion_variable(RISCOParser.Declaracion_variableContext ctx);
	/**
	 * Enter a parse tree produced by {@link RISCOParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(RISCOParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link RISCOParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(RISCOParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link RISCOParser#expresion_stmt}.
	 * @param ctx the parse tree
	 */
	void enterExpresion_stmt(RISCOParser.Expresion_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link RISCOParser#expresion_stmt}.
	 * @param ctx the parse tree
	 */
	void exitExpresion_stmt(RISCOParser.Expresion_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link RISCOParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterExpresion(RISCOParser.ExpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link RISCOParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitExpresion(RISCOParser.ExpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link RISCOParser#termino}.
	 * @param ctx the parse tree
	 */
	void enterTermino(RISCOParser.TerminoContext ctx);
	/**
	 * Exit a parse tree produced by {@link RISCOParser#termino}.
	 * @param ctx the parse tree
	 */
	void exitTermino(RISCOParser.TerminoContext ctx);
	/**
	 * Enter a parse tree produced by {@link RISCOParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(RISCOParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link RISCOParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(RISCOParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link RISCOParser#potencia}.
	 * @param ctx the parse tree
	 */
	void enterPotencia(RISCOParser.PotenciaContext ctx);
	/**
	 * Exit a parse tree produced by {@link RISCOParser#potencia}.
	 * @param ctx the parse tree
	 */
	void exitPotencia(RISCOParser.PotenciaContext ctx);
	/**
	 * Enter a parse tree produced by {@link RISCOParser#primario}.
	 * @param ctx the parse tree
	 */
	void enterPrimario(RISCOParser.PrimarioContext ctx);
	/**
	 * Exit a parse tree produced by {@link RISCOParser#primario}.
	 * @param ctx the parse tree
	 */
	void exitPrimario(RISCOParser.PrimarioContext ctx);
	/**
	 * Enter a parse tree produced by {@link RISCOParser#lista}.
	 * @param ctx the parse tree
	 */
	void enterLista(RISCOParser.ListaContext ctx);
	/**
	 * Exit a parse tree produced by {@link RISCOParser#lista}.
	 * @param ctx the parse tree
	 */
	void exitLista(RISCOParser.ListaContext ctx);
}