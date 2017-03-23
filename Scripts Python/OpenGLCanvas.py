# -*- coding: UTF-8 -*-
from PopUpMenu import *

"""
    ->Classe CanvasBase:
        Classe para manipulação do GLcanvas, responsável pela definição inicial do draw do OpenGL e da captura de eventos de mouse

"""
class CanvasBase(glcanvas.GLCanvas):
    def __init__(self, parent, ref):
        glcanvas.GLCanvas.__init__(self, parent, -1)
        self.parent = parent
        self.init = False
        self.context = glcanvas.GLContext(self)
        self.numJanela = ref # Variável para armazenar o id da janela
        self.dClickEvent = False #Variável referênte a se o usuário está durante o evento de duplo click do mouse, usado para não disparar o evento mouse_motion
        self.dx = 0 # variável que controla o quanto de deslocamento nesse eixo ocorreu assim que começou o evento de mouseMotion
        self.dy = 0
        self.dz = 0


        if ref == 0:
            self.visionAxis = Vars.ASCII_Z
            self.visionOption = Vars.VISION_Z_PERSP
        elif ref == 1:
            self.visionAxis = Vars.ASCII_Z
            self.visionOption = Vars.VISION_Z_PERSP
        elif ref == 2:
            self.visionAxis = Vars.ASCII_Z
            self.visionOption = Vars.VISION_Z_PERSP
        else:
            self.visionAxis = Vars.ASCII_Z
            self.visionOption = Vars.VISION_Z_PERSP

        self.camZoom = 16  # Variável que armazena o raio da coordenada esférica correspondente ao zoom da câmera
        self.theta = math.pi / 4  # Variável que armazena em radianos o ângulo XY da câmera
        self.phi = math.pi / 3  # Variável que armazena em radianos o ângulo do eixo Z com o plano XY
        self.centro = (0,0,0) #Variável que armazena a posição do foco da cãmera
        self.orthoCenter = (0,0) #Tupla que armazena o ponto central da visão ortho
        self.orthoZoom = 5 #Variável que armazena a distancia do centro para visao ortho

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

        self.parent.drawArea0.Refresh()
        self.parent.drawArea1.Refresh()
        self.parent.drawArea2.Refresh()
        self.parent.drawArea3.Refresh()
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

        if self.parent.botaoSelecionado == Vars.MOVETELA_SELECIONADO:
            myCursor = wx.Cursor(r"icones/cursorMoveTelaClick.cur",
                                 wx.BITMAP_TYPE_CUR)

            self.SetCursor(myCursor)
        self.Refresh(False)
        self.parent.ultimoDrawSelected = self
        self.atualizaCentroFocus()
        self.x, self.y = e.GetPosition()
        ponto = Vars.KitLib.getPonto3D(c_int(self.x), c_int(self.y))
        if not(Vars.shiftPress):
            Vars.KitLib.deSelectAll()
            self.parent.moveObjetos = False
        idObj = Vars.KitLib.select(ponto, self.visionAxis)
        if idObj != 0:
            obj = Vars.KitLib.getObjById(idObj)
            centro = (obj.contents.centro.x, obj.contents.centro.y, obj.contents.centro.z)
            self.parent.tabs.tabInfo.AlteraLayoutInfo(obj.contents.id, obj.contents.obj,centro,0,0)
        else:
            self.parent.tabs.tabInfo.AlteraLayoutInfo(0, 0, None,None,None)

        self.parent.drawArea0.Refresh()
        self.parent.drawArea1.Refresh()
        self.parent.drawArea2.Refresh()
        self.parent.drawArea3.Refresh()

    def atualizaCentroFocus(self):

        if self.visionOption == Vars.VISION_Z_PERSP:
            self.parent.tabs.tabConfig.txtFocusX.SetValue(str(round(self.centro[0],3)))
            self.parent.tabs.tabConfig.txtFocusY.SetValue(str(round(self.centro[1],3)))
            self.parent.tabs.tabConfig.txtFocusZ.SetValue(str(round(self.centro[2],3)))
        elif self.visionOption == Vars.VISION_X_POS:
            self.parent.tabs.tabConfig.txtFocusX.SetValue("0")
            self.parent.tabs.tabConfig.txtFocusY.SetValue(str(round(self.orthoCenter[1],3)))
            self.parent.tabs.tabConfig.txtFocusZ.SetValue(str(round(-self.orthoCenter[0],3)))
        elif self.visionOption == Vars.VISION_X_NEG:
            self.parent.tabs.tabConfig.txtFocusX.SetValue("0")
            self.parent.tabs.tabConfig.txtFocusY.SetValue(str(round(-self.orthoCenter[1],3)))
            self.parent.tabs.tabConfig.txtFocusZ.SetValue(str(round(-self.orthoCenter[0],3)))
        elif self.visionOption == Vars.VISION_Y_POS:
            self.parent.tabs.tabConfig.txtFocusX.SetValue(str(round(-self.orthoCenter[1],3)))
            self.parent.tabs.tabConfig.txtFocusY.SetValue("0")
            self.parent.tabs.tabConfig.txtFocusZ.SetValue(str(round(-self.orthoCenter[0],3)))
        elif self.visionOption == Vars.VISION_Y_NEG:
            self.parent.tabs.tabConfig.txtFocusX.SetValue(str(round(self.orthoCenter[1],3)))
            self.parent.tabs.tabConfig.txtFocusY.SetValue("0")
            self.parent.tabs.tabConfig.txtFocusZ.SetValue(str(round(-self.orthoCenter[1],3)))
        else:
            self.parent.tabs.tabConfig.txtFocusX.SetValue(str(round(self.orthoCenter[1],3)))
            self.parent.tabs.tabConfig.txtFocusY.SetValue(str(round(-self.orthoCenter[0],3)))
            self.parent.tabs.tabConfig.txtFocusZ.SetValue("0")


    def OnScrollClick(self, evt):
        self.parent.ultimoDrawSelected = self
        self.atualizaCentroFocus()

        Vars.toolBox.SetFocus()
        self.CaptureMouse()
        self.x, self.y = self.lastx, self.lasty = evt.GetPosition()
        Vars.centroAux = self.centro
        if(self.parent.moveObjetos):
            ponto = Vars.KitLib.getPonto3D(c_int(self.x), c_int(self.y))
            self.parent.moveObjetosEixo = Vars.KitLib.selectMoveSeta(ponto, self.visionAxis)
            if(self.parent.moveObjetosEixo == -1):
                if(Vars.KitLib.MBRSelectPonto(ponto)):
                    self.parent.moveObjetosEixo = -2


    def OnMouseUp(self, evt):

        try:
            self.dx = 0
            self.dy = 0
            self.dz = 0
            if self.parent.botaoSelecionado == Vars.MOVETELA_SELECIONADO:
                myCursor = wx.Cursor(r"icones/cursorMoveTela.cur",
                                     wx.BITMAP_TYPE_CUR)

                self.SetCursor(myCursor)
            self.ReleaseMouse()
        except:
            pass

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

        if evt.Dragging() and evt.MiddleIsDown() and not(self.dClickEvent):

            self.lastx, self.lasty = self.x, self.y
            self.x, self.y = evt.GetPosition()

            if Vars.ctrlPress and self.visionOption == 0: #Se o Control estiver pressionado e estiver na visão perspectiva então fará o deslocamento da câmera livre

                dTheta = (-math.sin(self.theta),
                         math.cos(self.theta), 0)

                dPhi = (-math.cos(self.theta) * math.cos(self.phi),
                        -math.sin(self.theta) * math.cos(self.phi),
                        math.sin(self.phi))

                xCentro = self.centro[0] + (dTheta[0] * ((self.lastx - self.x)/100) * c_float(Vars.KitLib.getEspacoGrid()).value) + (dPhi[0] * (((self.y - self.lasty)/100) * c_float(Vars.KitLib.getEspacoGrid()).value))
                yCentro = self.centro[1] + (dTheta[1] * ((self.lastx - self.x)/100) * c_float(Vars.KitLib.getEspacoGrid()).value) + (dPhi[1] * (((self.y - self.lasty)/100) * c_float(Vars.KitLib.getEspacoGrid()).value))
                zCentro = self.centro[2] - dPhi[2] * (((self.lasty - self.y)/100) * c_float(Vars.KitLib.getEspacoGrid()).value)

                self.centro = (xCentro, yCentro, zCentro)
                if Vars.drawPrincipal != -1:
                    self.parent.tabs.tabConfig.txtFocusX.SetValue(str(round(self.centro[0], 3)))
                    self.parent.tabs.tabConfig.txtFocusY.SetValue(str(round(self.centro[1], 3)))
                    self.parent.tabs.tabConfig.txtFocusZ.SetValue(str(round(self.centro[2], 3)))

            else: #já que o control nao está pressionado, fará uma das opções de movimento abaixo

                if(self.parent.moveObjetos):#Se o usuário selecionou a opção de movimentar objetos.

                    if self.parent.moveObjetosEixo == -1: #Porém nenhum eixo de movimento foi clicado anteriormente e nem em um objeto selecionado
                        if self.visionOption == 0: #Logo se está no modo perspectiva, apenas altera os parâmetros das coordenadas esféricas
                            self.theta = self.theta + (self.lastx - self.x) / 100
                            self.phi = self.phi + (self.lasty - self.y) / 100
                            if self.phi > math.pi / 2:
                               self.phi = math.pi / 2
                            elif self.phi < 0:
                               self.phi = 0.001
                        else: #Se não altera os parâmetros para visao ortogonal
                            self.orthoCenter = (
                                ((self.lasty - self.y) / 60) * c_float(Vars.KitLib.getEspacoGrid()).value + self.orthoCenter[0],
                                ((self.lastx - self.x) / 60) * c_float(Vars.KitLib.getEspacoGrid()).value + self.orthoCenter[1])

                    else:#Porém se o usuário selecionou algum modo de movimentar objetos
                        if self.visionOption == 0:# e está em modo perspectiva
                            dTheta = (-math.sin(self.theta),
                                     math.cos(self.theta), 0)
                            dPhi = (-math.cos(self.theta) * math.cos(self.phi),
                                   -math.sin(self.theta) * math.cos(self.phi),
                                   math.sin(self.phi))
                            xDes =  (dTheta[0] * (self.lastx - self.x) / 50) + (dPhi[0] * (self.y - self.lasty) / 50)
                            yDes =  (dTheta[1] * (self.lastx - self.x) / 50) + (dPhi[1] * (self.y - self.lasty) / 50)
                            zDes = - dPhi[2] * (self.lasty - self.y) / 50

                            spaceGrid = c_float(Vars.KitLib.getEspacoGrid()).value

                            if spaceGrid == 9.0:
                                spaceGrid *= 0.6
                            elif spaceGrid == 18.0:
                                spaceGrid *= 0.4

                            if self.parent.moveObjetosEixo == 0 or self.parent.moveObjetosEixo == 1:#se o eixo dos X está selecionado
                                if self.parent.tabs.tabConfig.blockInsert[0]:
                                    self.moveSelectX(-xDes,spaceGrid)
                                else:
                                    Vars.KitLib.moveSelect(c_float(-xDes * spaceGrid), c_float(0.0), c_float(0.0))

                            elif self.parent.moveObjetosEixo == 2 or self.parent.moveObjetosEixo == 3:#se o eixo dos y está selecionado
                                if self.parent.tabs.tabConfig.blockInsert[0]:
                                    self.moveSelectY(-yDes, spaceGrid)
                                else:
                                    Vars.KitLib.moveSelect(c_float(0.0), c_float(-yDes*spaceGrid), c_float(0.0))
                            elif self.parent.moveObjetosEixo == 4 or self.parent.moveObjetosEixo == 5:#se o eixo dos Z está selecionado
                                if self.parent.tabs.tabConfig.blockInsert[0]:
                                    self.moveSelectZ(-zDes, spaceGrid)
                                else:
                                    Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(-zDes*spaceGrid))
                            else:#Porém se nenhuma seta foi selecionada, caiu na opção de ter clicado em um objeto selecionado, logo a movimentação desses objetos é livre em XYZ
                                    Vars.KitLib.moveSelect(c_float(-xDes*spaceGrid), c_float(-yDes*spaceGrid), c_float(-zDes*spaceGrid))

                        elif self.visionOption == 5:# agora, se está na visao de cima, move os o objetos na direção correspondente
                            xDes = (self.lastx - self.x)/100
                            yDes = (self.lasty - self.y)/100

                            spaceGrid = c_float(Vars.KitLib.getEspacoGrid()).value

                            if spaceGrid == 9.0:
                                spaceGrid *= 0.6
                            elif spaceGrid == 18.0:
                                spaceGrid *= 0.4

                            if self.parent.moveObjetosEixo == 0 or self.parent.moveObjetosEixo == 1:
                                if self.parent.tabs.tabConfig.blockInsert[0]:
                                    self.moveSelectX(-xDes, spaceGrid)
                                else:
                                    Vars.KitLib.moveSelect(c_float(-xDes*spaceGrid), c_float(0.0), c_float(0.0))
                            elif self.parent.moveObjetosEixo == 2 or self.parent.moveObjetosEixo == 3:
                                if self.parent.tabs.tabConfig.blockInsert[0]:
                                    self.moveSelectY(yDes, spaceGrid)
                                else:
                                    Vars.KitLib.moveSelect(c_float(0.0), c_float(yDes*spaceGrid), c_float(0.0))
                            elif self.parent.moveObjetosEixo == -2:
                                Vars.KitLib.moveSelect(c_float(-xDes*spaceGrid), c_float(yDes*spaceGrid), c_float(0.0))

                        elif self.visionOption == 1 or self.visionOption == 2:# agora, se está na visão de frente ou de trás, move os o objetos na direção correspondente
                            yDes = (self.lastx - self.x) / 100
                            zDes = (self.lasty - self.y) / 100

                            spaceGrid = c_float(Vars.KitLib.getEspacoGrid()).value

                            if spaceGrid == 9.0:
                                spaceGrid *= 0.6
                            elif spaceGrid == 18.0:
                                spaceGrid *= 0.4

                            if self.visionOption == 1:
                                if self.parent.moveObjetosEixo == 2 or self.parent.moveObjetosEixo == 3:
                                    if self.parent.tabs.tabConfig.blockInsert[0]:
                                        self.moveSelectY(-yDes, spaceGrid)
                                    else:
                                        Vars.KitLib.moveSelect(c_float(0.0), c_float(-yDes * spaceGrid), c_float(0.0))
                                elif self.parent.moveObjetosEixo == 4 or self.parent.moveObjetosEixo == 5:
                                    if self.parent.tabs.tabConfig.blockInsert[0]:
                                        self.moveSelectZ(zDes, spaceGrid)
                                    else:
                                        Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(zDes*spaceGrid))
                                elif self.parent.moveObjetosEixo == -2:
                                        Vars.KitLib.moveSelect(c_float(0.0), c_float(-yDes*spaceGrid), c_float(zDes*spaceGrid))
                            else:
                                if self.parent.moveObjetosEixo == 2 or self.parent.moveObjetosEixo == 3:
                                    if self.parent.tabs.tabConfig.blockInsert[0]:
                                        self.moveSelectY(yDes, spaceGrid)
                                    else:
                                        Vars.KitLib.moveSelect(c_float(0.0), c_float(yDes*spaceGrid), c_float(0.0))
                                elif self.parent.moveObjetosEixo == 4 or self.parent.moveObjetosEixo == 5:
                                    if self.parent.tabs.tabConfig.blockInsert[0]:
                                        self.moveSelectZ(zDes, spaceGrid)
                                    else:
                                        Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(zDes*spaceGrid))
                                elif self.parent.moveObjetosEixo == -2:
                                    Vars.KitLib.moveSelect(c_float(0.0), c_float(yDes*spaceGrid), c_float(zDes*spaceGrid))


                        elif self.visionOption == 3 or self.visionOption == 4:# agora, se está na visao da direita ou da esquerda, move os o objetos na direção correspondente
                            xDes = (self.lastx - self.x) / 100
                            zDes = (self.lasty - self.y) / 100

                            spaceGrid = c_float(Vars.KitLib.getEspacoGrid()).value

                            if spaceGrid == 9.0:
                                spaceGrid *= 0.6
                            elif spaceGrid == 18.0:
                                spaceGrid *= 0.4

                            if self.visionOption == 3:
                                if self.parent.moveObjetosEixo == 0 or self.parent.moveObjetosEixo == 1:
                                    if self.parent.tabs.tabConfig.blockInsert[0]:
                                        self.moveSelectX(xDes, spaceGrid)
                                    else:
                                        Vars.KitLib.moveSelect(c_float(xDes*spaceGrid), c_float(0.0), c_float(0.0))
                                elif self.parent.moveObjetosEixo == 4 or self.parent.moveObjetosEixo == 5:
                                    if self.parent.tabs.tabConfig.blockInsert[0]:
                                        self.moveSelectZ(zDes, spaceGrid)
                                    else:
                                        Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(zDes*spaceGrid))
                                elif self.parent.moveObjetosEixo == -2:
                                    Vars.KitLib.moveSelect(c_float(xDes*spaceGrid), c_float(0.0), c_float(zDes*spaceGrid))
                            else:
                                if self.parent.moveObjetosEixo == 0 or self.parent.moveObjetosEixo == 1:
                                    if self.parent.tabs.tabConfig.blockInsert[0]:
                                        self.moveSelectX(-xDes, spaceGrid)
                                    else:
                                        Vars.KitLib.moveSelect(c_float(-xDes*spaceGrid), c_float(0.0), c_float(0.0))
                                elif self.parent.moveObjetosEixo == 4 or self.parent.moveObjetosEixo == 5:
                                    if self.parent.tabs.tabConfig.blockInsert[0]:
                                        self.moveSelectZ(zDes, spaceGrid)
                                    else:
                                        Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(zDes*spaceGrid))
                                elif self.parent.moveObjetosEixo == -2:
                                    Vars.KitLib.moveSelect(c_float(-xDes*spaceGrid), c_float(0.0), c_float(zDes*spaceGrid))
                    self.parent.tabs.tabInfo.alteraCentroMBR()
                    self.parent.atualizaPrecisaSalvar(True)
                else: #se a opção de movimentar objetos não foi selecionado pelo usuário
                    if self.visionOption == 0: #e está na visao perspectiva, apenas altera os parâmetros da coordenada esférica
                        self.theta = self.theta + (self.lastx - self.x) / 100
                        self.phi = self.phi + (self.lasty - self.y) / 100
                        if self.phi > math.pi / 2:
                           self.phi = math.pi / 2
                        elif self.phi < 0:
                           self.phi = 0.001
                    else: #se não, apenas altera os parametros da visão ortogonal
                        self.orthoCenter = (
                            ((self.lasty - self.y) * self.orthoZoom * 0.5 / 200) * c_float(Vars.KitLib.getEspacoGrid()).value + self.orthoCenter[0],
                            ((self.lastx - self.x) * self.orthoZoom * 0.5 / 200) * c_float(Vars.KitLib.getEspacoGrid()).value + self.orthoCenter[1])

            self.atualizaCentroFocus()
            self.Refresh(True)

        if self.dClickEvent:
            self.dClickEvent = False

    def OnZoomIn(self):
        if self.visionOption == Vars.VISION_Z_PERSP:
            zoom = 0.5
            self.camZoom -= zoom
            if self.camZoom <= 0:
                self.camZoom = 0.2
        else:
            zoom = 0.5
            self.orthoZoom -= zoom
            if self.orthoZoom <= 0:
                self.orthoZoom = 0.2


        self.parent.Refresh(False)

    def OnZoomOut(self):
        if self.visionOption == Vars.VISION_Z_PERSP:

            zoom = 0.5

            self.camZoom += zoom

        else:
            zoom = 0.5
            self.orthoZoom += zoom



        self.Refresh(False)

    """
        -> Função OnMouseScroll:
            Função para manipular o zoom da câmera assim que o scrool do mouse for ativado
            -> 'evt' : instância de evento, pode ou não ser usado para o tratamento do evento de mouseScroll
        -> Retorno: vazio
    """
    def OnMouseScroll(self, evt):
        if self.visionOption == Vars.VISION_Z_PERSP:

            zoom = 0.5
            if evt.GetWheelRotation() < 0:

                self.camZoom += zoom

            else:

                self.camZoom -= zoom
                if self.camZoom <= 0:
                    self.camZoom = 0.2
        else:
            zoom = 0.5
            if evt.GetWheelRotation() < 0:

                self.orthoZoom += zoom

            else:

                self.orthoZoom -= zoom
                if self.orthoZoom <= 0:
                    self.orthoZoom = 0.2


        self.Refresh(False)


    """
        -> Função OnRightDown:
            Função para criar o PopupMenulogo que o botao direito do mouse for clicado
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnRightDown(self,e):
        Vars.ultimoDrawSelected = self
        self.atualizaCentroFocus()
        Vars.toolBox.SetFocus()
        self.Refresh()
        Vars.rightMouse = (e.GetPosition()[0],e.GetPosition()[1])
        try:
            self.PopupMenu(RightMenu(self), e.GetPosition())
        except:
            pass
        self.Refresh(True)
    def InitGL(self):

        Vars.KitLib.initGL()
        """luzAmbiente = (0.2, 0.2, 0.2, 1.0)
        luzDifusa = (0.7, 0.7, 0.7, 1.0)
        glClearColor(0.5, 0.5, 0.5, 0.0)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glEnable(GL_NORMALIZE)
        glEnable(GL_LIGHTING)

        glShadeModel(GL_SMOOTH)
        glEnable( GL_LINE_SMOOTH )
        glEnable(GL_BLEND)
        glEnable( GL_POLYGON_SMOOTH )
        glHint( GL_LINE_SMOOTH_HINT, GL_NICEST )
        glHint( GL_POLYGON_SMOOTH_HINT, GL_NICEST )
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


        glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa)
        glLightfv(GL_LIGHT0, GL_POSITION, Vars.posLuz)

        glEnable(GL_LIGHT0)"""

    def OnDraw(self):

        #Definições de câmera perspectiva
        if self.visionOption == 0:
            zoom = self.camZoom * c_float(Vars.KitLib.getEspacoGrid()).value
            eye = (zoom * math.cos(self.theta) * math.sin(self.phi) + self.centro[0],
                   zoom * math.sin(self.theta) * math.sin(self.phi) + self.centro[1], zoom * math.cos(self.phi) + self.centro[2])
            up = (-zoom * math.cos(self.theta) * math.cos(self.phi),
                  -zoom * math.sin(self.theta) * math.cos(self.phi), zoom * math.sin(self.phi))


            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            Vars.posLuz = (eye[0], eye[1], eye[2], 1.0)
            glLightfv(GL_LIGHT0, GL_POSITION, Vars.posLuz)

            glViewport(0, 0, self.GetClientSize()[0], self.GetClientSize()[1])
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            #gluPerspective(60.0, self.GetClientSize()[0] / self.GetClientSize()[1], 0.01, 500*c_float(Vars.KitLib.getEspacoGrid()).value)
            gluPerspective(60.0, self.GetClientSize()[0] / self.GetClientSize()[1], 0.3,500*c_float(Vars.KitLib.getEspacoGrid()).value)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            gluLookAt(eye[0], eye[1], eye[2], self.centro[0], self.centro[1], self.centro[2], up[0], up[1], up[2])

        #Definições de câmera ortho positiva
        elif self.visionOption == 5 or self.visionOption == 1 or self.visionOption == 4:
            zoom = self.orthoZoom * c_float(Vars.KitLib.getEspacoGrid()).value
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            Vars.posLuz = (0,0,500000, 1.0)
            glLightfv(GL_LIGHT0, GL_POSITION, Vars.posLuz)
            glViewport(0, 0, self.GetClientSize()[0], self.GetClientSize()[1])
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(-zoom*self.GetClientSize()[0]/self.GetClientSize()[1] + self.orthoCenter[1],
                    zoom*self.GetClientSize()[0]/self.GetClientSize()[1] + self.orthoCenter[1],
                    -zoom - self.orthoCenter[0], zoom - self.orthoCenter[0], -10000, 10000.0)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
        #Definições de câmera ortho negativa
        elif self.visionOption == 2 or self.visionOption == 3:
            zoom = self.orthoZoom * c_float(Vars.KitLib.getEspacoGrid()).value
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            Vars.posLuz = (0, 0, -500000, 1.0)
            glLightfv(GL_LIGHT0, GL_POSITION, Vars.posLuz)
            glViewport(0, 0, self.GetClientSize()[0], self.GetClientSize()[1])
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(zoom*self.GetClientSize()[0]/self.GetClientSize()[1] - self.orthoCenter[1],
                    -zoom*self.GetClientSize()[0]/self.GetClientSize()[1] - self.orthoCenter[1],
                    -zoom - self.orthoCenter[0], zoom - self.orthoCenter[0], 10000, -10000.0)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

        Vars.KitLib.drawCena(self.visionAxis, self.visionOption)
        Vars.KitLib.drawAxis(self.visionAxis)
        Vars.KitLib.drawGrid(self.visionAxis)

        if self.parent.moveObjetos and self.visionOption == 0:
            Vars.KitLib.drawMoveAxis(self.visionAxis, self.visionOption, c_float(self.camZoom))
        elif self.parent.moveObjetos:
            Vars.KitLib.drawMoveAxis(self.visionAxis, self.visionOption, c_float(self.orthoZoom))

        self.SwapBuffers()

