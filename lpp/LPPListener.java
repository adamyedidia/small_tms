// Generated from LPP.g4 by ANTLR 4.5
import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link LPPParser}.
 */
public interface LPPListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link LPPParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(LPPParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(LPPParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#trueprog}.
	 * @param ctx the parse tree
	 */
	void enterTrueprog(LPPParser.TrueprogContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#trueprog}.
	 * @param ctx the parse tree
	 */
	void exitTrueprog(LPPParser.TrueprogContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(LPPParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(LPPParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#nondefprog}.
	 * @param ctx the parse tree
	 */
	void enterNondefprog(LPPParser.NondefprogContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#nondefprog}.
	 * @param ctx the parse tree
	 */
	void exitNondefprog(LPPParser.NondefprogContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#nondefcommand}.
	 * @param ctx the parse tree
	 */
	void enterNondefcommand(LPPParser.NondefcommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#nondefcommand}.
	 * @param ctx the parse tree
	 */
	void exitNondefcommand(LPPParser.NondefcommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#funcdef}.
	 * @param ctx the parse tree
	 */
	void enterFuncdef(LPPParser.FuncdefContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#funcdef}.
	 * @param ctx the parse tree
	 */
	void exitFuncdef(LPPParser.FuncdefContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#procdef}.
	 * @param ctx the parse tree
	 */
	void enterProcdef(LPPParser.ProcdefContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#procdef}.
	 * @param ctx the parse tree
	 */
	void exitProcdef(LPPParser.ProcdefContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#funcprocbody}.
	 * @param ctx the parse tree
	 */
	void enterFuncprocbody(LPPParser.FuncprocbodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#funcprocbody}.
	 * @param ctx the parse tree
	 */
	void exitFuncprocbody(LPPParser.FuncprocbodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#declare}.
	 * @param ctx the parse tree
	 */
	void enterDeclare(LPPParser.DeclareContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#declare}.
	 * @param ctx the parse tree
	 */
	void exitDeclare(LPPParser.DeclareContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#intdecl}.
	 * @param ctx the parse tree
	 */
	void enterIntdecl(LPPParser.IntdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#intdecl}.
	 * @param ctx the parse tree
	 */
	void exitIntdecl(LPPParser.IntdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#listdecl}.
	 * @param ctx the parse tree
	 */
	void enterListdecl(LPPParser.ListdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#listdecl}.
	 * @param ctx the parse tree
	 */
	void exitListdecl(LPPParser.ListdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#list2decl}.
	 * @param ctx the parse tree
	 */
	void enterList2decl(LPPParser.List2declContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#list2decl}.
	 * @param ctx the parse tree
	 */
	void exitList2decl(LPPParser.List2declContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#funcproccall}.
	 * @param ctx the parse tree
	 */
	void enterFuncproccall(LPPParser.FuncproccallContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#funcproccall}.
	 * @param ctx the parse tree
	 */
	void exitFuncproccall(LPPParser.FuncproccallContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#funcproccallbody}.
	 * @param ctx the parse tree
	 */
	void enterFuncproccallbody(LPPParser.FuncproccallbodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#funcproccallbody}.
	 * @param ctx the parse tree
	 */
	void exitFuncproccallbody(LPPParser.FuncproccallbodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#whileloop}.
	 * @param ctx the parse tree
	 */
	void enterWhileloop(LPPParser.WhileloopContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#whileloop}.
	 * @param ctx the parse tree
	 */
	void exitWhileloop(LPPParser.WhileloopContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#forloop}.
	 * @param ctx the parse tree
	 */
	void enterForloop(LPPParser.ForloopContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#forloop}.
	 * @param ctx the parse tree
	 */
	void exitForloop(LPPParser.ForloopContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#ifstate}.
	 * @param ctx the parse tree
	 */
	void enterIfstate(LPPParser.IfstateContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#ifstate}.
	 * @param ctx the parse tree
	 */
	void exitIfstate(LPPParser.IfstateContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#printstate}.
	 * @param ctx the parse tree
	 */
	void enterPrintstate(LPPParser.PrintstateContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#printstate}.
	 * @param ctx the parse tree
	 */
	void exitPrintstate(LPPParser.PrintstateContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#ifelsestate}.
	 * @param ctx the parse tree
	 */
	void enterIfelsestate(LPPParser.IfelsestateContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#ifelsestate}.
	 * @param ctx the parse tree
	 */
	void exitIfelsestate(LPPParser.IfelsestateContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#ifelsenondefprog}.
	 * @param ctx the parse tree
	 */
	void enterIfelsenondefprog(LPPParser.IfelsenondefprogContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#ifelsenondefprog}.
	 * @param ctx the parse tree
	 */
	void exitIfelsenondefprog(LPPParser.IfelsenondefprogContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#elsenondefprog}.
	 * @param ctx the parse tree
	 */
	void enterElsenondefprog(LPPParser.ElsenondefprogContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#elsenondefprog}.
	 * @param ctx the parse tree
	 */
	void exitElsenondefprog(LPPParser.ElsenondefprogContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#ifnondefprog}.
	 * @param ctx the parse tree
	 */
	void enterIfnondefprog(LPPParser.IfnondefprogContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#ifnondefprog}.
	 * @param ctx the parse tree
	 */
	void exitIfnondefprog(LPPParser.IfnondefprogContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#whilenondefprog}.
	 * @param ctx the parse tree
	 */
	void enterWhilenondefprog(LPPParser.WhilenondefprogContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#whilenondefprog}.
	 * @param ctx the parse tree
	 */
	void exitWhilenondefprog(LPPParser.WhilenondefprogContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#ifelseexpr}.
	 * @param ctx the parse tree
	 */
	void enterIfelseexpr(LPPParser.IfelseexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#ifelseexpr}.
	 * @param ctx the parse tree
	 */
	void exitIfelseexpr(LPPParser.IfelseexprContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#ifexpr}.
	 * @param ctx the parse tree
	 */
	void enterIfexpr(LPPParser.IfexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#ifexpr}.
	 * @param ctx the parse tree
	 */
	void exitIfexpr(LPPParser.IfexprContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#whileexpr}.
	 * @param ctx the parse tree
	 */
	void enterWhileexpr(LPPParser.WhileexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#whileexpr}.
	 * @param ctx the parse tree
	 */
	void exitWhileexpr(LPPParser.WhileexprContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(LPPParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(LPPParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(LPPParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(LPPParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#returnstate}.
	 * @param ctx the parse tree
	 */
	void enterReturnstate(LPPParser.ReturnstateContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#returnstate}.
	 * @param ctx the parse tree
	 */
	void exitReturnstate(LPPParser.ReturnstateContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#intexpr}.
	 * @param ctx the parse tree
	 */
	void enterIntexpr(LPPParser.IntexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#intexpr}.
	 * @param ctx the parse tree
	 */
	void exitIntexpr(LPPParser.IntexprContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#listexpr}.
	 * @param ctx the parse tree
	 */
	void enterListexpr(LPPParser.ListexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#listexpr}.
	 * @param ctx the parse tree
	 */
	void exitListexpr(LPPParser.ListexprContext ctx);
	/**
	 * Enter a parse tree produced by {@link LPPParser#list2expr}.
	 * @param ctx the parse tree
	 */
	void enterList2expr(LPPParser.List2exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link LPPParser#list2expr}.
	 * @param ctx the parse tree
	 */
	void exitList2expr(LPPParser.List2exprContext ctx);
}