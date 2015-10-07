import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.io.*;

class Compiler {
    public static void main(String[] args) {
        LoseLexer lexer = null;
        try {
            lexer = new LoseLexer(new ANTLRFileStream(args[0]));
        } catch (IOException e) {
            e.printStackTrace();
        }

        LoseParser parser = new LoseParser(new CommonTokenStream(lexer));
        ParseTree tree = parser.prog();
        ParseTreeWalker.DEFAULT.walk(new CodeWriter("",""), tree);
    }
}
