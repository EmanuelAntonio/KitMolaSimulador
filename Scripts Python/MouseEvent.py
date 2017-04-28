
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
        if (window.moveObjetos):
            ponto = Vars.KitLib.getPonto3D(c_int(canvas.x), c_int(canvas.y))
            window.moveObjetosEixo = Vars.KitLib.selectMoveSeta(ponto, canvas.camera.visionAxis)
            if (window.moveObjetosEixo == -1):
                if (Vars.KitLib.MBRSelectPonto(ponto)):
                    window.moveObjetosEixo = -2

    @staticmethod
    def OnMouseUp(canvas, window):
        try:
            canvas.dx = 0
            canvas.dy = 0
            canvas.dz = 0
            if window.botaoSelecionado == Vars.MOVETELA_SELECIONADO:
                myCursor = wx.Cursor(r"icones/cursorMoveTela.cur",
                                     wx.BITMAP_TYPE_CUR)

                window.SetCursor(myCursor)
            canvas.ReleaseMouse()
        except:
            pass

    @staticmethod
    def OnMouseMotion(evt, canvas, window):

        if (evt.Dragging() and evt.MiddleIsDown() and not(canvas.dClickEvent)) or (evt.LeftIsDown() and window.botaoSelecionado == Vars.MOVETELA_SELECIONADO):

            canvas.lastx, canvas.lasty = canvas.x, canvas.y
            canvas.x, canvas.y = evt.GetPosition()

            if Vars.ctrlPress and canvas.camera.visionOption == 0: #Se o Control estiver pressionado e estiver na visão perspectiva então fará o deslocamento da câmera livre

                dTheta = (-math.sin(canvas.camera.theta),
                         math.cos(canvas.camera.theta), 0)

                dPhi = (-math.cos(canvas.camera.theta) * math.cos(canvas.camera.phi),
                        -math.sin(canvas.camera.theta) * math.cos(canvas.camera.phi),
                        math.sin(canvas.camera.phi))

                xCentro = canvas.camera.centro[0] + (dTheta[0] * ((canvas.lastx - canvas.x)/200) * c_float(Vars.KitLib.getEspacoGrid()).value) + (dPhi[0] * (((canvas.y - canvas.lasty)/200) * c_float(Vars.KitLib.getEspacoGrid()).value))
                yCentro = canvas.camera.centro[1] + (dTheta[1] * ((canvas.lastx - canvas.x)/200) * c_float(Vars.KitLib.getEspacoGrid()).value) + (dPhi[1] * (((canvas.y - canvas.lasty)/200) * c_float(Vars.KitLib.getEspacoGrid()).value))
                zCentro = canvas.camera.centro[2] - dPhi[2] * (((canvas.lasty - canvas.y)/200) * c_float(Vars.KitLib.getEspacoGrid()).value)

                canvas.camera.centro = (xCentro, yCentro, zCentro)
                if Vars.drawPrincipal != -1:
                    window.tabs.tabConfig.txtFocusX.SetValue(str(round(canvas.camera.centro[0], 3)))
                    window.tabs.tabConfig.txtFocusY.SetValue(str(round(canvas.camera.centro[1], 3)))
                    window.tabs.tabConfig.txtFocusZ.SetValue(str(round(canvas.camera.centro[2], 3)))

            else: #já que o control nao está pressionado, fará uma das opções de movimento abaixo

                if(window.moveObjetos):#Se o usuário selecionou a opção de movimentar objetos.

                    if window.moveObjetosEixo == -1: #Porém nenhum eixo de movimento foi clicado anteriormente e nem em um objeto selecionado
                        if canvas.camera.visionOption == 0: #Logo se está no modo perspectiva, apenas altera os parâmetros das coordenadas esféricas
                            canvas.camera.theta = canvas.camera.theta + (canvas.lastx - canvas.x) / 100
                            canvas.camera.phi = canvas.camera.phi + (canvas.lasty - canvas.y) / 100
                            if canvas.camera.phi > math.pi / 2:
                               canvas.camera.phi = math.pi / 2
                            elif canvas.camera.phi < 0:
                               canvas.camera.phi = 0.001
                        else: #Se não altera os parâmetros para visao ortogonal
                            canvas.camera.orthoCenter = (
                                ((canvas.lasty - canvas.y) / 60) * c_float(Vars.KitLib.getEspacoGrid()).value + canvas.camera.orthoCenter[0],
                                ((canvas.lastx - canvas.x) / 60) * c_float(Vars.KitLib.getEspacoGrid()).value + canvas.camera.orthoCenter[1])

                    else:#Porém se o usuário selecionou algum modo de movimentar objetos
                        if canvas.camera.visionOption == 0:# e está em modo perspectiva
                            dTheta = (-math.sin(canvas.camera.theta),
                                     math.cos(canvas.camera.theta), 0)
                            dPhi = (-math.cos(canvas.camera.theta) * math.cos(canvas.camera.phi),
                                   -math.sin(canvas.camera.theta) * math.cos(canvas.camera.phi),
                                   math.sin(canvas.camera.phi))
                            xDes =  (dTheta[0] * (canvas.lastx - canvas.x) / 50) + (dPhi[0] * (canvas.y - canvas.lasty) / 50)
                            yDes =  (dTheta[1] * (canvas.lastx - canvas.x) / 50) + (dPhi[1] * (canvas.y - canvas.lasty) / 50)
                            zDes = - dPhi[2] * (canvas.lasty - canvas.y) / 50

                            spaceGrid = c_float(Vars.KitLib.getEspacoGrid()).value

                            if spaceGrid == 9.0:
                                spaceGrid *= 0.6
                            elif spaceGrid == 18.0:
                                spaceGrid *= 0.4

                            if window.moveObjetosEixo == 0 or window.moveObjetosEixo == 1:#se o eixo dos X está selecionado
                                if window.tabs.tabConfig.blockInsert[0]:
                                    canvas.moveSelectX(-xDes,spaceGrid)
                                else:
                                    Vars.KitLib.moveSelect(c_float(-xDes * spaceGrid), c_float(0.0), c_float(0.0))

                            elif window.moveObjetosEixo == 2 or window.moveObjetosEixo == 3:#se o eixo dos y está selecionado
                                if window.tabs.tabConfig.blockInsert[0]:
                                    canvas.moveSelectY(-yDes, spaceGrid)
                                else:
                                    Vars.KitLib.moveSelect(c_float(0.0), c_float(-yDes*spaceGrid), c_float(0.0))
                            elif window.moveObjetosEixo == 4 or window.moveObjetosEixo == 5:#se o eixo dos Z está selecionado
                                if window.tabs.tabConfig.blockInsert[0]:
                                    canvas.moveSelectZ(-zDes, spaceGrid)
                                else:
                                    Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(-zDes*spaceGrid))
                            else:#Porém se nenhuma seta foi selecionada, caiu na opção de ter clicado em um objeto selecionado, logo a movimentação desses objetos é livre em XYZ
                                    Vars.KitLib.moveSelect(c_float(-xDes*spaceGrid), c_float(-yDes*spaceGrid), c_float(-zDes*spaceGrid))

                        elif canvas.camera.visionOption == 5:# agora, se está na visao de cima, move os o objetos na direção correspondente
                            xDes = (canvas.lastx - canvas.x)/100
                            yDes = (canvas.lasty - canvas.y)/100

                            spaceGrid = c_float(Vars.KitLib.getEspacoGrid()).value

                            if spaceGrid == 9.0:
                                spaceGrid *= 0.6
                            elif spaceGrid == 18.0:
                                spaceGrid *= 0.4

                            if window.moveObjetosEixo == 0 or window.moveObjetosEixo == 1:
                                if window.tabs.tabConfig.blockInsert[0]:
                                    canvas.moveSelectX(-xDes, spaceGrid)
                                else:
                                    Vars.KitLib.moveSelect(c_float(-xDes*spaceGrid), c_float(0.0), c_float(0.0))
                            elif window.moveObjetosEixo == 2 or window.moveObjetosEixo == 3:
                                if window.tabs.tabConfig.blockInsert[0]:
                                    canvas.moveSelectY(yDes, spaceGrid)
                                else:
                                    Vars.KitLib.moveSelect(c_float(0.0), c_float(yDes*spaceGrid), c_float(0.0))
                            elif window.moveObjetosEixo == -2:
                                Vars.KitLib.moveSelect(c_float(-xDes*spaceGrid), c_float(yDes*spaceGrid), c_float(0.0))

                        elif canvas.camera.visionOption == 1 or canvas.camera.visionOption == 2:# agora, se está na visão de frente ou de trás, move os o objetos na direção correspondente
                            yDes = (canvas.lastx - canvas.x) / 100
                            zDes = (canvas.lasty - canvas.y) / 100

                            spaceGrid = c_float(Vars.KitLib.getEspacoGrid()).value

                            if spaceGrid == 9.0:
                                spaceGrid *= 0.6
                            elif spaceGrid == 18.0:
                                spaceGrid *= 0.4

                            if canvas.camera.visionOption == 1:
                                if window.moveObjetosEixo == 2 or window.moveObjetosEixo == 3:
                                    if window.tabs.tabConfig.blockInsert[0]:
                                        canvas.moveSelectY(-yDes, spaceGrid)
                                    else:
                                        Vars.KitLib.moveSelect(c_float(0.0), c_float(-yDes * spaceGrid), c_float(0.0))
                                elif window.moveObjetosEixo == 4 or window.moveObjetosEixo == 5:
                                    if window.tabs.tabConfig.blockInsert[0]:
                                        canvas.moveSelectZ(zDes, spaceGrid)
                                    else:
                                        Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(zDes*spaceGrid))
                                elif window.moveObjetosEixo == -2:
                                        Vars.KitLib.moveSelect(c_float(0.0), c_float(-yDes*spaceGrid), c_float(zDes*spaceGrid))
                            else:
                                if window.moveObjetosEixo == 2 or window.moveObjetosEixo == 3:
                                    if window.tabs.tabConfig.blockInsert[0]:
                                        canvas.moveSelectY(yDes, spaceGrid)
                                    else:
                                        Vars.KitLib.moveSelect(c_float(0.0), c_float(yDes*spaceGrid), c_float(0.0))
                                elif window.moveObjetosEixo == 4 or window.moveObjetosEixo == 5:
                                    if window.tabs.tabConfig.blockInsert[0]:
                                        canvas.moveSelectZ(zDes, spaceGrid)
                                    else:
                                        Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(zDes*spaceGrid))
                                elif window.moveObjetosEixo == -2:
                                    Vars.KitLib.moveSelect(c_float(0.0), c_float(yDes*spaceGrid), c_float(zDes*spaceGrid))


                        elif canvas.camera.visionOption == 3 or canvas.camera.visionOption == 4:# agora, se está na visao da direita ou da esquerda, move os o objetos na direção correspondente
                            xDes = (canvas.lastx - canvas.x) / 100
                            zDes = (canvas.lasty - canvas.y) / 100

                            spaceGrid = c_float(Vars.KitLib.getEspacoGrid()).value

                            if spaceGrid == 9.0:
                                spaceGrid *= 0.6
                            elif spaceGrid == 18.0:
                                spaceGrid *= 0.4

                            if canvas.camera.visionOption == 3:
                                if window.moveObjetosEixo == 0 or window.moveObjetosEixo == 1:
                                    if window.tabs.tabConfig.blockInsert[0]:
                                        canvas.moveSelectX(xDes, spaceGrid)
                                    else:
                                        Vars.KitLib.moveSelect(c_float(xDes*spaceGrid), c_float(0.0), c_float(0.0))
                                elif window.moveObjetosEixo == 4 or window.moveObjetosEixo == 5:
                                    if window.tabs.tabConfig.blockInsert[0]:
                                        canvas.moveSelectZ(zDes, spaceGrid)
                                    else:
                                        Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(zDes*spaceGrid))
                                elif window.moveObjetosEixo == -2:
                                    Vars.KitLib.moveSelect(c_float(xDes*spaceGrid), c_float(0.0), c_float(zDes*spaceGrid))
                            else:
                                if window.moveObjetosEixo == 0 or window.moveObjetosEixo == 1:
                                    if window.tabs.tabConfig.blockInsert[0]:
                                        canvas.moveSelectX(-xDes, spaceGrid)
                                    else:
                                        Vars.KitLib.moveSelect(c_float(-xDes*spaceGrid), c_float(0.0), c_float(0.0))
                                elif window.moveObjetosEixo == 4 or window.moveObjetosEixo == 5:
                                    if window.tabs.tabConfig.blockInsert[0]:
                                        canvas.moveSelectZ(zDes, spaceGrid)
                                    else:
                                        Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(zDes*spaceGrid))
                                elif window.moveObjetosEixo == -2:
                                    Vars.KitLib.moveSelect(c_float(-xDes*spaceGrid), c_float(0.0), c_float(zDes*spaceGrid))
                    window.tabs.tabInfo.alteraCentroMBR()
                    window.atualizaPrecisaSalvar(True)
                else: #se a opção de movimentar objetos não foi selecionado pelo usuário
                    if canvas.camera.visionOption == 0: #e está na visao perspectiva, apenas altera os parâmetros da coordenada esférica
                        canvas.camera.theta = canvas.camera.theta + (canvas.lastx - canvas.x) / 300
                        canvas.camera.phi = canvas.camera.phi + (canvas.lasty - canvas.y) / 300
                        if canvas.camera.phi > math.pi / 2:
                           canvas.camera.phi = math.pi / 2
                        elif canvas.camera.phi < 0:
                           canvas.camera.phi = 0.001
                    else: #se não, apenas altera os parametros da visão ortogonal
                        canvas.camera.orthoCenter = (
                            ((canvas.lasty - canvas.y) * canvas.camera.orthoZoom * 0.5 / 300) * c_float(Vars.KitLib.getEspacoGrid()).value + canvas.camera.orthoCenter[0],
                            ((canvas.lastx - canvas.x) * canvas.camera.orthoZoom * 0.5 / 300) * c_float(Vars.KitLib.getEspacoGrid()).value + canvas.camera.orthoCenter[1])

            canvas.camera.atualizaCentroFocus()
            canvas.Refresh(True)

        if canvas.dClickEvent:
            canvas.dClickEvent = False

    @staticmethod
    def OnMouseScroll(evt, canvas):

        if canvas.camera.visionOption == Vars.VISION_Z_PERSP:

            zoom = 0.3
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

        if window.botaoSelecionado == Vars.MOVETELA_SELECIONADO:
            myCursor = wx.Cursor(r"icones/cursorMoveTelaClick.cur",
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
                AdicionarObjetos.OnAddBase(canvas, window)
            elif window.botaoSelecionado == Vars.LIVRE_SELECIONADO:
                Vars.KitLib.terminaMovimentacao()
                Vars.KitLib.deSelectAll()
                window.moveObjetos = False
        idObj = Vars.KitLib.select(ponto, canvas.camera.visionAxis,canvas.camera.visionOption)
        if idObj != 0:
            obj = Vars.KitLib.getObjById(idObj)
            centro = (obj.contents.centro.x, obj.contents.centro.y, obj.contents.centro.z)
            window.tabs.tabInfo.AlteraLayoutInfo(obj.contents.id, obj.contents.obj,centro,0,0)
        else:
            window.tabs.tabInfo.AlteraLayoutInfo(0, 0, None,None,None)

        window.drawArea0.Refresh()
        window.drawArea1.Refresh()
        window.drawArea2.Refresh()
        window.drawArea3.Refresh()

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