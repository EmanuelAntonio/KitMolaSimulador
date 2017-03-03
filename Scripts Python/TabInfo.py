from VarsAmbient import *

"""
    ->Classe TabPanel:
        Classe utilizada para instânciar uma das abas, será substituida futuramente por classes específicas para cada aba.

"""
class TabInfo(wx.lib.scrolledpanel.ScrolledPanel):
    """
    This will be the first notebook tab
    """

    # ----------------------------------------------------------------------
    def __init__(self, parent):


        self.parent = parent

        wx.lib.scrolledpanel.ScrolledPanel.__init__(self, parent=parent,size = (10,-1), id=wx.ID_ANY,style=wx.DOUBLE_BORDER)
        self.SetScrollbar(wx.VERTICAL, 0, 0, 2, 0)
        self.SetupScrolling(scroll_x=False)

        self.idUltObj = 0
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.strId = "\n\nId: "
        self.strCentro = "\n\nCentro: "
        self.strTipo = "\n\nTipo: "
        self.strTam = "\n\nTamanho: "
        self.strRaio = "\n\nRaio: "
        self.lblTipo = wx.StaticText(self, wx.ID_ANY, self.strTipo + "Nenhum Objeto Selecionado")
        self.lblId = wx.StaticText(self, wx.ID_ANY, self.strId + "0")
        self.lblTam = wx.StaticText(self, wx.ID_ANY, self.strTam + "0mm")
        self.lblRaio = wx.StaticText(self, wx.ID_ANY, self.strRaio + "0mm")
        self.lblCentro = wx.StaticText(self, wx.ID_ANY, self.strCentro + "(-,-,-)")

        sizerFocus = wx.BoxSizer(wx.VERTICAL)
        self.sizerX = wx.BoxSizer(wx.HORIZONTAL)
        self.sizerY = wx.BoxSizer(wx.HORIZONTAL)
        self.sizerZ = wx.BoxSizer(wx.HORIZONTAL)
        self.lblX = wx.StaticText(self, wx.ID_ANY, "X: ")
        self.lblX.SetExtraStyle(wx.TE_RIGHT)
        self.lblY = wx.StaticText(self, wx.ID_ANY, "Y: ")
        self.lblY.SetExtraStyle(wx.TE_RIGHT)
        self.lblZ = wx.StaticText(self, wx.ID_ANY, "Z: ")
        self.lblZ.SetExtraStyle(wx.TE_RIGHT)
        self.txtFocusX = wx.TextCtrl(self, wx.ID_ANY, "0", style=wx.TE_PROCESS_ENTER)
        self.txtFocusY = wx.TextCtrl(self, wx.ID_ANY, "0", style=wx.TE_PROCESS_ENTER)
        self.txtFocusZ = wx.TextCtrl(self, wx.ID_ANY, "0", style=wx.TE_PROCESS_ENTER)
        self.lblCmX = wx.StaticText(self, wx.ID_ANY, "cm")
        self.lblCmX.SetExtraStyle(wx.TE_RIGHT)
        self.lblCmY = wx.StaticText(self, wx.ID_ANY, "cm")
        self.lblCmY.SetExtraStyle(wx.TE_RIGHT)
        self.lblCmZ = wx.StaticText(self, wx.ID_ANY, "cm")
        self.lblCmZ.SetExtraStyle(wx.TE_RIGHT)
        #self.btnObj = wx.Button(self, wx.ID_ANY, "Mover Objeto")
        self.btnSelect = wx.Button(self, wx.ID_ANY, "Mover Seleção")
        self.sizerX.Add(self.lblX, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER, 5)
        self.sizerX.Add(self.txtFocusX, 0, wx.ALIGN_RIGHT, 5)
        self.sizerX.Add(self.lblCmX, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER, 5)
        self.sizerY.Add(self.lblY, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER, 5)
        self.sizerY.Add(self.txtFocusY, 0, wx.ALIGN_RIGHT, 5)
        self.sizerY.Add(self.lblCmY, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER, 5)
        self.sizerZ.Add(self.lblZ, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER, 5)
        self.sizerZ.Add(self.txtFocusZ, 0, wx.ALIGN_RIGHT, 5)
        self.sizerZ.Add(self.lblCmZ, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER, 5)
        sizerFocus.Add(self.sizerX, 0, wx.ALIGN_CENTER, 5)
        sizerFocus.Add(self.sizerY, 0, wx.ALIGN_CENTER, 5)
        sizerFocus.Add(self.sizerZ, 0, wx.ALIGN_CENTER, 5)
        #sizerFocus.Add(self.btnObj, 0, wx.ALIGN_CENTER, 5)
        sizerFocus.Add(self.btnSelect, 0, wx.ALIGN_CENTER, 5)
        #self.Bind(wx.EVT_BUTTON, self.OnMoveObj, self.btnObj)
        self.Bind(wx.EVT_BUTTON, self.OnMoveObjSelect, self.btnSelect)

        self.sizer.Add(wx.StaticText(self, wx.ID_ANY,"Informações Sobre Objetos"), 0, wx.ALIGN_CENTRE, 5)
        self.sizer.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizer.Add(self.lblTipo, 0, wx.ALIGN_LEFT, 5)
        self.sizer.Add(self.lblId, 0, wx.ALIGN_LEFT, 5)
        self.sizer.Add(self.lblCentro, 0, wx.ALIGN_LEFT, 5)
        self.sizer.Add(self.lblTam, 0, wx.ALIGN_LEFT, 5)
        self.sizer.Add(self.lblRaio, 0, wx.ALIGN_LEFT, 5)
        self.sizer.Add(wx.StaticText(self, wx.ID_ANY, "\n"), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizer.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizer.Add(wx.StaticText(self, wx.ID_ANY, "Opções:"), 0, wx.ALIGN_CENTER, 5)
        self.sizer.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizer.Add(sizerFocus, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizer.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)

        self.SetSizer(self.sizer)



    def OnMoveObj(self,e):
        if self.idUltObj != 0:
            Vars.KitLib.moveObjSelect(c_int(self.idUltObj), c_float(float(self.txtFocusX.GetValue())),
                                      c_float(float(self.txtFocusY.GetValue())),
                                      c_float(float(self.txtFocusZ.GetValue())))
            Vars.drawArea0.Refresh()
            Vars.drawArea1.Refresh()
            Vars.drawArea2.Refresh()
            Vars.drawArea3.Refresh()
        else:
            msg = "Selecione um objeto primeiro!\n"
            msgCx = wx.MessageDialog(None, msg, "ERRO!", wx.OK)
            msgCx.ShowModal()
            msgCx.Destroy()
        self.parent.SetFocus()


    def OnMoveObjSelect(self,e):
        Vars.KitLib.moveObjSelect(c_float(float(self.txtFocusX.GetValue())),c_float(float(self.txtFocusY.GetValue())),c_float(float(self.txtFocusZ.GetValue())))
        Vars.drawArea0.Refresh()
        Vars.drawArea1.Refresh()
        Vars.drawArea2.Refresh()
        Vars.drawArea3.Refresh()
        self.parent.SetFocus()

    def AlteraLayoutInfo(self, id, obj, centro, extId1, extId2):
        if id == 0:
            self.idUltObj = 0
            self.lblTipo.SetLabel(self.strTipo + "Nenhum Objeto Selecionado")
            self.lblId.SetLabel(self.strId + "---")
            self.lblTam.SetLabel(self.strTam + "---")
            self.lblRaio.SetLabel(self.strRaio + "---")
            self.lblCentro.SetLabel(self.strCentro + "(-,-,-)")
            self.txtFocusX.SetValue(str(0))
            self.txtFocusY.SetValue(str(0))
            self.txtFocusZ.SetValue(str(0))
        else:

            self.idUltObj = id
            if obj == Vars.SPHERE:
                self.lblTipo.SetLabel(self.strTipo + "Esfera de Ligação")
                self.lblRaio.SetLabel(self.strRaio + str(Vars.SPHERE_RADIUS) + "cm")
                self.lblCentro.SetLabel(self.strCentro + "(" + str(round(centro[0], 3)) + "," + str(round(centro[1], 3)) + "," + str(round(centro[2], 3)) + ")")
                self.lblTam.SetLabel(self.strTam + "---")
            elif obj == Vars.BAR_SMALL:
                self.lblTipo.SetLabel(self.strTipo + "Barra Pequena")
                self.lblRaio.SetLabel(self.strRaio + str(Vars.BAR_RADIUS) + "cm")
                self.lblTam.SetLabel(self.strTam + str(Vars.BAR_LENGTH_SMALL) + "cm")
                self.lblCentro.SetLabel(self.strCentro + "(-,-,-)")
            elif obj == Vars.BAR_LARGE:
                self.lblTipo.SetLabel(self.strTipo + "Barra Grande")
                self.lblRaio.SetLabel(self.strRaio + str(Vars.BAR_RADIUS) + "cm")
                self.lblTam.SetLabel(self.strTam + str(Vars.BAR_LENGTH_LARGE) + "cm")
                self.lblCentro.SetLabel(self.strCentro + "(-,-,-)")
            elif obj == Vars.BASE:
                self.lblTipo.SetLabel(self.strTipo + "Base")
                self.lblRaio.SetLabel(self.strRaio + str(Vars.BASE_RADIUS) + "cm")
                self.lblCentro.SetLabel(self.strCentro + "(" + str(round(centro[0],3)) + "," +str(round(centro[1],3)) + "," + str(round(centro[2],3)) + ")")
                self.lblTam.SetLabel(self.strTam + "---")
            self.lblId.SetLabel(self.strId + str(id))
            self.alteraCentroMBR()
        self.parent.SetFocus()

    def alteraCentroMBR(self):

        MBRSelect = Vars.KitLib.getCentroMBRSelect()
        self.txtFocusX.SetValue(str(round(MBRSelect.contents.x,3)))
        self.txtFocusY.SetValue(str(round(MBRSelect.contents.y,3)))
        self.txtFocusZ.SetValue(str(round(MBRSelect.contents.z,3)))