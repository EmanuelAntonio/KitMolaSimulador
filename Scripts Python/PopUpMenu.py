# -*- coding: UTF-8 -*-
from AdicionarObjetos import *

"""
    ->Classe RightMenu:
        Classe que trata sobre o menu aberto ao clique do botão direito do mouse

"""

class RightMenu(wx.Menu):
    def __init__(self, parent):
        super(RightMenu, self).__init__()

        self.parent = parent
        if self.parent.parent.botaoSelecionado != Vars.LIVRE_SELECIONADO:
            return

        #Submenu adicionar

        addMenu = wx.Menu()
        addSphere = wx.MenuItem(self, wx.NewId(), 'Esfera')
        addSBar = wx.MenuItem(self, wx.NewId(), 'Barra Pequena')
        addLBar = wx.MenuItem(self, wx.NewId(), 'Barra Grande')
        addBase = wx.MenuItem(self, wx.NewId(), 'Base')
        addBaseX = wx.MenuItem(self, wx.NewId(), 'Base Bloqueada em X')
        addBaseY = wx.MenuItem(self, wx.NewId(), 'Base Bloqueada em Y')
        addBaseXY = wx.MenuItem(self, wx.NewId(), 'Base Bloqueada em XY')
        addLaje = wx.MenuItem(self, wx.NewId(), 'Laje')
        addSDiag = wx.MenuItem(self, wx.NewId(), 'Diagonal 9x9')
        addLDiag = wx.MenuItem(self, wx.NewId(), 'Diagonal 18x9')
        addLigRigida = wx.MenuItem(self, wx.NewId(), 'Ligação Rígida')
        if self.parent.camera.visionOption != 0:
            addMenu.Append(addSphere)
            addMenu.Append(addBase)
            addMenu.Append(addBaseX)
            addMenu.Append(addBaseY)
            addMenu.Append(addBaseXY)
        addMenu.Append(addSBar)
        addMenu.Append(addLBar)
        addMenu.Append(addLaje)
        addMenu.Append(addSDiag)
        addMenu.Append(addLDiag)
        addMenu.Append(addLigRigida)
        self.AppendSubMenu(addMenu, 'Adicionar')
        if self.parent.camera.visionOption != 0:
            self.Bind(wx.EVT_MENU, self.OnAddSphere, addSphere)
            self.Bind(wx.EVT_MENU, self.OnAddBase, addBase)
        self.Bind(wx.EVT_MENU, self.OnAddSmallBar, addSBar)
        self.Bind(wx.EVT_MENU, self.OnAddLargeBar, addLBar)
        self.Bind(wx.EVT_MENU, self.OnAddLaje, addLaje)
        self.Bind(wx.EVT_MENU, self.OnAddLaje, addLaje)
        self.Bind(wx.EVT_MENU, self.OnAddSmallDiag, addSDiag)
        self.Bind(wx.EVT_MENU, self.OnAddLargeDiag, addLDiag)
        self.Bind(wx.EVT_MENU, self.OnAddLigRigida, addLigRigida)
        self.Bind(wx.EVT_MENU, self.OnAddBaseX, addBaseX)
        self.Bind(wx.EVT_MENU, self.OnAddBaseY, addBaseY)
        self.Bind(wx.EVT_MENU, self.OnAddBaseXY, addBaseXY)

        self.AppendSeparator()

        #Submenu camera
        camMenu = wx.Menu()
        persp = wx.MenuItem(self, wx.NewId(), 'Perspectiva')
        cima = wx.MenuItem(self, wx.NewId(), 'Cima')
        frente = wx.MenuItem(self, wx.NewId(), 'Frente')
        atras = wx.MenuItem(self, wx.NewId(), 'Atrás')
        direita = wx.MenuItem(self, wx.NewId(), 'Direita')
        esquerda = wx.MenuItem(self, wx.NewId(), 'Esquerda')
        camMenu.Append(persp)
        camMenu.Append(cima)
        camMenu.Append(frente)
        camMenu.Append(atras)
        camMenu.Append(direita)
        camMenu.Append(esquerda)
        self.AppendSubMenu(camMenu, 'Câmera')
        self.Bind(wx.EVT_MENU, self.OnPerspectiva, persp)
        self.Bind(wx.EVT_MENU, self.OnTop, cima)
        self.Bind(wx.EVT_MENU, self.OnFront, frente)
        self.Bind(wx.EVT_MENU, self.OnBack, atras)
        self.Bind(wx.EVT_MENU, self.OnRight, direita)
        self.Bind(wx.EVT_MENU, self.OnLeft, esquerda)

        #submenu zoomIn zoomOut
        zoomInItem = wx.MenuItem(self, wx.NewId(), 'Zoom In')
        zoomOutItem = wx.MenuItem(self, wx.NewId(), 'Zoom Out')
        self.Append(zoomInItem)
        self.Append(zoomOutItem)
        self.Bind(wx.EVT_MENU, self.OnZoomIn, zoomInItem)
        self.Bind(wx.EVT_MENU, self.OnZoomOut, zoomOutItem)

        self.AppendSeparator()

        #ItemMenu excluir
        delItem = wx.MenuItem(self, wx.NewId(), 'Excluir')
        delAllItem = wx.MenuItem(self, wx.NewId(), 'Excluir Selecionados')
        removeAll = wx.MenuItem(self,wx.NewId(), 'Limpar Cena')
        self.Append(delItem)
        self.Append(delAllItem)
        self.Append(removeAll)
        self.Bind(wx.EVT_MENU, self.OnDel, delItem)
        self.Bind(wx.EVT_MENU, self.OnDelAll, delAllItem)
        self.Bind(wx.EVT_MENU, self.OnClear, removeAll)

        self.AppendSeparator()

        #ItemSelectAll
        selectItem = wx.MenuItem(self, wx.NewId(), 'Selecionar Tudo')
        self.Append(selectItem)
        self.Bind(wx.EVT_MENU, self.OnSelectAll, selectItem)

        #ItemMenu setFocus
        focusItem = wx.MenuItem(self, wx.NewId(), 'Mudar Foco Para Objeto')
        self.Append(focusItem)
        self.Bind(wx.EVT_MENU, self.OnSetFocus, focusItem)

        #ItemMenu setFocusToSelect
        focusItem = wx.MenuItem(self, wx.NewId(), 'Mudar Foco Para Seleção')
        self.Append(focusItem)
        self.Bind(wx.EVT_MENU, self.OnSetFocusAll, focusItem)

        #ItemMenu DuplicarSelect
        duplicaItem = wx.MenuItem(self, wx.NewId(), 'Duplicar')
        self.Append(duplicaItem)
        self.Bind(wx.EVT_MENU, self.OnDuplicaSelect, duplicaItem)

        self.AppendSeparator()

        #ItemMenu fechar
        cmi = wx.MenuItem(self, wx.NewId(), 'Fechar')
        self.Append(cmi)
        self.Bind(wx.EVT_MENU, self.OnClose, cmi)


    """
        -> Função OnClose:
            Função para fechar a janela com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnClose(self, e):
        self.parent.parent.Close()

    def OnAddLaje(self, e):

        AdicionarObjetos.OnAddLaje(self.parent.parent)

    def OnZoomIn(self, e):
        self.parent.OnZoomIn()

    def OnZoomOut(self, e):
        self.parent.OnZoomOut()

    def OnDuplicaSelect(self, e):
        if Vars.KitLib.duplicaSelect():
            self.parent.parent.moveObjetos = (True,Vars.ASCII_0)
        self.parent.parent.OnRefreshAll()
        self.parent.parent.atualizaPrecisaSalvar(True)

    def OnAddSphere(self, e):

        AdicionarObjetos.OnAddSphere(self.parent, self.parent.parent)

    """
        -> Função OnPerspectiva:
            Função para alternar o modo de visão para perspectiva com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnPerspectiva(self, evt):
        self.parent.camera.visionOption = 0
        #Vars.visionItem.SetLabelText(Vars.visionModes[0])
        self.parent.camera.visionAxis = Vars.ASCII_Z  # 122 Codigo ASCII para 'z'
        self.parent.Refresh(True)

    """
        -> Função OnTop:
            Função para alternar o modo de visão para ortogonal de cima com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnTop(self, evt):
        self.parent.camera.visionOption = 5
        #Vars.visionItem.SetLabelText(Vars.visionModes[5])
        self.parent.camera.visionAxis = Vars.ASCII_Z  # 122 Codigo ASCII para 'z'
        self.parent.Refresh(True)

    """
        -> Função OnFront:
            Função para alternar o modo de visão para ortogonal em x positivo com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnFront(self, evt):
        self.parent.caemera.visionOption = 1
        #Vars.visionItem.SetLabelText(Vars.visionModes[1])
        self.parent.camera.visionAxis = Vars.ASCII_X  # 120 Codigo ASCII para 'x'
        self.parent.Refresh(True)

    """
        -> Função OnBack:
            Função para alternar o modo de visão para ortogonal em x negativo com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnBack(self, evt):
        self.parent.camera.visionOption = 2
        #Vars.visionItem.SetLabelText(Vars.visionModes[2])
        self.parent.camera.visionAxis = Vars.ASCII_X  # 120 Codigo ASCII para 'x'
        self.parent.Refresh(True)

    """
        -> Função OnRight:
            Função para alternar o modo de visão para ortogonal em y positivo com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnRight(self, evt):
        self.parent.camera.visionOption = 3
        #Vars.visionItem.SetLabelText(Vars.visionModes[3])
        self.parent.camera.visionAxis = Vars.ASCII_Y  # 121 Codigo ASCII para 'y'
        self.parent.Refresh(True)

    """
        -> Função OnLeft:
            Função para alternar o modo de visão para ortogonal em y negativo com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnLeft(self, evt):
        self.parent.camera.visionOption = 4
        #Vars.visionItem.SetLabelText(Vars.visionModes[4])
        self.parent.camera.visionAxis = Vars.ASCII_Y  # 121 Codigo ASCII para 'y'
        self.parent.Refresh()

    """
        -> Função OnSelectAll:
            Função para selecionar todos os objetos da cena
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnSelectAll(self,e):
        Vars.KitLib.selectAll()
    """
        -> Função OnDel:
            Função para deletar um objeto da cena
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnDel(self,evt):
        x, y = Vars.rightMouse
        ponto = Vars.KitLib.getPonto3D(c_int(x), c_int(y))
        Vars.KitLib.remover(ponto)

    """
        -> Função OnDelAll:
            Função para deletar todos os objetos selecionados da cena
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnDelAll(self, evt):
        Vars.KitLib.removeAll()
        if Vars.KitLib.desfazerSize() > 0:
            self.parent.parent.toolbar.EnableTool(wx.ID_UNDO, True)
        if Vars.KitLib.refazerSize() > 0:
            self.parent.parent.toolbar.EnableTool(wx.ID_REDO, True)

    """
        -> Função OnClear:
            Função para deletar todos os objetos da cena
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnClear(self, evt):
        Vars.KitLib.clear()

    """
        -> Função OnSetFocus:
            Função para altera o foco da câmera para um objeto
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnSetFocus(self,evt):
        ponto = Vars.KitLib.getPonto3D(c_int(Vars.rightMouse[0]), c_int(Vars.rightMouse[1]))
        centro = [0, 0, 0]
        centro_size = len(centro)
        centro = (ctypes.c_float * centro_size)(*centro)
        if Vars.KitLib.getCenter(ponto, centro):
            self.parent.centro = (centro[0], centro[1], centro[2])
            self.parent.parent.tabs.tabConfig.txtFocusX.SetValue(str(round(centro[0],3)))
            self.parent.parent.tabs.tabConfig.txtFocusY.SetValue(str(round(centro[1],3)))
            self.parent.parent.tabs.tabConfig.txtFocusZ.SetValue(str(round(centro[2],3)))
        self.parent.parent.ultimoDrawSelected.Refresh()


    """
        -> Função OnSetFocusAll:
            Função para altera o foco da câmera para a seleção de objetos
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnSetFocusAll(self, e):

        centro = [0, 0, 0]
        centro_size = len(centro)
        centro = (ctypes.c_float * centro_size)(*centro)
        if Vars.KitLib.setFocusToSelect(centro):
            if self.parent.camera.visionOption == Vars.VISION_Z_PERSP:
                self.parent.camera.centro = (centro[0], centro[1], centro[2])
                Vars.toolBox.tabConfig.txtFocusX.SetValue(str(round(centro[0], 3)))
            elif self.parent.camera.visionOption == Vars.VISION_Z_ORTHO:
                self.parent.camera.orthoCenter = (-centro[0], centro[1], centro[2])
                Vars.toolBox.tabConfig.txtFocusX.SetValue(str(round(-centro[0], 3)))
            self.parent.parent.tabs.tabConfig.txtFocusY.SetValue(str(round(centro[1], 3)))
            self.parent.parent.tabs.tabConfig.txtFocusZ.SetValue(str(round(centro[2], 3)))
        self.parent.parent.OnRefreshAll()

    """
        -> Função OnAddBar:
            Função para adicionar uma barra na lista de objetos
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnAddSmallBar(self,e):

        AdicionarObjetos.OnAddSmallBar(self.parent, self.parent.parent)

    def OnAddLargeBar(self,e):

        AdicionarObjetos.OnAddLargeBar(self.parent, self.parent.parent)

    def OnAddBase(self,e):

        AdicionarObjetos.OnAddBase(Vars.BASE_LIVRE, self.parent,self.parent.parent)

    def OnAddSmallDiag(self,e):
        AdicionarObjetos.OnAddSmallDiag(self.parent,self.parent.parent)

    def OnAddLargeDiag(self, e):
        AdicionarObjetos.OnAddLargeDiag(self.parent, self.parent.parent)

    def OnAddLigRigida(self,e):
        AdicionarObjetos.OnAddLigRigida(self.parent, self.parent.parent)

    def OnAddBaseX(self, e):

        AdicionarObjetos.OnAddBase(Vars.BASE_BLOQUEADA_X, self.parent, self.parent.parent)

    def OnAddBaseY(self, e):

        AdicionarObjetos.OnAddBase(Vars.BASE_BLOQUEADA_Y, self.parent, self.parent.parent)

    def OnAddBaseXY(self, e):

        AdicionarObjetos.OnAddBase(Vars.BASE_BLOQUEADA_XY, self.parent, self.parent.parent)