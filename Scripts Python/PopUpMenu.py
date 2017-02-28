# -*- coding: UTF-8 -*-
from VarsAmbient import *

"""
    ->Classe RightMenu:
        Classe que trata sobre o menu aberto ao clique do botão direito do mouse

"""

class RightMenu(wx.Menu):
    def __init__(self, parent):
        super(RightMenu, self).__init__()

        self.parent = parent

        #Submenu adicionar
        if self.parent.visionOption != 0:
            addMenu = wx.Menu()
            addSphere = wx.MenuItem(self, wx.NewId(),'Esfera')
            addSBar = wx.MenuItem(self, wx.NewId(), 'Barra Pequena')
            addLBar = wx.MenuItem(self, wx.NewId(), 'Barra Grande')
            addBase = wx.MenuItem(self, wx.NewId(), 'Base')
            addMenu.Append(addSphere)
            addMenu.Append(addSBar)
            addMenu.Append(addLBar)
            addMenu.Append(addBase)
            self.AppendSubMenu(addMenu, 'Adicionar')
            self.Bind(wx.EVT_MENU, self.OnAddSphere, addSphere)
            self.Bind(wx.EVT_MENU, self.OnAddSmallBar, addSBar)
            self.Bind(wx.EVT_MENU, self.OnAddLargeBar, addLBar)
            self.Bind(wx.EVT_MENU, self.OnAddBase, addBase)

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
        self.parent.Close()

    def OnAddSphere(self, e):

        x, y = Vars.rightMouse
        if self.parent.visionOption != Vars.VISION_Z_PERSP:

            ponto = [0, 0, 0]
            ponto_size = len(ponto)
            ponto = (ctypes.c_float * ponto_size)(*ponto)
            Vars.KitLib.getPonto3DFloat(c_int(x), c_int(y), ponto)
            if self.parent.visionAxis == Vars.ASCII_Z:  # 122 Codigo ASCII para 'z'
                x = ponto[0]
                y = ponto[1]
                if self.parent.parent.tabs.tabConfig.blockInsert:
                    space = c_float(Vars.KitLib.getEspacoGrid()).value
                    x = x / space
                    dx = x - int(x)
                    dx = math.fabs(dx)
                    if dx < 0.5:
                        x = int(x) * space
                    else:
                        if x >= 0:
                            x = (int(x) + 1) * space
                        else:
                            x = (int(x) - 1) * space
                    y = y / space
                    dy = y - int(y)
                    dy = math.fabs(dy)
                    if dy < 0.5:
                        y = int(y) * space
                    else:
                        if y >= 0:
                            y = (int(y) + 1) * space
                        else:
                            y = (int(y) - 1) * space
                Vars.KitLib.addSphere(c_float(x), c_float(y), 0)
            elif self.parent.visionAxis == Vars.ASCII_X:  # 120 Codigo ASCII para 'x'

                x = ponto[0]
                y = ponto[1]
                if self.parent.parent.tabs.tabConfig.blockInsert:
                    space = c_float(Vars.KitLib.getEspacoGrid()).value
                    x = x / space
                    dx = x - int(x)
                    dx = math.fabs(dx)
                    if dx < 0.5:
                        x = int(x) * space
                    else:
                        if x >= 0:
                            x = (int(x) + 1) * space
                        else:
                            x = (int(x) - 1) * space
                    y = y / space
                    dy = y - int(y)
                    dy = math.fabs(dy)
                    if dy < 0.5:
                        y = int(y) * space
                    else:
                        if y >= 0:
                            y = (int(y) + 1) * space
                        else:
                            y = (int(y) - 1) * space
                if self.parent.visionOption == Vars.VISION_X_POS:
                    Vars.KitLib.addSphere(0, ctypes.c_float(x), ctypes.c_float(y))
                else:
                    Vars.KitLib.addSphere(0, ctypes.c_float(y), ctypes.c_float(x))
            elif self.parent.visionAxis == Vars.ASCII_Y:  # 121 Codigo ASCII para 'y'
                x = ponto[0]
                y = ponto[1]
                if self.parent.parent.tabs.tabConfig.blockInsert:
                    space = c_float(Vars.KitLib.getEspacoGrid()).value
                    x = x / space
                    dx = x - int(x)
                    dx = math.fabs(dx)
                    if dx < 0.5:
                        x = int(x) * space
                    else:
                        if x >= 0:
                            x = (int(x) + 1) * space
                        else:
                            x = (int(x) - 1) * space
                    y = y / space
                    dy = y - int(y)
                    dy = math.fabs(dy)
                    if dy < 0.5:
                        y = int(y) * space
                    else:
                        if y >= 0:
                            y = (int(y) + 1) * space
                        else:
                            y = (int(y) - 1) * space

                Vars.KitLib.addSphere(ctypes.c_float(x), 0, ctypes.c_float(y))

        Vars.drawArea0.Refresh(False)
        Vars.drawArea1.Refresh(False)
        Vars.drawArea2.Refresh(False)
        Vars.drawArea3.Refresh(False)

    """
        -> Função OnPerspectiva:
            Função para alternar o modo de visão para perspectiva com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnPerspectiva(self, evt):
        self.parent.visionOption = 0
        Vars.visionItem.SetLabelText(Vars.visionModes[0])
        self.parent.visionAxis = Vars.ASCII_Z  # 122 Codigo ASCII para 'z'
        self.parent.Refresh()

    """
        -> Função OnTop:
            Função para alternar o modo de visão para ortogonal de cima com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnTop(self, evt):
        self.parent.visionOption = 5
        Vars.visionItem.SetLabelText(Vars.visionModes[5])
        Vars.KitLib.setVisionAxis = Vars.ASCII_Z  # 122 Codigo ASCII para 'z'
        self.parent.Refresh()

    """
        -> Função OnFront:
            Função para alternar o modo de visão para ortogonal em x positivo com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnFront(self, evt):
        self.parent.visionOption = 1
        Vars.visionItem.SetLabelText(Vars.visionModes[1])
        self.parent.visionAxis = Vars.ASCII_X  # 120 Codigo ASCII para 'x'
        self.parent.Refresh()

    """
        -> Função OnBack:
            Função para alternar o modo de visão para ortogonal em x negativo com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnBack(self, evt):
        self.parent.visionOption = 2
        Vars.visionItem.SetLabelText(Vars.visionModes[2])
        Vars.KitLib.setVisionAxis = Vars.ASCII_X  # 120 Codigo ASCII para 'x'
        self.parent.Refresh()

    """
        -> Função OnRight:
            Função para alternar o modo de visão para ortogonal em y positivo com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnRight(self, evt):
        self.parent.visionOption = 3
        Vars.visionItem.SetLabelText(Vars.visionModes[3])
        Vars.KitLib.setVisionAxis = Vars.ASCII_Y  # 121 Codigo ASCII para 'y'
        self.parent.Refresh()

    """
        -> Função OnLeft:
            Função para alternar o modo de visão para ortogonal em y negativo com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnLeft(self, evt):
        self.parent.visionOption = 4
        Vars.visionItem.SetLabelText(Vars.visionModes[4])
        Vars.KitLib.setVisionAxis = Vars.ASCII_Y  # 121 Codigo ASCII para 'y'
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
            Vars.toolBar.EnableTool(wx.ID_UNDO, True)
        if Vars.KitLib.refazerSize() > 0:
            Vars.toolBar.EnableTool(wx.ID_REDO, True)

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
            Vars.centro = (centro[0], centro[1], centro[2])
            Vars.toolBox.tabConfig.txtFocusX.SetValue(str(round(centro[0],3)))
            Vars.toolBox.tabConfig.txtFocusY.SetValue(str(round(centro[1],3)))
            Vars.toolBox.tabConfig.txtFocusZ.SetValue(str(round(centro[2],3)))
        Vars.drawArea.Refresh()


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
            if self.parent.visionOption == Vars.VISION_Z_PERSP:
                self.parent.centro = (centro[0], centro[1], centro[2])
                Vars.toolBox.tabConfig.txtFocusX.SetValue(str(round(centro[0], 3)))
            elif self.parent.visionOption == Vars.VISION_Z_ORTHO:
                self.parent.orthoCenter = (-centro[0], centro[1], centro[2])
                Vars.toolBox.tabConfig.txtFocusX.SetValue(str(round(-centro[0], 3)))
            Vars.toolBox.tabConfig.txtFocusY.SetValue(str(round(centro[1], 3)))
            Vars.toolBox.tabConfig.txtFocusZ.SetValue(str(round(centro[2], 3)))
        Vars.drawArea0.Refresh()
        Vars.drawArea1.Refresh()
        Vars.drawArea2.Refresh()
        Vars.drawArea3.Refresh()

    """
        -> Função OnAddBar:
            Função para adicionar uma barra na lista de objetos
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnAddSmallBar(self,e):

        BAR_SMALL = 2
        add = Vars.KitLib.addBar(BAR_SMALL)
        if not(add):
            msg = "Para adicionar uma barra pequena certifique-se que tenha duas esferas selecionadas e que a distância entre elas seja de 7.5 cm."
            msgCx = wx.MessageDialog(None, msg, "ERRO!", wx.OK)
            msgCx.ShowModal()
            msgCx.Destroy()
        Vars.drawArea0.Refresh()
        Vars.drawArea1.Refresh()
        Vars.drawArea2.Refresh()
        Vars.drawArea3.Refresh()
        self.parent.Refresh()

    def OnAddLargeBar(self,e):

        BAR_LARGE = 3
        add = Vars.KitLib.addBar(BAR_LARGE)
        if not(add):
            msg = "Para adicionar uma barra grande certifique-se que tenha duas esferas selecionadas e que a distância entre elas seja de 16.3 cm."
            msgCx = wx.MessageDialog(None, msg, "ERRO!", wx.OK)
            msgCx.ShowModal()
            msgCx.Destroy()

        Vars.drawArea0.Refresh()
        Vars.drawArea1.Refresh()
        Vars.drawArea2.Refresh()
        Vars.drawArea3.Refresh()
        self.parent.Refresh()

    def OnAddBase(self,e):

        x, y = Vars.rightMouse
        if self.parent.visionOption != Vars.VISION_Z_PERSP:

            ponto = [0, 0, 0]
            ponto_size = len(ponto)
            ponto = (ctypes.c_float * ponto_size)(*ponto)
            Vars.KitLib.getPonto3DFloat(c_int(x), c_int(y), ponto)
            if self.parent.visionAxis == Vars.ASCII_Z:  # 122 Codigo ASCII para 'z'
                x = ponto[0]
                y = ponto[1]
                if self.parent.parent.tabs.tabConfig.blockInsert:
                    space = c_float(Vars.KitLib.getEspacoGrid()).value
                    x = x / space
                    dx = x - int(x)
                    dx = math.fabs(dx)
                    if dx < 0.5:
                        x = int(x) * space
                    else:
                        if x >= 0:
                            x = (int(x) + 1) * space
                        else:
                            x = (int(x) - 1) * space
                    y = y / space
                    dy = y - int(y)
                    dy = math.fabs(dy)
                    if dy < 0.5:
                        y = int(y) * space
                    else:
                        if y >= 0:
                            y = (int(y) + 1) * space
                        else:
                            y = (int(y) - 1) * space
                Vars.KitLib.addBase(c_float(x), c_float(y), 0)
            elif self.parent.visionAxis == Vars.ASCII_X:  # 120 Codigo ASCII para 'x'

                x = ponto[0]
                y = ponto[1]
                if self.parent.parent.tabs.tabConfig.blockInsert:
                    space = c_float(Vars.KitLib.getEspacoGrid()).value
                    x = x / space
                    dx = x - int(x)
                    dx = math.fabs(dx)
                    if dx < 0.5:
                        x = int(x) * space
                    else:
                        if x >= 0:
                            x = (int(x) + 1) * space
                        else:
                            x = (int(x) - 1) * space
                    y = y / space
                    dy = y - int(y)
                    dy = math.fabs(dy)
                    if dy < 0.5:
                        y = int(y) * space
                    else:
                        if y >= 0:
                            y = (int(y) + 1) * space
                        else:
                            y = (int(y) - 1) * space
                if self.parent.visionOption == Vars.VISION_X_POS:
                    Vars.KitLib.addBase(0, ctypes.c_float(x), ctypes.c_float(y))
                else:
                    Vars.KitLib.addBase(0, ctypes.c_float(y), ctypes.c_float(x))
            elif self.parent.visionAxis == Vars.ASCII_Y:  # 121 Codigo ASCII para 'y'
                x = ponto[0]
                y = ponto[1]
                if self.parent.parent.tabs.tabConfig.blockInsert:
                    space = c_float(Vars.KitLib.getEspacoGrid()).value
                    x = x / space
                    dx = x - int(x)
                    dx = math.fabs(dx)
                    if dx < 0.5:
                        x = int(x) * space
                    else:
                        if x >= 0:
                            x = (int(x) + 1) * space
                        else:
                            x = (int(x) - 1) * space
                    y = y / space
                    dy = y - int(y)
                    dy = math.fabs(dy)
                    if dy < 0.5:
                        y = int(y) * space
                    else:
                        if y >= 0:
                            y = (int(y) + 1) * space
                        else:
                            y = (int(y) - 1) * space

                Vars.KitLib.addBase(ctypes.c_float(x), 0, ctypes.c_float(y))

        Vars.drawArea0.Refresh()
        Vars.drawArea1.Refresh()
        Vars.drawArea2.Refresh()
        Vars.drawArea3.Refresh()
        self.parent.Refresh()