from Msg import *


class AdicionarObjetos(object):

    @staticmethod
    def OnAddSphere(drawArea, window):

        x, y = Vars.rightMouse
        if drawArea.camera.visionOption != Vars.VISION_Z_PERSP:

            ponto = [0, 0, 0]
            ponto_size = len(ponto)
            ponto = (ctypes.c_float * ponto_size)(*ponto)
            Vars.KitLib.getPonto3DFloat(c_int(x), c_int(y), ponto)
            if drawArea.camera.visionAxis == Vars.ASCII_Z:  # 122 Codigo ASCII para 'z'
                x = ponto[0]
                y = ponto[1]
                if window.tabs.tabConfig.blockInsert[0]:
                    space = window.tabs.tabConfig.blockInsert[1]
                    x = x / space
                    dx = x - int(x)
                    dx = math.fabs(dx)
                    if dx < 0.5:
                        x = int(x) * space
                    else:
                        if x >= 0:
                            x = (int(x) + 1) * space
                        else:
                            x = (int(x) - 1) * space
                    y = y / space
                    dy = y - int(y)
                    dy = math.fabs(dy)
                    if dy < 0.5:
                        y = int(y) * space
                    else:
                        if y >= 0:
                            y = (int(y) + 1) * space
                        else:
                            y = (int(y) - 1) * space
                Vars.KitLib.addSphere(c_float(x), c_float(y), 0)
            elif drawArea.camera.visionAxis == Vars.ASCII_X:  # 120 Codigo ASCII para 'x'

                x = ponto[0]
                y = ponto[1]
                if window.tabs.tabConfig.blockInsert[0]:
                    space = window.tabs.tabConfig.blockInsert[1]
                    x = x / space
                    dx = x - int(x)
                    dx = math.fabs(dx)
                    if dx < 0.5:
                        x = int(x) * space
                    else:
                        if x >= 0:
                            x = (int(x) + 1) * space
                        else:
                            x = (int(x) - 1) * space
                    y = y / space
                    dy = y - int(y)
                    dy = math.fabs(dy)
                    if dy < 0.5:
                        y = int(y) * space
                    else:
                        if y >= 0:
                            y = (int(y) + 1) * space
                        else:
                            y = (int(y) - 1) * space
                if drawArea.camera.visionOption == Vars.VISION_X_POS:
                    Vars.KitLib.addSphere(0, ctypes.c_float(x), ctypes.c_float(y))
                else:
                    Vars.KitLib.addSphere(0, ctypes.c_float(y), ctypes.c_float(x))
            elif drawArea.camera.visionAxis == Vars.ASCII_Y:  # 121 Codigo ASCII para 'y'
                x = ponto[0]
                y = ponto[1]
                if window.tabs.tabConfig.blockInsert[0]:
                    space = window.tabs.tabConfig.blockInsert[1]
                    x = x / space
                    dx = x - int(x)
                    dx = math.fabs(dx)
                    if dx < 0.5:
                        x = int(x) * space
                    else:
                        if x >= 0:
                            x = (int(x) + 1) * space
                        else:
                            x = (int(x) - 1) * space
                    y = y / space
                    dy = y - int(y)
                    dy = math.fabs(dy)
                    if dy < 0.5:
                        y = int(y) * space
                    else:
                        if y >= 0:
                            y = (int(y) + 1) * space
                        else:
                            y = (int(y) - 1) * space

                Vars.KitLib.addSphere(ctypes.c_float(x), 0, ctypes.c_float(y))

        window.OnRefreshAll()
        window.toolbar.EnableTool(wx.ID_UNDO, True)
        window.toolbar.EnableTool(wx.ID_REDO, False)
        window.atualizaPrecisaSalvar(True)
        window.tabs.SetFocus()

    @staticmethod
    def OnAddBase(tipo, drawArea, window):

        x, y = Vars.rightMouse
        if drawArea.camera.visionOption != Vars.VISION_Z_PERSP:

            ponto = [0, 0, 0]
            ponto_size = len(ponto)
            ponto = (ctypes.c_float * ponto_size)(*ponto)
            Vars.KitLib.getPonto3DFloat(c_int(x), c_int(y), ponto)
            if drawArea.camera.visionAxis == Vars.ASCII_Z:  # 122 Codigo ASCII para 'z'
                x = ponto[0]
                y = ponto[1]
                if window.tabs.tabConfig.blockInsert:
                    space = c_float(Vars.KitLib.getEspacoGrid()).value
                    x = x / space
                    dx = x - int(x)
                    dx = math.fabs(dx)
                    if dx < 0.5:
                        x = int(x) * space
                    else:
                        if x >= 0:
                            x = (int(x) + 1) * space
                        else:
                            x = (int(x) - 1) * space
                    y = y / space
                    dy = y - int(y)
                    dy = math.fabs(dy)
                    if dy < 0.5:
                        y = int(y) * space
                    else:
                        if y >= 0:
                            y = (int(y) + 1) * space
                        else:
                            y = (int(y) - 1) * space
                Vars.KitLib.addBase(tipo, c_float(x), c_float(y), 0)
            elif drawArea.camera.visionAxis == Vars.ASCII_X:  # 120 Codigo ASCII para 'x'

                x = ponto[0]
                y = ponto[1]
                if window.tabs.tabConfig.blockInsert:
                    space = c_float(Vars.KitLib.getEspacoGrid()).value
                    x = x / space
                    dx = x - int(x)
                    dx = math.fabs(dx)
                    if dx < 0.5:
                        x = int(x) * space
                    else:
                        if x >= 0:
                            x = (int(x) + 1) * space
                        else:
                            x = (int(x) - 1) * space
                    y = y / space
                    dy = y - int(y)
                    dy = math.fabs(dy)
                    if dy < 0.5:
                        y = int(y) * space
                    else:
                        if y >= 0:
                            y = (int(y) + 1) * space
                        else:
                            y = (int(y) - 1) * space
                if drawArea.camera.visionOption == Vars.VISION_X_POS:
                    Vars.KitLib.addBase(tipo, 0, ctypes.c_float(x), ctypes.c_float(y))
                else:
                    Vars.KitLib.addBase(tipo, 0, ctypes.c_float(y), ctypes.c_float(x))
            elif drawArea.camera.visionAxis == Vars.ASCII_Y:  # 121 Codigo ASCII para 'y'
                x = ponto[0]
                y = ponto[1]
                if window.tabs.tabConfig.blockInsert:
                    space = c_float(Vars.KitLib.getEspacoGrid()).value
                    x = x / space
                    dx = x - int(x)
                    dx = math.fabs(dx)
                    if dx < 0.5:
                        x = int(x) * space
                    else:
                        if x >= 0:
                            x = (int(x) + 1) * space
                        else:
                            x = (int(x) - 1) * space
                    y = y / space
                    dy = y - int(y)
                    dy = math.fabs(dy)
                    if dy < 0.5:
                        y = int(y) * space
                    else:
                        if y >= 0:
                            y = (int(y) + 1) * space
                        else:
                            y = (int(y) - 1) * space

                Vars.KitLib.addBase(tipo, ctypes.c_float(x), 0, ctypes.c_float(y))

        window.OnRefreshAll()
        drawArea.Refresh()
        window.toolbar.EnableTool(wx.ID_UNDO, True)
        window.toolbar.EnableTool(wx.ID_REDO, False)
        window.atualizaPrecisaSalvar(True)
        window.tabs.SetFocus()

    @staticmethod
    def OnAddSmallBar(drawArea, window):

        BAR_SMALL = 2
        add = Vars.KitLib.addBar(BAR_SMALL)
        if not (add):
            msg = "Para adicionar uma barra pequena certifique-se que tenha duas esferas selecionadas, ou uma esfera e uma base e que a distância entre elas seja de 7.5 cm."
            Msg.exibirStatusBar(msg,10)

        window.OnRefreshAll()
        if(drawArea is not None):
            drawArea.Refresh()
        window.toolbar.EnableTool(wx.ID_UNDO, True)
        window.toolbar.EnableTool(wx.ID_REDO, False)
        window.atualizaPrecisaSalvar(True)
        window.tabs.SetFocus()

    @staticmethod
    def OnAddLargeBar(drawArea, window):

        BAR_LARGE = 3
        add = Vars.KitLib.addBar(BAR_LARGE)
        if not (add):
            msg = "Para adicionar uma barra grande certifique-se que tenha duas esferas selecionadas, ou uma esfera e uma base e que a distância entre elas seja de 16.5 cm."
            Msg.exibirStatusBar(msg,10)

        window.OnRefreshAll()
        if (drawArea is not None):
            drawArea.Refresh()
        window.toolbar.EnableTool(wx.ID_UNDO, True)
        window.toolbar.EnableTool(wx.ID_REDO, False)
        window.atualizaPrecisaSalvar(True)
        window.tabs.SetFocus()

    @staticmethod
    def OnAddLaje(window):
        if not(Vars.KitLib.addLaje()):
            msg = "Para adicionar uma laje, certifique-se de selecionar quatro esferas, e estas sejam os vertices de um retângulo 9cm X 18cm(contando do centro da esfera)."
            Msg.exibirStatusBar(msg, 10)
            window.atualizaPrecisaSalvar(True)
        window.tabs.SetFocus()

    @staticmethod
    def OnAddSmallDiag(drawArea, window):
        DIAGONAL_SMALL = 6
        add = Vars.KitLib.addDiag(DIAGONAL_SMALL)
        if not (add):
            msg = "Para adicionar uma diagonal 9x9 certifique-se que tenha duas esferas selecionadas, ou uma esfera e uma base e que a distância entre elas seja de 10.61 cm"
            Msg.exibirStatusBar(msg, 10)
        window.OnRefreshAll()
        if (drawArea is not None):
            drawArea.Refresh()
        window.toolbar.EnableTool(wx.ID_UNDO, True)
        window.toolbar.EnableTool(wx.ID_REDO, False)
        window.atualizaPrecisaSalvar(True)
        window.tabs.SetFocus()

    @staticmethod
    def OnAddLargeDiag(drawArea, window):
        DIAGONAL_LARGE = 7
        add = Vars.KitLib.addDiag(DIAGONAL_LARGE)
        if not (add):
            msg = "Para adicionar uma barra pequena certifique-se que tenha duas esferas selecionadas, ou uma esfera e uma base e que a distância entre elas seja de 18.12 cm."
            Msg.exibirStatusBar(msg, 10)
        window.OnRefreshAll()
        if (drawArea is not None):
            drawArea.Refresh()
        window.toolbar.EnableTool(wx.ID_UNDO, True)
        window.toolbar.EnableTool(wx.ID_REDO, False)
        window.atualizaPrecisaSalvar(True)
        window.tabs.SetFocus()

    @staticmethod
    def OnAddLigRigida(drawArea, window):

        add = Vars.KitLib.addLigRigida()
        if not (add):
            msg = "Para adicionar uma ligação rígida é necessário que esteja com duas barras e uma esfera selecionada\nConfira que as duas barras estejam em 90º."
            Msg.exibirStatusBar(msg, 10)
        window.OnRefreshAll()
        if (drawArea is not None):
            drawArea.Refresh()
        window.toolbar.EnableTool(wx.ID_UNDO, True)
        window.toolbar.EnableTool(wx.ID_REDO, False)
        window.atualizaPrecisaSalvar(True)
        window.tabs.SetFocus()