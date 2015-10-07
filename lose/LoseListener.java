// Generated from Lose.g4 by ANTLR 4.5
import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link LoseParser}.
 */
public interface LoseListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link LoseParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(LoseParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link LoseParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(LoseParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link LoseParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(LoseParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link LoseParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(LoseParser.ExprContext ctx);
}