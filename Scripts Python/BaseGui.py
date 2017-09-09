# -*- coding: UTF-8 -*-
from OpenGLCanvas import *
from TabsMenu import *
from ToolBar import *
from KeyboardEvent import *
from SalvarProjeto import *
from SplashScreen import *
from Msg import *
from StatusBar import *

"""
    -> WindowClass:
        Classe para manipulação geral da interface, inclui todos os botões, menus, abas e o frame do OpenGL
"""
class WindowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(WindowClass,self).__init__(*args, **kwargs)

        #Variaveis da classe:
        self.version = "0.8.9"  # Variável de controle de versão
        self.dateModificacao = "26/07/2017"  # Data da última atualização do programa
        self.drawArea0 = None  # Variável que armazena uma referência a área de desenho do OpenGL, usado para corrigir o tamanho da área de desenho após um resize
        self.drawArea1 = None  # Variável que armazena uma referência a área de desenho do OpenGL, usado para corrigir o tamanho da área de desenho após um resize
        self.drawArea2 = None  # Variável que armazena uma referência a área de desenho do OpenGL, usado para corrigir o tamanho da área de desenho após um resize
        self.drawArea3 = None  # Variável que armazena uma referência a área de desenho do OpenGL, usado para corrigir o tamanho da área de desenho após um resize
        self.ultimoDrawSelected = None  # Variável que armazena uma referência para qual drawArea foi interagido por último
        self.botaoSelecionado = -1 # Variavel que armazena a opção selecionada pelo usuário nos botoes auxiliares na toolbar, se nao está nenhum selecionado
        self.moveObjetos = (False,Vars.ASCII_0)  # Variável que armazena se a opção de mover objetos está ativa, na segunda opção qual eixo esta selecionado para movimentacao
        self.rotacionaObjetos = (False,Vars.ASCII_0) # Variável que armazena se a opção de rotacionar objetos está ativa
        self.rotacionaObjetosEixo = -1 # Variável que armazena qual eixo a seleção irá rotacionar, apenas usado quando clica-se em cima da seta de rotação
        self.rotacionaSelectCentro = False
        self.salvar = SalvarProjeto(self)
        self.toolbar = None
        #splash = Splash(self)
        self.base_gui()

    """
        -> Função basic_gui:
            Função que instância todos os objetos da interface, futuramente será quebrado em mais funções auxiliares.
         -> Parâmetros: vazio
        -> Retorno: vazio
    """
    def base_gui(self):

        self.statusSizer = wx.BoxSizer(wx.VERTICAL)
        Msg.statusBar = StatusBar(self)
        self.statusSizer.Add(Msg.statusBar, 0, wx.ALIGN_LEFT | wx.EXPAND, 5)
        Msg.statusBar.SetColor(StatusBar.COLOR_RED)

        self.programIcon = wx.EmptyIcon()
        self.programIcon.CopyFromBitmap(wx.Bitmap(Vars.dirExec + 'icones/icon.ico', wx.BITMAP_TYPE_ANY))
        self.SetIcon(self.programIcon)
        self.sizerToolSide = wx.BoxSizer(wx.VERTICAL)
        self.showToolbarSide = True
        self.showToolbarTop = True

        self.createToolbar()

        if(Vars.thema == "dark"):
            Msg.statusBar.SetBackgroundColour(Vars.corThema)
        Vars.KitLib.init()
        Vars.KitSim.init(Vars.KitLib.getObjList())

        self.strTitle = "KitSim"
        self.strSemTitulo = "Sem Titulo"
        self.SetTitle(self.strTitle + " - " + self.strSemTitulo)

        #definição dos sizers
        self.sizerWindowStatus = wx.BoxSizer(wx.VERTICAL)
        self.sizerWindow = wx.BoxSizer(wx.HORIZONTAL)
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
        menuBar = wx.MenuBar(style=wx.MB_DOCKABLE)
        fileMenu = wx.Menu()
        janelaMenu = wx.Menu()
        aboutMenu = wx.Menu()

        #Criação dos itens dos menus
        openItem = fileMenu.Append(wx.ID_OPEN, 'Abrir...', 'Abrir projeto')
        saveItem = fileMenu.Append(wx.ID_SAVE, 'Salvar', 'Salvar projeto')
        saveAsItem = fileMenu.Append(wx.ID_SAVEAS, 'Salvar como...', 'Salvar como...')
        exitItem = fileMenu.Append(wx.ID_EXIT, 'Sair', 'Fechar Programa')
        helpItem = aboutMenu.Append(wx.ID_ABOUT, 'Ajuda', 'Ajuda')
        versionItem = aboutMenu.Append(wx.ID_DEFAULT, 'Versão', 'Informações sobre a versão')
        themaItemLight = janelaMenu.Append(wx.ID_ANY, 'Padrão', 'Altera o tema da janela padrão.')
        themaItemDark = janelaMenu.Append(wx.ID_ANY, 'Escuro', 'Altera o tema da janela escuro.')

        #Adição dos menus à barra de menus
        menuBar.Append(fileMenu, '&Arquivo')
        menuBar.Append(janelaMenu, '&Tema')
        menuBar.Append(aboutMenu, '&Sobre')

        #Criação da area de desenho
        self.drawArea0 = CanvasBase(self,0)
        self.drawArea1 = CanvasBase(self,1)
        self.drawArea2 = CanvasBase(self,2)
        self.drawArea3 = CanvasBase(self,3)
        self.drawArea0.camera.visionAxis = Vars.ASCII_Z
        self.drawArea0.camera.visionOption = Vars.VISION_Z_ORTHO
        self.drawArea1.camera.visionAxis = Vars.ASCII_X
        self.drawArea1.camera.visionOption = Vars.VISION_X_POS
        self.drawArea3.camera.visionAxis = Vars.ASCII_Y
        self.drawArea3.camera.visionOption = Vars.VISION_Y_POS

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
        self.Bind(wx.EVT_MENU, self.OnChangeToLight, themaItemLight)
        self.Bind(wx.EVT_MENU, self.OnChangeToDark, themaItemDark)
        self.Bind(wx.EVT_MENU, self.OnHelp, helpItem)
        self.Bind(wx.EVT_MENU, self.OnVersion, versionItem)
        self.tabs.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.tabs.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
        self.tabs.Bind(wx.EVT_CHAR_HOOK, self.OnEnterKeyDown)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_SET_FOCUS, self.OnFocus, self)

        Vars.toolBox = self.tabs

        self.sizerToolSide.Add(self.toolbarside,1, wx.EXPAND, 15)
        self.sizerWindow.Add(self.sizerToolSide,0, wx.ALIGN_LEFT | wx.EXPAND,15)
        self.sizerWindow.Add(self.boxMain, 1, wx.ALIGN_RIGHT | wx.EXPAND, 15)

        self.sizerWindowStatus.Add(self.sizerWindow,1, wx.ALIGN_TOP | wx.EXPAND,15)
        self.sizerWindowStatus.Add(self.statusSizer, 0, wx.ALIGN_BOTTOM | wx.EXPAND, 15)

        #Configurações finais

        self.SetMinSize((1024,768))

        self.boxBtn.Layout()
        self.boxMain.Layout()
        self.sizerWindow.Layout()
        self.sizerWindowStatus.Layout()
        self.Maximize(True)
        self.SetSizer(self.sizerWindowStatus)
        self.Show(True)
        self.tabs.SetFocus()

        if Vars.openFile != False:
            self.salvar.onOpen(Vars.openFile)

    def OnFocus(self, e):

        self.tabs.SetFocus()
        e.Skip()

    def createToolbar(self):

        self.toolbar = None
        self.toolbarside = None
        ToolBar.CreateToolBarTopo(self)
        ToolBar.CreateToolBar(self,self.sizerToolSide)

    def OnChangeToLight(self, e):

        if Vars.thema == "light":
            e.Skip()
        else:
            Vars.thema = "light"
            option = Msg.exibirMensagem("Para realizar as alterações é necessário reiniciar o programa, deseja fazer isso agora?",
                                        "Alterar tema",
                                        Msg.tipoYesNo,
                                        Msg.janelaWarning)
            if (option == wx.ID_YES):
                Vars.reset = True
                self.Destroy()

    def OnChangeToDark(self, e):
        if Vars.thema == "dark":
            e.Skip()
        else:
            Vars.thema = "dark"
            option = Msg.exibirMensagem("Para realizar as alterações é necessário reiniciar o programa, deseja fazer isso agora?",
                                        "Alterar tema",
                                        Msg.tipoYesNo,
                                        Msg.janelaWarning)
            if (option == wx.ID_YES):
                Vars.reset = True
                self.Destroy()

    """
        -> Função OnMoverSelectToolbar:
            Função usada ao clicar no botão de mover na toolbar do programa. Altera a variável de movimentação do objetos e atualiza todas as telas
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnMoverSelectToolbar(self,e):

        ToolBar.OnMoveSelectToolBar(self)


    """
        -> Função OnAddLajeToolbar:
            Função usada ao clicar no botão de adicionar laje na toolbar do programa.
            Passa o programa para o estado de esperando a seleção dos objetos necessários
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnAddLajeToolbar(self, e):

        ToolBar.OnAddLajeToolBar(self)

    """
        -> Função OnCopiarSelectToolbar:
            Função usada ao clicar no botão de copiar seleção na toolbar do programa. Chama a função de duplicar seleção no KitLib
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnCopiarSelectToolbar(self,e):

        ToolBar.OnCopiarSelectToolBar(self)

    """
        -> Função OnMoveTelaToolbar:
            Função usada ao clicar no botão de copiar seleção na toolbar do programa.
            Altera a variável de movimentação da tela, passando a função para que o botão esquerdo do mouse ganhe essa função.
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnMoveTelaToolbar(self,e):

        ToolBar.OnMoveTelaToolbar(self)

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

        ToolBar.OnAddEsferaToolbar(self)

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

        ToolBar.OnAddBaseToolbar(self)

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

        ToolBar.OnAddBarra9Toolbar(self)

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

        ToolBar.OnAddBarra18Toolbar(self)

    """
        -> Função OnAddTirante9Toolbar:
            Função usada ao clicar no botão de adicionar tirante de 9x9 na cena.
            Passa o programa para o estado de esperando a seleção dos objetos necessários,
            se o usuário entrar com o botão ENTER confirmará a seleção, caso pressione ESC, cancelará.
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnAddTirante9Toolbar(self,e):

        ToolBar.OnAddTirante9Toolbar(self)


    """
        -> Função OnAddTirante18Toolbar:
            Função usada ao clicar no botão de adicionar tirante de 18x9 na cena.
            Passa o programa para o estado de esperando a seleção dos objetos necessários,
            se o usuário entrar com o botão ENTER confirmará a seleção, caso pressione ESC, cancelará.
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnAddTirante18Toolbar(self,e):

        ToolBar.OnAddTirante18Toolbar(self)


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

        self.salvar.atualizaPrecisaSalvar(self,valor)

    """
        -> Função OnClose:
            Função usada na finalização do programa para saber se o usuário está tentando deixar o programa sem salvar
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnClose(self, e):
        if Msg.timer != None:
            Msg.timer.cancel()
            del Msg.timer
        if self.salvar.precisaSalvar:
            option = Msg.exibirMensagem("Deseja sair do programa sem salvar?", "Fechar Programa", Msg.tipoYesNo, Msg.janelaWarning)
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
            self.moveObjetos = (True,Vars.ASCII_0)
            Msg.exibirStatusBar("Selecione um eixo de mivimentação precionando x, y ou z", 10)
            if self.rotacionaObjetos:
                self.rotacionaObjetos = (False,Vars.ASCII_0)
            self.atualizaPrecisaSalvar(True)
        self.OnRefreshAll()
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

        """ver = wx.MessageDialog(None, "Versão: " + self.version + "\nData de modificação: " + self.dateModificacao, "Versão",  wx.OK)
        ver.ShowModal()
        ver.Destroy()"""
        ver = wx.adv.AboutDialogInfo()

        ver.SetIcon(wx.Icon(Vars.dirExec + 'icones\logoKitSim.png', wx.BITMAP_TYPE_PNG))
        ver.SetName('KitSim')
        ver.SetVersion(self.version + " " + self.dateModificacao)
        #ver.SetDescription(description)
        #ver.SetCopyright('(C) 2007 - 2014 Jan Bodnar')
        #ver.SetWebSite('http://www.zetcode.com')
        #ver.SetLicence(licence)
        ver.AddDeveloper('Adriele Valle\nEmanuel Antônio Parreiras')
        #ver.AddDocWriter('Jan Bodnar')
        #ver.AddArtist('The Tango crew')
        #ver.AddTranslator('Jan Bodnar')
        wx.adv.AboutBox(ver)



    """
        -> Função onOpen:
            Utilizada no menu Arquivo, na barra de menus. Essa função serve para abrir um projeto já existente
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnOpen(self, e):

        self.salvar.OnOpen(self)


    """
        -> Função onSave:
            Utilizada no menu Arquivo, na barra de menus. Essa função serve para salvar um projeto ja previamente salvo ou aberto
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnSave(self, e):

        self.salvar.OnSave(self)

    """
        -> Função onSaveAs:
            Utilizada no menu Arquivo, na barra de menus. Essa função serve para salvar o projeto em um arquivo
        -> Parâmetros:
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de saida
        -> Retorno: vazio
    """
    def OnSaveAs(self, e):

        self.salvar.OnSaveAs(self)

    """
        -> Função OnKeyDown:
            Função para monitorar as teclas que são precionadas sob a drawArea na execução do programa
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de key_down
        -> Retorno: vazio
    """
    def OnKeyDown(self, e):

        KeyboardEvent.OnKeyDown(e,self)

    """
        -> Função OnKeyUp:
            Função para monitorar as teclas que são soltas sob a drawArea na execução do programa
            -> 'e' : instância de evento, pode ou não ser usado para o tratamento do evento de key_down
        -> Retorno: vazio
    """
    def OnKeyUp(self, e):

        KeyboardEvent.OnKeyUp(e)

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
               self.toolbar.EnableTool(wx.ID_REDO, True)
            else:
                self.toolbar.EnableTool(wx.ID_REDO, False)
            if(Vars.KitLib.desfazerSize() == 0):
                self.toolbar.EnableTool(wx.ID_UNDO, False)
        else:
            self.toolbar.EnableTool(wx.ID_UNDO, False)
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
                self.toolbar.EnableTool(wx.ID_UNDO, True)
            else:
                self.toolbar.EnableTool(wx.ID_UNDO, False)
            if(Vars.KitLib.refazerSize() == 0):
                self.toolbar.EnableTool(wx.ID_REDO, False)

        else:
            self.toolbar.EnableTool(wx.ID_REDO, False)

        self.OnRefreshAll()

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
        KeyboardEvent.OnEnterKeyDown(e, self)

    def OnRefreshAll(self):
        self.drawArea0.Refresh()
        self.drawArea1.Refresh()
        self.drawArea2.Refresh()
        self.drawArea3.Refresh()

