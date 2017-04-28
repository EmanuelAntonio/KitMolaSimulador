
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

        elif (e.GetKeyCode() == Vars.W_PRESS and window.moveObjetos):

            delta = 0.1
            if window.tabs.tabConfig.blockInsert[0]:
                delta = window.tabs.tabConfig.blockInsert[1]
            if (window.ultimoDrawSelected.camera.visionOption == 5):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(delta), c_float(0.0))
            elif (window.ultimoDrawSelected.camera.visionOption != 0):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(delta))

            window.atualizaPrecisaSalvar(True)

        elif (e.GetKeyCode() == Vars.S_PRESS and window.moveObjetos):

            delta = 0.1
            if window.tabs.tabConfig.blockInsert[0]:
                delta = window.tabs.tabConfig.blockInsert[1]
            if (window.ultimoDrawSelected.camera.visionOption == 5):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(-delta), c_float(0.0))
            elif (window.ultimoDrawSelected.camera.visionOption != 0):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(-delta))
            window.atualizaPrecisaSalvar(True)

        elif (e.GetKeyCode() == Vars.A_PRESS and window.moveObjetos):
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

        elif (e.GetKeyCode() == Vars.D_PRESS and window.moveObjetos):
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
            window.moveObjetos = not (window.moveObjetos)
            # window.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))

        elif (e.GetKeyCode() == Vars.Z_PRESS):
            Vars.KitLib.setWireframe(not (Vars.KitLib.getWireframe()))
        elif (e.GetKeyCode() == Vars.NUM_0_PRESS or e.GetKeyCode() == Vars.N_0_PRESS):
            if window.ultimoDrawSelected != None:
                window.ultimoDrawSelected.camera.visionOption = Vars.VISION_Z_PERSP
                window.ultimoDrawSelected.camera.visionAxis = Vars.ASCII_Z  # 122 Codigo ASCII para 'z'
                # Vars.visionItem.SetLabelText(Vars.visionModes[0])
                window.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.NUM_1_PRESS or e.GetKeyCode() == Vars.N_1_PRESS):
            if window.ultimoDrawSelected != None:
                window.ultimoDrawSelected.camera.visionOption = Vars.VISION_Z_ORTHO
                window.ultimoDrawSelected.camera.visionAxis = Vars.ASCII_Z  # 122 Codigo ASCII para 'z'
                # Vars.visionItem.SetLabelText(Vars.visionModes[5])
                window.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.NUM_2_PRESS or e.GetKeyCode() == Vars.N_2_PRESS):
            if window.ultimoDrawSelected != None:
                window.ultimoDrawSelected.camera.visionOption = Vars.VISION_X_POS
                window.ultimoDrawSelected.camera.visionAxis = Vars.ASCII_X  # 122 Codigo ASCII para 'z'
                # Vars.visionItem.SetLabelText(Vars.visionModes[1])
                window.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.NUM_3_PRESS or e.GetKeyCode() == Vars.N_3_PRESS):
            if window.ultimoDrawSelected != None:
                window.ultimoDrawSelected.camera.visionOption = Vars.VISION_X_NEG
                window.ultimoDrawSelected.camera.visionAxis = Vars.ASCII_X  # 122 Codigo ASCII para 'z'
                # Vars.visionItem.SetLabelText(Vars.visionModes[2])
                window.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.NUM_4_PRESS or e.GetKeyCode() == Vars.N_4_PRESS):
            if window.ultimoDrawSelected != None:
                window.ultimoDrawSelected.camera.visionOption = Vars.VISION_Y_POS
                window.ultimoDrawSelected.camera.visionAxis = Vars.ASCII_Y  # 122 Codigo ASCII para 'z'
                # window.visionItem.SetLabelText(Vars.visionModes[3])
                window.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.NUM_5_PRESS or e.GetKeyCode() == Vars.N_5_PRESS):
            if window.ultimoDrawSelected != None:
                window.ultimoDrawSelected.camera.visionOption = Vars.VISION_Y_NEG
                window.ultimoDrawSelected.camera.visionAxis = Vars.ASCII_Y  # 122 Codigo ASCII para 'z'
                # window.visionItem.SetLabelText(Vars.visionModes[4])
                window.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.ESC_PRESS):
            if window.moveObjetos:
                Vars.KitLib.cancelarMovimentacao()
                window.moveObjetos = False
                Vars.KitLib.deSelectAll()
            if window.botaoSelecionado != Vars.LIVRE_SELECIONADO:
                window.botaoSelecionado = Vars.LIVRE_SELECIONADO
                window.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        elif (e.GetKeyCode() == Vars.T_PRESS):
            if window.showTabs:
                window.showTabs = False
                window.tabs.Hide()
                window.boxMain.Layout()
                window.tabs.SetFocus()
            else:
                window.showTabs = True
                window.tabs.Show(True)
                window.boxMain.Layout()
                window.tabs.SetFocus()
        elif (e.GetKeyCode() == e.GetKeyCode() == Vars.NUM_PLUS):
            window.ultimoDrawSelected.OnZoomOut()
        elif (e.GetKeyCode() == e.GetKeyCode() == Vars.NUM_LESS or e.GetKeyCode() == e.GetKeyCode() == Vars.LESS_PRESS):
            window.ultimoDrawSelected.OnZoomIn()
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

        if e.GetKeyCode() == Vars.ENTER_PRESS:
            if window.botaoSelecionado != Vars.LIVRE_SELECIONADO:
                if window.botaoSelecionado == Vars.LAJE_SELECIONADO:
                    AdicionarObjetos.OnAddLaje(window)
                elif window.botaoSelecionado == Vars.BAR9_SELECIONADO:
                    AdicionarObjetos.OnAddSmallBar(None,window)
                elif window.botaoSelecionado == Vars.BAR18_SELECIONADO:
                    AdicionarObjetos.OnAddLargeBar(None,window)
                window.botaoSelecionado = Vars.LIVRE_SELECIONADO
                window.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
            if window.moveObjetos:
                Vars.KitLib.terminaMovimentacao()
                window.moveObjetos = False
            window.ultimoDrawSelected.Refresh(True)
        else:# Se  caso não for pressionado a tecla enter, o else libera o evento para que possa ser usado no wx.EVT_KEY_DOWN
            e.Skip()