# -*- coding: UTF-8 -*-
from OpenGLObjects import *

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
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.Bind(wx.EVT_MOUSEWHEEL, self.OnMouseScroll)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

    def OnEraseBackground(self, event):
        pass  # Do nothing, to avoid flashing on MSW.

    def OnSize(self, event):
        #wx.CallAfter(self.DoSetViewport)
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

    def OnMouseDown(self, evt):
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

            if Vars.visionOption == 0:
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

        if Vars.visionOption == 0:

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
        Vars.rightMouse = (e.GetPosition()[0],e.GetPosition()[1])
        self.PopupMenu(RightMenu(self.parent), e.GetPosition())
        self.Refresh()


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
        if Vars.visionOption == 0:
            eye = (Vars.camZoom * math.cos(Vars.theta) * math.sin(Vars.phi),
                   Vars.camZoom * math.sin(Vars.theta) * math.sin(Vars.phi), Vars.camZoom * math.cos(Vars.phi))
            up = (-Vars.camZoom * math.cos(Vars.theta) * math.cos(Vars.phi),
                  -Vars.camZoom * math.sin(Vars.theta) * math.cos(Vars.phi), Vars.camZoom * math.sin(Vars.phi))
            center = (0, 0, 0)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glViewport(0, 0, self.GetClientSize()[0], self.GetClientSize()[1])
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(60.0, self.GetClientSize()[0] / self.GetClientSize()[1], 0.1, 50)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            gluLookAt(eye[0], eye[1], eye[2], center[0], center[1], center[2], up[0], up[1], up[2])

        #Definições de câmera ortho positiva
        elif Vars.visionOption == 5 or Vars.visionOption == 1 or Vars.visionOption == 3:
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
        elif Vars.visionOption == 2 or Vars.visionOption == 4:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glViewport(0, 0, self.GetClientSize()[0], self.GetClientSize()[1])
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(Vars.orthoZoom*self.GetClientSize()[0]/self.GetClientSize()[1] - Vars.orthoCenter[1],
                    -Vars.orthoZoom*self.GetClientSize()[0]/self.GetClientSize()[1] - Vars.orthoCenter[1],
                    -Vars.orthoZoom - Vars.orthoCenter[0], Vars.orthoZoom - Vars.orthoCenter[0], -100, 100.0)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

        drawAxis()
        drawGrid()

        if Vars.cube != None:
            drawCube(Vars.cube)

        self.SwapBuffers()


"""
    ->Classe PopupMenu:
        Classe que trata sobre o menu aberto ao clique do botão direito do mouse

"""

class RightMenu(wx.Menu):
    def __init__(self, parent):
        super(RightMenu, self).__init__()

        self.parent = parent

        #Submenu adicionar
        addMenu = wx.Menu()
        addCube = wx.MenuItem(self, wx.NewId(), 'Cubo')
        addMenu.Append(addCube)
        self.AppendSubMenu(addMenu,'Adicionar')
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


        #ItemMenu minimizar
        mmi = wx.MenuItem(self, wx.NewId(), 'Minimizar')
        self.Append(mmi)
        self.Bind(wx.EVT_MENU, self.OnMinimize, mmi)

        #ItemMenu fechar
        cmi = wx.MenuItem(self, wx.NewId(), 'Fechar')
        self.Append(cmi)
        self.Bind(wx.EVT_MENU, self.OnClose, cmi)

    def OnMinimize(self, e):
        self.parent.Iconize()

    def OnClose(self, e):
        self.parent.Close()

    def OnAddCube(self,e):
        #Vars.cube = True
        x,y = Vars.rightMouse

        y = self.parent.GetClientSize()[1] - y

        if Vars.visionOption != 0:
            x = x / (Vars.drawArea.GetClientSize()[0])
            y = y / (Vars.drawArea.GetClientSize()[1])

            x = (x * 2 * Vars.orthoZoom * Vars.drawArea.GetClientSize()[0] / Vars.drawArea.GetClientSize()[1]) - (Vars.orthoZoom * Vars.drawArea.GetClientSize()[0] / Vars.drawArea.GetClientSize()[1])
            y = y * 2 * Vars.orthoZoom - Vars.orthoZoom

            if Vars.visionAxis == 'z':
                Vars.cube = (x, y, 0)
            elif Vars.visionAxis == 'x':
                Vars.cube = (0, x, y)
            elif Vars.visionAxis == 'y':
                Vars.cube = (x, 0, y)


    def OnPerspectiva(self, evt):

        Vars.visionOption = 0
        Vars.visionItem.SetLabelText(Vars.visionModes[0])
        Vars.visionAxis = 'z'
        Vars.drawArea.Refresh()

    def OnTop(self, evt):

        Vars.visionOption = 5
        Vars.visionItem.SetLabelText(Vars.visionModes[5])
        Vars.visionAxis = 'z'
        Vars.drawArea.Refresh()

    def OnFront(self, evt):

        Vars.visionOption = 1
        Vars.visionItem.SetLabelText(Vars.visionModes[1])
        Vars.visionAxis = 'x'
        Vars.drawArea.Refresh()

    def OnBack(self, evt):
        Vars.visionOption = 2
        Vars.visionItem.SetLabelText(Vars.visionModes[2])
        Vars.visionAxis = 'x'
        Vars.drawArea.Refresh()

    def OnRight(self, evt):
        Vars.visionOption = 3
        Vars.visionItem.SetLabelText(Vars.visionModes[3])
        Vars.visionAxis = 'y'
        Vars.drawArea.Refresh()

    def OnLeft(self, evt):
        Vars.visionOption = 4
        Vars.visionItem.SetLabelText(Vars.visionModes[4])
        Vars.visionAxis = 'y'
        Vars.drawArea.Refresh()