import org.antlr.v4.runtime.*;
import java.io.*;

class CodeWriter extends LoseBaseListener {
    public CodeWriter(String inputFile, String outputFile){
    }

    public void enterExpr(LoseParser.ExprContext ctx) {
        if (ctx.INT() != null) {
            System.out.println(ctx.INT().getText());
        }
    }

}
