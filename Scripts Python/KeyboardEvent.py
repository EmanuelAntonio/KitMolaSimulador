
from VarsAmbient import *
from AdicionarObjetos import *

"""
    ->Classe KeyboardEvent:
        Classe para tratar eventos de teclado gerado a partir da classe BaseGui

"""
class KeyboardEvent(object):

    @staticmethod
    def OnKeyDown(e, window):
        if (e.GetKeyCode() == wx.WXK_SHIFT):
            Vars.shiftPress = True

        elif (e.GetKeyCode() == wx.WXK_DELETE):
            Vars.KitLib.removeAll()
            if Vars.KitLib.desfazerSize() > 0:
                window.toolbar.EnableTool(wx.ID_UNDO, True)
            if Vars.KitLib.refazerSize() > 0:
                window.toolbar.EnableTool(wx.ID_REDO, True)
            window.OnRefreshAll()

        elif (e.GetKeyCode() == wx.WXK_CONTROL):

            Vars.ctrlPress = True

        elif (e.GetKeyCode() == Vars.W_PRESS and window.moveObjetos[0]):

            delta = 0.1
            if window.tabs.tabConfig.blockInsert[0]:
                delta = window.tabs.tabConfig.blockInsert[1]
            if (window.ultimoDrawSelected.camera.visionOption == 5):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(delta), c_float(0.0))
            elif (window.ultimoDrawSelected.camera.visionOption != 0):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(delta))

            window.atualizaPrecisaSalvar(True)

        elif (e.GetKeyCode() == Vars.S_PRESS and window.moveObjetos[0]):

            delta = 0.1
            if window.tabs.tabConfig.blockInsert[0]:
                delta = window.tabs.tabConfig.blockInsert[1]
            if (window.ultimoDrawSelected.camera.visionOption == 5):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(-delta), c_float(0.0))
            elif (window.ultimoDrawSelected.camera.visionOption != 0):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(-delta))
            window.atualizaPrecisaSalvar(True)

        elif (e.GetKeyCode() == Vars.A_PRESS and window.moveObjetos[0]):
            delta = 0.1
            if window.tabs.tabConfig.blockInsert[0]:
                delta = window.tabs.tabConfig.blockInsert[1]
            if (window.ultimoDrawSelected.camera.visionOption == 5):
                Vars.KitLib.moveSelect(c_float(-delta), c_float(0.0), c_float(0.0))
            elif (window.ultimoDrawSelected.camera.visionOption == 1):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(-delta), c_float(0.0))
            elif (window.ultimoDrawSelected.camera.visionOption == 2):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(delta), c_float(0.0))
            elif (window.ultimoDrawSelected.camera.visionOption == 3):
                Vars.KitLib.moveSelect(c_float(delta), c_float(0.0), c_float(0.0))
            elif (window.ultimoDrawSelected.camera.visionOption == 4):
                Vars.KitLib.moveSelect(c_float(-delta), c_float(0.0), c_float(0.0))

            window.atualizaPrecisaSalvar(True)

        elif (e.GetKeyCode() == Vars.D_PRESS and window.moveObjetos[0]):
            delta = 0.1
            if window.tabs.tabConfig.blockInsert[0]:
                delta = window.tabs.tabConfig.blockInsert[1]
            if (window.ultimoDrawSelected.camera.visionOption == 5):
                Vars.KitLib.moveSelect(c_float(delta), c_float(0.0), c_float(0.0))
            elif (window.ultimoDrawSelected.camera.visionOption == 1):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(delta), c_float(0.0))
            elif (window.ultimoDrawSelected.camera.visionOption == 2):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(-delta), c_float(0.0))
            elif (window.ultimoDrawSelected.camera.visionOption == 3):
                Vars.KitLib.moveSelect(c_float(-delta), c_float(0.0), c_float(0.0))
            elif (window.ultimoDrawSelected.camera.visionOption == 4):
                Vars.KitLib.moveSelect(c_float(0.1), c_float(0.0), c_float(0.0))
            window.atualizaPrecisaSalvar(True)

        elif (e.GetKeyCode() == Vars.G_PRESS):

            window.moveObjetos = (not (window.moveObjetos[0]), Vars.ASCII_0)
            if window.moveObjetos[0]:
                Msg.exibirStatusBar("Selecione um eixo de mivimentação precionando x, y ou z",10)

            if window.rotacionaObjetos[0]:
                window.rotacionaObjetos = (False, Vars.ASCII_0)
            # window.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
            window.OnRefreshAll()
        elif (e.GetKeyCode() == Vars.NUM_0_PRESS or e.GetKeyCode() == Vars.N_0_PRESS):
            if (window.rotacionaObjetos[0]):
                KeyboardEvent.OnRotObj(window, 0)
            elif window.ultimoDrawSelected != None:
                window.ultimoDrawSelected.camera.visionOption = Vars.VISION_Z_PERSP
                window.ultimoDrawSelected.camera.visionAxis = Vars.ASCII_Z  # 122 Codigo ASCII para 'z'
                # Vars.visionItem.SetLabelText(Vars.visionModes[0])
                window.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.NUM_1_PRESS or e.GetKeyCode() == Vars.N_1_PRESS):
            if (window.rotacionaObjetos[0]):
                KeyboardEvent.OnRotObj(window, 1)
            elif window.ultimoDrawSelected != None:
                window.ultimoDrawSelected.camera.visionOption = Vars.VISION_Z_ORTHO
                window.ultimoDrawSelected.camera.visionAxis = Vars.ASCII_Z  # 122 Codigo ASCII para 'z'
                # Vars.visionItem.SetLabelText(Vars.visionModes[5])
                window.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.NUM_2_PRESS or e.GetKeyCode() == Vars.N_2_PRESS):
            if (window.rotacionaObjetos[0]):
                KeyboardEvent.OnRotObj(window, 2)
            elif window.ultimoDrawSelected != None:
                window.ultimoDrawSelected.camera.visionOption = Vars.VISION_X_POS
                window.ultimoDrawSelected.camera.visionAxis = Vars.ASCII_X  # 122 Codigo ASCII para 'z'
                # Vars.visionItem.SetLabelText(Vars.visionModes[1])
                window.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.NUM_3_PRESS or e.GetKeyCode() == Vars.N_3_PRESS):
            if (window.rotacionaObjetos[0]):
                KeyboardEvent.OnRotObj(window, 3)
            elif window.ultimoDrawSelected != None:
                window.ultimoDrawSelected.camera.visionOption = Vars.VISION_X_NEG
                window.ultimoDrawSelected.camera.visionAxis = Vars.ASCII_X  # 122 Codigo ASCII para 'z'
                # Vars.visionItem.SetLabelText(Vars.visionModes[2])
                window.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.NUM_4_PRESS or e.GetKeyCode() == Vars.N_4_PRESS):
            if (window.rotacionaObjetos[0]):
                KeyboardEvent.OnRotObj(window, 4)
            elif window.ultimoDrawSelected != None:
                window.ultimoDrawSelected.camera.visionOption = Vars.VISION_Y_POS
                window.ultimoDrawSelected.camera.visionAxis = Vars.ASCII_Y  # 122 Codigo ASCII para 'z'
                # window.visionItem.SetLabelText(Vars.visionModes[3])
                window.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.NUM_5_PRESS or e.GetKeyCode() == Vars.N_5_PRESS):
            if (window.rotacionaObjetos[0]):
                KeyboardEvent.OnRotObj(window, 5)
            elif window.ultimoDrawSelected != None:
                window.ultimoDrawSelected.camera.visionOption = Vars.VISION_Y_NEG
                window.ultimoDrawSelected.camera.visionAxis = Vars.ASCII_Y  # 122 Codigo ASCII para 'z'
                # window.visionItem.SetLabelText(Vars.visionModes[4])
                window.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.NUM_6_PRESS or e.GetKeyCode() == Vars.N_6_PRESS):
            if(window.rotacionaObjetos[0]):
                KeyboardEvent.OnRotObj(window,6)
        elif (e.GetKeyCode() == Vars.NUM_7_PRESS or e.GetKeyCode() == Vars.N_7_PRESS):
            if(window.rotateObjetos[0]):
                KeyboardEvent.OnRotObj(window,7)
        elif (e.GetKeyCode() == Vars.NUM_8_PRESS or e.GetKeyCode() == Vars.N_8_PRESS):
            if(window.rotacionaObjetos[0]):
                KeyboardEvent.OnRotObj(window,8)
        elif (e.GetKeyCode() == Vars.NUM_9_PRESS or e.GetKeyCode() == Vars.N_9_PRESS):
            if(window.rotacionaObjetos[0]):
                KeyboardEvent.OnRotObj(window,9)
        elif (e.GetKeyCode() == Vars.BACK_SPACE):
            if (window.rotacionaObjetos[0]):
                KeyboardEvent.OnDeleteRotObj(window)
        elif (e.GetKeyCode() == Vars.ESC_PRESS):
            if window.moveObjetos[0]:
                if window.botaoSelecionado != Vars.MOVETELA_SELECIONADO:
                    Vars.KitLib.cancelarMovimentacao()
                    window.moveObjetos = (False, Vars.ASCII_0)
                    Vars.KitLib.deSelectAll()
                    Msg.limpaStatusBar()
            if window.rotacionaObjetos[0]:
                if window.botaoSelecionado != Vars.MOVETELA_SELECIONADO:
                    Vars.KitLib.cancelarRotacao()
                    window.rotacionaObjetos = (False, Vars.ASCII_0)
                    Vars.KitLib.deSelectAll()
                    Msg.limpaStatusBar()
            if window.botaoSelecionado != Vars.LIVRE_SELECIONADO:
                window.botaoSelecionado = Vars.LIVRE_SELECIONADO
                window.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            Msg.exibirStatusBar("", 0)
        elif (e.GetKeyCode() == Vars.T_PRESS):
            if window.showTabs or window.showToolbarSide:
                window.showTabs = False
                window.showToolbarSide = False
                window.tabs.Hide()
                window.toolbarside.Hide()
                window.sizerToolSide.Layout()
                window.boxBtn.Layout()
                window.boxMain.Layout()
                window.sizerWindow.Layout()
                window.sizerWindowStatus.Layout()
                window.tabs.SetFocus()
            else:
                window.showTabs = True
                window.showToolbarSide = True
                window.tabs.Show(True)
                window.toolbarside.Show(True)
                window.sizerToolSide.Layout()
                window.boxBtn.Layout()
                window.boxMain.Layout()
                window.sizerWindow.Layout()
                window.sizerWindowStatus.Layout()
                window.tabs.SetFocus()

        elif(e.GetKeyCode() == Vars.F1_PRESS):
            if window.showTabs:
                window.showTabs = False
                window.tabs.Hide()
                window.boxBtn.Layout()
                window.boxMain.Layout()
                window.sizerWindow.Layout()
                window.sizerWindowStatus.Layout()
                window.tabs.SetFocus()
            else:
                window.showTabs = True
                window.tabs.Show(True)
                window.boxBtn.Layout()
                window.boxMain.Layout()
                window.sizerWindow.Layout()
                window.sizerWindowStatus.Layout()
                window.tabs.SetFocus()
        elif(e.GetKeyCode() == Vars.F2_PRESS):
            if window.showToolbarSide:
                window.showToolbarSide = False
                window.toolbarside.Hide()
                window.sizerToolSide.Layout()
                window.boxMain.Layout()
                window.sizerWindow.Layout()
                window.sizerWindowStatus.Layout()
                window.tabs.SetFocus()
            else:
                window.showToolbarSide = True
                window.toolbarside.Show(True)
                window.sizerToolSide.Layout()
                window.sizerWindow.Layout()
                window.sizerWindowStatus.Layout()
                window.tabs.SetFocus()

        elif (e.GetKeyCode() == e.GetKeyCode() == Vars.NUM_PLUS):
            window.ultimoDrawSelected.OnZoomOut()
        elif (e.GetKeyCode() == e.GetKeyCode() == Vars.NUM_LESS or e.GetKeyCode() == e.GetKeyCode() == Vars.LESS_PRESS):
            window.ultimoDrawSelected.OnZoomIn()
        elif (e.GetKeyCode() == Vars.K_PRESS):
            """if Vars.KitSim.getSSim():
                Vars.KitSim.stop()
            else:
                Vars.KitSim.setListaObjetos(Vars.KitLib.getObjList())
                Vars.KitSim.start()"""
            Vars.KitSim.processarObjetos()
        elif (e.GetKeyCode() == Vars.R_PRESS):
            window.rotacionaObjetos = (not(window.rotacionaObjetos[0]), Vars.ASCII_0)
            if window.rotacionaObjetos[0]:
                window.rotacionaSelectCentro = True
                Msg.exibirStatusBar("Selecione um objeto com o botão esquerdo do mouse para ser o centro de rotacão", 10)
            else:
                Vars.KitLib.cancelarRotacao()
            if window.moveObjetos[0]:
                window.moveObjetos = (False,Vars.ASCII_0)


        elif (e.GetKeyCode() == Vars.X_PRESS):
            if window.moveObjetos[0]:
                window.moveObjetos = (window.moveObjetos[0],Vars.ASCII_X)
                Msg.exibirStatusBar("Use o botão esquerdo do mouse para movimentar os objetos selecionados, ESC para cancelar, ou ENTER para confirmar a ação", 10)

            elif window.rotacionaObjetos[0]:
                window.rotacionaObjetos = (window.rotacionaObjetos[0],Vars.ASCII_X)
                window.rotacionaSelectCentro = False
                Msg.exibirStatusBar("Use o botão esquerdo do mouse para rotacionar os objetos selecionados, ESC para cancelar, ou ENTER para confirmar a ação",10)
                Vars.anguloRotacao = 0

        elif (e.GetKeyCode() == Vars.Y_PRESS):
            if window.moveObjetos[0]:
                window.moveObjetos = (window.moveObjetos[0],Vars.ASCII_Y)
                Msg.exibirStatusBar("Use o botão esquerdo do mouse para movimentar os objetos selecionados, ESC para cancelar, ou ENTER para confirmar a ação",10)

            elif window.rotacionaObjetos[0]:
                window.rotacionaObjetos = (window.rotacionaObjetos[0], Vars.ASCII_Y)
                window.rotacionaSelectCentro = False
                Msg.exibirStatusBar("Use o botão esquerdo do mouse para rotacionar os objetos selecionados, ESC para cancelar, ou ENTER para confirmar a ação",10)
                Vars.anguloRotacao = 0

        elif (e.GetKeyCode() == Vars.Z_PRESS):
            if window.moveObjetos[0]:
                window.moveObjetos = (window.moveObjetos[0], Vars.ASCII_Z)
                Msg.exibirStatusBar("Use o botão esquerdo do mouse para movimentar os objetos selecionados, ESC para cancelar, ou ENTER para confirmar a ação",10)

            elif window.rotacionaObjetos[0]:
                window.rotacionaObjetos = (window.rotacionaObjetos[0], Vars.ASCII_Z)
                window.rotacionaSelectCentro = False
                Msg.exibirStatusBar("Use o botão esquerdo do mouse para rotacionar os objetos selecionados, ESC para cancelar, ou ENTER para confirmar a ação",10)
                Vars.anguloRotacao = 0
            else:
                Vars.KitLib.setWireframe(not (Vars.KitLib.getWireframe()))
        else:
            print(e.GetKeyCode())

        window.OnRefreshAll()

    @staticmethod
    def OnKeyUp(e):
        if (e.GetKeyCode() == wx.WXK_SHIFT):
            Vars.shiftPress = False
        elif (e.GetKeyCode() == wx.WXK_CONTROL):
            Vars.ctrlPress = False
        e.Skip()

    @staticmethod
    def OnEnterKeyDown(e, window):

        moveTelaSelected = False
        if e.GetKeyCode() == Vars.ENTER_PRESS:
            if window.botaoSelecionado != Vars.LIVRE_SELECIONADO:
                if window.botaoSelecionado == Vars.LAJE_SELECIONADO:
                    AdicionarObjetos.OnAddLaje(window)
                elif window.botaoSelecionado == Vars.BAR9_SELECIONADO:
                    AdicionarObjetos.OnAddBar(None,window)
                elif window.botaoSelecionado == Vars.TIRANTE9_SELECIONADO:
                    AdicionarObjetos.OnAddSmallDiag(None,window)
                elif window.botaoSelecionado == Vars.TIRANTE18_SELECIONADO:
                    AdicionarObjetos.OnAddLargeDiag(None,window)
                elif window.botaoSelecionado == Vars.MOVETELA_SELECIONADO:
                    moveTelaSelected = True
                window.botaoSelecionado = Vars.LIVRE_SELECIONADO
                window.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))

            if window.moveObjetos[0] and not(moveTelaSelected):
                Vars.KitLib.terminaMovimentacao()
                window.moveObjetos = (False,Vars.ASCII_0)
                Msg.limpaStatusBar()
            if window.rotacionaObjetos[0]:
                if window.rotacionaSelectCentro:
                    window.rotacionaSelectCentro = False
                    Msg.exibirStatusBar("Selecione um eixo de mivimentação precionando x, y ou z", 10)
                else:
                    Vars.KitLib.terminarRotacao()
                    window.rotacionaObjetos = (False, Vars.ASCII_0)
                    Vars.KitLib.deSelectAll()
                    Msg.limpaStatusBar()

            if window.ultimoDrawSelected != None:
                window.ultimoDrawSelected.Refresh(True)

            Msg.exibirStatusBar("",0)
        else:# Se  caso não for pressionado a tecla enter, o else libera o evento para que possa ser usado no wx.EVT_KEY_DOWN
            e.Skip()

    @staticmethod
    def OnRotObj(window, anguloAcrescimo):

        stringEixo = ""

        rot = False

        if window.rotacionaObjetos[1] == Vars.ASCII_X:
            Vars.KitLib.rotacionaSelect(True, False, False, c_float(-Vars.anguloRotacao))
            rot = Vars.KitLib.rotacionaSelect(True, False, False, c_float(math.radians(math.degrees(Vars.anguloRotacao)*10 + anguloAcrescimo)))
            stringEixo = "X = "
        elif window.rotacionaObjetos[1] == Vars.ASCII_Y:
            Vars.KitLib.rotacionaSelect(False, True, False, c_float(-Vars.anguloRotacao))
            rot = Vars.KitLib.rotacionaSelect(False, True, False, c_float(math.radians(math.degrees(Vars.anguloRotacao)*10 + anguloAcrescimo)))
            stringEixo = "Y = "
        elif window.rotacionaObjetos[1] == Vars.ASCII_Z:
            Vars.KitLib.rotacionaSelect(False, False, True, c_float(-Vars.anguloRotacao))
            rot = Vars.KitLib.rotacionaSelect(False, False, True, c_float(math.radians(math.degrees(Vars.anguloRotacao)*10 + anguloAcrescimo)))
            stringEixo = "Z = "

        Vars.anguloRotacao = math.radians(math.degrees(Vars.anguloRotacao)*10 + anguloAcrescimo)
        if not (rot):
            Msg.exibirStatusBar("Bases só podem ser rotacionadas no eixo Z.", 10)
        else:
            angulo = math.degrees(Vars.anguloRotacao)
            Msg.exibirStatusBar(stringEixo + str(round(angulo, 2)) + "º", 0)

    @staticmethod
    def OnDeleteRotObj(window):

        stringEixo = ""

        if window.rotacionaObjetos[1] == Vars.ASCII_X:
            Vars.KitLib.rotacionaSelect(True, False, False, c_float(-Vars.anguloRotacao))
            rot = Vars.KitLib.rotacionaSelect(True, False, False, c_float(
                math.radians(int(math.degrees(Vars.anguloRotacao) / 10))))
            stringEixo = "X = "
        elif window.rotacionaObjetos[1] == Vars.ASCII_Y:
            Vars.KitLib.rotacionaSelect(False, True, False, c_float(-Vars.anguloRotacao))
            rot = Vars.KitLib.rotacionaSelect(False, True, False, c_float(
                math.radians(int(math.degrees(Vars.anguloRotacao) / 10))))
            stringEixo = "Y = "
        elif window.rotacionaObjetos[1] == Vars.ASCII_Z:
            Vars.KitLib.rotacionaSelect(False, False, True, c_float(-Vars.anguloRotacao))
            rot = Vars.KitLib.rotacionaSelect(False, False, True, c_float(
                math.radians(int(math.degrees(Vars.anguloRotacao) / 10))))
            stringEixo = "Z = "

        Vars.anguloRotacao = math.radians(int(math.degrees(Vars.anguloRotacao) / 10))
        if not (rot):
            Msg.exibirStatusBar("Bases só podem ser rotacionadas no eixo Z.", 10)
        else:
            angulo = math.degrees(Vars.anguloRotacao)
            Msg.exibirStatusBar(stringEixo + str(round(angulo, 2)) + "º", 0)