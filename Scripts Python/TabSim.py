from VarsAmbient import *

"""
    ->Classe TabPanel:
        Classe utilizada para instânciar uma das abas, será substituida futuramente por classes específicas para cada aba.

"""
class TabSim(wx.lib.scrolledpanel.ScrolledPanel):
    """
    This will be the first notebook tab
    """

    # ----------------------------------------------------------------------
    def __init__(self, parent):


        self.parent = parent

        wx.lib.scrolledpanel.ScrolledPanel.__init__(self, parent=parent,size = (10,-1), id=wx.ID_ANY)#,style=wx.DOUBLE_BORDER)
        self.SetScrollbar(wx.VERTICAL, 0, 0, 2, 0)
        self.SetupScrolling(scroll_x=False)

        self.sizerSim = wx.BoxSizer(wx.VERTICAL)

        self.lblOp = wx.StaticText(self, wx.ID_ANY, "Opções de Simulação:")

        self.sizerSim.Add(self.lblOp, 0, wx.ALIGN_CENTRE, 5)
        self.sizerSim.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizerSim.Add(self.createAddForcas(), 0, wx.ALIGN_CENTRE, 5)

        if Vars.thema == "dark":
            self.themaDark()

        self.SetSizer(self.sizerSim)


    def themaDark(self):

        self.lblOp.SetForegroundColour("white")
        self.lblOp.SetBackgroundColour(Vars.corThema)

        self.lblFor.SetForegroundColour("white")
        self.lblFor.SetBackgroundColour(Vars.corThema)

        self.lblX.SetForegroundColour("white")
        self.lblX.SetBackgroundColour(Vars.corThema)

        self.lblY.SetForegroundColour("white")
        self.lblY.SetBackgroundColour(Vars.corThema)

        self.lblZ.SetForegroundColour("white")
        self.lblZ.SetBackgroundColour(Vars.corThema)

        self.lblNX.SetForegroundColour("white")
        self.lblNX.SetBackgroundColour(Vars.corThema)

        self.lblNY.SetForegroundColour("white")
        self.lblNY.SetBackgroundColour(Vars.corThema)

        self.lblNZ.SetForegroundColour("white")
        self.lblNZ.SetBackgroundColour(Vars.corThema)

    def createAddForcas(self):

        self.sizerForca = wx.BoxSizer(wx.VERTICAL)

        self.lblFor = wx.StaticText(self, wx.ID_ANY, "\nManipulação de Forças: ")

        self.sizerX = wx.BoxSizer(wx.HORIZONTAL)
        self.sizerY = wx.BoxSizer(wx.HORIZONTAL)
        self.sizerZ = wx.BoxSizer(wx.HORIZONTAL)

        self.lblX = wx.StaticText(self, wx.ID_ANY, "X = ")
        self.txtX = wx.TextCtrl(self, wx.ID_ANY, "0", style=wx.TE_PROCESS_ENTER)
        self.lblNX = wx.StaticText(self, wx.ID_ANY, "N")
        self.sizerX.Add(self.lblX, 0, wx.ALIGN_CENTRE, 5)
        self.sizerX.Add(self.txtX, 0, wx.ALIGN_CENTRE, 5)
        self.sizerX.Add(self.lblNX, 0, wx.ALIGN_CENTRE, 5)

        self.lblY = wx.StaticText(self, wx.ID_ANY, "Y = ")
        self.txtY = wx.TextCtrl(self, wx.ID_ANY, "0", style=wx.TE_PROCESS_ENTER)
        self.lblNY = wx.StaticText(self, wx.ID_ANY, "N")
        self.sizerY.Add(self.lblY, 0, wx.ALIGN_CENTRE, 5)
        self.sizerY.Add(self.txtY, 0, wx.ALIGN_CENTRE, 5)
        self.sizerY.Add(self.lblNY, 0, wx.ALIGN_CENTRE, 5)


        self.lblZ = wx.StaticText(self, wx.ID_ANY, "Z = ")
        self.txtZ = wx.TextCtrl(self, wx.ID_ANY, "0", style=wx.TE_PROCESS_ENTER)
        self.lblNZ = wx.StaticText(self, wx.ID_ANY, "N")
        self.sizerZ.Add(self.lblZ, 0, wx.ALIGN_CENTRE, 5)
        self.sizerZ.Add(self.txtZ, 0, wx.ALIGN_CENTRE, 5)
        self.sizerZ.Add(self.lblNZ, 0, wx.ALIGN_CENTRE, 5)

        self.btnAddForca = wx.Button(self, wx.ID_ANY, "Adicionar Força")

        self.sizerForca.Add(self.lblFor, 0, wx.ALIGN_CENTRE, 5)
        self.sizerForca.Add(self.sizerX, 0, wx.ALIGN_CENTRE, 5)
        self.sizerForca.Add(self.sizerY, 0, wx.ALIGN_CENTRE, 5)
        self.sizerForca.Add(self.sizerZ, 0, wx.ALIGN_CENTRE, 5)
        self.sizerForca.Add(self.btnAddForca, 0, wx.ALIGN_CENTRE, 5)

        self.Bind(wx.EVT_BUTTON, self.OnAddForca, self.btnAddForca)

        return self.sizerForca

    def OnAlteraTmp(self, e):

        Vars.KitSim.setTempoTotal(c_float(float(self.txtTmp.GetValue())))
        self.parent.SetFocus()

    def OnAddForca(self,e):

        self.parent.SetFocus()
        self.parent.parent.botaoSelecionado = Vars.ADDFORCA_SELECIONADO