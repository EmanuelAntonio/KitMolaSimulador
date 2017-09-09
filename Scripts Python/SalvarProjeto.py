
from VarsAmbient import *

class SalvarProjeto(object):

    def __init__(self,parent):
        self.arquivoProjeto = ""  # Variável que armazena o diretorio com o nome do projeto que está aberto atualmente
        self.precisaSalvar = True  # Variável que armazena se houve alteração no projeto após o último salvamento
        self.parent = parent

    def atualizaPrecisaSalvar(self, window, valor):

        if valor:
            if self.arquivoProjeto != "":
                self.precisaSalvar = True
                window.SetTitle(window.strTitle + " - *[" + self.arquivoProjeto + "]")
            else:
                self.precisaSalvar = True
                window.SetTitle(window.strTitle + " - *[" + window.strSemTitulo + "]")
        else:
            if self.arquivoProjeto != "":
                self.precisaSalvar = False
                window.SetTitle(window.strTitle + " - [" + self.arquivoProjeto + "]")
            else:
                self.precisaSalvar = False
                window.SetTitle(window.strTitle + " - [" + window.strSemTitulo + "]")

    def OnOpen(self, window):

        window.toolbar.EnableTool(wx.ID_UNDO, False)
        window.toolbar.EnableTool(wx.ID_REDO, False)
        openFileDialog = wx.FileDialog(window, "Abrir...", "", "",
                                       "Projeto KitSim (*.kmp)|*.kmp",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()
        arquivo = openFileDialog.GetPath()
        openFileDialog.Destroy()
        if arquivo != "":
            self.arquivoProjeto = arquivo
            window.SetTitle(window.strTitle + " - [" + self.arquivoProjeto + "]")

            self.onOpen(self.arquivoProjeto)

            window.tabs.tabConfig.txtTamGrid.SetValue(str(Vars.KitLib.getTamGrid()))
            espacoGrid = c_float(Vars.KitLib.getEspacoGrid()).value
            window.tabs.tabConfig.cbxDistGrid.SetValue(str(int(espacoGrid)) + "cm")
            window.tabs.tabConfig.sldQuality.SetValue(int(Vars.KitLib.getMeshQual()))
            window.OnRefreshAll()
        Vars.ctrlPress = False

    def OnSave(self, window):

        if self.arquivoProjeto == "":
            self.OnSaveAs(window)
        else:
            window.toolbar.EnableTool(wx.ID_UNDO, False)
            window.toolbar.EnableTool(wx.ID_REDO, False)
            self.onSave(self.arquivoProjeto)
            self.atualizaPrecisaSalvar(window,False)
        Vars.ctrlPress = False

    def OnSaveAs(self, window):
        window.toolbar.EnableTool(wx.ID_UNDO, False)
        window.toolbar.EnableTool(wx.ID_REDO, False)
        saveFileDialog = wx.FileDialog(window, "Salvar como...", "", "",
                                       "Projeto KitSim (*.kmp)|*.kmp",
                                       wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        saveFileDialog.ShowModal()
        arquivo = saveFileDialog.GetPath()
        saveFileDialog.Destroy()
        if arquivo != "": # se o diretorio de retorno for vazio, quer dizer que o usuário cancelou a operação
            self.arquivoProjeto = arquivo
            c_s = arquivo.encode("utf-8")
            Vars.KitLib.save(c_s)
            window.atualizaPrecisaSalvar(False)
        Vars.ctrlPress = False

    def onOpen(self, dir):

        c_s = dir.encode("utf-8")
        try:
            Vars.KitLib.open(c_s)
        except:
            msg = wx.MessageDialog(None, "Arquivo Corrompido!", "Erro!", wx.OK)
            msg.ShowModal()
            msg.Destroy()

    def onSave(self, dir):
        try:
            Vars.KitLib.save(dir.encode("utf-8"))
        except:
            msg = wx.MessageDialog(None, "Erro ao Salvar o Arquivo!", "Erro!", wx.OK)
            msg.ShowModal()
            msg.Destroy()