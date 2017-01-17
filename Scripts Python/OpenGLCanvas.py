# -*- coding: UTF-8 -*-
from VarsAmbient import *

"""
    ->Classe MyCanvasBase:
        Classe para manipulação geral da área de canvas do wxPython, como eventos de mouse e teclado

"""
class MyCanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.parent = parent
        self.init = False
        self.context = glcanvas.GLContext(self)

        # initial mouse position
        self.lastx = self.x = 30
        self.lasty = self.y = 30
        self.size = None
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.Bind(wx.EVT_MOUSEWHEEL, self.OnMouseScroll)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.Bind(wx.EVT_MIDDLE_DOWN, self.OnScrollClick)


    """
        -> Função OnSize:
            Função para reoganizar a viewport da drawArea assim que sofrer um resize na janela
            -> 'evt' : instância de evento, pode ou não ser usado para o tratamento do evento size
        -> Retorno: vazio
    """
    def OnSize(self, event):
        wx.CallAfter(self.DoSetViewport)
        self.DoSetViewport()
        event.Skip()

    def DoSetViewport(self):
        size = self.size = self.GetClientSize()
        self.SetCurrent(self.context)
        glViewport(0, 0, size.width, size.height)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()

    def OnScrollClick(self,e):
        Vars.toolBox.SetFocus()
        self.x, self.y = self.lastx, self.lasty = e.GetPosition()
        ponto = Vars.KitLib.getPonto3D(c_int(self.x), c_int(self.y))
        if not(Vars.shiftPress):
            Vars.KitLib.deSelectAll()
        op = Vars.KitLib.select(ponto)
        if(op):
            self.Refresh()

    def OnMouseDown(self, evt):
        Vars.toolBox.SetFocus()
        self.CaptureMouse()
        self.x, self.y = self.lastx, self.lasty = evt.GetPosition()


    def OnMouseUp(self, evt):
        try:
            self.ReleaseMouse()
        except:
            pass

    """
        -> Função OnMouseMotion:
            Função para manipular a localização da camera assim que o botão esquerdo do mouse for pressionado e o mouse for arrastado
            -> 'evt' : instância de evento, pode ou não ser usado para o tratamento do evento de mouseScroll
        -> Retorno: vazio
    """
    def OnMouseMotion(self, evt):

        if evt.Dragging() and evt.LeftIsDown():
            self.lastx, self.lasty = self.x, self.y
            self.x, self.y = evt.GetPosition()

            if Vars.KitLib.getVisionOption() == 0:
                Vars.theta = Vars.theta + (self.lastx - self.x) / 100
                Vars.phi = Vars.phi + (self.lasty - self.y) / 100
                if Vars.phi > math.pi / 2:
                    Vars.phi = math.pi / 2
                elif Vars.phi < 0:
                    Vars.phi = 0.001
            else:
                Vars.orthoCenter = ((self.lasty - self.y) / 60 + Vars.orthoCenter[0],(self.lastx - self.x) / 60 + Vars.orthoCenter[1])
            self.Refresh(False)

    """
        -> Função OnMouseScroll:
            Função para manipular o zoom da câmera assim que o scrool do mouse for ativado
            -> 'evt' : instância de evento, pode ou não ser usado para o tratamento do evento de mouseScroll
        -> Retorno: vazio
    """
    def OnMouseScroll(self, evt):

        if Vars.KitLib.getVisionOption() == 0:

            zoom = 0.3
            if evt.GetWheelRotation() > 0:

                Vars.camZoom += zoom

            else:

                Vars.camZoom -= zoom
                if Vars.camZoom < 0:
                    Vars.camZoom = 0
        else:
            zoom = 0.3
            if evt.GetWheelRotation() > 0:

                Vars.orthoZoom += zoom

            else:

                Vars.orthoZoom -= zoom
                if Vars.orthoZoom < 0:
                    Vars.orthoZoom = 0.1


        self.Refresh(False)


    """
        -> Função OnRightDown:
            Função para criar o PopupMenulogo que o botao direito do mouse for clicado
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnRightDown(self,e):
        Vars.toolBox.SetFocus()
        Vars.rightMouse = (e.GetPosition()[0],e.GetPosition()[1])
        try:
            self.PopupMenu(RightMenu(self.parent), e.GetPosition())
        except:
            pass
        self.Refresh()

#########################################################################################################################################################################################

"""
    -> Classe CubeCanvas:
        Classe para desenhar os objetos em OpenGL

"""

class CubeCanvas(MyCanvasBase):

    def InitGL(self):

        glClearColor(0.5, 0.5, 0.5, 0.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glEnable(GL_NORMALIZE)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)

    def OnDraw(self):

        #Definições de câmera perspectiva
        if Vars.KitLib.getVisionOption() == 0:
            eye = (Vars.camZoom * math.cos(Vars.theta) * math.sin(Vars.phi),
                   Vars.camZoom * math.sin(Vars.theta) * math.sin(Vars.phi), Vars.camZoom * math.cos(Vars.phi))
            up = (-Vars.camZoom * math.cos(Vars.theta) * math.cos(Vars.phi),
                  -Vars.camZoom * math.sin(Vars.theta) * math.cos(Vars.phi), Vars.camZoom * math.sin(Vars.phi))
            center = (0, 0, 0)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glViewport(0, 0, self.GetClientSize()[0], self.GetClientSize()[1])
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(60.0, self.GetClientSize()[0] / self.GetClientSize()[1], 0.01, 500)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            gluLookAt(eye[0], eye[1], eye[2], center[0], center[1], center[2], up[0], up[1], up[2])

        #Definições de câmera ortho positiva
        elif Vars.KitLib.getVisionOption() == 5 or Vars.KitLib.getVisionOption() == 1 or Vars.KitLib.getVisionOption() == 4:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glViewport(0, 0, self.GetClientSize()[0], self.GetClientSize()[1])
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(-Vars.orthoZoom*self.GetClientSize()[0]/self.GetClientSize()[1] + Vars.orthoCenter[1],
                    Vars.orthoZoom*self.GetClientSize()[0]/self.GetClientSize()[1] + Vars.orthoCenter[1],
                    -Vars.orthoZoom - Vars.orthoCenter[0], Vars.orthoZoom - Vars.orthoCenter[0], -100, 100.0)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
        #Definições de câmera ortho negativa
        elif Vars.KitLib.getVisionOption() == 2 or Vars.KitLib.getVisionOption() == 3:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glViewport(0, 0, self.GetClientSize()[0], self.GetClientSize()[1])
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(Vars.orthoZoom*self.GetClientSize()[0]/self.GetClientSize()[1] - Vars.orthoCenter[1],
                    -Vars.orthoZoom*self.GetClientSize()[0]/self.GetClientSize()[1] - Vars.orthoCenter[1],
                    -Vars.orthoZoom - Vars.orthoCenter[0], Vars.orthoZoom - Vars.orthoCenter[0], -100, 100.0)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

        Vars.KitLib.drawCena()
        Vars.KitLib.drawAxis()
        Vars.KitLib.drawGrid()


        self.SwapBuffers()

#########################################################################################################################################################################################

"""
    ->Classe PopupMenu:
        Classe que trata sobre o menu aberto ao clique do botão direito do mouse

"""

class RightMenu(wx.Menu):
    def __init__(self, parent):
        super(RightMenu, self).__init__()

        self.parent = parent

        #Submenu adicionar
        if Vars.KitLib.getVisionOption() != 0:
            addMenu = wx.Menu()
            addCube = wx.MenuItem(self, wx.NewId(), 'Cubo')
            addMenu.Append(addCube)
            self.AppendSubMenu(addMenu, 'Adicionar')
            self.Bind(wx.EVT_MENU, self.OnAddCube, addCube)

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

        #ItemMenu minimizar
        mmi = wx.MenuItem(self, wx.NewId(), 'Minimizar')
        self.Append(mmi)
        self.Bind(wx.EVT_MENU, self.OnMinimize, mmi)

        #ItemMenu fechar
        cmi = wx.MenuItem(self, wx.NewId(), 'Fechar')
        self.Append(cmi)
        self.Bind(wx.EVT_MENU, self.OnClose, cmi)


    """
        -> Função OnMinimize:
            Função para minimizar a janela com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnMinimize(self, e):
        self.parent.Iconize()

    """
        -> Função OnClose:
            Função para fechar a janela com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnClose(self, e):
        self.parent.Close()
    """
        -> Função OnAddCube:
            Função para adicionar a lista de objetos com o botão direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnAddCube(self,e):

        x,y = Vars.rightMouse

        y = self.parent.GetClientSize()[1] - y

        if Vars.KitLib.getVisionOption() != 0:
            x = x / (Vars.drawArea.GetClientSize()[0])
            y = y / (Vars.drawArea.GetClientSize()[1])

            x = (x * 2 * Vars.orthoZoom * Vars.drawArea.GetClientSize()[0] / Vars.drawArea.GetClientSize()[1]) - (Vars.orthoZoom * Vars.drawArea.GetClientSize()[0] / Vars.drawArea.GetClientSize()[1])
            y = y * 2 * Vars.orthoZoom - Vars.orthoZoom

            if Vars.KitLib.getVisionAxis() == 122: #122 Codigo ASCII para 'z'
                Vars.KitLib.addCubo(ctypes.c_float(x),ctypes.c_float(y),0)
            elif Vars.KitLib.getVisionAxis() == 120:#120 Codigo ASCII para 'x'
                if Vars.KitLib.getVisionOption() == 1:
                    Vars.KitLib.addCubo(0, ctypes.c_float(x),ctypes.c_float(y))
                else:
                    Vars.KitLib.addCubo(0, ctypes.c_float(y), ctypes.c_float(-x))
            elif Vars.KitLib.getVisionAxis() == 121:#121 Codigo ASCII para 'y'
                if Vars.KitLib.getVisionOption() == 3:
                    Vars.KitLib.addCubo(ctypes.c_float(-x), 0, ctypes.c_float(y))
                else:
                    Vars.KitLib.addCubo(ctypes.c_float(x), 0, ctypes.c_float(y))

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
        Vars.KitLib.setVisionAxis(122)  # 122 Codigo ASCII para 'z'
        Vars.drawArea.Refresh()

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
        Vars.KitLib.setVisionAxis(122)  # 122 Codigo ASCII para 'z'
        Vars.drawArea.Refresh()

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
        Vars.KitLib.setVisionAxis(120)  # 120 Codigo ASCII para 'x'
        Vars.drawArea.Refresh()

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
        Vars.KitLib.setVisionAxis(120)  # 120 Codigo ASCII para 'x'
        Vars.drawArea.Refresh()

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
        Vars.KitLib.setVisionAxis(121)  # 121 Codigo ASCII para 'y'
        Vars.drawArea.Refresh()

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
        Vars.KitLib.setVisionAxis(121)  # 121 Codigo ASCII para 'y'
        Vars.drawArea.Refresh()

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

    """
        -> Função OnClear:
            Função para deletar todos os objetos da cena
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnClear(self, evt):
        Vars.KitLib.clear()