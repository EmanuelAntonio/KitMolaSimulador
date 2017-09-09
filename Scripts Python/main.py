from BaseGui import *
import sys

start = True

while Vars.reset:
    Vars.dirExec = sys.argv[0]
    if Vars.dirExec.endswith('main.py'):
        Vars.dirExec = Vars.dirExec[:-7]
        Vars.__init__()
        app = wx.App()
        Vars.reset = False
        if start:
            if len(sys.argv) >= 2:
                if sys.argv[1].endswith(".kmp"):
                    Vars.openFile = sys.argv[1]
            start = False
        else:
            Vars.openFile = False
        WindowClass(None)
        app.MainLoop()
        del app
    else:
        break
