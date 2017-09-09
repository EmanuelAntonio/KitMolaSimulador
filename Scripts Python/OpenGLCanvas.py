# -*- coding: UTF-8 -*-
from PopUpMenu import *
from MouseEvent import *
from Camera import *

"""
    ->Classe CanvasBase:
        Classe para manipulação do GLcanvas, responsável pela definição inicial do draw do OpenGL e da captura de eventos de mouse

"""
class CanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent, ref):
        attrib = (glcanvas.WX_GL_RGBA,
                  glcanvas.WX_GL_DOUBLEBUFFER,
                  glcanvas.WX_GL_DEPTH_SIZE,24)
        glcanvas.GLCanvas.__init__(self, parent, -1,attrib)
        self.parent = parent
        self.init = False
        self.context = glcanvas.GLContext(self)
        self.numJanela = ref # Variável para armazenar o id da janela
        self.dClickEvent = False #Variável referênte a se o usuário está durante o evento de duplo click do mouse, usado para não disparar o evento mouse_motion
        self.dx = 0 # variável que controla o quanto de deslocamento nesse eixo ocorreu assim que começou o evento de mouseMotion
        self.dy = 0
        self.dz = 0

        self.camera = Camera(ref,self)

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
        self.Bind(wx.EVT_LEFT_DCLICK, self.OnDClick)
        self.Bind(wx.EVT_MIDDLE_UP, self.OnScrollMotion)
        self.Bind(wx.EVT_IDLE, self.OnIdle)


    def OnIdle(self, e):

        if Vars.KitSim.getSSim():
            self.Refresh(True)
        else:
            e.Skip()

    def OnScrollMotion(self, e):
        try:
            self.ReleaseMouse()
        except:
            pass
    def OnDClick(self, e):

        self.dClickEvent = True
        if Vars.drawPrincipal == -1:
            Vars.drawPrincipal = self.numJanela
            if self.numJanela == 0:
                self.parent.drawArea1.Hide()
                self.parent.drawArea2.Hide()
                self.parent.drawArea3.Hide()
                Vars.lineDown.Hide()
                Vars.lineUp.Hide()
                Vars.lineBox.Hide()
                Vars.boxDown.Hide(True)
                Vars.boxUp.Layout()
                Vars.boxDraw.Layout()

            elif self.numJanela == 1:
                self.parent.drawArea0.Hide()
                self.parent.drawArea2.Hide()
                self.parent.drawArea3.Hide()
                Vars.lineDown.Hide()
                Vars.lineUp.Hide()
                Vars.lineBox.Hide()
                Vars.boxDown.Hide(True)
                Vars.boxUp.Layout()
                Vars.boxDraw.Layout()

            elif self.numJanela == 2:

                self.parent.drawArea0.Hide()
                self.parent.drawArea1.Hide()
                self.parent.drawArea3.Hide()
                Vars.lineDown.Hide()
                Vars.lineUp.Hide()
                Vars.lineBox.Hide()
                Vars.boxUp.Hide(True)
                Vars.boxDown.Layout()
                Vars.boxDraw.Layout()

            else:

                self.parent.drawArea0.Hide()
                self.parent.drawArea1.Hide()
                self.parent.drawArea2.Hide()
                Vars.lineDown.Hide()
                Vars.lineUp.Hide()
                Vars.lineBox.Hide()
                Vars.boxUp.Hide(True)
                Vars.boxDown.Layout()
                Vars.boxDraw.Layout()

        else:
            Vars.drawPrincipal = -1
            self.parent.drawArea0.Show()
            self.parent.drawArea1.Show()
            self.parent.drawArea2.Show()
            self.parent.drawArea3.Show()
            Vars.lineDown.Show()
            Vars.lineUp.Show()
            Vars.lineBox.Show()
            Vars.boxUp.Show(True)
            Vars.boxDown.Show(True)
            Vars.boxDown.Layout()
            Vars.boxUp.Layout()
            Vars.boxDraw.Layout()

        self.parent.OnRefreshAll()
        self.Refresh(True)

    """
        -> Função OnSize:
            Função para reoganizar a viewport da drawArea assim que sofrer um resize na janela
            -> 'evt' : instância de evento, pode ou não ser usado para o tratamento do evento size
        -> Retorno: vazio
    """
    def OnSize(self, event):
        wx.CallAfter(self.DoSetViewport)
        self.DoSetViewport()

    def DoSetViewport(self):
        self.size = self.GetClientSize()
        self.SetCurrent(self.context)
        glViewport(0, 0, self.size.width, self.size.height)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.SetCurrent(self.context)
        if not self.init:
            self.InitGL()
            self.init = True
        self.OnDraw()

    def OnMouseDown(self,e):

        MouseEvent.OnMouseDown(e,self,self.parent)


    def OnScrollClick(self, evt):

        MouseEvent.OnScrollClick(evt, self, self.parent)

    def OnMouseUp(self, evt):

        MouseEvent.OnMouseUp(self,self.parent)

    def moveSelectX(self,xDes, spaceGrid):

        self.dx += xDes * spaceGrid
        if self.dx >= self.parent.tabs.tabConfig.blockInsert[1]:
            Vars.KitLib.moveSelect(c_float(self.parent.tabs.tabConfig.blockInsert[1]), c_float(0.0), c_float(0.0))
            self.dx = 0
        elif self.dx <= -self.parent.tabs.tabConfig.blockInsert[1]:
            Vars.KitLib.moveSelect(c_float(-self.parent.tabs.tabConfig.blockInsert[1]), c_float(0.0), c_float(0.0))
            self.dx = 0

    def moveSelectY(self,yDes, spaceGrid):
        self.dy += yDes * spaceGrid
        if self.dy >= self.parent.tabs.tabConfig.blockInsert[1]:
            Vars.KitLib.moveSelect(c_float(0.0), c_float(self.parent.tabs.tabConfig.blockInsert[1]), c_float(0.0))
            self.dy = 0
        elif self.dy <= -self.parent.tabs.tabConfig.blockInsert[1]:
            Vars.KitLib.moveSelect(c_float(0.0), c_float(-self.parent.tabs.tabConfig.blockInsert[1]), c_float(0.0))
            self.dy = 0

    def moveSelectZ(self,zDes, spaceGrid):
        self.dz += zDes * spaceGrid
        if self.dz >= self.parent.tabs.tabConfig.blockInsert[1]:
            Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(self.parent.tabs.tabConfig.blockInsert[1]))
            self.dz = 0
        elif self.dz <= -self.parent.tabs.tabConfig.blockInsert[1]:
            Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(-self.parent.tabs.tabConfig.blockInsert[1]))
            self.dz = 0
    """
        -> Função OnMouseMotion:
            Função para manipular a localização da camera assim que o botão esquerdo do mouse for pressionado e o mouse for arrastado
            -> 'evt' : instância de evento, pode ou não ser usado para o tratamento do evento de mouseScroll
        -> Retorno: vazio
    """
    def OnMouseMotion(self, evt):

        MouseEvent.OnMouseMotion(evt,self,self.parent)

    def OnZoomIn(self):
        if self.camera.visionOption == Vars.VISION_Z_PERSP:
            zoom = 0.5
            self.camera.camZoom -= zoom
            if self.camera.camZoom <= 0:
                self.camera.camZoom = 0.2
        else:
            zoom = 0.5
            self.camera.orthoZoom -= zoom
            if self.camera.orthoZoom <= 0:
                self.camera.orthoZoom = 0.2


        self.parent.Refresh(False)

    def OnZoomOut(self):
        if self.camera.visionOption == Vars.VISION_Z_PERSP:

            zoom = 0.5

            self.camera.camZoom += zoom

        else:
            zoom = 0.5
            self.camera.orthoZoom += zoom



        self.Refresh(False)

    """
        -> Função OnMouseScroll:
            Função para manipular o zoom da câmera assim que o scrool do mouse for ativado
            -> 'evt' : instância de evento, pode ou não ser usado para o tratamento do evento de mouseScroll
        -> Retorno: vazio
    """
    def OnMouseScroll(self, evt):

        MouseEvent.OnMouseScroll(evt, self)

    """
        -> Função OnRightDown:
            Função para criar o PopupMenulogo que o botao direito do mouse for clicado
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnRightDown(self,e):
        MouseEvent.OnRightDown(e, self, self.parent)

    def InitGL(self):

        Vars.KitLib.initGL(c_float(0.003921/2), c_float(0.27059/2), c_float(0.3098/2))

    def OnDraw(self):

        self.camera.OnDrawCamera(self)
        if Vars.KitSim.getSSim():
            Vars.KitSim.drawSim()
        else:
            Vars.KitLib.drawCena(self.camera.visionAxis, self.camera.visionOption)

        Vars.KitLib.drawAxis(self.camera.visionAxis)
        Vars.KitLib.drawGrid(self.camera.visionAxis)

        if self.parent.moveObjetos[0] and not(Vars.KitSim.getSSim()):
            Vars.KitLib.drawMoveAxis(self.camera.visionAxis, self.camera.visionOption, self.parent.moveObjetos[1])

        if self.parent.rotacionaObjetos[0] and not(Vars.KitSim.getSSim()):
            Vars.KitLib.drawRotAxis(self.camera.visionAxis, self.camera.visionOption, self.parent.rotacionaObjetos[1])

        self.SwapBuffers()