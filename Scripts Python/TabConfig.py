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
        lblTamGrid = wx.StaticText(self,wx.ID_ANY,"Tamanho do grid: ")
        lblTamGrid.SetExtraStyle(wx.TE_CENTRE)
        self.txtTamGrid = wx.TextCtrl(self, wx.ID_ANY, str(Vars.KitLib.getTamGrid()),style=wx.TE_PROCESS_ENTER)
        self.txtTamGrid.Bind(wx.EVT_KEY_DOWN, self.OnEnter)
        btnTamGrid = wx.Button(self,wx.ID_ANY,"Ok")

        sizerX = wx.BoxSizer(wx.HORIZONTAL)
        sizerY = wx.BoxSizer(wx.HORIZONTAL)
        sizerZ = wx.BoxSizer(wx.HORIZONTAL)
        lblFocus = wx.StaticText(self, wx.ID_ANY, "Foco da Câmera: ")
        lblFocus.SetExtraStyle(wx.TE_CENTRE)
        lblX = wx.StaticText(self, wx.ID_ANY, "X: ")
        lblX.SetExtraStyle(wx.TE_RIGHT)
        lblY = wx.StaticText(self, wx.ID_ANY, "Y: ")
        lblY.SetExtraStyle(wx.TE_RIGHT)
        lblZ = wx.StaticText(self, wx.ID_ANY, "Z: ")
        lblZ.SetExtraStyle(wx.TE_RIGHT)
        self.txtFocusX = wx.TextCtrl(self, wx.ID_ANY, str(Vars.centro[0]), style=wx.TE_PROCESS_ENTER)
        self.txtFocusX.Bind(wx.EVT_KEY_DOWN, self.OnEnterFocusX)
        self.txtFocusY = wx.TextCtrl(self, wx.ID_ANY, str(Vars.centro[1]), style=wx.TE_PROCESS_ENTER)
        self.txtFocusY.Bind(wx.EVT_KEY_DOWN, self.OnEnterFocusY)
        self.txtFocusZ = wx.TextCtrl(self, wx.ID_ANY, str(Vars.centro[2]), style=wx.TE_PROCESS_ENTER)
        self.txtFocusZ.Bind(wx.EVT_KEY_DOWN, self.OnEnterFocusZ)
        lblCmX = wx.StaticText(self, wx.ID_ANY, "cm")
        lblCmX.SetExtraStyle(wx.TE_RIGHT)
        lblCmY = wx.StaticText(self, wx.ID_ANY, "cm")
        lblCmY.SetExtraStyle(wx.TE_RIGHT)
        lblCmZ = wx.StaticText(self, wx.ID_ANY, "cm")
        lblCmZ.SetExtraStyle(wx.TE_RIGHT)
        self.btnFocus = wx.Button(self,wx.ID_ANY,"Mudar Foco")

        sizerX.Add(lblX, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER, 5 )
        sizerX.Add(self.txtFocusX, 0, wx.ALIGN_RIGHT, 5)
        sizerX.Add(lblCmX,0,wx.ALIGN_RIGHT | wx.ALIGN_CENTER, 5 )
        sizerY.Add(lblY, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER, 5 )
        sizerY.Add(self.txtFocusY, 0, wx.ALIGN_RIGHT, 5)
        sizerY.Add(lblCmY, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER, 5)
        sizerZ.Add(lblZ, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER, 5 )
        sizerZ.Add(self.txtFocusZ, 0, wx.ALIGN_RIGHT, 5)
        sizerZ.Add(lblCmZ, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER, 5)

        sizer.Add(lblTamGrid, 0, wx.ALIGN_CENTER,5)
        sizer.Add(self.txtTamGrid, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(btnTamGrid, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        sizer.Add(lblFocus, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(sizerX,0,wx.ALIGN_CENTER,5)
        sizer.Add(sizerY,0,wx.ALIGN_CENTER,5)
        sizer.Add(sizerZ,0,wx.ALIGN_CENTER,5)
        sizer.Add(self.btnFocus, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)

        self.Bind(wx.EVT_BUTTON, self.OnTamGrid,btnTamGrid)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnTamGrid,self.txtTamGrid)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnEnterFocus, self.txtFocusX)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnEnterFocus, self.txtFocusY)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnEnterFocus, self.txtFocusZ)
        self.Bind(wx.EVT_BUTTON, self.OnEnterFocus, self.btnFocus)

        self.SetSizer(sizer)

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
        Vars.drawArea.Refresh()
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
            Vars.centro = (float(self.txtFocusX.GetValue()), float(self.txtFocusY.GetValue()), float(self.txtFocusZ.GetValue()))
        except:
            ex = wx.MessageDialog(None, "Caracter Inválido! \nTente usar ponto ao invés de virgula.", "Erro!", wx.OK)
            ex.ShowModal()
        self.Parent.SetFocus()
        Vars.drawArea.Refresh()