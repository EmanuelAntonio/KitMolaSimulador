# -*- coding: UTF-8 -*-
from VarsAmbient import *

"""
    ->Classe CamPanel:
        Classe utilizada para instânciar os objetos da aba camera do menu principal.

"""
class CamPanel(wx.Panel):


    # ----------------------------------------------------------------------
    def __init__(self, parent):


        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        sizer = wx.BoxSizer(wx.VERTICAL)

        btnPerspectiva = wx.Button(self, wx.ID_ANY,"Perspectiva")
        btnTop = wx.Button(self, wx.ID_ANY, "Cima")
        btnFront = wx.Button(self, wx.ID_ANY, "Frente")
        btnBack = wx.Button(self, wx.ID_ANY, "Atrás")
        btnRight = wx.Button(self, wx.ID_ANY, "Direita")
        btnLeft = wx.Button(self, wx.ID_ANY, "Esquerda")

        Vars.visionButtons = (btnPerspectiva,btnTop,btnFront,btnBack,btnRight,btnLeft)

        sizer.Add(btnPerspectiva, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        sizer.Add(btnTop, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        sizer.Add(btnFront, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        sizer.Add(btnBack, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        sizer.Add(btnRight, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        sizer.Add(btnLeft, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)

        self.Bind(wx.EVT_BUTTON, self.OnPerspectiva, btnPerspectiva)
        self.Bind(wx.EVT_BUTTON, self.OnTop, btnTop)
        self.Bind(wx.EVT_BUTTON, self.OnFront, btnFront)
        self.Bind(wx.EVT_BUTTON, self.OnBack, btnBack)
        self.Bind(wx.EVT_BUTTON, self.OnRight, btnRight)
        self.Bind(wx.EVT_BUTTON, self.OnLeft, btnLeft)


        self.SetSizer(sizer)

    """
        -> Função OnPerspectiva:
            Função para alternar o modo de visão para perspectiva com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnPerspectiva(self, evt):
        Vars.KitLib.setVisionOption(0)
        Vars.visionItem.SetLabelText(Vars.visionModes[0])
        Vars.KitLib.setVisionAxis(122)#122 Codigo ASCII para 'z'
        self.Parent.SetFocus()
        Vars.drawArea0.Refresh()
    """
        -> Função OnTop:
            Função para alternar o modo de visão para ortogonal de cima com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnTop(self, evt):
        Vars.KitLib.setVisionOption(5)
        Vars.visionItem.SetLabelText(Vars.visionModes[5])
        Vars.KitLib.setVisionAxis(122)#122 Codigo ASCII para 'z'
        self.Parent.SetFocus()
        Vars.drawArea0.Refresh()

    """
        -> Função OnFront:
            Função para alternar o modo de visão para ortogonal em x positivo com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnFront(self, evt):
        Vars.KitLib.setVisionOption(1)
        Vars.visionItem.SetLabelText(Vars.visionModes[1])
        Vars.KitLib.setVisionAxis(120)#120 Codigo ASCII para 'x'
        self.Parent.SetFocus()
        Vars.drawArea0.Refresh()

    """
        -> Função OnBack:
            Função para alternar o modo de visão para ortogonal em x negativo com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnBack(self, evt):
        Vars.KitLib.setVisionOption(2)
        Vars.visionItem.SetLabelText(Vars.visionModes[2])
        Vars.KitLib.setVisionAxis(120)#120 Codigo ASCII para 'x'
        self.Parent.SetFocus()
        Vars.drawArea0.Refresh()
    """
        -> Função OnRight:
            Função para alternar o modo de visão para ortogonal em y positivo com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnRight(self, evt):
        Vars.KitLib.setVisionOption(3)
        Vars.visionItem.SetLabelText(Vars.visionModes[3])
        Vars.KitLib.setVisionAxis(121)#121 Codigo ASCII para 'y'
        self.Parent.SetFocus()
        Vars.drawArea0.Refresh()

    """
        -> Função OnLeft:
            Função para alternar o modo de visão para ortogonal em y negativo com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnLeft(self, evt):
        Vars.KitLib.setVisionOption(4)
        Vars.visionItem.SetLabelText(Vars.visionModes[4])
        Vars.KitLib.setVisionAxis(121)#121 Codigo ASCII para 'y'
        self.Parent.SetFocus()
        Vars.drawArea0.Refresh()