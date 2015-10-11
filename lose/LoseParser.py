# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .LoseListener import LoseListener
else:
    from LoseListener import LoseListener
def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\33\u00f0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\3\2\3\2\3\3\7\3@\n\3\f\3\16\3C\13\3\3")
        buf.write(u"\3\3\3\3\4\3\4\3\4\3\4\5\4K\n\4\3\5\7\5N\n\5\f\5\16\5")
        buf.write(u"Q\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6Z\n\6\3\7\3\7\3")
        buf.write(u"\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\5")
        buf.write(u"\nk\n\n\3\13\3\13\3\13\3\13\5\13q\n\13\3\13\3\13\3\f")
        buf.write(u"\3\f\3\f\3\f\5\fy\n\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u0081")
        buf.write(u"\n\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16\u0089\n\16\3\16")
        buf.write(u"\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\7\20\u0094\n")
        buf.write(u"\20\f\20\16\20\u0097\13\20\3\20\3\20\3\20\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write(u"\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3")
        buf.write(u"\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write(u"\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3")
        buf.write(u"\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write(u"\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3")
        buf.write(u"\36\3\36\3\36\5\36\u00e0\n\36\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\3\36\3\36\3\36\3\36\7\36\u00eb\n\36\f\36\16\36\u00ee")
        buf.write(u"\13\36\3\36\2\3:\37\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write(u"\34\36 \"$&(*,.\60\62\64\668:\2\3\3\2\24\25\u00ea\2<")
        buf.write(u"\3\2\2\2\4A\3\2\2\2\6J\3\2\2\2\bO\3\2\2\2\nY\3\2\2\2")
        buf.write(u"\f[\3\2\2\2\16^\3\2\2\2\20a\3\2\2\2\22j\3\2\2\2\24l\3")
        buf.write(u"\2\2\2\26t\3\2\2\2\30|\3\2\2\2\32\u0084\3\2\2\2\34\u008c")
        buf.write(u"\3\2\2\2\36\u008f\3\2\2\2 \u009b\3\2\2\2\"\u00a3\3\2")
        buf.write(u"\2\2$\u00af\3\2\2\2&\u00b7\3\2\2\2(\u00c2\3\2\2\2*\u00c4")
        buf.write(u"\3\2\2\2,\u00c6\3\2\2\2.\u00c8\3\2\2\2\60\u00ca\3\2\2")
        buf.write(u"\2\62\u00cc\3\2\2\2\64\u00ce\3\2\2\2\66\u00d0\3\2\2\2")
        buf.write(u"8\u00d5\3\2\2\2:\u00df\3\2\2\2<=\5\4\3\2=\3\3\2\2\2>")
        buf.write(u"@\5\6\4\2?>\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2BD\3")
        buf.write(u"\2\2\2CA\3\2\2\2DE\7\2\2\3E\5\3\2\2\2FK\5\f\7\2GK\5\16")
        buf.write(u"\b\2HK\5\22\n\2IK\5\n\6\2JF\3\2\2\2JG\3\2\2\2JH\3\2\2")
        buf.write(u"\2JI\3\2\2\2K\7\3\2\2\2LN\5\n\6\2ML\3\2\2\2NQ\3\2\2\2")
        buf.write(u"OM\3\2\2\2OP\3\2\2\2P\t\3\2\2\2QO\3\2\2\2RZ\5\34\17\2")
        buf.write(u"SZ\5 \21\2TZ\5\"\22\2UZ\5$\23\2VZ\5&\24\2WZ\5\66\34\2")
        buf.write(u"XZ\58\35\2YR\3\2\2\2YS\3\2\2\2YT\3\2\2\2YU\3\2\2\2YV")
        buf.write(u"\3\2\2\2YW\3\2\2\2YX\3\2\2\2Z\13\3\2\2\2[\\\7\3\2\2\\")
        buf.write(u"]\5\20\t\2]\r\3\2\2\2^_\7\4\2\2_`\5\20\t\2`\17\3\2\2")
        buf.write(u"\2ab\5\36\20\2bc\7\5\2\2cd\5\b\5\2de\7\6\2\2e\21\3\2")
        buf.write(u"\2\2fk\5\24\13\2gk\5\26\f\2hk\5\30\r\2ik\5\32\16\2jf")
        buf.write(u"\3\2\2\2jg\3\2\2\2jh\3\2\2\2ji\3\2\2\2k\23\3\2\2\2lm")
        buf.write(u"\7\7\2\2mp\7\32\2\2no\7\b\2\2oq\5:\36\2pn\3\2\2\2pq\3")
        buf.write(u"\2\2\2qr\3\2\2\2rs\7\t\2\2s\25\3\2\2\2tu\7\n\2\2ux\7")
        buf.write(u"\32\2\2vw\7\b\2\2wy\5:\36\2xv\3\2\2\2xy\3\2\2\2yz\3\2")
        buf.write(u"\2\2z{\7\t\2\2{\27\3\2\2\2|}\7\13\2\2}\u0080\7\32\2\2")
        buf.write(u"~\177\7\b\2\2\177\u0081\5:\36\2\u0080~\3\2\2\2\u0080")
        buf.write(u"\u0081\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\7\t\2")
        buf.write(u"\2\u0083\31\3\2\2\2\u0084\u0085\7\f\2\2\u0085\u0088\7")
        buf.write(u"\32\2\2\u0086\u0087\7\b\2\2\u0087\u0089\5:\36\2\u0088")
        buf.write(u"\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\3\2\2")
        buf.write(u"\2\u008a\u008b\7\t\2\2\u008b\33\3\2\2\2\u008c\u008d\5")
        buf.write(u"\36\20\2\u008d\u008e\7\t\2\2\u008e\35\3\2\2\2\u008f\u0090")
        buf.write(u"\7\32\2\2\u0090\u0095\7\r\2\2\u0091\u0092\7\32\2\2\u0092")
        buf.write(u"\u0094\7\16\2\2\u0093\u0091\3\2\2\2\u0094\u0097\3\2\2")
        buf.write(u"\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098")
        buf.write(u"\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099\7\32\2\2\u0099")
        buf.write(u"\u009a\7\17\2\2\u009a\37\3\2\2\2\u009b\u009c\7\20\2\2")
        buf.write(u"\u009c\u009d\7\r\2\2\u009d\u009e\5\64\33\2\u009e\u009f")
        buf.write(u"\7\17\2\2\u009f\u00a0\7\5\2\2\u00a0\u00a1\5.\30\2\u00a1")
        buf.write(u"\u00a2\7\6\2\2\u00a2!\3\2\2\2\u00a3\u00a4\7\21\2\2\u00a4")
        buf.write(u"\u00a5\7\r\2\2\u00a5\u00a6\5\n\6\2\u00a6\u00a7\7\t\2")
        buf.write(u"\2\u00a7\u00a8\5:\36\2\u00a8\u00a9\7\t\2\2\u00a9\u00aa")
        buf.write(u"\5\n\6\2\u00aa\u00ab\7\17\2\2\u00ab\u00ac\7\5\2\2\u00ac")
        buf.write(u"\u00ad\5\b\5\2\u00ad\u00ae\7\6\2\2\u00ae#\3\2\2\2\u00af")
        buf.write(u"\u00b0\7\22\2\2\u00b0\u00b1\7\r\2\2\u00b1\u00b2\5\62")
        buf.write(u"\32\2\u00b2\u00b3\7\17\2\2\u00b3\u00b4\7\5\2\2\u00b4")
        buf.write(u"\u00b5\5,\27\2\u00b5\u00b6\7\6\2\2\u00b6%\3\2\2\2\u00b7")
        buf.write(u"\u00b8\7\23\2\2\u00b8\u00b9\7\r\2\2\u00b9\u00ba\5\60")
        buf.write(u"\31\2\u00ba\u00bb\7\17\2\2\u00bb\u00bc\7\5\2\2\u00bc")
        buf.write(u"\u00bd\5(\25\2\u00bd\u00be\7\6\2\2\u00be\u00bf\7\5\2")
        buf.write(u"\2\u00bf\u00c0\5*\26\2\u00c0\u00c1\7\6\2\2\u00c1\'\3")
        buf.write(u"\2\2\2\u00c2\u00c3\5\b\5\2\u00c3)\3\2\2\2\u00c4\u00c5")
        buf.write(u"\5\b\5\2\u00c5+\3\2\2\2\u00c6\u00c7\5\b\5\2\u00c7-\3")
        buf.write(u"\2\2\2\u00c8\u00c9\5\b\5\2\u00c9/\3\2\2\2\u00ca\u00cb")
        buf.write(u"\5:\36\2\u00cb\61\3\2\2\2\u00cc\u00cd\5:\36\2\u00cd\63")
        buf.write(u"\3\2\2\2\u00ce\u00cf\5:\36\2\u00cf\65\3\2\2\2\u00d0\u00d1")
        buf.write(u"\7\32\2\2\u00d1\u00d2\7\b\2\2\u00d2\u00d3\5:\36\2\u00d3")
        buf.write(u"\u00d4\7\t\2\2\u00d4\67\3\2\2\2\u00d5\u00d6\t\2\2\2\u00d6")
        buf.write(u"\u00d7\7\t\2\2\u00d79\3\2\2\2\u00d8\u00d9\b\36\1\2\u00d9")
        buf.write(u"\u00e0\7\33\2\2\u00da\u00db\7\r\2\2\u00db\u00dc\5:\36")
        buf.write(u"\2\u00dc\u00dd\7\17\2\2\u00dd\u00e0\3\2\2\2\u00de\u00e0")
        buf.write(u"\7\32\2\2\u00df\u00d8\3\2\2\2\u00df\u00da\3\2\2\2\u00df")
        buf.write(u"\u00de\3\2\2\2\u00e0\u00ec\3\2\2\2\u00e1\u00e2\f\b\2")
        buf.write(u"\2\u00e2\u00e3\7\26\2\2\u00e3\u00eb\5:\36\t\u00e4\u00e5")
        buf.write(u"\f\7\2\2\u00e5\u00e6\7\27\2\2\u00e6\u00eb\5:\36\b\u00e7")
        buf.write(u"\u00e8\f\6\2\2\u00e8\u00e9\7\30\2\2\u00e9\u00eb\5:\36")
        buf.write(u"\7\u00ea\u00e1\3\2\2\2\u00ea\u00e4\3\2\2\2\u00ea\u00e7")
        buf.write(u"\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec")
        buf.write(u"\u00ed\3\2\2\2\u00ed;\3\2\2\2\u00ee\u00ec\3\2\2\2\17")
        buf.write(u"AJOYjpx\u0080\u0088\u0095\u00df\u00ea\u00ec")
        return buf.getvalue()


class LoseParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'func'", u"'proc'", u"'{'", u"'}'", 
                     u"'nat'", u"'='", u"';'", u"'signed'", u"'list'", u"'list2'", 
                     u"'('", u"','", u"')'", u"'while'", u"'for'", u"'if'", 
                     u"'ifelse'", u"'return'", u"'halt'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"OPERATOR_MUL_DIV", u"OPERATOR_ADD_SUB", u"OPERATOR_COMPARE", 
                      u"WS", u"VAR", u"INT" ]

    RULE_prog = 0
    RULE_trueprog = 1
    RULE_command = 2
    RULE_nondefprog = 3
    RULE_nondefcommand = 4
    RULE_funcdef = 5
    RULE_procdef = 6
    RULE_funcprocbody = 7
    RULE_declare = 8
    RULE_natdecl = 9
    RULE_signdecl = 10
    RULE_listdecl = 11
    RULE_list2decl = 12
    RULE_funcproccall = 13
    RULE_funcproccallbody = 14
    RULE_whileloop = 15
    RULE_forloop = 16
    RULE_ifstate = 17
    RULE_ifelsestate = 18
    RULE_ifelsenondefprog = 19
    RULE_elsenondefprog = 20
    RULE_ifnondefprog = 21
    RULE_whilenondefprog = 22
    RULE_ifelseexpr = 23
    RULE_ifexpr = 24
    RULE_whileexpr = 25
    RULE_assign = 26
    RULE_returnstate = 27
    RULE_expr = 28

    ruleNames =  [ u"prog", u"trueprog", u"command", u"nondefprog", u"nondefcommand", 
                   u"funcdef", u"procdef", u"funcprocbody", u"declare", 
                   u"natdecl", u"signdecl", u"listdecl", u"list2decl", u"funcproccall", 
                   u"funcproccallbody", u"whileloop", u"forloop", u"ifstate", 
                   u"ifelsestate", u"ifelsenondefprog", u"elsenondefprog", 
                   u"ifnondefprog", u"whilenondefprog", u"ifelseexpr", u"ifexpr", 
                   u"whileexpr", u"assign", u"returnstate", u"expr" ]

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
    T__16=17
    T__17=18
    T__18=19
    OPERATOR_MUL_DIV=20
    OPERATOR_ADD_SUB=21
    OPERATOR_COMPARE=22
    WS=23
    VAR=24
    INT=25

    def __init__(self, input):
        super(LoseParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.ProgContext, self).__init__(parent, invokingState)
            self.parser = parser

        def trueprog(self):
            return self.getTypedRuleContext(LoseParser.TrueprogContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_prog

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterProg(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitProg(self)




    def prog(self):

        localctx = LoseParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.trueprog()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TrueprogContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.TrueprogContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LoseParser.EOF, 0)

        def command(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LoseParser.CommandContext)
            else:
                return self.getTypedRuleContext(LoseParser.CommandContext,i)


        def getRuleIndex(self):
            return LoseParser.RULE_trueprog

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterTrueprog(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitTrueprog(self)




    def trueprog(self):

        localctx = LoseParser.TrueprogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_trueprog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LoseParser.T__0) | (1 << LoseParser.T__1) | (1 << LoseParser.T__4) | (1 << LoseParser.T__7) | (1 << LoseParser.T__8) | (1 << LoseParser.T__9) | (1 << LoseParser.T__13) | (1 << LoseParser.T__14) | (1 << LoseParser.T__15) | (1 << LoseParser.T__16) | (1 << LoseParser.T__17) | (1 << LoseParser.T__18) | (1 << LoseParser.VAR))) != 0):
                self.state = 60
                self.command()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(LoseParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.CommandContext, self).__init__(parent, invokingState)
            self.parser = parser

        def funcdef(self):
            return self.getTypedRuleContext(LoseParser.FuncdefContext,0)


        def procdef(self):
            return self.getTypedRuleContext(LoseParser.ProcdefContext,0)


        def declare(self):
            return self.getTypedRuleContext(LoseParser.DeclareContext,0)


        def nondefcommand(self):
            return self.getTypedRuleContext(LoseParser.NondefcommandContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_command

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterCommand(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitCommand(self)




    def command(self):

        localctx = LoseParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            token = self._input.LA(1)
            if token in [LoseParser.T__0]:
                self.state = 68
                self.funcdef()

            elif token in [LoseParser.T__1]:
                self.state = 69
                self.procdef()

            elif token in [LoseParser.T__4, LoseParser.T__7, LoseParser.T__8, LoseParser.T__9]:
                self.state = 70
                self.declare()

            elif token in [LoseParser.T__13, LoseParser.T__14, LoseParser.T__15, LoseParser.T__16, LoseParser.T__17, LoseParser.T__18, LoseParser.VAR]:
                self.state = 71
                self.nondefcommand()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NondefprogContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.NondefprogContext, self).__init__(parent, invokingState)
            self.parser = parser

        def nondefcommand(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LoseParser.NondefcommandContext)
            else:
                return self.getTypedRuleContext(LoseParser.NondefcommandContext,i)


        def getRuleIndex(self):
            return LoseParser.RULE_nondefprog

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterNondefprog(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitNondefprog(self)




    def nondefprog(self):

        localctx = LoseParser.NondefprogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_nondefprog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LoseParser.T__13) | (1 << LoseParser.T__14) | (1 << LoseParser.T__15) | (1 << LoseParser.T__16) | (1 << LoseParser.T__17) | (1 << LoseParser.T__18) | (1 << LoseParser.VAR))) != 0):
                self.state = 74
                self.nondefcommand()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NondefcommandContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.NondefcommandContext, self).__init__(parent, invokingState)
            self.parser = parser

        def funcproccall(self):
            return self.getTypedRuleContext(LoseParser.FuncproccallContext,0)


        def whileloop(self):
            return self.getTypedRuleContext(LoseParser.WhileloopContext,0)


        def forloop(self):
            return self.getTypedRuleContext(LoseParser.ForloopContext,0)


        def ifstate(self):
            return self.getTypedRuleContext(LoseParser.IfstateContext,0)


        def ifelsestate(self):
            return self.getTypedRuleContext(LoseParser.IfelsestateContext,0)


        def assign(self):
            return self.getTypedRuleContext(LoseParser.AssignContext,0)


        def returnstate(self):
            return self.getTypedRuleContext(LoseParser.ReturnstateContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_nondefcommand

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterNondefcommand(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitNondefcommand(self)




    def nondefcommand(self):

        localctx = LoseParser.NondefcommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_nondefcommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 80
                self.funcproccall()
                pass

            elif la_ == 2:
                self.state = 81
                self.whileloop()
                pass

            elif la_ == 3:
                self.state = 82
                self.forloop()
                pass

            elif la_ == 4:
                self.state = 83
                self.ifstate()
                pass

            elif la_ == 5:
                self.state = 84
                self.ifelsestate()
                pass

            elif la_ == 6:
                self.state = 85
                self.assign()
                pass

            elif la_ == 7:
                self.state = 86
                self.returnstate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncdefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.FuncdefContext, self).__init__(parent, invokingState)
            self.parser = parser

        def funcprocbody(self):
            return self.getTypedRuleContext(LoseParser.FuncprocbodyContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_funcdef

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterFuncdef(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitFuncdef(self)




    def funcdef(self):

        localctx = LoseParser.FuncdefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcdef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(LoseParser.T__0)
            self.state = 90
            self.funcprocbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProcdefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.ProcdefContext, self).__init__(parent, invokingState)
            self.parser = parser

        def funcprocbody(self):
            return self.getTypedRuleContext(LoseParser.FuncprocbodyContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_procdef

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterProcdef(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitProcdef(self)




    def procdef(self):

        localctx = LoseParser.ProcdefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_procdef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(LoseParser.T__1)
            self.state = 93
            self.funcprocbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncprocbodyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.FuncprocbodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def funcproccallbody(self):
            return self.getTypedRuleContext(LoseParser.FuncproccallbodyContext,0)


        def nondefprog(self):
            return self.getTypedRuleContext(LoseParser.NondefprogContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_funcprocbody

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterFuncprocbody(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitFuncprocbody(self)




    def funcprocbody(self):

        localctx = LoseParser.FuncprocbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcprocbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.funcproccallbody()
            self.state = 96
            self.match(LoseParser.T__2)
            self.state = 97
            self.nondefprog()
            self.state = 98
            self.match(LoseParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclareContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.DeclareContext, self).__init__(parent, invokingState)
            self.parser = parser

        def natdecl(self):
            return self.getTypedRuleContext(LoseParser.NatdeclContext,0)


        def signdecl(self):
            return self.getTypedRuleContext(LoseParser.SigndeclContext,0)


        def listdecl(self):
            return self.getTypedRuleContext(LoseParser.ListdeclContext,0)


        def list2decl(self):
            return self.getTypedRuleContext(LoseParser.List2declContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_declare

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterDeclare(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitDeclare(self)




    def declare(self):

        localctx = LoseParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            token = self._input.LA(1)
            if token in [LoseParser.T__4]:
                self.state = 100
                self.natdecl()

            elif token in [LoseParser.T__7]:
                self.state = 101
                self.signdecl()

            elif token in [LoseParser.T__8]:
                self.state = 102
                self.listdecl()

            elif token in [LoseParser.T__9]:
                self.state = 103
                self.list2decl()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NatdeclContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.NatdeclContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(LoseParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(LoseParser.ExprContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_natdecl

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterNatdecl(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitNatdecl(self)




    def natdecl(self):

        localctx = LoseParser.NatdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_natdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(LoseParser.T__4)
            self.state = 107
            self.match(LoseParser.VAR)
            self.state = 110
            _la = self._input.LA(1)
            if _la==LoseParser.T__5:
                self.state = 108
                self.match(LoseParser.T__5)
                self.state = 109
                self.expr(0)


            self.state = 112
            self.match(LoseParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SigndeclContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.SigndeclContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(LoseParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(LoseParser.ExprContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_signdecl

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterSigndecl(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitSigndecl(self)




    def signdecl(self):

        localctx = LoseParser.SigndeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_signdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(LoseParser.T__7)
            self.state = 115
            self.match(LoseParser.VAR)
            self.state = 118
            _la = self._input.LA(1)
            if _la==LoseParser.T__5:
                self.state = 116
                self.match(LoseParser.T__5)
                self.state = 117
                self.expr(0)


            self.state = 120
            self.match(LoseParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListdeclContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.ListdeclContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(LoseParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(LoseParser.ExprContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_listdecl

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterListdecl(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitListdecl(self)




    def listdecl(self):

        localctx = LoseParser.ListdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(LoseParser.T__8)
            self.state = 123
            self.match(LoseParser.VAR)
            self.state = 126
            _la = self._input.LA(1)
            if _la==LoseParser.T__5:
                self.state = 124
                self.match(LoseParser.T__5)
                self.state = 125
                self.expr(0)


            self.state = 128
            self.match(LoseParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List2declContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.List2declContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(LoseParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(LoseParser.ExprContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_list2decl

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterList2decl(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitList2decl(self)




    def list2decl(self):

        localctx = LoseParser.List2declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list2decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(LoseParser.T__9)
            self.state = 131
            self.match(LoseParser.VAR)
            self.state = 134
            _la = self._input.LA(1)
            if _la==LoseParser.T__5:
                self.state = 132
                self.match(LoseParser.T__5)
                self.state = 133
                self.expr(0)


            self.state = 136
            self.match(LoseParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncproccallContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.FuncproccallContext, self).__init__(parent, invokingState)
            self.parser = parser

        def funcproccallbody(self):
            return self.getTypedRuleContext(LoseParser.FuncproccallbodyContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_funcproccall

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterFuncproccall(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitFuncproccall(self)




    def funcproccall(self):

        localctx = LoseParser.FuncproccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_funcproccall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.funcproccallbody()
            self.state = 139
            self.match(LoseParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncproccallbodyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.FuncproccallbodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i=None):
            if i is None:
                return self.getTokens(LoseParser.VAR)
            else:
                return self.getToken(LoseParser.VAR, i)

        def getRuleIndex(self):
            return LoseParser.RULE_funcproccallbody

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterFuncproccallbody(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitFuncproccallbody(self)




    def funcproccallbody(self):

        localctx = LoseParser.FuncproccallbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_funcproccallbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(LoseParser.VAR)
            self.state = 142
            self.match(LoseParser.T__10)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 143
                    self.match(LoseParser.VAR)
                    self.state = 144
                    self.match(LoseParser.T__11) 
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 150
            self.match(LoseParser.VAR)
            self.state = 151
            self.match(LoseParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhileloopContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.WhileloopContext, self).__init__(parent, invokingState)
            self.parser = parser

        def whileexpr(self):
            return self.getTypedRuleContext(LoseParser.WhileexprContext,0)


        def whilenondefprog(self):
            return self.getTypedRuleContext(LoseParser.WhilenondefprogContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_whileloop

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterWhileloop(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitWhileloop(self)




    def whileloop(self):

        localctx = LoseParser.WhileloopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_whileloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(LoseParser.T__13)
            self.state = 154
            self.match(LoseParser.T__10)
            self.state = 155
            self.whileexpr()
            self.state = 156
            self.match(LoseParser.T__12)
            self.state = 157
            self.match(LoseParser.T__2)
            self.state = 158
            self.whilenondefprog()
            self.state = 159
            self.match(LoseParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForloopContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.ForloopContext, self).__init__(parent, invokingState)
            self.parser = parser

        def nondefcommand(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LoseParser.NondefcommandContext)
            else:
                return self.getTypedRuleContext(LoseParser.NondefcommandContext,i)


        def expr(self):
            return self.getTypedRuleContext(LoseParser.ExprContext,0)


        def nondefprog(self):
            return self.getTypedRuleContext(LoseParser.NondefprogContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_forloop

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterForloop(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitForloop(self)




    def forloop(self):

        localctx = LoseParser.ForloopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_forloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(LoseParser.T__14)
            self.state = 162
            self.match(LoseParser.T__10)
            self.state = 163
            self.nondefcommand()
            self.state = 164
            self.match(LoseParser.T__6)
            self.state = 165
            self.expr(0)
            self.state = 166
            self.match(LoseParser.T__6)
            self.state = 167
            self.nondefcommand()
            self.state = 168
            self.match(LoseParser.T__12)
            self.state = 169
            self.match(LoseParser.T__2)
            self.state = 170
            self.nondefprog()
            self.state = 171
            self.match(LoseParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfstateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.IfstateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ifexpr(self):
            return self.getTypedRuleContext(LoseParser.IfexprContext,0)


        def ifnondefprog(self):
            return self.getTypedRuleContext(LoseParser.IfnondefprogContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_ifstate

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterIfstate(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitIfstate(self)




    def ifstate(self):

        localctx = LoseParser.IfstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_ifstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(LoseParser.T__15)
            self.state = 174
            self.match(LoseParser.T__10)
            self.state = 175
            self.ifexpr()
            self.state = 176
            self.match(LoseParser.T__12)
            self.state = 177
            self.match(LoseParser.T__2)
            self.state = 178
            self.ifnondefprog()
            self.state = 179
            self.match(LoseParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfelsestateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.IfelsestateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ifelseexpr(self):
            return self.getTypedRuleContext(LoseParser.IfelseexprContext,0)


        def ifelsenondefprog(self):
            return self.getTypedRuleContext(LoseParser.IfelsenondefprogContext,0)


        def elsenondefprog(self):
            return self.getTypedRuleContext(LoseParser.ElsenondefprogContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_ifelsestate

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterIfelsestate(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitIfelsestate(self)




    def ifelsestate(self):

        localctx = LoseParser.IfelsestateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ifelsestate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(LoseParser.T__16)
            self.state = 182
            self.match(LoseParser.T__10)
            self.state = 183
            self.ifelseexpr()
            self.state = 184
            self.match(LoseParser.T__12)
            self.state = 185
            self.match(LoseParser.T__2)
            self.state = 186
            self.ifelsenondefprog()
            self.state = 187
            self.match(LoseParser.T__3)
            self.state = 188
            self.match(LoseParser.T__2)
            self.state = 189
            self.elsenondefprog()
            self.state = 190
            self.match(LoseParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfelsenondefprogContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.IfelsenondefprogContext, self).__init__(parent, invokingState)
            self.parser = parser

        def nondefprog(self):
            return self.getTypedRuleContext(LoseParser.NondefprogContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_ifelsenondefprog

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterIfelsenondefprog(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitIfelsenondefprog(self)




    def ifelsenondefprog(self):

        localctx = LoseParser.IfelsenondefprogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ifelsenondefprog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.nondefprog()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElsenondefprogContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.ElsenondefprogContext, self).__init__(parent, invokingState)
            self.parser = parser

        def nondefprog(self):
            return self.getTypedRuleContext(LoseParser.NondefprogContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_elsenondefprog

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterElsenondefprog(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitElsenondefprog(self)




    def elsenondefprog(self):

        localctx = LoseParser.ElsenondefprogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_elsenondefprog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.nondefprog()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfnondefprogContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.IfnondefprogContext, self).__init__(parent, invokingState)
            self.parser = parser

        def nondefprog(self):
            return self.getTypedRuleContext(LoseParser.NondefprogContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_ifnondefprog

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterIfnondefprog(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitIfnondefprog(self)




    def ifnondefprog(self):

        localctx = LoseParser.IfnondefprogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_ifnondefprog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.nondefprog()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhilenondefprogContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.WhilenondefprogContext, self).__init__(parent, invokingState)
            self.parser = parser

        def nondefprog(self):
            return self.getTypedRuleContext(LoseParser.NondefprogContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_whilenondefprog

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterWhilenondefprog(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitWhilenondefprog(self)




    def whilenondefprog(self):

        localctx = LoseParser.WhilenondefprogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_whilenondefprog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.nondefprog()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfelseexprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.IfelseexprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LoseParser.ExprContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_ifelseexpr

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterIfelseexpr(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitIfelseexpr(self)




    def ifelseexpr(self):

        localctx = LoseParser.IfelseexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ifelseexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfexprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.IfexprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LoseParser.ExprContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_ifexpr

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterIfexpr(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitIfexpr(self)




    def ifexpr(self):

        localctx = LoseParser.IfexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_ifexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhileexprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.WhileexprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LoseParser.ExprContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_whileexpr

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterWhileexpr(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitWhileexpr(self)




    def whileexpr(self):

        localctx = LoseParser.WhileexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_whileexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.AssignContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(LoseParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(LoseParser.ExprContext,0)


        def getRuleIndex(self):
            return LoseParser.RULE_assign

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterAssign(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitAssign(self)




    def assign(self):

        localctx = LoseParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(LoseParser.VAR)
            self.state = 207
            self.match(LoseParser.T__5)
            self.state = 208
            self.expr(0)
            self.state = 209
            self.match(LoseParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnstateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.ReturnstateContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LoseParser.RULE_returnstate

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterReturnstate(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitReturnstate(self)




    def returnstate(self):

        localctx = LoseParser.ReturnstateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_returnstate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            _la = self._input.LA(1)
            if not(_la==LoseParser.T__17 or _la==LoseParser.T__18):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 212
            self.match(LoseParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LoseParser.INT, 0)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LoseParser.ExprContext)
            else:
                return self.getTypedRuleContext(LoseParser.ExprContext,i)


        def VAR(self):
            return self.getToken(LoseParser.VAR, 0)

        def OPERATOR_MUL_DIV(self):
            return self.getToken(LoseParser.OPERATOR_MUL_DIV, 0)

        def OPERATOR_ADD_SUB(self):
            return self.getToken(LoseParser.OPERATOR_ADD_SUB, 0)

        def OPERATOR_COMPARE(self):
            return self.getToken(LoseParser.OPERATOR_COMPARE, 0)

        def getRuleIndex(self):
            return LoseParser.RULE_expr

        def enterRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.enterExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, LoseListener ):
                listener.exitExpr(self)



    def expr(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LoseParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            token = self._input.LA(1)
            if token in [LoseParser.INT]:
                self.state = 215
                self.match(LoseParser.INT)

            elif token in [LoseParser.T__10]:
                self.state = 216
                self.match(LoseParser.T__10)
                self.state = 217
                self.expr(0)
                self.state = 218
                self.match(LoseParser.T__12)

            elif token in [LoseParser.VAR]:
                self.state = 220
                self.match(LoseParser.VAR)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 232
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = LoseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 223
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 224
                        self.match(LoseParser.OPERATOR_MUL_DIV)
                        self.state = 225
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = LoseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 226
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 227
                        self.match(LoseParser.OPERATOR_ADD_SUB)
                        self.state = 228
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = LoseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 229
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 230
                        self.match(LoseParser.OPERATOR_COMPARE)
                        self.state = 231
                        self.expr(5)
                        pass

             
                self.state = 236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[28] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         



