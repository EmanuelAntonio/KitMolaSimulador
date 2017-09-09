from VarsAmbient import *
from threading import Timer
import time


class Msg(object):

    tipoYesNo = wx.YES_NO

    janelaWarning = wx.ICON_WARNING

    timer = None
    statusBar = None
    tmp = 0

    @staticmethod
    def exibirMensagem(mensagem, titulo, tipoMsg, tipoJanela):
        msg = wx.MessageDialog(None,
                               mensagem,
                               titulo, tipoMsg | tipoJanela)
        option = msg.ShowModal()
        msg.Destroy()
        return option

    @staticmethod
    def exibirStatusBar(mensagem, tempo):

        if Msg.statusBar != None:
            Msg.tmp = tempo
            if Msg.timer != None:
                Msg.limpaStatusBar()
            Msg.timer = Timer(tempo, Msg.limpaStatusBar)
            Msg.timer.start()
            Msg.statusBar.SetStatusText(mensagem)

    @staticmethod
    def limpaStatusBar():
        Msg.tmp = 0
        if Msg.timer != None:
            Msg.timer.cancel()
            del Msg.timer
            Msg.timer = None
        Msg.statusBar.SetStatusText("")