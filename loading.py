import consolemod,os,sys
console = consolemod.cursor()
if sys.platform.lower() == "win32":
    os.system('color')
def get_terminal_size(fallback=(80, 24)):
    for i in range(0,3):
        try:
            columns, rows = os.get_terminal_size(i)
        except OSError:
            continue
        break
    else:  # set default if the loop completes which means all failed
        columns, rows = fallback
    return columns, rows
class classicLoading:
    def __str__(self):
        return 'classicLoadingAnimation'
    def _init(self,args):
        self.maintext=args[0]
        self.fillchar=args[1]
        self.fillRHStext=args[2] or ''
        self.length=args[3] or 100
        print(self.maintext,end='',flush=True)
        print(self.fillRHStext,end='',flush=True)
    def _update(self,value):
        print(self.maintext,end='',flush=True)
        for i in range(round(value * self.length)):
            print(self.fillchar,end='',flush=True)
        print(self.fillRHStext,end='',flush=True)
    def __init__(self,*args,**kwargs):
        self.prefix=kwargs or {}
        global console
        console.savepos()
        self._init(args)
    def update(self,value):
        """arg: value (float)"""
        console.restorepos()
        self._update(value)

class fullLineLoading(classicLoading):
    def __str__(self):
        return 'fullLineLoadingAnimation'
    def _init(self,args):
        self.maintext=args[0]
        self.RHStext=args[1] or ''
        self.fg=args[2]
        self.bg=args[3]
        columns, rows = get_terminal_size()
        self.columns = columns
        nonspace = columns - len(self.maintext) - len(self.RHStext)
        self.result=self.maintext
        for i in range(nonspace):
            self.result += ' '
        self.result += self.RHStext
        print(self.result)
        for char in self.result:
            print(self.fg,end=char,flush=True)
    def _update(self,value):
        i = 0
        for char in self.result:
            if i < round(value * self.columns):
                print(self.bg,end=char + consolemod.style.reset(),flush=True)
            else:
                print(self.fg,end=char + consolemod.style.reset(),flush=True)
            i += 1