# -*- coding: UTF-8 -*-
from PopUpMenu import *

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
        self.Bind(wx.EVT_IDLE, self.OnIdle)

    def OnIdle(self, e):
        self.Refresh(True)
        e.Skip()
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
        self.x, self.y = self.lastx, self.lasty = e.GetPosition()
        ponto = Vars.KitLib.getPonto3D(c_int(self.x), c_int(self.y))
        if not(Vars.shiftPress):
            Vars.KitLib.deSelectAll()
        Vars.KitLib.select(ponto)
        self.Refresh()


    def OnMouseDown(self, evt):
        Vars.toolBox.SetFocus()
        self.CaptureMouse()
        self.x, self.y = self.lastx, self.lasty = evt.GetPosition()
        Vars.centroAux = Vars.centro
        if(Vars.moveObjetos):
            ponto = Vars.KitLib.getPonto3D(c_int(self.x), c_int(self.y))
            print(Vars.KitLib.selectMoveSeta(ponto))


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

            if Vars.ctrlPress and Vars.KitLib.getVisionOption() == 0:

                dTheta = (-math.sin(Vars.theta),
                         math.cos(Vars.theta), 0)

                dPhi = (-math.cos(Vars.theta) * math.cos(Vars.phi),
                        -math.sin(Vars.theta) * math.cos(Vars.phi),
                        math.sin(Vars.phi))

                xCentro = Vars.centro[0] + (dTheta[0] * (self.lastx - self.x)/50) + (dPhi[0] * (self.y - self.lasty)/50)
                yCentro = Vars.centro[1] + (dTheta[1] * (self.lastx - self.x)/50) + (dPhi[1] * (self.y - self.lasty)/50)
                zCentro = Vars.centro[2] - dPhi[2] * (self.lasty - self.y)/50

                Vars.centro = (xCentro, yCentro, zCentro)
                self.parent.tabs.tabConfig.txtFocusX.SetValue(str(round(Vars.centro[0],3)))
                self.parent.tabs.tabConfig.txtFocusY.SetValue(str(round(Vars.centro[1],3)))
                self.parent.tabs.tabConfig.txtFocusZ.SetValue(str(round(Vars.centro[2],3)))
            else:
               if Vars.KitLib.getVisionOption() == 0:
                   Vars.theta = Vars.theta + (self.lastx - self.x) / 100
                   Vars.phi = Vars.phi + (self.lasty - self.y) / 100
                   if Vars.phi > math.pi / 2:
                       Vars.phi = math.pi / 2
                   elif Vars.phi < 0:
                       Vars.phi = 0.001
               else:
                   Vars.orthoCenter = (
                   (self.lasty - self.y) / 60 + Vars.orthoCenter[0], (self.lastx - self.x) / 60 + Vars.orthoCenter[1])
            self.Refresh(False)

    """
        -> Função OnMouseScroll:
            Função para manipular o zoom da câmera assim que o scrool do mouse for ativado
            -> 'evt' : instância de evento, pode ou não ser usado para o tratamento do evento de mouseScroll
        -> Retorno: vazio
    """
    def OnMouseScroll(self, evt):

        if Vars.KitLib.getVisionOption() == 0:

            zoom = 0.8
            if evt.GetWheelRotation() > 0:

                Vars.camZoom += zoom

            else:

                Vars.camZoom -= zoom
                if Vars.camZoom <= 0:
                    Vars.camZoom = 0.2
        else:
            zoom = 0.8
            if evt.GetWheelRotation() > 0:

                Vars.orthoZoom += zoom

            else:

                Vars.orthoZoom -= zoom
                if Vars.orthoZoom <= 0:
                    Vars.orthoZoom = 0.2


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
            eye = (Vars.camZoom * math.cos(Vars.theta) * math.sin(Vars.phi) + Vars.centro[0],
                   Vars.camZoom * math.sin(Vars.theta) * math.sin(Vars.phi) + Vars.centro[1], Vars.camZoom * math.cos(Vars.phi) + Vars.centro[2])
            up = (-Vars.camZoom * math.cos(Vars.theta) * math.cos(Vars.phi),
                  -Vars.camZoom * math.sin(Vars.theta) * math.cos(Vars.phi), Vars.camZoom * math.sin(Vars.phi))

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glViewport(0, 0, self.GetClientSize()[0], self.GetClientSize()[1])
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(60.0, self.GetClientSize()[0] / self.GetClientSize()[1], 0.01, 500)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            gluLookAt(eye[0], eye[1], eye[2], Vars.centro[0], Vars.centro[1], Vars.centro[2], up[0], up[1], up[2])

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
        if Vars.moveObjetos:
            Vars.KitLib.drawMoveAxis()


        self.SwapBuffers()
