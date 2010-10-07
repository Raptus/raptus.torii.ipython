import sys
from raptus.torii.interpreter import AbstractInterpreter
from IPython.ipmaker import make_IPython
from IPython.ultraTB import AutoFormattedTB as BaseAutoFormattedTB
from IPython.iplib import SyntaxTB as BaseSyntaxTB
from pprint import PrettyPrinter
import StringIO



def result_display(self, arg):
    self.outStringIO = StringIO.StringIO()
    if self.rc.pprint:
        out =  PrettyPrinter().pformat(arg)
        if '\n' in out:
            self.outStringIO.write('\n')
        print >> self.outStringIO, out
    else:
        print >> self.outStringIO, repr(arg)
    return None 

class AutoFormattedTB(BaseAutoFormattedTB):
    def __call__(self, *args, **kw):
        self.errStringIO = StringIO.StringIO()
        kw.update(dict(out=self.errStringIO))
        return BaseAutoFormattedTB.__call__(self, *args, **kw)

class SyntaxTB(BaseSyntaxTB):
    def __call__(self, etype, value, elist):
        self.errStringIO = StringIO.StringIO()
        self.last_syntax_error = value
        print >> self.errStringIO, self.text(etype,value,elist)


class IPython(AbstractInterpreter):
    
    def __init__(self, locals):
        self.locals = locals
        self.interpreter = make_IPython(argv=[],embedded=True,user_global_ns=self.locals)
        self.interpreter.set_hook('result_display',result_display)
        color = self.interpreter.rc.colors
        self.interpreter.InteractiveTB = AutoFormattedTB(mode = 'Plain',
                                                         color_scheme=color,
                                                         tb_offset = 1)
        self.interpreter.SyntaxTB = SyntaxTB(color_scheme=color)
        
    def getReadline(self):
        return self.interpreter.readline
    
    def getPrompt1(self):
        return sys.displayhook.prompt1
    
    def getPrompt2(self):
        return sys.displayhook.prompt2

    def resetStream(self):
        self.interpreter.outStringIO = StringIO.StringIO()
        self.interpreter.InteractiveTB.errStringIO = StringIO.StringIO()
        self.interpreter.SyntaxTB.errStringIO = StringIO.StringIO()

    def push(self, line):
        self.interpreter.push(line)
    
    def runcode(self, code):
        self.interpreter.runcode(code)
        
    def complete(self, text):
        return self.interpreter.complete(text)
        
    def getStdout(self):
        return self.interpreter.outStringIO
    
    def getErrorStream(self):
        return self.interpreter.InteractiveTB.errStringIO
    
    def getSyntaxErrorStream(self):
        return self.interpreter.SyntaxTB.errStringIO
    
    
    
        