from VarsAmbient import *

class StatusBar(wx.Panel):

    COLOR_RED = "red"
    COLOR_BLACK = "black"
    COLOR_WHITE = "white"
    COLOR_BLUE = "blue"

    def __init__(self, parent):

        self.parent = parent
        wx.Panel.__init__(self, parent=parent,id=wx.ID_ANY)
        self.statusSizer = wx.BoxSizer(wx.VERTICAL)
        self.txtStatusBar = wx.StaticText(self,wx.ID_ANY," ")
        self.statusSizer.Add(self.txtStatusBar, 0, wx.ALIGN_LEFT | wx.EXPAND, 5)
        self.statusColor = StatusBar.COLOR_BLACK
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.txtStatusBar.SetFont(font)

        self.statusSizer.Layout()
        self.SetSizer(self.statusSizer)

    def SetStatusText(self, text):

        self.txtStatusBar.SetLabelText(text)
        self.txtStatusBar.SetForegroundColour(self.statusColor)

    def SetColor(self, color):

        self.statusColor = color

    def GetColor(self):

        return self.statusColor