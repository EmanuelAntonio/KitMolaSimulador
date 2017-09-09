
from VarsAmbient import *
from AdicionarObjetos import *
from PopUpMenu import *


class MouseEvent(object):
    
    @staticmethod
    def OnScrollClick(e, canvas, window):
        window.ultimoDrawSelected = canvas
        canvas.camera.atualizaCentroFocus()
        Vars.toolBox.SetFocus()
        canvas.CaptureMouse()
        canvas.x, canvas.y = canvas.lastx, canvas.lasty = e.GetPosition()
        Vars.centroAux = canvas.camera.centro

    @staticmethod
    def OnMouseUp(canvas, window):
        try:
            canvas.dx = 0
            canvas.dy = 0
            canvas.dz = 0
            if window.botaoSelecionado == Vars.MOVETELA_SELECIONADO:
                if Vars.thema == "dark":
                    myCursor = wx.Cursor(Vars.dirExec + "icones/cursorMoveTeladark.cur",
                                         wx.BITMAP_TYPE_CUR)
                else:
                    myCursor = wx.Cursor(Vars.dirExec + "icones/cursorMoveTela.cur",
                                         wx.BITMAP_TYPE_CUR)
                window.SetCursor(myCursor)
            canvas.ReleaseMouse()
        except:
            pass

    @staticmethod
    def OnMouseMotion(evt, canvas, window):

        if (evt.Dragging() and evt.MiddleIsDown() and not(canvas.dClickEvent) or(evt.LeftIsDown() and window.botaoSelecionado == Vars.MOVETELA_SELECIONADO)):

            canvas.lastx, canvas.lasty = canvas.x, canvas.y
            canvas.x, canvas.y = evt.GetPosition()

            if Vars.ctrlPress and canvas.camera.visionOption == 0: #Se o Control estiver pressionado e estiver na visão perspectiva então fará o deslocamento da câmera livre

                dTheta = (-math.sin(canvas.camera.theta),
                         math.cos(canvas.camera.theta), 0)

                dPhi = (-math.cos(canvas.camera.theta) * math.cos(canvas.camera.phi),
                        -math.sin(canvas.camera.theta) * math.cos(canvas.camera.phi),
                        math.sin(canvas.camera.phi))

                xCentro = canvas.camera.centro[0] + (dTheta[0] * ((canvas.lastx - canvas.x)/300) * c_float(Vars.KitLib.getEspacoGrid()).value) + (dPhi[0] * (((canvas.y - canvas.lasty)/300) * c_float(Vars.KitLib.getEspacoGrid()).value))
                yCentro = canvas.camera.centro[1] + (dTheta[1] * ((canvas.lastx - canvas.x)/300) * c_float(Vars.KitLib.getEspacoGrid()).value) + (dPhi[1] * (((canvas.y - canvas.lasty)/300) * c_float(Vars.KitLib.getEspacoGrid()).value))
                zCentro = canvas.camera.centro[2] - dPhi[2] * (((canvas.lasty - canvas.y)/300) * c_float(Vars.KitLib.getEspacoGrid()).value)

                canvas.camera.centro = (xCentro, yCentro, zCentro)
                if Vars.drawPrincipal != -1:
                    window.tabs.tabConfig.txtFocusX.SetValue(str(round(canvas.camera.centro[0], 3)))
                    window.tabs.tabConfig.txtFocusY.SetValue(str(round(canvas.camera.centro[1], 3)))
                    window.tabs.tabConfig.txtFocusZ.SetValue(str(round(canvas.camera.centro[2], 3)))

            else: #já que o control nao está pressionado, fará uma das opções de movimento abaixo

                if canvas.camera.visionOption == 0:  # e está na visao perspectiva, apenas altera os parâmetros da coordenada esférica
                    canvas.camera.theta = canvas.camera.theta + (canvas.lastx - canvas.x) / 300
                    canvas.camera.phi = canvas.camera.phi + (canvas.lasty - canvas.y) / 300
                    if canvas.camera.phi > math.pi / 2:
                        canvas.camera.phi = math.pi / 2
                    elif canvas.camera.phi < 0:
                        canvas.camera.phi = 0.001
                else:  # se não, apenas altera os parametros da visão ortogonal
                    canvas.camera.orthoCenter = (
                        ((canvas.lasty - canvas.y) * canvas.camera.orthoZoom * 0.5 / 300) * c_float(
                            Vars.KitLib.getEspacoGrid()).value + canvas.camera.orthoCenter[0],
                        ((canvas.lastx - canvas.x) * canvas.camera.orthoZoom * 0.5 / 300) * c_float(
                            Vars.KitLib.getEspacoGrid()).value + canvas.camera.orthoCenter[1])



        elif(evt.Dragging() and evt.LeftIsDown() and window.moveObjetos[0]):
            canvas.lastx, canvas.lasty = canvas.x, canvas.y
            canvas.x, canvas.y = evt.GetPosition()
            MouseEvent.OnMoveObjs(window, canvas)

        elif(evt.Dragging() and evt.LeftIsDown() and window.rotacionaObjetos[0]):
            canvas.lastx, canvas.lasty = canvas.x, canvas.y
            canvas.x, canvas.y = evt.GetPosition()
            MouseEvent.OnRotObjs(window, canvas)

        canvas.camera.atualizaCentroFocus()
        canvas.Refresh(True)
        if canvas.dClickEvent:
            canvas.dClickEvent = False

    @staticmethod
    def OnMouseScroll(evt, canvas):

        if canvas.camera.visionOption == Vars.VISION_Z_PERSP:

            zoom = 0.05 * canvas.camera.camZoom
            if evt.GetWheelRotation() < 0:

                canvas.camera.camZoom += zoom

            else:

                canvas.camera.camZoom -= zoom
                if canvas.camera.camZoom <= 0:
                    canvas.camera.camZoom = 0.2
        else:

            zoom = 0.3
            if evt.GetWheelRotation() < 0:

                canvas.camera.orthoZoom += zoom

            else:

                canvas.camera.orthoZoom -= zoom
                if canvas.camera.orthoZoom <= 0:
                    canvas.camera.orthoZoom = 0.2


        canvas.Refresh(False)


    @staticmethod
    def OnMouseDown(e, canvas, window):

        if Vars.KitSim.getSSim():
            return
        if window.botaoSelecionado == Vars.MOVETELA_SELECIONADO:
            if Vars.thema == "dark":
                myCursor = wx.Cursor(Vars.dirExec + "icones/cursorMoveTelaClickdark.cur",
                                     wx.BITMAP_TYPE_CUR)
            else:
                myCursor = wx.Cursor(Vars.dirExec + "icones/cursorMoveTelaClick.cur",
                                     wx.BITMAP_TYPE_CUR)

            window.SetCursor(myCursor)
            MouseEvent.OnScrollClick(e,canvas,window)
        canvas.Refresh(True)
        window.ultimoDrawSelected = canvas
        canvas.camera.atualizaCentroFocus()
        canvas.x, canvas.y = e.GetPosition()
        ponto = Vars.KitLib.getPonto3D(c_int(canvas.x), c_int(canvas.y))
        if not(Vars.shiftPress):
            if window.botaoSelecionado == Vars.SPHERE_SELECIONADO:

                Vars.rightMouse = e.GetPosition()
                AdicionarObjetos.OnAddSphere(canvas, window)
            if window.botaoSelecionado == Vars.BASE_SELECIONADO:

                Vars.rightMouse = e.GetPosition()
                AdicionarObjetos.OnAddBase(Vars.BASE_LIVRE,canvas, window)
            elif window.botaoSelecionado == Vars.LIVRE_SELECIONADO:
                if window.moveObjetos[0] or window.rotacionaObjetos[0]:
                    Vars.toolBox.SetFocus()
                    canvas.CaptureMouse()
                    canvas.x, canvas.y = canvas.lastx, canvas.lasty = e.GetPosition()
                    Vars.centroAux = canvas.camera.centro
                    if window.rotacionaSelectCentro and window.rotacionaObjetos[0]:
                        ponto = Vars.KitLib.getPonto3D(canvas.x,canvas.y)
                        Vars.KitLib.selectRotCenter(ponto, canvas.camera.visionAxis, canvas.camera.visionOption)

                else:
                    Vars.KitLib.deSelectAll()
                    idObj = Vars.KitLib.select(ponto, canvas.camera.visionAxis, canvas.camera.visionOption)
                    if idObj != 0:
                        obj = Vars.KitLib.getObjById(idObj)
                        centro = (obj.contents.centro.x, obj.contents.centro.y, obj.contents.centro.z)
                        window.tabs.tabInfo.AlteraLayoutInfo(obj.contents.id, obj.contents.obj, centro, 0, 0)
                    else:
                        window.tabs.tabInfo.AlteraLayoutInfo(0, 0, None, None, None)
            elif window.botaoSelecionado == Vars.ADDFORCA_SELECIONADO:
                XYTela = e.GetPosition()
                ponto = Vars.KitLib.getPonto3D(XYTela[0], XYTela[1])
                Vars.KitSim.addForca(ponto,c_float(float(window.tabs.tabSim.txtX.GetValue())),
                                     c_float(float(window.tabs.tabSim.txtY.GetValue())),
                                     c_float(float(window.tabs.tabSim.txtZ.GetValue())))
            else:
                idObj = Vars.KitLib.select(ponto, canvas.camera.visionAxis, canvas.camera.visionOption)
                if idObj != 0:
                    obj = Vars.KitLib.getObjById(idObj)
                    centro = (obj.contents.centro.x, obj.contents.centro.y, obj.contents.centro.z)
                    window.tabs.tabInfo.AlteraLayoutInfo(obj.contents.id, obj.contents.obj, centro, 0, 0)
                else:
                    window.tabs.tabInfo.AlteraLayoutInfo(0, 0, None, None, None)

        else:
            idObj = Vars.KitLib.select(ponto, canvas.camera.visionAxis, canvas.camera.visionOption)
            if idObj != 0:
                obj = Vars.KitLib.getObjById(idObj)
                centro = (obj.contents.centro.x, obj.contents.centro.y, obj.contents.centro.z)
                window.tabs.tabInfo.AlteraLayoutInfo(obj.contents.id, obj.contents.obj, centro, 0, 0)
        window.OnRefreshAll()

    @staticmethod
    def OnRightDown(e,canvas, window):
        window.ultimoDrawSelected = canvas
        canvas.camera.atualizaCentroFocus()
        Vars.toolBox.SetFocus()
        canvas.Refresh()
        Vars.rightMouse = (e.GetPosition()[0],e.GetPosition()[1])
        try:
            canvas.PopupMenu(RightMenu(canvas), e.GetPosition())
        except:
            pass
        canvas.Refresh(True)

    @staticmethod
    def OnMoveObjs(window, canvas):
        if canvas.camera.visionOption == 0:  # e está em modo perspectiva
            dTheta = (-math.sin(canvas.camera.theta),
                      math.cos(canvas.camera.theta), 0)
            dPhi = (-math.cos(canvas.camera.theta) * math.cos(canvas.camera.phi),
                    -math.sin(canvas.camera.theta) * math.cos(canvas.camera.phi),
                    math.sin(canvas.camera.phi))
            xDes = (dTheta[0] * (canvas.lastx - canvas.x) / 50) + (dPhi[0] * (canvas.y - canvas.lasty) / 50)
            yDes = (dTheta[1] * (canvas.lastx - canvas.x) / 50) + (dPhi[1] * (canvas.y - canvas.lasty) / 50)
            zDes = - dPhi[2] * (canvas.lasty - canvas.y) / 50

            MouseEvent.OnDeslocaObjs(xDes,yDes,zDes,window,canvas)

        elif canvas.camera.visionOption == 5:  # agora, se está na visao de cima, move os o objetos na direção correspondente
            xDes = (canvas.lastx - canvas.x) / 100
            yDes = (canvas.lasty - canvas.y) / 100

            MouseEvent.OnDeslocaObjs(xDes, -yDes, 0, window, canvas)

        elif canvas.camera.visionOption == 1:  # agora, se está na visão de frente, move os o objetos na direção correspondente
            yDes = (canvas.lastx - canvas.x) / 100
            zDes = (canvas.lasty - canvas.y) / 100

            MouseEvent.OnDeslocaObjs(0, yDes, -zDes, window, canvas)

        elif canvas.camera.visionOption == 2:  # agora, se está na visão de trás, move os o objetos na direção correspondente
            yDes = (canvas.lastx - canvas.x) / 100
            zDes = (canvas.lasty - canvas.y) / 100

            MouseEvent.OnDeslocaObjs(0, -yDes, -zDes, window, canvas)


        elif canvas.camera.visionOption == 3:  # agora, se está na visao da direita ou da esquerda, move os o objetos na direção correspondente
            xDes = (canvas.lastx - canvas.x) / 100
            zDes = (canvas.lasty - canvas.y) / 100

            MouseEvent.OnDeslocaObjs(-xDes, 0, -zDes, window, canvas)

        elif canvas.camera.visionOption == 4:  # agora, se está na visao da direita ou da esquerda, move os o objetos na direção correspondente
            xDes = (canvas.lastx - canvas.x) / 100
            zDes = (canvas.lasty - canvas.y) / 100

            MouseEvent.OnDeslocaObjs(xDes, 0, -zDes, window, canvas)

        window.tabs.tabInfo.alteraCentroMBR()
        window.atualizaPrecisaSalvar(True)


    @staticmethod
    def OnDeslocaObjs(xDes,yDes,zDes,window,canvas):

        spaceGrid = c_float(Vars.KitLib.getEspacoGrid()).value

        if spaceGrid == 9.0:
            spaceGrid *= 0.6
        elif spaceGrid == 18.0:
            spaceGrid *= 0.4

        if window.moveObjetos[1] == Vars.ASCII_X:  # se o eixo dos X está selecionado
            if window.tabs.tabConfig.blockInsert[0]:
                canvas.moveSelectX(-xDes, spaceGrid)
            else:
                Vars.KitLib.moveSelect(c_float(-xDes * spaceGrid), c_float(0.0), c_float(0.0))

        elif window.moveObjetos[1] == Vars.ASCII_Y:  # se o eixo dos y está selecionado
            if window.tabs.tabConfig.blockInsert[0]:
                canvas.moveSelectY(-yDes, spaceGrid)
            else:
                Vars.KitLib.moveSelect(c_float(0.0), c_float(-yDes * spaceGrid), c_float(0.0))
        elif window.moveObjetos[1] == Vars.ASCII_Z:  # se o eixo dos Z está selecionado
            if window.tabs.tabConfig.blockInsert[0]:
                canvas.moveSelectZ(-zDes, spaceGrid)

    @staticmethod
    def OnRotObjs(window, canvas):

        rot = False
        if canvas.camera.visionOption == 0:  # e está em modo perspectiva

            dTheta = (-math.sin(canvas.camera.theta),
                      math.cos(canvas.camera.theta), 0)
            dPhi = (-math.cos(canvas.camera.theta) * math.cos(canvas.camera.phi),
                    -math.sin(canvas.camera.theta) * math.cos(canvas.camera.phi),
                    math.sin(canvas.camera.phi))
            xDes = (dTheta[0] * (canvas.lastx - canvas.x) / 50) + (dPhi[0] * (canvas.y - canvas.lasty) / 50)
            yDes = (dTheta[1] * (canvas.lastx - canvas.x) / 50) + (dPhi[1] * (canvas.y - canvas.lasty) / 50)
            zDes = - dPhi[2] * (canvas.lasty - canvas.y) / 50
            if window.rotacionaObjetos[1] == Vars.ASCII_X:
                rot = Vars.KitLib.rotacionaSelect(True,False,False, c_float(xDes))
            elif window.rotacionaObjetos[1] == Vars.ASCII_Y:
                rot = Vars.KitLib.rotacionaSelect(False,True,False, c_float(yDes))
            elif window.rotacionaObjetos[1] == Vars.ASCII_Z:
                rot = Vars.KitLib.rotacionaSelect(False,False,True, c_float(zDes))

            if not(rot):
                Msg.exibirStatusBar("Bases só podem ser rotacionadas no eixo Z.",10)


        elif canvas.camera.visionOption == 5:  # agora, se está na visao de cima, move os o objetos na direção correspondente
            xDes = (canvas.lastx - canvas.x) / 100
            yDes = (canvas.lasty - canvas.y) / 100
