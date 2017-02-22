# -*- coding: UTF-8 -*-
from VarsAmbient import *

"""
    ->Classe TabConfig:
        Classe utilizada para instânciar a aba configurações no menu Principal.

"""
class TabConfig(wx.lib.scrolledpanel.ScrolledPanel):

    # ----------------------------------------------------------------------
    def __init__(self, parent):


        wx.lib.scrolledpanel.ScrolledPanel.__init__(self, parent=parent, id=wx.ID_ANY,style=wx.DOUBLE_BORDER)
        self.SetupScrolling()
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.parent = parent

        #Configurações de tamanho do grid
        lblTamGrid = wx.StaticText(self,wx.ID_ANY,"Tamanho do grid: ")
        lblTamGrid.SetExtraStyle(wx.TE_CENTRE)
        self.txtTamGrid = wx.TextCtrl(self, wx.ID_ANY, str(Vars.KitLib.getTamGrid()),style=wx.TE_PROCESS_ENTER)
        self.txtTamGrid.Bind(wx.EVT_KEY_DOWN, self.OnEnter)
        btnTamGrid = wx.Button(self,wx.ID_ANY,"Ok")

        # Configurações de espaçamento do grid
        sizerDistGrid = wx.BoxSizer(wx.VERTICAL)
        lblDistGrid = wx.StaticText(self, wx.ID_ANY, "Espaçamento do Grid:")
        cbxDistGrid = wx.ComboBox(self, wx.ID_ANY, "1cm", style=wx.CB_READONLY)
        cbxDistGrid.Append("1cm",1)
        cbxDistGrid.Append("9cm",2)
        cbxDistGrid.Append("18cm",3)
        sizerDistGrid.Add(lblDistGrid, 0, wx.ALIGN_CENTRE, 5)
        sizerDistGrid.Add(cbxDistGrid, 0, wx.ALIGN_CENTRE, 5)

        # Configurações de foco da câmera
        self.sizerFocus = wx.BoxSizer(wx.VERTICAL)
        self.sizerX = wx.BoxSizer(wx.HORIZONTAL)
        self.sizerY = wx.BoxSizer(wx.HORIZONTAL)
        self.sizerZ = wx.BoxSizer(wx.HORIZONTAL)
        self.lblFocus = wx.StaticText(self, wx.ID_ANY, "Foco da Câmera: ")
        self.lblFocus.SetExtraStyle(wx.TE_CENTRE)
        self.lblX = wx.StaticText(self, wx.ID_ANY, "X: ")
        self.lblX.SetExtraStyle(wx.TE_RIGHT)
        self.lblY = wx.StaticText(self, wx.ID_ANY, "Y: ")
        self.lblY.SetExtraStyle(wx.TE_RIGHT)
        self.lblZ = wx.StaticText(self, wx.ID_ANY, "Z: ")
        self.lblZ.SetExtraStyle(wx.TE_RIGHT)
        self.txtFocusX = wx.TextCtrl(self, wx.ID_ANY, "--", style=wx.TE_PROCESS_ENTER)
        self.txtFocusX.Bind(wx.EVT_KEY_DOWN, self.OnEnterFocusX)
        self.txtFocusY = wx.TextCtrl(self, wx.ID_ANY, "--", style=wx.TE_PROCESS_ENTER)
        self.txtFocusY.Bind(wx.EVT_KEY_DOWN, self.OnEnterFocusY)
        self.txtFocusZ = wx.TextCtrl(self, wx.ID_ANY, "--", style=wx.TE_PROCESS_ENTER)
        self.txtFocusZ.Bind(wx.EVT_KEY_DOWN, self.OnEnterFocusZ)
        self.lblCmX = wx.StaticText(self, wx.ID_ANY, "cm")
        self.lblCmX.SetExtraStyle(wx.TE_RIGHT)
        self.lblCmY = wx.StaticText(self, wx.ID_ANY, "cm")
        self.lblCmY.SetExtraStyle(wx.TE_RIGHT)
        self.lblCmZ = wx.StaticText(self, wx.ID_ANY, "cm")
        self.lblCmZ.SetExtraStyle(wx.TE_RIGHT)
        self.btnFocus = wx.Button(self, wx.ID_ANY, "Mudar Foco")
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
        self.sizerFocus.Add(self.btnFocus, 0, wx.ALIGN_CENTER, 5)

        # Configurações de qualidade da malha
        sizerQuality = wx.BoxSizer(wx.VERTICAL)
        lblQuality = wx.StaticText(self,wx.ID_ANY, "Qualidade da Malha:")
        sldQuality = wx.Slider(self, value=100, minValue=5, maxValue=100,style=wx.SL_HORIZONTAL | wx.SL_LABELS)
        sizerQuality.Add(lblQuality, 0, wx.ALIGN_CENTRE, 5)
        sizerQuality.Add(sldQuality, 1, wx.ALIGN_CENTRE | wx.EXPAND, 5)
        sldQuality.Bind(wx.EVT_SLIDER, self.OnSliderScroll)

        # Adição do sizer principal
        sizer.Add(lblTamGrid, 0, wx.ALIGN_CENTER,5)
        sizer.Add(self.txtTamGrid, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(btnTamGrid, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        sizer.Add(sizerDistGrid,0,wx.ALIGN_CENTRE,5)
        sizer.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)


        sizer.Add(self.lblFocus, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(self.sizerFocus, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        sizer.Add(sizerQuality, 0, wx.ALIGN_CENTRE | wx.EXPAND, 5)
        sizer.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)

        self.Bind(wx.EVT_BUTTON, self.OnTamGrid,btnTamGrid)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnTamGrid,self.txtTamGrid)

        self.Bind(wx.EVT_TEXT_ENTER, self.OnEnterFocus, self.txtFocusX)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnEnterFocus, self.txtFocusY)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnEnterFocus, self.txtFocusZ)
        self.Bind(wx.EVT_BUTTON, self.OnEnterFocus, self.btnFocus)
        cbxDistGrid.Bind(wx.EVT_COMBOBOX, self.OnGridCombox)

        self.SetSizer(sizer)

    def OnSliderScroll(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        Vars.KitLib.setMeshQual(c_float(val/100))
        self.parent.SetFocus()
        Vars.drawArea0.Refresh()
        Vars.drawArea1.Refresh()
        Vars.drawArea2.Refresh()
        Vars.drawArea3.Refresh()

    def OnGridCombox(self,e):

        if e.GetString() == "1cm":
            Vars.KitLib.setEspacoGrid(c_float(1.0))
        elif e.GetString() == "9cm":
            Vars.KitLib.setEspacoGrid(c_float(9.0))
        else:
            Vars.KitLib.setEspacoGrid(c_float(18.0))
        self.parent.SetFocus()
        Vars.drawArea0.Refresh()
        Vars.drawArea1.Refresh()
        Vars.drawArea2.Refresh()
        Vars.drawArea3.Refresh()

    """
        -> Função OnTamGrid:
            Função para alternar o tamanho do grid a ser exibido na cena
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnTamGrid(self, e):

        if int(self.txtTamGrid.GetValue())%2 == 0:
            Vars.KitLib.setTamGrid(c_int(int(self.txtTamGrid.GetValue())))
        else:
            Vars.KitLib.setTamGrid(c_int(int(self.txtTamGrid.GetValue())+1))
            self.txtTamGrid.SetValue(str(int(self.txtTamGrid.GetValue())+1))
        self.Parent.SetFocus()
        Vars.drawArea0.Refresh()
        Vars.drawArea1.Refresh()
        Vars.drawArea2.Refresh()
        Vars.drawArea3.Refresh()
    """
        -> Função OnEnter:
            Função para tratar o pressionamento da tecla enter sob o txtTamGrid
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnEnter(self,e):

        keycode = e.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER or keycode == wx.WXK_TAB:
            self.OnTamGrid(e)
            e.EventObject.Navigate()
        e.Skip()

    def OnEnterFocusX(self, e):

        keycode = e.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
            e.EventObject.Navigate()
        elif keycode == wx.WXK_TAB:
            pass
        e.Skip()

    def OnEnterFocusY(self, e):

        keycode = e.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
            e.EventObject.Navigate()
        elif keycode == wx.WXK_TAB:
            pass
        e.Skip()

    def OnEnterFocusZ(self, e):

        keycode = e.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
            e.EventObject.Navigate()
        elif keycode == wx.WXK_TAB:
            pass
        e.Skip()

    def OnEnterFocus(self, e):
        try:
            if Vars.ultimoDrawSelected.visionOption == Vars.VISION_Z_PERSP:
                Vars.ultimoDrawSelected.centro = (
                float(self.txtFocusX.GetValue()), float(self.txtFocusY.GetValue()), float(self.txtFocusZ.GetValue()))
            elif Vars.ultimoDrawSelected.visionOption == Vars.VISION_X_POS :
                Vars.ultimoDrawSelected.orthoCenter = (-float(self.txtFocusY.GetValue()), float(self.txtFocusZ.GetValue()))
                self.txtFocusX.SetValue("0")
            elif Vars.ultimoDrawSelected.visionOption == Vars.VISION_X_NEG:
                Vars.ultimoDrawSelected.orthoCenter = (
                -float(self.txtFocusY.GetValue()), -float(self.txtFocusZ.GetValue()))
                self.txtFocusX.SetValue("0")
            elif Vars.ultimoDrawSelected.visionOption == Vars.VISION_Y_POS :
                Vars.ultimoDrawSelected.orthoCenter = (-float(self.txtFocusZ.GetValue()), -float(self.txtFocusX.GetValue()))
                self.txtFocusY.SetValue("0")
            elif Vars.ultimoDrawSelected.visionOption == Vars.VISION_Y_NEG:
                Vars.ultimoDrawSelected.orthoCenter = (
                -float(self.txtFocusZ.GetValue()), float(self.txtFocusX.GetValue()))
                self.txtFocusY.SetValue("0")

        except:
            ex = wx.MessageDialog(None, "Caracter Inválido! \nTente usar ponto ao invés de virgula.", "Erro!", wx.OK)
            ex.ShowModal()
        self.Parent.SetFocus()
        Vars.drawArea0.Refresh()
        Vars.drawArea1.Refresh()
        Vars.drawArea2.Refresh()
        Vars.drawArea3.Refresh()