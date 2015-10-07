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
        buf.write(u"\32\u00d0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\3\2\7\2\64\n\2\f\2\16\2\67\13\2\3")
        buf.write(u"\3\3\3\3\3\3\3\5\3=\n\3\3\4\7\4@\n\4\f\4\16\4C\13\4\3")
        buf.write(u"\5\3\5\3\5\3\5\3\5\3\5\5\5K\n\5\3\6\3\6\3\6\3\7\3\7\3")
        buf.write(u"\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\\\n\t\3\n")
        buf.write(u"\3\n\3\n\3\n\5\nb\n\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13")
        buf.write(u"j\n\13\3\13\3\13\3\f\3\f\3\f\3\f\5\fr\n\f\3\f\3\f\3\r")
        buf.write(u"\3\r\3\r\3\r\5\rz\n\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17")
        buf.write(u"\3\17\3\17\7\17\u0085\n\17\f\17\16\17\u0088\13\17\3\17")
        buf.write(u"\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write(u"\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3")
        buf.write(u"\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write(u"\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write(u"\31\5\31\u00c0\n\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write(u"\3\31\3\31\7\31\u00cb\n\31\f\31\16\31\u00ce\13\31\3\31")
        buf.write(u"\2\3\60\32\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write(u"$&(*,.\60\2\3\3\2\23\24\u00ce\2\65\3\2\2\2\4<\3\2\2\2")
        buf.write(u"\6A\3\2\2\2\bJ\3\2\2\2\nL\3\2\2\2\fO\3\2\2\2\16R\3\2")
        buf.write(u"\2\2\20[\3\2\2\2\22]\3\2\2\2\24e\3\2\2\2\26m\3\2\2\2")
        buf.write(u"\30u\3\2\2\2\32}\3\2\2\2\34\u0080\3\2\2\2\36\u008c\3")
        buf.write(u"\2\2\2 \u0094\3\2\2\2\"\u00a0\3\2\2\2$\u00a8\3\2\2\2")
        buf.write(u"&\u00aa\3\2\2\2(\u00ac\3\2\2\2*\u00ae\3\2\2\2,\u00b0")
        buf.write(u"\3\2\2\2.\u00b5\3\2\2\2\60\u00bf\3\2\2\2\62\64\5\4\3")
        buf.write(u"\2\63\62\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66\3")
        buf.write(u"\2\2\2\66\3\3\2\2\2\67\65\3\2\2\28=\5\n\6\29=\5\f\7\2")
        buf.write(u":=\5\20\t\2;=\5\b\5\2<8\3\2\2\2<9\3\2\2\2<:\3\2\2\2<")
        buf.write(u";\3\2\2\2=\5\3\2\2\2>@\5\b\5\2?>\3\2\2\2@C\3\2\2\2A?")
        buf.write(u"\3\2\2\2AB\3\2\2\2B\7\3\2\2\2CA\3\2\2\2DK\5\32\16\2E")
        buf.write(u"K\5\36\20\2FK\5 \21\2GK\5\"\22\2HK\5,\27\2IK\5.\30\2")
        buf.write(u"JD\3\2\2\2JE\3\2\2\2JF\3\2\2\2JG\3\2\2\2JH\3\2\2\2JI")
        buf.write(u"\3\2\2\2K\t\3\2\2\2LM\7\3\2\2MN\5\16\b\2N\13\3\2\2\2")
        buf.write(u"OP\7\4\2\2PQ\5\16\b\2Q\r\3\2\2\2RS\5\34\17\2ST\7\5\2")
        buf.write(u"\2TU\5\6\4\2UV\7\6\2\2V\17\3\2\2\2W\\\5\22\n\2X\\\5\24")
        buf.write(u"\13\2Y\\\5\26\f\2Z\\\5\30\r\2[W\3\2\2\2[X\3\2\2\2[Y\3")
        buf.write(u"\2\2\2[Z\3\2\2\2\\\21\3\2\2\2]^\7\7\2\2^a\7\31\2\2_`")
        buf.write(u"\7\b\2\2`b\5\60\31\2a_\3\2\2\2ab\3\2\2\2bc\3\2\2\2cd")
        buf.write(u"\7\t\2\2d\23\3\2\2\2ef\7\n\2\2fi\7\31\2\2gh\7\b\2\2h")
        buf.write(u"j\5\60\31\2ig\3\2\2\2ij\3\2\2\2jk\3\2\2\2kl\7\t\2\2l")
        buf.write(u"\25\3\2\2\2mn\7\13\2\2nq\7\31\2\2op\7\b\2\2pr\5\60\31")
        buf.write(u"\2qo\3\2\2\2qr\3\2\2\2rs\3\2\2\2st\7\t\2\2t\27\3\2\2")
        buf.write(u"\2uv\7\f\2\2vy\7\31\2\2wx\7\b\2\2xz\5\60\31\2yw\3\2\2")
        buf.write(u"\2yz\3\2\2\2z{\3\2\2\2{|\7\t\2\2|\31\3\2\2\2}~\5\34\17")
        buf.write(u"\2~\177\7\t\2\2\177\33\3\2\2\2\u0080\u0081\7\31\2\2\u0081")
        buf.write(u"\u0086\7\r\2\2\u0082\u0083\7\31\2\2\u0083\u0085\7\16")
        buf.write(u"\2\2\u0084\u0082\3\2\2\2\u0085\u0088\3\2\2\2\u0086\u0084")
        buf.write(u"\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0089\3\2\2\2\u0088")
        buf.write(u"\u0086\3\2\2\2\u0089\u008a\7\31\2\2\u008a\u008b\7\17")
        buf.write(u"\2\2\u008b\35\3\2\2\2\u008c\u008d\7\20\2\2\u008d\u008e")
        buf.write(u"\7\r\2\2\u008e\u008f\5*\26\2\u008f\u0090\7\17\2\2\u0090")
        buf.write(u"\u0091\7\5\2\2\u0091\u0092\5&\24\2\u0092\u0093\7\6\2")
        buf.write(u"\2\u0093\37\3\2\2\2\u0094\u0095\7\21\2\2\u0095\u0096")
        buf.write(u"\7\r\2\2\u0096\u0097\5\b\5\2\u0097\u0098\7\t\2\2\u0098")
        buf.write(u"\u0099\5\60\31\2\u0099\u009a\7\t\2\2\u009a\u009b\5\b")
        buf.write(u"\5\2\u009b\u009c\7\17\2\2\u009c\u009d\7\5\2\2\u009d\u009e")
        buf.write(u"\5\6\4\2\u009e\u009f\7\6\2\2\u009f!\3\2\2\2\u00a0\u00a1")
        buf.write(u"\7\22\2\2\u00a1\u00a2\7\r\2\2\u00a2\u00a3\5(\25\2\u00a3")
        buf.write(u"\u00a4\7\17\2\2\u00a4\u00a5\7\5\2\2\u00a5\u00a6\5$\23")
        buf.write(u"\2\u00a6\u00a7\7\6\2\2\u00a7#\3\2\2\2\u00a8\u00a9\5\6")
        buf.write(u"\4\2\u00a9%\3\2\2\2\u00aa\u00ab\5\6\4\2\u00ab\'\3\2\2")
        buf.write(u"\2\u00ac\u00ad\5\60\31\2\u00ad)\3\2\2\2\u00ae\u00af\5")
        buf.write(u"\60\31\2\u00af+\3\2\2\2\u00b0\u00b1\7\31\2\2\u00b1\u00b2")
        buf.write(u"\7\b\2\2\u00b2\u00b3\5\60\31\2\u00b3\u00b4\7\t\2\2\u00b4")
        buf.write(u"-\3\2\2\2\u00b5\u00b6\t\2\2\2\u00b6\u00b7\7\t\2\2\u00b7")
        buf.write(u"/\3\2\2\2\u00b8\u00b9\b\31\1\2\u00b9\u00c0\7\32\2\2\u00ba")
        buf.write(u"\u00bb\7\r\2\2\u00bb\u00bc\5\60\31\2\u00bc\u00bd\7\17")
        buf.write(u"\2\2\u00bd\u00c0\3\2\2\2\u00be\u00c0\7\31\2\2\u00bf\u00b8")
        buf.write(u"\3\2\2\2\u00bf\u00ba\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0")
        buf.write(u"\u00cc\3\2\2\2\u00c1\u00c2\f\b\2\2\u00c2\u00c3\7\25\2")
        buf.write(u"\2\u00c3\u00cb\5\60\31\t\u00c4\u00c5\f\7\2\2\u00c5\u00c6")
        buf.write(u"\7\26\2\2\u00c6\u00cb\5\60\31\b\u00c7\u00c8\f\6\2\2\u00c8")
        buf.write(u"\u00c9\7\27\2\2\u00c9\u00cb\5\60\31\7\u00ca\u00c1\3\2")
        buf.write(u"\2\2\u00ca\u00c4\3\2\2\2\u00ca\u00c7\3\2\2\2\u00cb\u00ce")
        buf.write(u"\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd")
        buf.write(u"\61\3\2\2\2\u00ce\u00cc\3\2\2\2\17\65<AJ[aiqy\u0086\u00bf")
        buf.write(u"\u00ca\u00cc")
        return buf.getvalue()


class LoseParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'func'", u"'proc'", u"'{'", u"'}'", 
                     u"'nat'", u"'='", u"';'", u"'signed'", u"'list'", u"'list2'", 
                     u"'('", u"','", u"')'", u"'while'", u"'for'", u"'if'", 
                     u"'return'", u"'halt'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"OPERATOR_MUL_DIV", 
                      u"OPERATOR_ADD_SUB", u"OPERATOR_COMPARE", u"WS", u"VAR", 
                      u"INT" ]

    RULE_prog = 0
    RULE_command = 1
    RULE_nondefprog = 2
    RULE_nondefcommand = 3
    RULE_funcdef = 4
    RULE_procdef = 5
    RULE_funcprocbody = 6
    RULE_declare = 7
    RULE_natdecl = 8
    RULE_signdecl = 9
    RULE_listdecl = 10
    RULE_list2decl = 11
    RULE_funcproccall = 12
    RULE_funcproccallbody = 13
    RULE_whileloop = 14
    RULE_forloop = 15
    RULE_ifstate = 16
    RULE_ifnondefprog = 17
    RULE_whilenondefprog = 18
    RULE_ifexpr = 19
    RULE_whileexpr = 20
    RULE_assign = 21
    RULE_returnstate = 22
    RULE_expr = 23

    ruleNames =  [ u"prog", u"command", u"nondefprog", u"nondefcommand", 
                   u"funcdef", u"procdef", u"funcprocbody", u"declare", 
                   u"natdecl", u"signdecl", u"listdecl", u"list2decl", u"funcproccall", 
                   u"funcproccallbody", u"whileloop", u"forloop", u"ifstate", 
                   u"ifnondefprog", u"whilenondefprog", u"ifexpr", u"whileexpr", 
                   u"assign", u"returnstate", u"expr" ]

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
    OPERATOR_MUL_DIV=19
    OPERATOR_ADD_SUB=20
    OPERATOR_COMPARE=21
    WS=22
    VAR=23
    INT=24

    def __init__(self, input):
        super(LoseParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LoseParser.ProgContext, self).__init__(parent, invokingState)
            self.parser = parser

        def command(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LoseParser.CommandContext)
            else:
                return self.getTypedRuleContext(LoseParser.CommandContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LoseParser.T__0) | (1 << LoseParser.T__1) | (1 << LoseParser.T__4) | (1 << LoseParser.T__7) | (1 << LoseParser.T__8) | (1 << LoseParser.T__9) | (1 << LoseParser.T__13) | (1 << LoseParser.T__14) | (1 << LoseParser.T__15) | (1 << LoseParser.T__16) | (1 << LoseParser.T__17) | (1 << LoseParser.VAR))) != 0):
                self.state = 48
                self.command()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            token = self._input.LA(1)
            if token in [LoseParser.T__0]:
                self.state = 54
                self.funcdef()

            elif token in [LoseParser.T__1]:
                self.state = 55
                self.procdef()

            elif token in [LoseParser.T__4, LoseParser.T__7, LoseParser.T__8, LoseParser.T__9]:
                self.state = 56
                self.declare()

            elif token in [LoseParser.T__13, LoseParser.T__14, LoseParser.T__15, LoseParser.T__16, LoseParser.T__17, LoseParser.VAR]:
                self.state = 57
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
        self.enterRule(localctx, 4, self.RULE_nondefprog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LoseParser.T__13) | (1 << LoseParser.T__14) | (1 << LoseParser.T__15) | (1 << LoseParser.T__16) | (1 << LoseParser.T__17) | (1 << LoseParser.VAR))) != 0):
                self.state = 60
                self.nondefcommand()
                self.state = 65
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
        self.enterRule(localctx, 6, self.RULE_nondefcommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 66
                self.funcproccall()
                pass

            elif la_ == 2:
                self.state = 67
                self.whileloop()
                pass

            elif la_ == 3:
                self.state = 68
                self.forloop()
                pass

            elif la_ == 4:
                self.state = 69
                self.ifstate()
                pass

            elif la_ == 5:
                self.state = 70
                self.assign()
                pass

            elif la_ == 6:
                self.state = 71
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
        self.enterRule(localctx, 8, self.RULE_funcdef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(LoseParser.T__0)
            self.state = 75
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
        self.enterRule(localctx, 10, self.RULE_procdef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(LoseParser.T__1)
            self.state = 78
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
        self.enterRule(localctx, 12, self.RULE_funcprocbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.funcproccallbody()
            self.state = 81
            self.match(LoseParser.T__2)
            self.state = 82
            self.nondefprog()
            self.state = 83
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
        self.enterRule(localctx, 14, self.RULE_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            token = self._input.LA(1)
            if token in [LoseParser.T__4]:
                self.state = 85
                self.natdecl()

            elif token in [LoseParser.T__7]:
                self.state = 86
                self.signdecl()

            elif token in [LoseParser.T__8]:
                self.state = 87
                self.listdecl()

            elif token in [LoseParser.T__9]:
                self.state = 88
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
        self.enterRule(localctx, 16, self.RULE_natdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(LoseParser.T__4)
            self.state = 92
            self.match(LoseParser.VAR)
            self.state = 95
            _la = self._input.LA(1)
            if _la==LoseParser.T__5:
                self.state = 93
                self.match(LoseParser.T__5)
                self.state = 94
                self.expr(0)


            self.state = 97
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
        self.enterRule(localctx, 18, self.RULE_signdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(LoseParser.T__7)
            self.state = 100
            self.match(LoseParser.VAR)
            self.state = 103
            _la = self._input.LA(1)
            if _la==LoseParser.T__5:
                self.state = 101
                self.match(LoseParser.T__5)
                self.state = 102
                self.expr(0)


            self.state = 105
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
        self.enterRule(localctx, 20, self.RULE_listdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(LoseParser.T__8)
            self.state = 108
            self.match(LoseParser.VAR)
            self.state = 111
            _la = self._input.LA(1)
            if _la==LoseParser.T__5:
                self.state = 109
                self.match(LoseParser.T__5)
                self.state = 110
                self.expr(0)


            self.state = 113
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
        self.enterRule(localctx, 22, self.RULE_list2decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(LoseParser.T__9)
            self.state = 116
            self.match(LoseParser.VAR)
            self.state = 119
            _la = self._input.LA(1)
            if _la==LoseParser.T__5:
                self.state = 117
                self.match(LoseParser.T__5)
                self.state = 118
                self.expr(0)


            self.state = 121
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
        self.enterRule(localctx, 24, self.RULE_funcproccall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.funcproccallbody()
            self.state = 124
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
        self.enterRule(localctx, 26, self.RULE_funcproccallbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(LoseParser.VAR)
            self.state = 127
            self.match(LoseParser.T__10)
            self.state = 132
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 128
                    self.match(LoseParser.VAR)
                    self.state = 129
                    self.match(LoseParser.T__11) 
                self.state = 134
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 135
            self.match(LoseParser.VAR)
            self.state = 136
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
        self.enterRule(localctx, 28, self.RULE_whileloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(LoseParser.T__13)
            self.state = 139
            self.match(LoseParser.T__10)
            self.state = 140
            self.whileexpr()
            self.state = 141
            self.match(LoseParser.T__12)
            self.state = 142
            self.match(LoseParser.T__2)
            self.state = 143
            self.whilenondefprog()
            self.state = 144
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
        self.enterRule(localctx, 30, self.RULE_forloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(LoseParser.T__14)
            self.state = 147
            self.match(LoseParser.T__10)
            self.state = 148
            self.nondefcommand()
            self.state = 149
            self.match(LoseParser.T__6)
            self.state = 150
            self.expr(0)
            self.state = 151
            self.match(LoseParser.T__6)
            self.state = 152
            self.nondefcommand()
            self.state = 153
            self.match(LoseParser.T__12)
            self.state = 154
            self.match(LoseParser.T__2)
            self.state = 155
            self.nondefprog()
            self.state = 156
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
        self.enterRule(localctx, 32, self.RULE_ifstate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(LoseParser.T__15)
            self.state = 159
            self.match(LoseParser.T__10)
            self.state = 160
            self.ifexpr()
            self.state = 161
            self.match(LoseParser.T__12)
            self.state = 162
            self.match(LoseParser.T__2)
            self.state = 163
            self.ifnondefprog()
            self.state = 164
            self.match(LoseParser.T__3)
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
        self.enterRule(localctx, 34, self.RULE_ifnondefprog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
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
        self.enterRule(localctx, 36, self.RULE_whilenondefprog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.nondefprog()
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
        self.enterRule(localctx, 38, self.RULE_ifexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
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
        self.enterRule(localctx, 40, self.RULE_whileexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
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
        self.enterRule(localctx, 42, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(LoseParser.VAR)
            self.state = 175
            self.match(LoseParser.T__5)
            self.state = 176
            self.expr(0)
            self.state = 177
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
        self.enterRule(localctx, 44, self.RULE_returnstate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            _la = self._input.LA(1)
            if not(_la==LoseParser.T__16 or _la==LoseParser.T__17):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 180
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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            token = self._input.LA(1)
            if token in [LoseParser.INT]:
                self.state = 183
                self.match(LoseParser.INT)

            elif token in [LoseParser.T__10]:
                self.state = 184
                self.match(LoseParser.T__10)
                self.state = 185
                self.expr(0)
                self.state = 186
                self.match(LoseParser.T__12)

            elif token in [LoseParser.VAR]:
                self.state = 188
                self.match(LoseParser.VAR)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 202
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 200
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = LoseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 191
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 192
                        self.match(LoseParser.OPERATOR_MUL_DIV)
                        self.state = 193
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = LoseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 194
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 195
                        self.match(LoseParser.OPERATOR_ADD_SUB)
                        self.state = 196
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = LoseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 197
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 198
                        self.match(LoseParser.OPERATOR_COMPARE)
                        self.state = 199
                        self.expr(5)
                        pass

             
                self.state = 204
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
        self._predicates[23] = self.expr_sempred
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
         



