from VarsAmbient import *
from Msg import *

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

        wx.lib.scrolledpanel.ScrolledPanel.__init__(self, parent=parent,size = (200,-1), id=wx.ID_ANY)#,style=wx.DOUBLE_BORDER)
        self.SetScrollbar(wx.VERTICAL, 0, 0, 2, 0)
        self.SetupScrolling(scroll_x=False)

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.sizer.Add(self.createInfo(), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizer.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizer.Add(self.createMoveSelect(), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizer.Add(self.createGrausLiberdade(), 0, wx.ALIGN_CENTRE | wx.EXPAND , 5)
        self.sizer.Add(self.createPropriedadeBarra(), 0, wx.ALIGN_CENTRE | wx.EXPAND, 5)

        self.OnHidePropriedadeBarra()
        self.OnHideGrausLiberdade()

        self.SetSizer(self.sizer)

        #thema dark
        if(Vars.thema == "dark"):
            self.themaDark()


    def OnMoveObj(self,e):
        if self.idUltObj != 0:
            Vars.KitLib.moveObjSelect(c_int(self.idUltObj), c_float(float(self.txtFocusX.GetValue())),
                                      c_float(float(self.txtFocusY.GetValue())),
                                      c_float(float(self.txtFocusZ.GetValue())))
            self.parent.parent.OnRefreshAll()
            Vars.KitLib.terminaMovimentacao()
        else:
            Msg.exibirStatusBar("Selecione um objeto primeiro!",10)
        self.parent.SetFocus()


    def OnMoveObjSelect(self,e):
        Vars.KitLib.moveObjSelect(c_float(float(self.txtFocusX.GetValue())),c_float(float(self.txtFocusY.GetValue())),c_float(float(self.txtFocusZ.GetValue())))
        self.parent.parent.OnRefreshAll()
        self.parent.SetFocus()

    def AlteraLayoutInfo(self, id, obj, centro, Tx, Ty, Tz, Rx, Ry, Rz, E, poisson, termico, largura, altura, raio, secao):
        self.ckbTz.Enable()
        self.OnHideGrausLiberdade()
        self.OnHidePropriedadeBarra()
        if id == 0:
            self.idUltObj = 0
            self.lblTipo.SetLabel(self.strTipo + "---")
            self.lblId.SetLabel(self.strId + "---")
            self.lblTam.SetLabel(self.strTam + "---")
            self.lblRaio.SetLabel(self.strRaio + "---")
            self.lblCentro.SetLabel(self.strCentro + "(-,-,-)")
            self.txtFocusX.SetValue(str(0))
            self.txtFocusY.SetValue(str(0))
            self.txtFocusZ.SetValue(str(0))
            self.ckbTx.SetValue(False)
            self.ckbTy.SetValue(False)
            self.ckbTz.SetValue(False)
            self.ckbRx.SetValue(False)
            self.ckbRy.SetValue(False)
            self.ckbRz.SetValue(False)
        else:

            self.idUltObj = id
            if obj == Vars.SPHERE:
                self.lblTipo.SetLabel(self.strTipo + "Nó")
                self.lblRaio.SetLabel(self.strRaio + str(Vars.SPHERE_RADIUS) + "cm")
                self.lblCentro.SetLabel(self.strCentro + "(" + str(round(centro[0], 3)) + "," + str(round(centro[1], 3)) + "," + str(round(centro[2], 3)) + ")")
                self.lblTam.SetLabel(self.strTam + "---")
                self.ckbTx.SetValue(Tx)
                self.ckbTy.SetValue(Ty)
                self.ckbTz.SetValue(Tz)
                self.ckbRx.SetValue(Rx)
                self.ckbRy.SetValue(Ry)
                self.ckbRz.SetValue(Rz)
                self.OnShowGrausLiberdade()
            elif obj == Vars.BAR:
                self.lblTipo.SetLabel(self.strTipo + "Barra")
                self.lblRaio.SetLabel(self.strRaio + str(Vars.BAR_RADIUS) + "cm")
                self.lblTam.SetLabel(self.strTam + str(Vars.BAR_LENGTH_SMALL) + "cm")
                self.lblCentro.SetLabel(self.strCentro + "(-,-,-)")
                if secao == 0:
                    self.txtraio.SetValue(str(c_float(raio).value))
                    self.cbxSecao.SetValue("Circular")
                    self.OnShowRaio()
                elif secao == 1:
                    self.txtlargura.SetValue(str(c_float(largura).value))
                    self.txtaltura.SetValue(str(c_float(altura).value))
                    self.cbxSecao.SetValue("Retangular")
                    self.OnShowLargura()
                    self.OnShowAltura()
                self.OnShowPropriedadeBarra()
            elif obj == Vars.BASE:
                self.lblTipo.SetLabel(self.strTipo + "Base")
                self.lblRaio.SetLabel(self.strRaio + str(Vars.BASE_RADIUS) + "cm")
                self.lblCentro.SetLabel(self.strCentro + "(" + str(round(centro[0],3)) + "," +str(round(centro[1],3)) + "," + str(round(centro[2],3)) + ")")
                self.lblTam.SetLabel(self.strTam + "---")
                self.ckbTz.Disable()
                self.ckbTx.SetValue(Tx)
                self.ckbTy.SetValue(Ty)
                self.ckbTz.SetValue(Tz)
                self.ckbRx.SetValue(Rx)
                self.ckbRy.SetValue(Ry)
                self.ckbRz.SetValue(Rz)
                self.OnHideGrausLiberdade()
            elif obj == Vars.LAJE:
                self.lblTipo.SetLabel(self.strTipo + "Laje")
                self.lblRaio.SetLabel(self.strRaio + str(Vars.BAR_RADIUS) + "cm")
                self.lblTam.SetLabel(self.strTam + str(Vars.BAR_LENGTH_LARGE) + "cm")
                self.lblCentro.SetLabel(self.strCentro + "(-,-,-)")
            elif obj == Vars.DIAGONAL_SMALL:
                self.lblTipo.SetLabel(self.strTipo + "Tirante 9x9")
                self.lblRaio.SetLabel(self.strRaio + str(Vars.BAR_RADIUS) + "cm")
                self.lblTam.SetLabel(self.strTam + str(Vars.DIAGONAL_LENGTH_SMALL) + "cm")
                self.lblCentro.SetLabel(self.strCentro + "(-,-,-)")
            elif obj == Vars.DIAGONAL_LARGE:
                self.lblTipo.SetLabel(self.strTipo + "Tirante 18x9")
                self.lblRaio.SetLabel(self.strRaio + str(Vars.BAR_RADIUS) + "cm")
                self.lblTam.SetLabel(self.strTam + str(Vars.DIAGONAL_LENGTH_LARGE) + "cm")
                self.lblCentro.SetLabel(self.strCentro + "(-,-,-)")

            self.lblId.SetLabel(self.strId + str(id))
            self.alteraCentroMBR()
        self.parent.SetFocus()

    def alteraCentroMBR(self):

        MBRSelect = Vars.KitLib.getCentroMBRSelect()
        self.txtFocusX.SetValue(str(round(MBRSelect.contents.x,3)))
        self.txtFocusY.SetValue(str(round(MBRSelect.contents.y,3)))
        self.txtFocusZ.SetValue(str(round(MBRSelect.contents.z,3)))

    def createGrausLiberdade(self):

        self.sizerGrausLiberdadeV = wx.BoxSizer(wx.VERTICAL)
        self.sizerGrausLiberdadeH = wx.BoxSizer(wx.HORIZONTAL)
        self.sizerGrausTranslacao = wx.BoxSizer(wx.VERTICAL)
        self.sizerGrausRotacao = wx.BoxSizer(wx.VERTICAL)

        self.stlSeparacaoAcimaLiberdade = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL)
        self.stlSeparacaoAbaixoLiberdade = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL)

        self.lblEspacoLiberdadeAbaixo = wx.StaticText(self, wx.ID_ANY, "\n")

        self.lblGrLib = wx.StaticText(self, wx.ID_ANY, "Graus de Liberdade:")

        self.lblEspacoLiberdade = wx.StaticText(self, wx.ID_ANY, "\n")

        self.idTx = wx.NewId()
        self.idTy = wx.NewId()
        self.idTz = wx.NewId()
        self.idRx = wx.NewId()
        self.idRy = wx.NewId()
        self.idRz = wx.NewId()

        self.ckbTx = wx.CheckBox(self, id=self.idTx, label="Tx")
        self.ckbTy = wx.CheckBox(self, id=self.idTy, label="Ty")
        self.ckbTz = wx.CheckBox(self, id=self.idTz, label="Tz")
        self.ckbRx = wx.CheckBox(self, id=self.idRx, label="Rx")
        self.ckbRy = wx.CheckBox(self, id=self.idRy, label="Ry")
        self.ckbRz = wx.CheckBox(self, id=self.idRz, label="Rz")

        self.sizerGrausTranslacao.Add(self.ckbTx, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizerGrausTranslacao.Add(self.ckbTy, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizerGrausTranslacao.Add(self.ckbTz, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizerGrausRotacao.Add(self.ckbRx, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizerGrausRotacao.Add(self.ckbRy, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizerGrausRotacao.Add(self.ckbRz, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)

        self.sizerGrausLiberdadeV.Add(self.stlSeparacaoAcimaLiberdade, 0, wx.CENTRE | wx.EXPAND, 5)
        self.sizerGrausLiberdadeV.Add(self.lblGrLib, 0, wx.ALIGN_CENTRE, 5)
        self.sizerGrausLiberdadeV.Add(self.stlSeparacaoAbaixoLiberdade, 0, wx.CENTRE | wx.EXPAND, 5)
        self.sizerGrausLiberdadeV.Add(self.lblEspacoLiberdade, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizerGrausLiberdadeH.Add(self.sizerGrausTranslacao, 1, wx.ALIGN_CENTRE_HORIZONTAL, 5)
        self.sizerGrausLiberdadeH.Add(self.sizerGrausRotacao, 1, wx.ALIGN_CENTRE_HORIZONTAL, 5)
        self.sizerGrausLiberdadeV.Add(self.sizerGrausLiberdadeH, 0, wx.ALIGN_CENTER, 5)
        self.sizerGrausLiberdadeV.Add(self.lblEspacoLiberdadeAbaixo , 0, wx.ALIGN_CENTER, 5)

        self.Bind(wx.EVT_CHECKBOX, self.OnCheckGrauLiberdade, self.ckbTx)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckGrauLiberdade, self.ckbTy)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckGrauLiberdade, self.ckbTz)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckGrauLiberdade, self.ckbRx)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckGrauLiberdade, self.ckbRy)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckGrauLiberdade, self.ckbRz)

        return self.sizerGrausLiberdadeV

    def OnHideGrausLiberdade(self):

        self.stlSeparacaoAcima.Hide()
        self.lblGrLib.Hide()
        self.stlSeparacaoAbaixo.Hide()
        self.lblEspacoLiberdade.Hide()

        self.ckbTx.Hide()
        self.ckbTy.Hide()
        self.ckbTz.Hide()
        self.ckbRx.Hide()
        self.ckbRy.Hide()
        self.ckbRz.Hide()

        self.lblEspacoLiberdadeAbaixo.Hide()

        self.sizerGrausTranslacao.Hide(True)
        self.sizerGrausRotacao.Hide(True)
        self.sizerGrausLiberdadeH.Hide(True)
        self.sizerGrausLiberdadeV.Hide(True)

        self.sizerGrausTranslacao.Layout()
        self.sizerGrausRotacao.Layout()
        self.sizerGrausLiberdadeH.Layout()
        self.sizerGrausLiberdadeV.Layout()
        self.sizer.Layout()

    def OnShowGrausLiberdade(self):

        self.stlSeparacaoAcima.Show()
        self.lblGrLib.Show()
        self.stlSeparacaoAbaixo.Show()
        self.lblEspaco.Show()

        self.ckbTx.Show()
        self.ckbTy.Show()
        self.ckbTz.Show()
        self.ckbRx.Show()
        self.ckbRy.Show()
        self.ckbRz.Show()

        self.sizerGrausTranslacao.Show(True)
        self.sizerGrausRotacao.Show(True)
        self.sizerGrausLiberdadeH.Show(True)
        self.sizerGrausLiberdadeV.Show(True)

        self.sizerGrausTranslacao.Layout()
        self.sizerGrausRotacao.Layout()
        self.sizerGrausLiberdadeH.Layout()
        self.sizerGrausLiberdadeV.Layout()
        self.sizer.Layout()

    def createMoveSelect(self):

        self.lblOpt = wx.StaticText(self, wx.ID_ANY, "Opções:")
        self.sizerFocus = wx.BoxSizer(wx.VERTICAL)
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
        self.btnSelect = wx.Button(self, wx.ID_ANY, "Mover Seleção")
        self.sizerFocus.Add(self.lblOpt, 0, wx.ALIGN_CENTER, 5)
        self.sizerFocus.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizerFocus.Add(wx.StaticText(self, wx.ID_ANY, "\n"), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizerX.Add(self.lblX, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER, 5)
        self.sizerX.Add(self.txtFocusX, 0, wx.ALIGN_RIGHT, 5)
        self.sizerX.Add(self.lblCmX, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER, 5)
        self.sizerY.Add(self.lblY, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER, 5)
        self.sizerY.Add(self.txtFocusY, 0, wx.ALIGN_RIGHT, 5)
        self.sizerY.Add(self.lblCmY, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER, 5)
        self.sizerZ.Add(self.lblZ, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER, 5)
        self.sizerZ.Add(self.txtFocusZ, 0, wx.ALIGN_RIGHT, 5)
        self.sizerZ.Add(self.lblCmZ, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER, 5)
        self.sizerFocus.Add(self.sizerX, 0, wx.ALIGN_CENTER, 5)
        self.sizerFocus.Add(self.sizerY, 0, wx.ALIGN_CENTER, 5)
        self.sizerFocus.Add(self.sizerZ, 0, wx.ALIGN_CENTER, 5)
        self.sizerFocus.Add(self.btnSelect, 0, wx.ALIGN_CENTER, 5)
        self.sizerFocus.Add(wx.StaticText(self, wx.ID_ANY, "\n"), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.Bind(wx.EVT_BUTTON, self.OnMoveObjSelect, self.btnSelect)

        return self.sizerFocus

    def createInfo(self):

        self.idUltObj = 0
        self.sizerInfo = wx.BoxSizer(wx.VERTICAL)
        self.strId = "Id: "
        self.strCentro = "Centro: "
        self.strTipo = "\n\nTipo: "
        self.strTam = "Tamanho: "
        self.strRaio = "Raio: "
        self.strInfoObj = "Informações Sobre Objetos"
        self.lblIndoObj = wx.StaticText(self, wx.ID_ANY, self.strInfoObj)
        self.lblTipo = wx.StaticText(self, wx.ID_ANY, self.strTipo + "---")
        self.lblId = wx.StaticText(self, wx.ID_ANY, self.strId + "0")
        self.lblTam = wx.StaticText(self, wx.ID_ANY, self.strTam + "0mm")
        self.lblRaio = wx.StaticText(self, wx.ID_ANY, self.strRaio + "0mm")
        self.lblCentro = wx.StaticText(self, wx.ID_ANY, self.strCentro + "(-,-,-)")

        self.sizerInfo.Add(self.lblIndoObj, 0, wx.ALIGN_CENTRE, 5)
        self.sizerInfo.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizerInfo.Add(self.lblTipo, 0, wx.ALIGN_LEFT, 5)
        self.sizerInfo.Add(self.lblId, 0, wx.ALIGN_LEFT, 5)
        self.sizerInfo.Add(self.lblCentro, 0, wx.ALIGN_LEFT, 5)
        self.sizerInfo.Add(self.lblTam, 0, wx.ALIGN_LEFT, 5)
        self.sizerInfo.Add(self.lblRaio, 0, wx.ALIGN_LEFT, 5)
        self.sizerInfo.Add(wx.StaticText(self, wx.ID_ANY, "\n"), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)

        return self.sizerInfo

    def themaDark(self):

        self.lblTipo.SetForegroundColour("white")
        self.lblTipo.SetBackgroundColour(Vars.corThema)

        self.lblTam.SetForegroundColour("white")
        self.lblTam.SetBackgroundColour(Vars.corThema)

        self.lblId.SetForegroundColour("white")
        self.lblId.SetBackgroundColour(Vars.corThema)

        self.lblRaio.SetForegroundColour("white")
        self.lblRaio.SetBackgroundColour(Vars.corThema)

        self.lblCentro.SetForegroundColour("white")
        self.lblCentro.SetBackgroundColour(Vars.corThema)

        self.lblX.SetForegroundColour("white")
        self.lblX.SetBackgroundColour(Vars.corThema)

        self.lblY.SetForegroundColour("white")
        self.lblY.SetBackgroundColour(Vars.corThema)

        self.lblZ.SetForegroundColour("white")
        self.lblZ.SetBackgroundColour(Vars.corThema)

        self.lblCmX.SetForegroundColour("white")
        self.lblCmX.SetBackgroundColour(Vars.corThema)

        self.lblCmY.SetForegroundColour("white")
        self.lblCmY.SetBackgroundColour(Vars.corThema)

        self.lblCmZ.SetForegroundColour("white")
        self.lblCmZ.SetBackgroundColour(Vars.corThema)

        self.lblIndoObj.SetForegroundColour("white")
        self.lblIndoObj.SetBackgroundColour(Vars.corThema)

        self.lblOpt.SetForegroundColour("white")
        self.lblOpt.SetBackgroundColour(Vars.corThema)

        self.ckbTx.SetForegroundColour("white")
        self.ckbTx.SetBackgroundColour(Vars.corThema)

        self.ckbTy.SetForegroundColour("white")
        self.ckbTy.SetBackgroundColour(Vars.corThema)

        self.ckbTz.SetForegroundColour("white")
        self.ckbTz.SetBackgroundColour(Vars.corThema)

        self.ckbRx.SetForegroundColour("white")
        self.ckbRx.SetBackgroundColour(Vars.corThema)

        self.ckbRy.SetForegroundColour("white")
        self.ckbRy.SetBackgroundColour(Vars.corThema)

        self.ckbRz.SetForegroundColour("white")
        self.ckbRz.SetBackgroundColour(Vars.corThema)

        self.lblGrLib.SetForegroundColour("white")
        self.lblGrLib.SetBackgroundColour(Vars.corThema)

        self.lblPropriedades.SetForegroundColour("white")
        self.lblPropriedades.SetBackgroundColour(Vars.corThema)

        self.lblSecao.SetForegroundColour("white")
        self.lblSecao.SetBackgroundColour(Vars.corThema)

        self.lblcmAltura.SetForegroundColour("white")
        self.lblcmAltura.SetBackgroundColour(Vars.corThema)

        self.lbllargura.SetForegroundColour("white")
        self.lbllargura.SetBackgroundColour(Vars.corThema)

        self.lblaltura.SetForegroundColour("white")
        self.lblaltura.SetBackgroundColour(Vars.corThema)

        self.lblcmLargura.SetForegroundColour("white")
        self.lblcmLargura.SetBackgroundColour(Vars.corThema)

        self.lblraio.SetForegroundColour("white")
        self.lblraio.SetBackgroundColour(Vars.corThema)

        self.lblcmraio.SetForegroundColour("white")
        self.lblcmraio.SetBackgroundColour(Vars.corThema)

        self.lblE.SetForegroundColour("white")
        self.lblE.SetBackgroundColour(Vars.corThema)

        self.lblMpaE.SetForegroundColour("white")
        self.lblMpaE.SetBackgroundColour(Vars.corThema)

        self.lblPoisson.SetForegroundColour("white")
        self.lblPoisson.SetBackgroundColour(Vars.corThema)

        self.lblTermico.SetForegroundColour("white")
        self.lblTermico.SetBackgroundColour(Vars.corThema)

        self.lblCTermico.SetForegroundColour("white")
        self.lblCTermico.SetBackgroundColour(Vars.corThema)

        self.lblcmPoisson.SetForegroundColour("white")
        self.lblcmPoisson.SetBackgroundColour(Vars.corThema)

    def OnCheckGrauLiberdade(self, e):
        Tx = 100
        Ty = 101
        Tz = 102
        Rx = 103
        Ry = 104

        if self.idUltObj == 0:
            if e.GetId() == Tx:
                self.ckbTx.SetValue(False)
            elif e.GetId() == Ty:
                self.ckbTy.SetValue(False)
            elif e.GetId() == Tz:
                self.ckbTz.SetValue(False)
            elif e.GetId() == Rx:
                self.ckbRx.SetValue(False)
            elif e.GetId() == Ry:
                self.ckbRy.SetValue(False)
            else:
                self.ckbRz.SetValue(False)
        else:
            if e.GetId() == Tx:
                Vars.KitLib.alteraGrauLiberdadeTranslacao(c_int(self.idUltObj), True, False, False,
                                                          self.ckbTx.IsChecked())
            elif e.GetId() == Ty:
                Vars.KitLib.alteraGrauLiberdadeTranslacao(c_int(self.idUltObj), False, True, False,
                                                          self.ckbTy.IsChecked())
            elif e.GetId() == Tz:
                Vars.KitLib.alteraGrauLiberdadeTranslacao(c_int(self.idUltObj), False, False, True,
                                                          self.ckbTz.IsChecked())
            elif e.GetId() == Rx:
                Vars.KitLib.alteraGrauLiberdadeRotacao(c_int(self.idUltObj), True, False, False,
                                                          self.ckbRx.IsChecked())
            elif e.GetId() == Ry:
                Vars.KitLib.alteraGrauLiberdadeRotacao(c_int(self.idUltObj), False, True, False,
                                                          self.ckbRy.IsChecked())
            else:
                Vars.KitLib.alteraGrauLiberdadeRotacao(c_int(self.idUltObj), False, False, True,
                                                          self.ckbRz.IsChecked())


    def createPropriedadeBarra(self):

        self.sizerPropriedadeBarra = wx.BoxSizer(wx.VERTICAL)
        self.sizerSecao = wx.BoxSizer(wx.HORIZONTAL)
        self.sizerAltura = wx.BoxSizer(wx.HORIZONTAL)
        self.sizerLargura = wx.BoxSizer(wx.HORIZONTAL)
        self.sizerRaio = wx.BoxSizer(wx.HORIZONTAL)
        self.sizerCoefElastico = wx.BoxSizer(wx.HORIZONTAL)
        self.sizerCoefPoisson = wx.BoxSizer(wx.HORIZONTAL)
        self.sizerCoefTermico = wx.BoxSizer(wx.HORIZONTAL)

        self.lblEspaco = wx.StaticText(self, wx.ID_ANY, "\n")

        self.lblPropriedades = wx.StaticText(self, wx.ID_ANY, "Propriedades da Barra:")
        self.lblSecao =  wx.StaticText(self, wx.ID_ANY, "   Sessão: ")

        self.cbxSecao = wx.ComboBox(self, wx.ID_ANY, "Circular", style=wx.CB_READONLY)
        self.cbxSecao.Append("Circular", 1)
        self.cbxSecao.Append("Retangular", 2)

        self.lbllargura = wx.StaticText(self, wx.ID_ANY, "  Largura:")
        self.txtlargura = wx.TextCtrl(self, wx.ID_ANY, "0")
        self.lblcmLargura = wx.StaticText(self, wx.ID_ANY, "m              ")

        self.lblaltura = wx.StaticText(self, wx.ID_ANY, "  Altura:")
        self.txtaltura = wx.TextCtrl(self, wx.ID_ANY, "0")
        self.lblcmAltura = wx.StaticText(self, wx.ID_ANY, "m           ")

        self.lblraio = wx.StaticText(self, wx.ID_ANY, "  Raio:")
        self.txtraio = wx.TextCtrl(self, wx.ID_ANY, "0")
        self.lblcmraio = wx.StaticText(self, wx.ID_ANY, "m        ")

        self.lblE = wx.StaticText(self, wx.ID_ANY, "    E:")
        self.txtE = wx.TextCtrl(self, wx.ID_ANY, "0")
        self.lblMpaE = wx.StaticText(self, wx.ID_ANY, "MPa")

        self.lblPoisson = wx.StaticText(self, wx.ID_ANY, "  υ:")
        self.txtPoisson = wx.TextCtrl(self, wx.ID_ANY, "0")
        self.lblcmPoisson = wx.StaticText(self, wx.ID_ANY, "   \r   ")

        self.lblTermico = wx.StaticText(self, wx.ID_ANY, "  α:")
        self.txtTermico = wx.TextCtrl(self, wx.ID_ANY, "0")
        self.lblCTermico = wx.StaticText(self, wx.ID_ANY, "/ºC")

        self.stlSeparacaoAcima = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL)
        self.stlSeparacaoAbaixo = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL)

        self.sizerSecao.Add(self.lblSecao, 0, wx.ALIGN_CENTRE, 5)
        self.sizerSecao.Add(self.cbxSecao, 0, wx.ALIGN_CENTRE, 5)

        self.sizerAltura.Add(self.lblaltura, 0, wx.ALIGN_CENTRE, 5)
        self.sizerAltura.Add(self.txtaltura, 0, wx.ALIGN_CENTRE, 5)
        self.sizerAltura.Add(self.lblcmAltura, 0, wx.ALIGN_CENTRE, 5)

        self.sizerLargura.Add(self.lbllargura, 0, wx.ALIGN_CENTRE, 5)
        self.sizerLargura.Add(self.txtlargura, 0, wx.ALIGN_CENTRE, 5)
        self.sizerLargura.Add(self.lblcmLargura, 0, wx.ALIGN_CENTRE, 5)

        self.sizerRaio.Add(self.lblraio, 0, wx.ALIGN_CENTRE, 5)
        self.sizerRaio.Add(self.txtraio, 0, wx.ALIGN_CENTRE, 5)
        self.sizerRaio.Add(self.lblcmraio, 0, wx.ALIGN_CENTRE, 5)

        self.sizerCoefElastico.Add(self.lblE, 0, wx.ALIGN_CENTRE, 5)
        self.sizerCoefElastico.Add(self.txtE, 0, wx.ALIGN_CENTRE, 5)
        self.sizerCoefElastico.Add(self.lblMpaE, 0, wx.ALIGN_CENTRE, 5)

        self.sizerCoefPoisson.Add(self.lblPoisson, 0, wx.ALIGN_CENTRE, 5)
        self.sizerCoefPoisson.Add(self.txtPoisson, 0, wx.ALIGN_CENTRE, 5)
        self.sizerCoefPoisson.Add(self.lblcmPoisson, 0, wx.ALIGN_CENTRE, 5)

        self.sizerCoefTermico.Add(self.lblTermico, 0, wx.ALIGN_CENTRE, 5)
        self.sizerCoefTermico.Add(self.txtTermico, 0, wx.ALIGN_CENTRE, 5)
        self.sizerCoefTermico.Add(self.lblCTermico, 0, wx.ALIGN_CENTRE, 5)

        self.sizerPropriedadeBarra.Add(self.stlSeparacaoAcima, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizerPropriedadeBarra.Add(self.lblPropriedades, 0, wx.ALIGN_CENTRE, 5)
        self.sizerPropriedadeBarra.Add(self.stlSeparacaoAbaixo, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizerPropriedadeBarra.Add(self.lblEspaco, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        self.sizerPropriedadeBarra.Add(self.sizerSecao, 0, wx.ALIGN_LEFT, 5)
        self.sizerPropriedadeBarra.Add(self.sizerAltura, 0, wx.ALIGN_CENTRE, 5)
        self.sizerPropriedadeBarra.Add(self.sizerLargura, 0, wx.ALIGN_CENTRE, 5)
        self.sizerPropriedadeBarra.Add(self.sizerRaio, 0, wx.ALIGN_CENTRE, 5)
        self.sizerPropriedadeBarra.Add(self.sizerCoefElastico, 0, wx.ALIGN_CENTRE, 5)
        self.sizerPropriedadeBarra.Add(self.sizerCoefPoisson, 0, wx.ALIGN_CENTRE, 5)
        self.sizerPropriedadeBarra.Add(self.sizerCoefTermico, 0, wx.ALIGN_CENTRE, 5)

        self.cbxSecao.Bind(wx.EVT_COMBOBOX, self.OnComboPropriedade)

        return self.sizerPropriedadeBarra

    def OnHidePropriedadeBarra(self):

        self.stlSeparacaoAcima.Hide()
        self.stlSeparacaoAbaixo.Hide()
        self.lblEspaco.Hide()
        self.lblPropriedades.Hide()
        self.lblSecao.Hide()
        self.cbxSecao.Hide()
        self.sizerSecao.Hide(True)
        self.OnHideAltura()
        self.OnHideLargura()
        self.OnHideRaio()
        self.OnHideCoef()

    def OnComboPropriedade(self, e):

        if e.GetString() == "Circular":

            self.OnHideAltura()
            self.OnHideLargura()
            self.OnShowRaio()

        elif e.GetString() == "Retangular":

            self.OnHideRaio()
            self.OnShowAltura()
            self.OnShowLargura()

    def OnHideAltura(self):

        self.lblaltura.Hide()
        self.lblcmAltura.Hide()
        self.txtaltura.Hide()
        self.sizerAltura.Hide(True)
        self.sizerAltura.Layout()
        self.sizerPropriedadeBarra.Layout()
        self.sizer.Layout()

    def OnHideLargura(self):

        self.lbllargura.Hide()
        self.lblcmLargura.Hide()
        self.txtlargura.Hide()
        self.sizerLargura.Hide(True)
        self.sizerLargura.Layout()
        self.sizerPropriedadeBarra.Layout()
        self.sizer.Layout()

    def OnHideRaio(self):

        self.lblraio.Hide()
        self.lblcmraio.Hide()
        self.txtraio.Hide()
        self.sizerRaio.Hide(True)
        self.sizerRaio.Layout()
        self.sizerPropriedadeBarra.Layout()
        self.sizer.Layout()

    def OnHideSecao(self):

        self.lblSecao.Hide()
        self.cbxSecao.Hide()
        self.sizerSecao.Hide(True)
        self.sizerSecao.Layout()
        self.sizerPropriedadeBarra.Layout()
        self.sizer.Layout()

    def OnHideCoef(self):

        self.lblE.Hide()
        self.txtE.Hide()
        self.lblMpaE.Hide()
        self.lblPoisson.Hide()
        self.txtPoisson.Hide()
        self.lblcmPoisson.Hide()
        self.lblTermico.Hide()
        self.txtTermico.Hide()
        self.lblCTermico.Hide()
        self.sizerCoefElastico.Hide(True)
        self.sizerCoefPoisson.Hide(True)
        self.sizerCoefTermico.Hide(True)
        self.sizerCoefElastico.Layout()
        self.sizerCoefPoisson.Layout()
        self.sizerCoefTermico.Layout()
        self.sizerPropriedadeBarra.Layout()
        self.sizer.Layout()

    def OnShowAltura(self):
        self.lblaltura.Show()
        self.lblcmAltura.Show()
        self.txtaltura.Show()
        self.sizerAltura.Show(True)
        self.sizerAltura.Layout()
        self.sizerPropriedadeBarra.Layout()
        self.sizer.Layout()

    def OnShowLargura(self):

        self.lbllargura.Show()
        self.lblcmLargura.Show()
        self.txtlargura.Show()
        self.sizerLargura.Show(True)
        self.sizerLargura.Layout()
        self.sizerPropriedadeBarra.Layout()
        self.sizer.Layout()

    def OnShowRaio(self):

        self.lblraio.Show()
        self.lblcmraio.Show()
        self.txtraio.Show()
        self.sizerRaio.Show(True)
        self.sizerRaio.Layout()
        self.sizerPropriedadeBarra.Layout()
        self.sizer.Layout()

    def OnShowCoef(self):

        self.lblE.Show()
        self.txtE.Show()
        self.lblMpaE.Show()
        self.lblPoisson.Show()
        self.txtPoisson.Show()
        self.lblcmPoisson.Show()
        self.lblTermico.Show()
        self.txtTermico.Show()
        self.lblCTermico.Show()
        self.sizerCoefElastico.Show(True)
        self.sizerCoefPoisson.Show(True)
        self.sizerCoefTermico.Show(True)
        self.sizerCoefElastico.Layout()
        self.sizerCoefPoisson.Layout()
        self.sizerCoefTermico.Layout()
        self.sizerPropriedadeBarra.Layout()
        self.sizer.Layout()

    def OnShowPropriedadeBarra(self):

        self.stlSeparacaoAcima.Show()
        self.lblEspaco.Show()
        self.lblPropriedades.Show()
        self.stlSeparacaoAbaixo.Show()
        self.lblSecao.Show()
        self.cbxSecao.Show()
        self.sizerSecao.Show(True)
        self.sizerSecao.Show(True)
        self.sizerPropriedadeBarra.Layout()
        self.sizer.Layout()