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

    def OnMouseMotion(self, evt):

        if evt.Dragging() and evt.LeftIsDown():
            self.lastx, self.lasty = self.x, self.y
            self.x, self.y = evt.GetPosition()
            Vars.theta = Vars.theta + (self.lastx - self.x)/100
            Vars.phi = Vars.phi + (self.lasty - self.y)/100

            if Vars.phi > math.pi / 2:
                Vars.phi = math.pi / 2
            elif Vars.phi < 0:
                Vars.phi = 0.001
            self.Refresh(False)

    """
        -> Função OnMouseScroll:
            Função para manipular o zoom da câmera assim que o scrool do mouse for ativado
            -> 'evt' : instância de evento, pode ou não ser usado para o tratamento do evento de mouseScroll
        -> Retorno: vazio
    """
    def OnMouseScroll(self, evt):

        zoom = 0.3
        if evt.GetWheelRotation() > 0:

            Vars.camZoom += zoom

        else:

            Vars.camZoom -= zoom
            if Vars.camZoom < 0:

                Vars.camZoom = 0

        self.Refresh(False)


    """
        -> Função OnRightDown:
            Função para criar o PopupMenulogo que o botao direito do mouse for clicado
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnRightDown(self,e):
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
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

    def OnDraw(self):

        eye = (Vars.camZoom*math.cos(Vars.theta)*math.sin(Vars.phi), Vars.camZoom*math.sin(Vars.theta)*math.sin(Vars.phi), Vars.camZoom*math.cos(Vars.phi))
        up = (-Vars.camZoom*math.cos(Vars.theta)*math.cos(Vars.phi), -Vars.camZoom*math.sin(Vars.theta)*math.cos(Vars.phi), Vars.camZoom*math.sin(Vars.phi))
        center = (0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glViewport(0, 0, self.GetClientSize()[0], self.GetClientSize()[1])
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, self.GetClientSize()[0] / self.GetClientSize()[1], 0.1, 50)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(eye[0], eye[1], eye[2], center[0], center[1], center[2], up[0],up[1],up[2])

        drawAxis()
        drawGrid()

        if Vars.cube:
            drawCubeZero()

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
        Vars.cube = True