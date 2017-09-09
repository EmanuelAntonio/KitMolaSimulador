from VarsAmbient import *


class TabTools(wx.lib.scrolledpanel.ScrolledPanel):
    """
    This will be the first notebook tab
    """

    # ----------------------------------------------------------------------
    def __init__(self, parent):

        wx.lib.scrolledpanel.ScrolledPanel.__init__(self, parent=parent, size = (10,-1), id=wx.ID_ANY)#, style=wx.DOUBLE_BORDER)
        self.SetupScrolling(scroll_x=False)

        self.parent = parent
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        sizerDist = wx.BoxSizer(wx.VERTICAL)
        btnDist = wx.Button(self,wx.ID_ANY,"Distância Entre Objetos ")
        self.lblDist = wx.StaticText(self,wx.ID_ANY, "")
        self.Bind(wx.EVT_BUTTON, self.onDist, btnDist)
        sizerDist.Add(btnDist, 0,  wx.ALIGN_CENTRE, 5)
        sizerDist.Add(self.lblDist)
        self.sizer.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizer.Add(sizerDist, 0,  wx.ALIGN_CENTRE, 5)
        self.sizer.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)

        self.SetSizer(self.sizer)

    def onDist(self,e):

        dist = c_float(Vars.KitLib.distObjsSelect()).value

        if dist == -1:
            msg = "Selecione dois objetos para calcular a distância entre eles."
            msgCx = wx.MessageDialog(None, msg, "ERRO!", wx.OK)
            msgCx.ShowModal()
            msgCx.Destroy()
        else:
            self.lblDist.SetLabel(str(round(dist,3)) + ' cm')

        self.parent.SetFocus()