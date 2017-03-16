# -*- coding: UTF-8 -*-
from OpenGLCanvas import *
from TabsMenu import *

"""
    -> WindowClass:
        Classe para manipulação geral da interface, inclui todos os botões, menus, abas e o frame do OpenGL
"""
class WindowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(WindowClass,self).__init__(*args, **kwargs)

        #Variaveis da classe:
        self.version = "0.7.5"  # Variável de controle de versão
        self.dateModificacao = "16/03/2017"  # Data da última atualização do programa
        self.arquivoProjeto = ""  # Variável que armazena o diretorio com o nome do projeto que está aberto atualmente
        self.precisaSalvar = True # Variável que armazena se houve alteração no projeto após o último salvamento
        self.drawArea0 = None  # Variável que armazena uma referência a área de desenho do OpenGL, usado para corrigir o tamanho da área de desenho após um resize
        self.drawArea1 = None  # Variável que armazena uma referência a área de desenho do OpenGL, usado para corrigir o tamanho da área de desenho após um resize
        self.drawArea2 = None  # Variável que armazena uma referência a área de desenho do OpenGL, usado para corrigir o tamanho da área de desenho após um resize
        self.drawArea3 = None  # Variável que armazena uma referência a área de desenho do OpenGL, usado para corrigir o tamanho da área de desenho após um resize
        self.ultimoDrawSelected = None  # Variável que armazena uma referência para qual drawArea foi interagido por último
        self.botaoSelecionado = -1 # Variavel que armazena a opção selecionada pelo usuário nos botoes auxiliares na toolbar, se nao está nenhum selecionado
        self.moveObjetos = False  # Variável que armazena se a opção de mover objetos está ativa
        self.moveObjetosEixo = -1  # Variável que armazena qual eixo a seleção irá se mover, apenas usado quando clica-se em cima da seta de movimento

        self.base_gui()

    """
        -> Função basic_gui:
            Função que instância todos os objetos da interface, futuramente será quebrado em mais funções auxiliares.
         -> Parâmetros: vazio
        -> Retorno: vazio
    """
    def base_gui(self):

        self.programIcon = wx.EmptyIcon()
        self.programIcon.CopyFromBitmap(wx.Bitmap('icones/icon.ico', wx.BITMAP_TYPE_ANY))
        self.SetIcon(self.programIcon)
        self.createToolbar()
        Vars.KitLib.init()

        Vars.status = self.GetStatusBar()
        self.strTitle = "KitSim"
        self.strSemTitulo = "Sem Titulo"
        self.SetTitle(self.strTitle + " - " + self.strSemTitulo)

        #definição dos sizers
        self.boxMain = wx.BoxSizer(wx.HORIZONTAL)
        box = wx.BoxSizer(wx.VERTICAL)
        self.boxBtn = wx.BoxSizer(wx.VERTICAL)
        Vars.boxUp = wx.BoxSizer(wx.HORIZONTAL)
        Vars.boxDown = wx.BoxSizer(wx.HORIZONTAL)

        #Criação da area das tabs
        self.tabs = Tabs(self)
        self.showTabs = True
        self.boxBtn.Add(self.tabs, 1, wx.ALIGN_TOP | wx.EXPAND, 1)

        #Definição dos menus
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        aboutMenu = wx.Menu()

        #Criação dos itens dos menus
        openItem = fileMenu.Append(wx.ID_OPEN, 'Abrir...', 'Abrir projeto')
        saveItem = fileMenu.Append(wx.ID_SAVE, 'Salvar', 'Salvar projeto')
        saveAsItem = fileMenu.Append(wx.ID_SAVEAS, 'Salvar como...', 'Salvar como...')
        exitItem = fileMenu.Append(wx.ID_EXIT, 'Sair', 'Fechar Programa')
        helpItem = aboutMenu.Append(wx.ID_ABOUT, 'Ajuda', 'Ajuda')
        versionItem = aboutMenu.Append(wx.ID_DEFAULT, 'Versão', 'Informações sobre a versão')

        """
        #Criação do label de visao(ao lado esquerdo)
        visionItem = wx.StaticText(self,0,Vars.visionModes[0], pos=(10,10), style=wx.ALIGN_CENTER)
        visionItem.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        visionItem.SetBackgroundColour((128,128,128))
        visionItem.SetForegroundColour((255,255,255))
        Vars.visionItem = visionItem"""

        #Adição dos menus à barra de menus
        menuBar.Append(fileMenu, '&Arquivo')
        menuBar.Append(aboutMenu, '&Sobre')

        #Criação da area de desenho
        self.drawArea0 = CanvasBase(self,0)
        self.drawArea1 = CanvasBase(self,1)
        self.drawArea2 = CanvasBase(self,2)
        self.drawArea3 = CanvasBase(self,3)
        self.drawArea0.visionAxis = Vars.ASCII_Z
        self.drawArea0.visionOption = Vars.VISION_Z_ORTHO
        self.drawArea1.visionAxis = Vars.ASCII_X
        self.drawArea1.visionOption = Vars.VISION_X_POS
        self.drawArea3.visionAxis = Vars.ASCII_Y
        self.drawArea3.visionOption = Vars.VISION_Y_POS

        Vars.lineUp = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        Vars.lineDown = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        Vars.lineBox = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_HORIZONTAL)
        Vars.boxUp.Add(self.drawArea0,1,wx.ALIGN_LEFT | wx.EXPAND, 15)
        Vars.boxUp.Add(Vars.lineUp, 0, wx.ALIGN_CENTRE | wx.EXPAND, 5)
        Vars.boxUp.Add(self.drawArea1, 1, wx.ALIGN_RIGHT | wx.EXPAND, 15)
        Vars.boxDown.Add(self.drawArea2, 1, wx.ALIGN_LEFT | wx.EXPAND, 15)
        Vars.boxDown.Add(Vars.lineDown, 0, wx.ALIGN_CENTRE | wx.EXPAND, 5)
        Vars.boxDown.Add(self.drawArea3, 1, wx.ALIGN_RIGHT | wx.EXPAND, 15)
        box.Add(Vars.boxUp,1, wx.ALIGN_RIGHT | wx.EXPAND, 15)
        box.Add(Vars.lineBox, 0, wx.ALIGN_CENTRE | wx.EXPAND, 5)
        box.Add(Vars.boxDown, 1, wx.ALIGN_RIGHT | wx.EXPAND, 15)

        Vars.boxDraw = box

        #Junção dos sizers das tabs com o sizer principal
        self.boxMain.Add(box, 1, wx.ALIGN_RIGHT | wx.EXPAND,15)
        self.boxMain.Add(self.boxBtn,0, wx.ALIGN_LEFT | wx.EXPAND, 15)

        #adicionar atalhos de teclado

        #CTRL+Z desfazer
        undoId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnUndo, id = undoId)

        #CTRL+SHIFT+Z refazer
        redoId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnRedo, id = redoId)

        #CTRL+S salvar
        saveId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnSave, id = saveId)

        #CTRL+O abrir
        openId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnOpen, id = openId)

        #CTRL+A selecionar tudo
        selectId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnSelectAll, id = selectId)

        #SHIFT+D duplica objetos selecionados
        duplicaId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnDuplica, id = duplicaId)

        #SHIFT + = zoom out
        zoomOutId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnZoomOut, id = zoomOutId)

        #CTRL + Q fecha o programa
        quitId = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnQuit, id = quitId)


        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('Z'), undoId),
                                         (wx.ACCEL_CTRL | wx.ACCEL_SHIFT, ord('Z'), redoId),
                                         (wx.ACCEL_CTRL, ord('S'), saveId),
                                         (wx.ACCEL_CTRL, ord('O'), openId),
                                         (wx.ACCEL_CTRL, ord('A'), selectId),
                                         (wx.ACCEL_SHIFT, ord('D'), duplicaId),
                                         (wx.ACCEL_SHIFT, ord('='), zoomOutId),
                                         (wx.ACCEL_CTRL, ord('Q'), quitId)

                                        ])
        self.SetAcceleratorTable(accel_tbl)

        self.SetAcceleratorTable(accel_tbl)
        #Setar as funções de controle dos menus
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_SIZE, self.OnSize, self)
        self.Bind(wx.EVT_MENU, self.OnQuit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnOpen, openItem)
        self.Bind(wx.EVT_MENU, self.OnSave, saveItem)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, saveAsItem)
        self.Bind(wx.EVT_MENU, self.OnHelp, helpItem)
        self.Bind(wx.EVT_MENU, self.OnVersion, versionItem)
        self.tabs.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.tabs.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        self.tabs.Bind(wx.EVT_CHAR_HOOK, self.OnEnterKeyDown)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        Vars.toolBox = self.tabs
        Vars.toolBar = self.toolbar

        #Configurações finais
        self.Maximize(True)
        self.SetSizer(self.boxMain)
        self.Show()

    def createToolbar(self):
        """
        Create a toolbar.
        """

        self.toolbar = self.CreateToolBar()
        self.toolbar.SetToolBitmapSize((32, 32))  # sets icon size

        # Use wx.ArtProvider for default icons
        open_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, (32, 32))
        openTool = self.toolbar.AddTool(wx.ID_OPEN, "Abre um Projeto Existente", open_ico,"Abrir")
        self.Bind(wx.EVT_MENU, self.OnOpen, openTool)

        save_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, (32, 32))
        saveTool = self.toolbar.AddTool(wx.ID_SAVE, "Salva o Projeto Corrente", save_ico,"Salvar")
        self.Bind(wx.EVT_MENU, self.OnSave, saveTool)

        saveAs_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_TOOLBAR, (32, 32))
        saveAsTool = self.toolbar.AddTool(wx.ID_SAVEAS, "Salva o Projeto Corrente em um Novo Arquivo", saveAs_ico,"Salvar Como...")
        self.Bind(wx.EVT_MENU, self.OnSaveAs, saveAsTool)

        self.toolbar.AddSeparator()

        undo_ico = wx.ArtProvider.GetBitmap(wx.ART_UNDO, wx.ART_TOOLBAR, (32, 32))
        self.undoTool = self.toolbar.AddTool(wx.ID_UNDO, "Desfazer", undo_ico,"Desfazer")
        self.toolbar.EnableTool(wx.ID_UNDO, False)
        self.Bind(wx.EVT_TOOL, self.OnUndo, self.undoTool)

        redo_ico = wx.ArtProvider.GetBitmap(wx.ART_REDO, wx.ART_TOOLBAR, (32, 32))
        self.redoTool = self.toolbar.AddTool(wx.ID_REDO, "Refazer", redo_ico,"Refazer")
        self.toolbar.EnableTool(wx.ID_REDO, False)
        self.Bind(wx.EVT_TOOL, self.OnRedo, self.redoTool)

        self.toolbar.AddSeparator()

        imgCopiar = wx.Bitmap('icones/copiar.ico')

        self.copiarSelect = self.toolbar.AddTool(wx.ID_ANY, "Copiar Seleção", imgCopiar, "Copiar Seleção")
        self.Bind(wx.EVT_TOOL, self.OnCopiarSelectToolbar, self.copiarSelect)


        imgMoverObj = wx.Bitmap('icones/moverObj.ico')

        self.copiarSelect = self.toolbar.AddTool(wx.ID_ANY, "Mover Seleção", imgMoverObj, "Mover Seleção")
        self.Bind(wx.EVT_TOOL, self.OnMoverSelectToolbar, self.copiarSelect)

        self.toolbar.AddSeparator()

        imgEsfera = wx.Bitmap('icones/esfera.ico')
        imgBase = wx.Bitmap('icones/base.ico')
        imgBarra9 = wx.Bitmap('icones/barra9.ico')
        imgBarra18 = wx.Bitmap('icones/barra18.ico')
        imgLaje = wx.Bitmap('icones/laje.ico')

        self.addEsfera = self.toolbar.AddTool(wx.ID_ANY, "Adicionar Esfera", imgEsfera, "Esfera")
        self.Bind(wx.EVT_TOOL, self.OnAddEsferaToolbar, self.addEsfera)
        self.addBase = self.toolbar.AddTool(wx.ID_ANY, "Adicionar Base", imgBase, "Base")
        self.Bind(wx.EVT_TOOL, self.OnAddBaseToolbar, self.addBase)
        self.addBarra9 = self.toolbar.AddTool(wx.ID_ANY, "Adicionar Barra de 9cm", imgBarra9, "Barra de 9cm")
        self.Bind(wx.EVT_TOOL, self.OnAddBarra9Toolbar, self.addBarra9)
        self.addBarra18 = self.toolbar.AddTool(wx.ID_ANY, "Adicionar Barra de 18cm", imgBarra18, "Barra de 18cm")
        self.Bind(wx.EVT_TOOL, self.OnAddBarra18Toolbar, self.addBarra18)
        self.addLaje = self.toolbar.AddTool(wx.ID_ANY, "Adicionar Laje", imgLaje, "Laje")
        self.Bind(wx.EVT_TOOL, self.OnAddLajeToolbar, self.addLaje)

        self.toolbar.AddSeparator()

        imgMoveTela = wx.Bitmap('icones/move.ico')

        self.moveTela = self.toolbar.AddTool(wx.ID_ANY, "Mover Tela", imgMoveTela, "Mover Tela")
        self.Bind(wx.EVT_TOOL, self.OnMoveTelaToolbar, self.moveTela)

        self.toolbar.Realize()


    """
        -> Função OnMoverSelectToolbar:
            Função usada ao clicar no botão de mover na toolbar do programa. Altera a variável de movimentação do objetos e atualiza todas as telas
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnMoverSelectToolbar(self,e):

        self.moveObjetos = True
        self.drawArea0.Refresh(True)
        self.drawArea1.Refresh(True)
        self.drawArea2.Refresh(True)
        self.drawArea3.Refresh(True)


    """
        -> Função OnAddLajeToolbar:
            Função usada ao clicar no botão de adicionar laje na toolbar do programa.
            Passa o programa para o estado de esperando a seleção dos objetos necessários
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnAddLajeToolbar(self, e):
        myCursor = wx.Cursor(r"icones/lajeCursor.cur",
                             wx.BITMAP_TYPE_CUR)

        self.botaoSelecionado = Vars.LAJE_SELECIONADO

        self.SetCursor(myCursor)

    """
        -> Função OnCopiarSelectToolbar:
            Função usada ao clicar no botão de copiar seleção na toolbar do programa. Chama a função de duplicar seleção no KitLib
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnCopiarSelectToolbar(self,e):
        if Vars.KitLib.duplicaSelect():
            self.moveObjetos = True
            self.atualizaPrecisaSalvar(True)
        self.drawArea0.Refresh()
        self.drawArea1.Refresh()
        self.drawArea2.Refresh()
        self.drawArea3.Refresh()

    """
        -> Função OnMoveTelaToolbar:
            Função usada ao clicar no botão de copiar seleção na toolbar do programa.
            Altera a variável de movimentação da tela, passando a função para que o botão esquerdo do mouse ganhe essa função.
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnMoveTelaToolbar(self,e):
        myCursor = wx.Cursor(r"icones/cursorMoveTela.cur",
                             wx.BITMAP_TYPE_CUR)

        self.botaoSelecionado = Vars.MOVETELA_SELECIONADO

        self.SetCursor(myCursor)

    """
        -> Função OnAddEsferaToolbar:
            Função usada ao clicar no botão de adicionar esferas na toolbar do programa.
            Altera o estado do programa(variável desta classe) para que o botão esquerdo do mouse ganhe a função de adicionar varias
            esferas até que o botão ENTER ou ESC seja precionado.
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnAddEsferaToolbar(self,e):

        myCursor = wx.Cursor(r"icones/cursorEsfera.cur",
                             wx.BITMAP_TYPE_CUR)

        self.botaoSelecionado = Vars.SPHERE_SELECIONADO

        self.SetCursor(myCursor)

    """
        -> Função OnAddEsferaToolbar:
            Função usada ao clicar no botão de adicionar bases na toolbar do programa.
            Altera o estado do programa(variável desta classe) para que o botão esquerdo do mouse ganhe a função de adicionar varias bases
            até que o botão ENTER ou ESC seja precionado.
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnAddBaseToolbar(self,e):

        myCursor = wx.Cursor(r"icones/baseCursor.cur",
                             wx.BITMAP_TYPE_CUR)

        self.botaoSelecionado = Vars.BASE_SELECIONADO

        self.SetCursor(myCursor)

    """
        -> Função OnAddBarra9Toolbar:
            Função usada ao clicar no botão de adicionar barra de 9cm na toolbar do programa.
            Passa o programa para o estado de esperando a seleção dos objetos necessários,
            se o usuário entrar com o botão ENTER confirmará a seleção, caso pressione ESC, cancelará.
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnAddBarra9Toolbar(self,e):

        myCursor = wx.Cursor(r"icones/cursorBarra.cur",
                             wx.BITMAP_TYPE_CUR)

        self.botaoSelecionado = Vars.BAR9_SELECIONADO

        self.SetCursor(myCursor)


    """
        -> Função OnAddBarra9Toolbar:
            Função usada ao clicar no botão de adicionar barra de 18cm na toolbar do programa.
            Passa o programa para o estado de esperando a seleção dos objetos necessários,
            se o usuário entrar com o botão ENTER confirmará a seleção, caso pressione ESC, cancelará.
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnAddBarra18Toolbar(self,e):
        myCursor = wx.Cursor(r"icones/cursorBarra.cur",
                             wx.BITMAP_TYPE_CUR)

        self.botaoSelecionado = Vars.BAR18_SELECIONADO

        self.SetCursor(myCursor)

    """
        -> Função atualizaPrecisaSalvar:
            Função usada quando houver uma modificação no projeto, logo, esta função atualiza o título da janela com o asterisco,
            ou simplesmente atualiza o título da janela para adicinar o nome do projeto que acabou de ser salvo removendo o asterisco.
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
            -> 'valor': booleano se simboliza se é necessário salvar, utilizado para distinguir qual vai ser o novo título da janela.
        -> Retorno: vazio
    """
    def atualizaPrecisaSalvar(self, valor):

        if valor:
            if self.arquivoProjeto != "":
                self.precisaSalvar = True
                self.SetTitle(self.strTitle + " - *[" + self.arquivoProjeto + "]")
            else:
                self.precisaSalvar = True
                self.SetTitle(self.strTitle + " - *[" + self.strSemTitulo + "]")
        else:
            if self.arquivoProjeto != "":
                self.precisaSalvar = False
                self.SetTitle(self.strTitle + " - [" + self.arquivoProjeto + "]")
            else:
                self.precisaSalvar = False
                self.SetTitle(self.strTitle + " - [" + self.strSemTitulo + "]")

    """
        -> Função OnClose:
            Função usada na finalização do programa para saber se o usuário está tentando deixar o programa sem salvar
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnClose(self, e):
        if self.precisaSalvar:
            msg = wx.MessageDialog(None, "Deseja sair do programa sem salvar?", "Fechar Programa", wx.YES_NO | wx.ICON_WARNING)
            option = msg.ShowModal()
            msg.Destroy()
            if(option == wx.ID_YES):
                self.Destroy()
        else:
            self.Destroy()


    """
        -> Função OnQuit:
            Função chamada para terminar a execução do programa
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnQuit(self, e):

        self.Close()

    """
        -> Função OnDuplica:
            Função para duplicar objetos selecionados na cena, utiliza a função do KitLib para realizar a tarefa de duplicar,
            após isso, se houve a duplicação, simplesmente atualiza todas as janelas.
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnDuplica(self, e):
        if Vars.KitLib.duplicaSelect():
            self.moveObjetos = True
            self.atualizaPrecisaSalvar(True)
        self.drawArea0.Refresh()
        self.drawArea1.Refresh()
        self.drawArea2.Refresh()
        self.drawArea3.Refresh()
    """
        -> Função OnSelectAll:
            Função para selecionar todos os objetos da cena. Utiliza a função do KitLib para fazer isso.
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnSelectAll(self,e):
        Vars.KitLib.selectAll()
        self.tabs.tabInfo.alteraCentroMBR()
        self.drawArea0.Refresh()
        self.drawArea1.Refresh()
        self.drawArea2.Refresh()
        self.drawArea3.Refresh()

    """
        ->Função OnSize:
            Função que trata o evento de RESIZE da janela.
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio

    """
    def OnSize(self,e):

        tamJanela = self.GetSize()
        #resize = tamJanela
        #resize[0] = resize[0]*Vars.drawSize
        #Vars.drawArea.SetMinSize(resize)
        self.Layout()


    """
        -> Função onQuit:
            Função utilizada na barra de menus para terminar a execução do programa em python.
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio

    """
    def OnQuit(self, e):

        self.Close()

    """
        ->Função onHelp:
            Função utilizada para testes, será substituida em versões futuras
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio

    """
    def OnHelp(self,e):

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
        -> Função OnVersion:
            Utilizada no menu Sobre, na barra de menus. Essa função serve para exibir uma caixa de dialogo com a versão do programa
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnVersion(self,e):

        ver = wx.MessageDialog(None, "Versão: " + self.version + "\nData de modificação: " + self.dateModificacao, "Versão",  wx.OK)
        ver.ShowModal()
        ver.Destroy()


    """
        -> Função onOpen:
            Utilizada no menu Arquivo, na barra de menus. Essa função serve para abrir um projeto já existente
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnOpen(self, e):
        self.toolbar.EnableTool(wx.ID_UNDO, False)
        self.toolbar.EnableTool(wx.ID_REDO, False)
        openFileDialog = wx.FileDialog(self, "Abrir...", "", "",
                                       "Projeto KitMola (*.kmp)|*.kmp",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()
        arquivo = openFileDialog.GetPath()
        openFileDialog.Destroy()
        if arquivo != "":
            self.arquivoProjeto = arquivo
            self.SetTitle(self.strTitle + " - [" + self.arquivoProjeto + "]")
            c_s = arquivo.encode("utf-8")
            try:
                Vars.KitLib.open(c_s)
            except:
                msg = wx.MessageDialog(None, "Arquivo Corrompido!", "Erro!", wx.OK)
                msg.ShowModal()
                msg.Destroy()
            self.tabs.tabConfig.txtTamGrid.SetValue(str(Vars.KitLib.getTamGrid()))
            espacoGrid = c_float(Vars.KitLib.getEspacoGrid()).value
            self.tabs.tabConfig.cbxDistGrid.SetValue(str(int(espacoGrid)) + "cm")
            self.tabs.tabConfig.sldQuality.SetValue(int(Vars.KitLib.getMeshQual()))
            self.drawArea0.Refresh()
            self.drawArea1.Refresh()
            self.drawArea2.Refresh()
            self.drawArea3.Refresh()


        Vars.ctrlPress = False


    """
        -> Função onSave:
            Utilizada no menu Arquivo, na barra de menus. Essa função serve para salvar um projeto ja previamente salvo ou aberto
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnSave(self, e):

        if self.arquivoProjeto == "":
            self.OnSaveAs(e)
        else:
            self.toolbar.EnableTool(wx.ID_UNDO, False)
            self.toolbar.EnableTool(wx.ID_REDO, False)
            try:
                Vars.KitLib.save(self.arquivoProjeto.encode("utf-8"))
            except:
                msg = wx.MessageDialog(None, "Erro ao Salvar o Arquivo!", "Erro!", wx.OK)
                msg.ShowModal()
                msg.Destroy()
            self.atualizaPrecisaSalvar(False)
        Vars.ctrlPress = False

    """
        -> Função onSaveAs:
            Utilizada no menu Arquivo, na barra de menus. Essa função serve para salvar o projeto em um arquivo
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnSaveAs(self, e):
        self.toolbar.EnableTool(wx.ID_UNDO, False)
        self.toolbar.EnableTool(wx.ID_REDO, False)
        saveFileDialog = wx.FileDialog(self, "Salvar como...", "", "",
                                       "Projeto KitMola (*.kmp)|*.kmp",
                                       wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        saveFileDialog.ShowModal()
        arquivo = saveFileDialog.GetPath()
        saveFileDialog.Destroy()
        if arquivo != "": # se o diretorio de retorno for vazio, quer dizer que o usuário cancelou a operação
            self.arquivoProjeto = arquivo
            c_s = arquivo.encode("utf-8")
            Vars.KitLib.save(c_s)
            self.atualizaPrecisaSalvar(False)
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
            if Vars.KitLib.desfazerSize() > 0:
                self.toolbar.EnableTool(wx.ID_UNDO, True)
            if Vars.KitLib.refazerSize() > 0:
                self.toolbar.EnableTool(wx.ID_REDO, True)
            self.drawArea0.Refresh()
            self.drawArea1.Refresh()
            self.drawArea2.Refresh()
            self.drawArea3.Refresh()

        elif(e.GetKeyCode() == wx.WXK_CONTROL):

            Vars.ctrlPress = True

        elif(e.GetKeyCode() == Vars.W_PRESS and self.moveObjetos):

            delta = 0.1
            if self.tabs.tabConfig.blockInsert[0]:
                delta = self.tabs.tabConfig.blockInsert[1]
            if(self.ultimoDrawSelected.visionOption == 5):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(delta), c_float(0.0))
            elif(self.ultimoDrawSelected.visionOption != 0):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(delta))

            self.atualizaPrecisaSalvar(True)

        elif (e.GetKeyCode() == Vars.S_PRESS and self.moveObjetos):

            delta = 0.1
            if self.tabs.tabConfig.blockInsert[0]:
                delta = self.tabs.tabConfig.blockInsert[1]
            if (self.ultimoDrawSelected.visionOption == 5):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(-delta), c_float(0.0))
            elif(self.ultimoDrawSelected.visionOption != 0):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(0.0), c_float(-delta))
            self.atualizaPrecisaSalvar(True)

        elif (e.GetKeyCode() == Vars.A_PRESS and self.moveObjetos):
            delta = 0.1
            if self.tabs.tabConfig.blockInsert[0]:
                delta = self.tabs.tabConfig.blockInsert[1]
            if (self.ultimoDrawSelected.visionOption == 5):
                Vars.KitLib.moveSelect(c_float(-delta), c_float(0.0), c_float(0.0))
            elif(self.ultimoDrawSelected.visionOption == 1):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(-delta), c_float(0.0))
            elif(self.ultimoDrawSelected.visionOption == 2):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(delta), c_float(0.0))
            elif(self.ultimoDrawSelected.visionOption == 3):
                Vars.KitLib.moveSelect(c_float(delta), c_float(0.0), c_float(0.0))
            elif(self.ultimoDrawSelected.visionOption == 4):
                Vars.KitLib.moveSelect(c_float(-delta), c_float(0.0), c_float(0.0))

            self.atualizaPrecisaSalvar(True)

        elif (e.GetKeyCode() == Vars.D_PRESS and self.moveObjetos):
            delta = 0.1
            if self.tabs.tabConfig.blockInsert[0]:
                delta = self.tabs.tabConfig.blockInsert[1]
            if (self.ultimoDrawSelected.visionOption == 5):
                Vars.KitLib.moveSelect(c_float(delta), c_float(0.0), c_float(0.0))
            elif(self.ultimoDrawSelected.visionOption == 1):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(delta), c_float(0.0))
            elif(self.ultimoDrawSelected.visionOption == 2):
                Vars.KitLib.moveSelect(c_float(0.0), c_float(-delta), c_float(0.0))
            elif(self.ultimoDrawSelected.visionOption == 3):
                Vars.KitLib.moveSelect(c_float(-delta), c_float(0.0), c_float(0.0))
            elif(self.ultimoDrawSelected.visionOption == 4):
                Vars.KitLib.moveSelect(c_float(0.1), c_float(0.0), c_float(0.0))
            self.atualizaPrecisaSalvar(True)

        elif (e.GetKeyCode() == Vars.G_PRESS ):
            self.moveObjetos = not(self.moveObjetos)
            #self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))

        elif (e.GetKeyCode() == Vars.Z_PRESS ):
            Vars.KitLib.setWireframe(not(Vars.KitLib.getWireframe()))
        elif (e.GetKeyCode() == Vars.NUM_0_PRESS or e.GetKeyCode() == Vars.N_0_PRESS):
            if self.ultimoDrawSelected != None:
                self.ultimoDrawSelected.visionOption = Vars.VISION_Z_PERSP
                self.ultimoDrawSelected.visionAxis = Vars.ASCII_Z  # 122 Codigo ASCII para 'z'
                #Vars.visionItem.SetLabelText(Vars.visionModes[0])
                self.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.NUM_1_PRESS or e.GetKeyCode() == Vars.N_1_PRESS):
            if self.ultimoDrawSelected != None:
                self.ultimoDrawSelected.visionOption = Vars.VISION_Z_ORTHO
                self.ultimoDrawSelected.visionAxis = Vars.ASCII_Z  # 122 Codigo ASCII para 'z'
                #Vars.visionItem.SetLabelText(Vars.visionModes[5])
                self.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.NUM_2_PRESS or e.GetKeyCode() == Vars.N_2_PRESS):
            if self.ultimoDrawSelected != None:
                self.ultimoDrawSelected.visionOption = Vars.VISION_X_POS
                self.ultimoDrawSelected.visionAxis = Vars.ASCII_X  # 122 Codigo ASCII para 'z'
                #Vars.visionItem.SetLabelText(Vars.visionModes[1])
                self.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.NUM_3_PRESS or e.GetKeyCode() == Vars.N_3_PRESS):
            if self.ultimoDrawSelected != None:
                self.ultimoDrawSelected.visionOption = Vars.VISION_X_NEG
                self.ultimoDrawSelected.visionAxis = Vars.ASCII_X  # 122 Codigo ASCII para 'z'
                #Vars.visionItem.SetLabelText(Vars.visionModes[2])
                self.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.NUM_4_PRESS or e.GetKeyCode() == Vars.N_4_PRESS):
            if self.ultimoDrawSelected != None:
                self.ultimoDrawSelected.visionOption = Vars.VISION_Y_POS
                self.ultimoDrawSelected.visionAxis = Vars.ASCII_Y  # 122 Codigo ASCII para 'z'
                #self.visionItem.SetLabelText(Vars.visionModes[3])
                self.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.NUM_5_PRESS or e.GetKeyCode() == Vars.N_5_PRESS):
            if self.ultimoDrawSelected != None:
                self.ultimoDrawSelected.visionOption = Vars.VISION_Y_NEG
                self.ultimoDrawSelected.visionAxis = Vars.ASCII_Y  # 122 Codigo ASCII para 'z'
                #self.visionItem.SetLabelText(Vars.visionModes[4])
                self.ultimoDrawSelected.Refresh()
        elif (e.GetKeyCode() == Vars.ESC_PRESS):
            Vars.KitLib.deSelectAll()
        elif (e.GetKeyCode() == Vars.T_PRESS):
            if self.showTabs:
                self.showTabs = False
                self.tabs.Hide()
                self.boxMain.Layout()
                self.tabs.SetFocus()
            else:
                self.showTabs = True
                self.tabs.Show(True)
                self.boxMain.Layout()
                self.tabs.SetFocus()
        elif (e.GetKeyCode() == e.GetKeyCode() == Vars.NUM_PLUS):
            self.ultimoDrawSelected.OnZoomOut()
        elif (e.GetKeyCode() == e.GetKeyCode() == Vars.NUM_LESS or e.GetKeyCode() == e.GetKeyCode() == Vars.LESS_PRESS):
            self.ultimoDrawSelected.OnZoomIn()
        else:
            print(e.GetKeyCode())

        self.drawArea0.Refresh()
        self.drawArea1.Refresh()
        self.drawArea2.Refresh()
        self.drawArea3.Refresh()

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
        self.drawArea0.Refresh()
        self.drawArea1.Refresh()
        self.drawArea2.Refresh()
        self.drawArea3.Refresh()

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

        self.drawArea0.Refresh()
        self.drawArea1.Refresh()
        self.drawArea2.Refresh()
        self.drawArea3.Refresh()

    """
        -> Função OnZoomOut:
            Função para dar um zoom out na ultima janela do OpenGL selecionada.
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de key_down
        -> Retorno: vazio
    """
    def OnZoomOut(self, e):
        if(self.ultimoDrawSelected != None):
            self.ultimoDrawSelected.OnZoomOut()

    """
        -> Função OnEnterKeyDown:
            Função para tratar o envento de quando o usuário pressionar a tecla Enter
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de key_down
        -> Retorno: vazio
    """
    def OnEnterKeyDown(self, e):

        if e.GetKeyCode() == Vars.ENTER_PRESS:
            if self.botaoSelecionado != Vars.LIVRE_SELECIONADO:
                self.botaoSelecionado = Vars.LIVRE_SELECIONADO
                self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        else:# Se  caso não for pressionado a tecla enter, o else libera o evento para que possa ser usado no wx.EVT_KEY_DOWN
            e.Skip()
