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

        self.base_gui()

    """
        -> Função basic_gui:
            Função que instância todos os objetos da interface, futuramente será quebrado em mais funções auxiliares.
         -> Parâmetros: vazio
        -> Retorno: vazio
    """
    def base_gui(self):

        self.CreateStatusBar()

        self.createToolbar()

        Vars.status = self.GetStatusBar()
        self.SetTitle("Simulador KitMola")

        #definição dos sizers
        boxMain = wx.BoxSizer(wx.HORIZONTAL)
        box = wx.BoxSizer(wx.VERTICAL)
        boxBtn = wx.BoxSizer(wx.VERTICAL)

        #Criação da area das tabs
        self.tabs = Tabs(self)

        self.cam = CamOp(self)
        boxBtn.Add(self.tabs, 1, wx.ALIGN_TOP | wx.EXPAND, 1)
        boxBtn.Add(self.cam,0,wx.ALIGN_BOTTOM | wx.EXPAND, 1)

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
        boxMain.Add(boxBtn,0, wx.ALIGN_RIGHT | wx.EXPAND, 0)

        #adicionar atalhos de teclado

        #CTRL+Z desfazer
        undoId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnUndo, id=undoId)

        #CTRL+SHIFT+Z refazer
        redoId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnRedo, id=redoId)

        #CTRL+S salvar
        saveId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onSave, id=saveId)

        #CTRL+O abrir
        openId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onOpen, id=openId)

        #CTRL+A selecionar tudo
        selectId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnSelectAll, id=selectId)

        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('Z'), undoId),
                                         (wx.ACCEL_CTRL | wx.ACCEL_SHIFT, ord('Z'), redoId),
                                         (wx.ACCEL_CTRL, ord('S'), saveId),
                                         (wx.ACCEL_CTRL, ord('O'), openId),
                                         (wx.ACCEL_CTRL, ord('A'), selectId)
                                        ])
        self.SetAcceleratorTable(accel_tbl)

        self.SetAcceleratorTable(accel_tbl)
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
        self.cam.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.cam.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        self.tabs.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.tabs.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        Vars.toolBox = self.tabs

        #Configurações finais
        self.Maximize(True)
        self.SetSizer(boxMain)
        #self.SetAutoLayout(True)
        self.Layout()
        self.Show()

    def createToolbar(self):
        """
        Create a toolbar.
        """

        self.toolbar = self.CreateToolBar()
        Vars.toolBar = self.toolbar
        self.toolbar.SetToolBitmapSize((16, 16))  # sets icon size

        # Use wx.ArtProvider for default icons
        open_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, (16, 16))
        openTool = self.toolbar.AddTool(wx.ID_OPEN, "Abre um Projeto Existente", open_ico,"Abrir")
        self.Bind(wx.EVT_MENU, self.onOpen, openTool)

        save_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, (16, 16))
        saveTool = self.toolbar.AddTool(wx.ID_SAVE, "Salva o Projeto Corrente", save_ico,"Salvar")
        self.Bind(wx.EVT_MENU, self.onSave, saveTool)

        saveAs_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_TOOLBAR, (16, 16))
        saveAsTool = self.toolbar.AddTool(wx.ID_SAVEAS, "Salva o Projeto Corrente em um Novo Arquivo", saveAs_ico,"Salvar Como...")
        self.Bind(wx.EVT_MENU, self.onSaveAs, saveAsTool)

        self.toolbar.AddSeparator()

        undo_ico = wx.ArtProvider.GetBitmap(wx.ART_UNDO, wx.ART_TOOLBAR, (16, 16))
        self.undoTool = self.toolbar.AddTool(wx.ID_UNDO, "Desfazer", undo_ico,"Desfazer")
        self.toolbar.EnableTool(wx.ID_UNDO, False)
        self.Bind(wx.EVT_TOOL, self.OnUndo, self.undoTool)

        redo_ico = wx.ArtProvider.GetBitmap(wx.ART_REDO, wx.ART_TOOLBAR, (16, 16))
        self.redoTool = self.toolbar.AddTool(wx.ID_REDO, "Refazer", redo_ico,"Refazer")
        self.toolbar.EnableTool(wx.ID_REDO, False)
        self.Bind(wx.EVT_TOOL, self.OnRedo, self.redoTool)

        # This basically shows the toolbar
        self.toolbar.Realize()

    """
        -> Função OnSelectAll:
            Função para selecionar todos os objetos da cena
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnSelectAll(self,e):
        Vars.KitLib.selectAll()
        Vars.drawArea.Refresh()

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

        hlp = "Comandos básicos:\n" \
              "     ->Clique e arraste do mouse para movimentar a câmera;\n" \
              "     ->Rolar o botão domeio do mouse ajusta o zoom;\n" \
              "     ->Botão direito do mouse abre um menu com varias opções de manipulação objetos e ajustes de câmera;\n" \
              "     ->Clique com o botão do meio do mouse para selecionar um objeto e segure shift para selecionar vários;\n" \
              "     ->A toolbox à esquerda contêm várias opções de objetos, câmeras e configurações\n"
        help = wx.MessageDialog(None, hlp, "Ajuda", wx.OK)
        help.ShowModal()
        help.Destroy()

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
        self.toolbar.EnableTool(wx.ID_UNDO, False)
        self.toolbar.EnableTool(wx.ID_REDO, False)
        openFileDialog = wx.FileDialog(self, "Abrir...", "", "",
                                       "Projeto KitMola (*.kmp)|*.kmp",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()
        arquivo = openFileDialog.GetPath()
        openFileDialog.Destroy()
        if arquivo != "":
            Vars.arquivoProjeto = arquivo
            c_s = arquivo.encode("utf-8")
            try:
                Vars.KitLib.open(c_s)
            except:
                msg = wx.MessageDialog(None, "Arquivo Corrompido!", "Erro!", wx.OK)
                msg.ShowModal()
                msg.Destroy()
            Vars.drawArea.Refresh()

        Vars.ctrlPress = False


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
            self.toolbar.EnableTool(wx.ID_UNDO, False)
            self.toolbar.EnableTool(wx.ID_REDO, False)
            try:
                Vars.KitLib.save(Vars.arquivoProjeto.encode("utf-8"))
            except:
                msg = wx.MessageDialog(None, "Erro ao Salvar o Arquivo!", "Erro!", wx.OK)
                msg.ShowModal()
                msg.Destroy()
        Vars.ctrlPress = False

    """
        -> Função onSaveAs:
            Utilizada no menu Arquivo, na barra de menus. Essa função serve para salvar o projeto em um arquivo
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def onSaveAs(self, e):
        self.toolbar.EnableTool(wx.ID_UNDO, False)
        self.toolbar.EnableTool(wx.ID_REDO, False)
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
        Vars.ctrlPress = False

    """
        -> Função OnKeyDown:
            Função para monitorar as teclas que são precionadas sob a drawArea na execução do programa
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de key_down
        -> Retorno: vazio
    """
    def OnKeyDown(self, e):

        if(e.GetKeyCode() == wx.WXK_SHIFT):
            Vars.shiftPress = True
        elif(e.GetKeyCode() == wx.WXK_DELETE):
            Vars.KitLib.removeAll()
            Vars.drawArea.Refresh()
        elif(e.GetKeyCode() == wx.WXK_CONTROL):
            Vars.ctrlPress = True
            Vars.centroAux = Vars.centro
        e.Skip()

    """
        -> Função OnKeyUp:
            Função para monitorar as teclas que são soltas sob a drawArea na execução do programa
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de key_down
        -> Retorno: vazio
    """
    def OnKeyUp(self, e):

        if(e.GetKeyCode() == wx.WXK_SHIFT):
            Vars.shiftPress = False
        elif(e.GetKeyCode() == wx.WXK_CONTROL):
            Vars.ctrlPress = False
        e.Skip()

    """
        -> Função OnUndo:
            Função para desfazer uma ação feita pelo usuário
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de key_down
        -> Retorno: vazio
    """
    def OnUndo(self, e):

        if(Vars.KitLib.desfazerSize() > 0):
            Vars.KitLib.desfazer()
            if (Vars.KitLib.refazerSize() > 0):
                Vars.toolBar.EnableTool(wx.ID_REDO, True)
            else:
                Vars.toolBar.EnableTool(wx.ID_REDO, False)
            if(Vars.KitLib.desfazerSize() == 0):
                Vars.toolBar.EnableTool(wx.ID_UNDO, False)
        else:
            Vars.toolBar.EnableTool(wx.ID_UNDO, False)
        Vars.drawArea.Refresh()

    """
        -> Função OnRedo:
            Função para refazer uma ação feita pelo usuário
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de key_down
        -> Retorno: vazio
    """
    def OnRedo(self, e):

        if(Vars.KitLib.refazerSize() > 0):
            Vars.KitLib.refazer()
            if (Vars.KitLib.desfazerSize() > 0):
                Vars.toolBar.EnableTool(wx.ID_UNDO, True)
            else:
                Vars.toolBar.EnableTool(wx.ID_UNDO, False)
            if(Vars.KitLib.refazerSize() == 0):
                Vars.toolBar.EnableTool(wx.ID_REDO, False)

        else:
            Vars.toolBar.EnableTool(wx.ID_REDO, False)

        Vars.drawArea.Refresh()
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
        self.tabOne = TabPanel(self)
        #tabOne.SetBackgroundColour("Gray")
        self.AddPage(self.tabOne, "Objetos")
        imL = wx.ImageList(32,32)

        # Create and add the second tab
        self.tabTwo = TabPanel(self)
        self.AddPage(self.tabTwo, "Ferramentas")

        # Create and add the third tab
        self.tabThree = TabConfig(self)
        self.AddPage(self.tabThree, "Configurações")

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

#########################################################################################################################################################################################
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

        sizer.Add(txtOne, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(txtTwo, 0, wx.ALIGN_CENTER, 5)

        self.SetSizer(sizer)


################################################################################################################################################################################################
"""
    ->Classe TabConfig:
        Classe utilizada para instânciar a aba configurações no menu Principal.

"""
class TabConfig(wx.Panel):

    # ----------------------------------------------------------------------
    def __init__(self, parent):


        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        sizer = wx.BoxSizer(wx.VERTICAL)
        lblTamGrid = wx.StaticText(self,wx.ID_ANY,"Tamanho do grid: ")
        lblTamGrid.SetExtraStyle(wx.TE_CENTRE)
        self.txtTamGrid = wx.TextCtrl(self, wx.ID_ANY, str(Vars.KitLib.getTamGrid()),style=wx.TE_PROCESS_ENTER)
        self.txtTamGrid.Bind(wx.EVT_KEY_DOWN, self.OnEnter)
        btnTamGrid = wx.Button(self,wx.ID_ANY,"Ok")

        sizerX = wx.BoxSizer(wx.HORIZONTAL)
        sizerY = wx.BoxSizer(wx.HORIZONTAL)
        sizerZ = wx.BoxSizer(wx.HORIZONTAL)
        lblFocus = wx.StaticText(self, wx.ID_ANY, "Foco da Câmera: ")
        lblFocus.SetExtraStyle(wx.TE_CENTRE)
        lblX = wx.StaticText(self, wx.ID_ANY, "X: ")
        lblX.SetExtraStyle(wx.TE_RIGHT)
        lblY = wx.StaticText(self, wx.ID_ANY, "Y: ")
        lblY.SetExtraStyle(wx.TE_RIGHT)
        lblZ = wx.StaticText(self, wx.ID_ANY, "Z: ")
        lblZ.SetExtraStyle(wx.TE_RIGHT)
        self.txtFocusX = wx.TextCtrl(self, wx.ID_ANY, str(Vars.centro[0]), style=wx.TE_PROCESS_ENTER)
        self.txtFocusX.Bind(wx.EVT_KEY_DOWN, self.OnEnterFocusX)
        self.txtFocusY = wx.TextCtrl(self, wx.ID_ANY, str(Vars.centro[1]), style=wx.TE_PROCESS_ENTER)
        self.txtFocusY.Bind(wx.EVT_KEY_DOWN, self.OnEnterFocusY)
        self.txtFocusZ = wx.TextCtrl(self, wx.ID_ANY, str(Vars.centro[2]), style=wx.TE_PROCESS_ENTER)
        self.txtFocusZ.Bind(wx.EVT_KEY_DOWN, self.OnEnterFocusZ)
        lblCmX = wx.StaticText(self, wx.ID_ANY, "cm")
        lblCmX.SetExtraStyle(wx.TE_RIGHT)
        lblCmY = wx.StaticText(self, wx.ID_ANY, "cm")
        lblCmY.SetExtraStyle(wx.TE_RIGHT)
        lblCmZ = wx.StaticText(self, wx.ID_ANY, "cm")
        lblCmZ.SetExtraStyle(wx.TE_RIGHT)
        self.btnFocus = wx.Button(self,wx.ID_ANY,"Mudar Foco")

        sizerX.Add(lblX, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER, 5 )
        sizerX.Add(self.txtFocusX, 0, wx.ALIGN_RIGHT, 5)
        sizerX.Add(lblCmX,0,wx.ALIGN_RIGHT | wx.ALIGN_CENTER, 5 )
        sizerY.Add(lblY, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER, 5 )
        sizerY.Add(self.txtFocusY, 0, wx.ALIGN_RIGHT, 5)
        sizerY.Add(lblCmY, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER, 5)
        sizerZ.Add(lblZ, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER, 5 )
        sizerZ.Add(self.txtFocusZ, 0, wx.ALIGN_RIGHT, 5)
        sizerZ.Add(lblCmZ, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER, 5)

        sizer.Add(lblTamGrid, 0, wx.ALIGN_CENTER,5)
        sizer.Add(self.txtTamGrid, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(btnTamGrid, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)
        sizer.Add(lblFocus, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(sizerX,0,wx.ALIGN_CENTER,5)
        sizer.Add(sizerY,0,wx.ALIGN_CENTER,5)
        sizer.Add(sizerZ,0,wx.ALIGN_CENTER,5)
        sizer.Add(self.btnFocus, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL), 0, wx.ALIGN_CENTER | wx.EXPAND, 5)

        self.Bind(wx.EVT_BUTTON, self.OnTamGrid,btnTamGrid)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnTamGrid,self.txtTamGrid)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnEnterFocus, self.txtFocusX)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnEnterFocus, self.txtFocusY)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnEnterFocus, self.txtFocusZ)
        self.Bind(wx.EVT_BUTTON, self.OnEnterFocus, self.btnFocus)

        self.SetSizer(sizer)

    """
        -> Função OnTamGrid:
            Função para alternar o tamanho do grid a ser exibido na cena
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnTamGrid(self, e):

        if int(self.txtTamGrid.GetValue())%2 == 0:
            Vars.KitLib.setTamGrid(c_int(int(self.txtTamGrid.GetValue())))
        else:
            Vars.KitLib.setTamGrid(c_int(int(self.txtTamGrid.GetValue())+1))
            self.txtTamGrid.SetValue(str(int(self.txtTamGrid.GetValue())+1))
        self.Parent.SetFocus()
        Vars.drawArea.Refresh()
    """
        -> Função OnEnter:
            Função para tratar o pressionamento da tecla enter sob o txtTamGrid
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnEnter(self,e):

        keycode = e.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER or keycode == wx.WXK_TAB:
            self.OnTamGrid(e)
            e.EventObject.Navigate()
        e.Skip()

    def OnEnterFocusX(self, e):

        keycode = e.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER or keycode == wx.WXK_TAB:

            e.EventObject.Navigate()
        e.Skip()

    def OnEnterFocusY(self, e):

        keycode = e.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER or keycode == wx.WXK_TAB:
            e.EventObject.Navigate()
        e.Skip()

    def OnEnterFocusZ(self, e):

        keycode = e.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER or keycode == wx.WXK_TAB:
            e.EventObject.Navigate()
        e.Skip()

    def OnEnterFocus(self, e):
        try:
            Vars.centro = (float(self.txtFocusX.GetValue()), float(self.txtFocusY.GetValue()), float(self.txtFocusZ.GetValue()))
        except:
            ex = wx.MessageDialog(None, "Caracter Inválido! \nTente usar ponto ao invés de virgula.", "Erro!", wx.OK)
            ex.ShowModal()
        self.Parent.SetFocus()
        Vars.drawArea.Refresh()


################################################################################################################################################################################################
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


################################################################################################################################################################################################

"""
    ->Classe CamPanel:
        Classe utilizada para instânciar os objetos da aba camera do menu principal.

"""
class CamPanel(wx.Panel):


    # ----------------------------------------------------------------------
    def __init__(self, parent):


        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        sizer = wx.BoxSizer(wx.VERTICAL)

        btnPerspectiva = wx.Button(self, wx.ID_ANY,"Perspectiva")
        btnTop = wx.Button(self, wx.ID_ANY, "Cima")
        btnFront = wx.Button(self, wx.ID_ANY, "Frente")
        btnBack = wx.Button(self, wx.ID_ANY, "Atrás")
        btnRight = wx.Button(self, wx.ID_ANY, "Direita")
        btnLeft = wx.Button(self, wx.ID_ANY, "Esquerda")

        Vars.visionButtons = (btnPerspectiva,btnTop,btnFront,btnBack,btnRight,btnLeft)

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
        self.Parent.SetFocus()
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
        self.Parent.SetFocus()
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
        self.Parent.SetFocus()
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
        self.Parent.SetFocus()
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
        self.Parent.SetFocus()
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
        self.Parent.SetFocus()
        Vars.drawArea.Refresh()