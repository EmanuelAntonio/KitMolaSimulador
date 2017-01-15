# -*- coding: UTF-8 -*-
from OpenGLCanvas import *
from VarsAmbient import *

"""
    -> WindowClass:
        Classe para manipulação geral da interface, inclui todos os botões, menus, abas e o frame do OpenGL
"""
class WindowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(WindowClass,self).__init__(*args, **kwargs)

        self.basic_gui()

    """
        -> Função basic_gui:
            Função que instância todos os objetos da interface, futuramente será quebrado em mais funções auxiliares.
         -> Parâmetros: vazio
        -> Retorno: vazio
    """
    def basic_gui(self):


        self.CreateStatusBar()
        Vars.status = self.GetStatusBar()
        self.SetTitle("Simulador KitMola")

        #definição dos sizers
        boxMain = wx.BoxSizer(wx.HORIZONTAL)
        box = wx.BoxSizer(wx.HORIZONTAL)
        boxBtn = wx.BoxSizer(wx.VERTICAL)

        #Criação da area das tabs
        notebook = Tabs(self)
        cam = CamOp(self)
        boxBtn.Add(notebook, 1, wx.ALIGN_TOP | wx.EXPAND, 10)
        boxBtn.Add(cam,1,wx.ALIGN_BOTTOM | wx.EXPAND,10)

        #Definição dos menus
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        editMenu = wx.Menu()
        aboutMenu = wx.Menu()

        #Criação dos itens dos menus
        openItem = fileMenu.Append(wx.ID_OPEN, 'Abrir...', 'Abrir projeto')
        saveItem = fileMenu.Append(wx.ID_SAVE, 'Salvar', 'Salvar projeto')
        saveAsItem = fileMenu.Append(wx.ID_SAVEAS, 'Salvar como...', 'Salvar como...')
        exitItem = fileMenu.Append(wx.ID_EXIT, 'Sair', 'Fechar Programa')

        editItem = editMenu.Append(wx.ID_EDIT, 'Editar', 'Editar')
        copyItem = editMenu.Append(wx.ID_COPY, 'Copiar', 'Copiar')
        pasteItem = editMenu.Append(wx.ID_PASTE, 'Colar', 'Colar')

        helpItem = aboutMenu.Append(wx.ID_ABOUT, 'Ajuda', 'Ajuda')

        #Criação do label de visao(ao lado esquerdo)
        versionItem = aboutMenu.Append(wx.ID_DEFAULT, 'Versão', 'Informações sobre a versão')
        visionItem = wx.StaticText(self,0,Vars.visionModes[0], pos=(10,10), style=wx.ALIGN_CENTER)
        visionItem.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        visionItem.SetBackgroundColour((128,128,128))
        visionItem.SetForegroundColour((255,255,255))
        Vars.visionItem = visionItem

        #Adição dos menus à barra de menus
        menuBar.Append(fileMenu, '&Arquivo')
        menuBar.Append(editMenu, '&Editar')
        menuBar.Append(aboutMenu, '&Sobre')

        #Criação da area de desenho
        c = CubeCanvas(self)
        Vars.drawArea = c
        box.Add(c,0, wx.ALIGN_CENTRE | wx.EXPAND, 15)

        #Junção dos sizers das tabs com o sizer principal
        boxMain.Add(box, 1, wx.ALIGN_LEFT | wx.EXPAND,0)
        boxMain.Add(boxBtn,1, wx.ALIGN_RIGHT | wx.EXPAND, 0)

        #Setar as funções de controle dos menus
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_SIZE, self.onSize, self)
        self.Bind(wx.EVT_MENU, self.onQuit, exitItem)
        self.Bind(wx.EVT_MENU, self.onOpen, openItem)
        self.Bind(wx.EVT_MENU, self.onSave, saveItem)
        self.Bind(wx.EVT_MENU, self.onSaveAs, saveAsItem)
        self.Bind(wx.EVT_MENU, self.onEdit, editItem)
        self.Bind(wx.EVT_MENU, self.onHelp, helpItem)
        self.Bind(wx.EVT_MENU, self.version, versionItem)

        #Configurações finais
        self.Maximize(True)
        self.SetSizer(boxMain)
        self.SetAutoLayout(True)
        self.Layout()
        self.Show()


    """
        ->Função onSize:
            Função que trata o evento de RESIZE da janela.
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio

    """
    def onSize(self,e):

        tamJanela = self.GetSize()
        resize = tamJanela
        resize[0] = resize[0]*Vars.drawSize
        Vars.drawArea.SetMinSize(resize)
        self.Layout()


    """
        -> Função onQuit:
            Função utilizada na barra de menus para terminar a execução do programa em python.
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio

    """
    def onQuit(self, e):

        self.Close()


    """
        ->Função onEdit:
            Função utilizada para testes, será substituida em versões futuras
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def onEdit(self, e):

        edit = wx.MessageDialog(None,"Edit", "Edit", wx.OK)
        edit.ShowModal()
        edit.Destroy()


    """
        ->Função onHelp:
            Função utilizada para testes, será substituida em versões futuras
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio

    """
    def onHelp(self,e):

        help = wx.MessageDialog(None, "Help", "Ajuda?", wx.OK)
        yesNo = help.ShowModal()
        help.Destroy()
        if yesNo == wx.ID_YES:
            helpYes = wx.MessageDialog(None, "Você disse sim!", "Help", wx.OK)
            helpYes.ShowModal()
            helpYes.Destroy()
        else:
            helpNo = wx.MessageDialog(None, "Você disse não!", "Help", wx.OK)
            helpNo.ShowModal()
            helpNo.Destroy()

    """
        -> Função version:
            Utilizada no menu Sobre, na barra de menus. Essa função serve para exibir uma caixa de dialogo com a versão do programa
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def version(self,e):

        ver = wx.MessageDialog(None, "Versão: " + Vars.version + "\nData de modificação: " + Vars.dateModificacao, "Versão",  wx.OK)
        ver.ShowModal()
        ver.Destroy()


    """
        -> Função onOpen:
            Utilizada no menu Arquivo, na barra de menus. Essa função serve para abrir um projeto já existente
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def onOpen(self, e):
        openFileDialog = wx.FileDialog(self, "Abrir...", "", "",
                                       "Projeto KitMola (*.kmp)|*.kmp",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()
        arquivo = openFileDialog.GetPath()
        openFileDialog.Destroy()
        if arquivo != "":
            Vars.arquivoProjeto = arquivo
            c_s = arquivo.encode("utf-8")
            Vars.KitLib.open(c_s)
            Vars.drawArea.Refresh()


    """
        -> Função onSave:
            Utilizada no menu Arquivo, na barra de menus. Essa função serve para salvar um projeto ja previamente salvo ou aberto
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def onSave(self, e):

        if Vars.arquivoProjeto == "":
            self.onSaveAs(e)
        else:
            Vars.KitLib.save(Vars.arquivoProjeto.encode("utf-8"))


    """
        -> Função onSaveAs:
            Utilizada no menu Arquivo, na barra de menus. Essa função serve para salvar o projeto em um arquivo
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def onSaveAs(self, e):
        saveFileDialog = wx.FileDialog(self, "Salvar como...", "", "",
                                       "Projeto KitMola (*.kmp)|*.kmp",
                                       wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        saveFileDialog.ShowModal()
        arquivo = saveFileDialog.GetPath()
        saveFileDialog.Destroy()
        if arquivo != "": # se o diretorio de retorno for vazio, quer dizer que o usuário cancelou a operação
            Vars.arquivoProjeto = arquivo
            c_s = arquivo.encode("utf-8")
            Vars.KitLib.save(c_s)


#########################################################################################################################################################################################
"""
    -> Classe Tabs:
        Classe responsável pela manipulação de todas as instâncias das abas laterais do programa

"""
class Tabs(wx.Notebook):
    """
    Notebook class
    """

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=
        #wx.BK_DEFAULT
                             # wx.BK_TOP
                             # wx.BK_BOTTOM
                              wx.BK_LEFT
                             # wx.BK_RIGHT
                             )

        # Create the first tab and add it to the notebook
        tabOne = TabPanel(self)
        #tabOne.SetBackgroundColour("Gray")
        self.AddPage(tabOne, "Objetos")
        imL = wx.ImageList(32,32)

        # Create and add the second tab
        tabTwo = TabPanel(self)
        self.AddPage(tabTwo, "Ferramentas")

        # Create and add the third tab
        self.AddPage(TabPanel(self), "Configurações")

        # Adiciona os icones nas tabs
        imgObj = imL.Add(wx.Bitmap('icones/obj.ico'))
        imgTool = imL.Add(wx.Bitmap('icones/tool.ico'))
        imgConfig = imL.Add(wx.Bitmap('icones/config.ico'))
        self.AssignImageList(imL)
        self.SetPageImage(0, imgObj)
        self.SetPageImage(1, imgTool)
        self.SetPageImage(2, imgConfig)

        #self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        #self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)


"""
    ->Classe TabPanel:
        Classe utilizada para instânciar uma das abas, será substituida futuramente por classes específicas para cada aba.

"""
class TabPanel(wx.Panel):
    """
    This will be the first notebook tab
    """

    # ----------------------------------------------------------------------
    def __init__(self, parent):


        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        sizer = wx.BoxSizer(wx.VERTICAL)
        txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
        txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")

        #sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(txtOne, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(txtTwo, 0, wx.ALIGN_CENTER, 5)

        self.SetSizer(sizer)



"""
    -> Classe CamOp:
        Classe responsável pela manipulação de troca dos tipos de visão

"""

class CamOp(wx.Notebook):
    """
    Notebook class
    """

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=
        #wx.BK_DEFAULT
                             # wx.BK_TOP
                             # wx.BK_BOTTOM
                              wx.BK_LEFT
                             # wx.BK_RIGHT
                             )

        # Create the first tab and add it to the notebook
        tabOne = CamPanel(self)
        #tabOne.SetBackgroundColour("Gray")
        self.AddPage(tabOne, "Câmera")
        imL = wx.ImageList(32,32)
        # Adiciona os icones nas tabs
        imgObj = imL.Add(wx.Bitmap('icones/cam.ico'))
        self.AssignImageList(imL)
        self.SetPageImage(0, imgObj)


"""
    ->Classe CamPanel:
        Classe utilizada para instânciar os objetos da aba camera do menu principal.

"""
class CamPanel(wx.Panel):


    # ----------------------------------------------------------------------
    def __init__(self, parent):


        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        sizer = wx.BoxSizer(wx.VERTICAL)

        btnPerspectiva = wx.Button(self,wx.ID_ANY,"Perspectiva")
        btnTop = wx.Button(self, wx.ID_ANY, "Cima")
        btnFront = wx.Button(self, wx.ID_ANY, "Frente")
        btnBack = wx.Button(self, wx.ID_ANY, "Atrás")
        btnRight = wx.Button(self, wx.ID_ANY, "Direita")
        btnLeft = wx.Button(self, wx.ID_ANY, "Esquerda")


        sizer.Add(btnPerspectiva, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        sizer.Add(btnTop, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        sizer.Add(btnFront, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        sizer.Add(btnBack, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        sizer.Add(btnRight, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        sizer.Add(btnLeft, 0, wx.ALIGN_CENTER | wx.EXPAND, 5)

        self.Bind(wx.EVT_BUTTON, self.OnPerspectiva, btnPerspectiva)
        self.Bind(wx.EVT_BUTTON, self.OnTop, btnTop)
        self.Bind(wx.EVT_BUTTON, self.OnFront, btnFront)
        self.Bind(wx.EVT_BUTTON, self.OnBack, btnBack)
        self.Bind(wx.EVT_BUTTON, self.OnRight, btnRight)
        self.Bind(wx.EVT_BUTTON, self.OnLeft, btnLeft)


        self.SetSizer(sizer)

    """
        -> Função OnPerspectiva:
            Função para alternar o modo de visão para perspectiva com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnPerspectiva(self, evt):
        Vars.KitLib.setVisionOption(0)
        Vars.visionItem.SetLabelText(Vars.visionModes[0])
        Vars.KitLib.setVisionAxis(122)#122 Codigo ASCII para 'z'
        Vars.drawArea.Refresh()
    """
        -> Função OnTop:
            Função para alternar o modo de visão para ortogonal de cima com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnTop(self, evt):
        Vars.KitLib.setVisionOption(5)
        Vars.visionItem.SetLabelText(Vars.visionModes[5])
        Vars.KitLib.setVisionAxis(122)#122 Codigo ASCII para 'z'
        Vars.drawArea.Refresh()
    """
        -> Função OnFront:
            Função para alternar o modo de visão para ortogonal em x positivo com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnFront(self, evt):
        Vars.KitLib.setVisionOption(1)
        Vars.visionItem.SetLabelText(Vars.visionModes[1])
        Vars.KitLib.setVisionAxis(120)#120 Codigo ASCII para 'x'
        Vars.drawArea.Refresh()
    """
        -> Função OnBack:
            Função para alternar o modo de visão para ortogonal em x negativo com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnBack(self, evt):
        Vars.KitLib.setVisionOption(2)
        Vars.visionItem.SetLabelText(Vars.visionModes[2])
        Vars.KitLib.setVisionAxis(120)#120 Codigo ASCII para 'x'
        Vars.drawArea.Refresh()
    """
        -> Função OnRight:
            Função para alternar o modo de visão para ortogonal em y positivo com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnRight(self, evt):
        Vars.KitLib.setVisionOption(3)
        Vars.visionItem.SetLabelText(Vars.visionModes[3])
        Vars.KitLib.setVisionAxis(121)#121 Codigo ASCII para 'y'
        Vars.drawArea.Refresh()
    """
        -> Função OnLeft:
            Função para alternar o modo de visão para ortogonal em y negativo com o botao direito do mouse
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnLeft(self, evt):
        Vars.KitLib.setVisionOption(4)
        Vars.visionItem.SetLabelText(Vars.visionModes[4])
        Vars.KitLib.setVisionAxis(121)#121 Codigo ASCII para 'y'
        Vars.drawArea.Refresh()