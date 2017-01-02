from OpenGLObjects import *

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
        self.SetStatusText('Hello World!')


        boxMain = wx.BoxSizer(wx.HORIZONTAL)
        box = wx.BoxSizer(wx.HORIZONTAL)
        boxBtn = wx.BoxSizer(wx.HORIZONTAL)

        notebook = Tabs(self)
        boxBtn.Add(notebook, 1, wx.ALIGN_CENTRE | wx.EXPAND, 10)

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        editMenu = wx.Menu()
        aboutMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.ID_EXIT, 'Sair', 'Fechar Programa')
        editItem = editMenu.Append(wx.ID_EDIT, 'Editar', 'Editar')
        copyItem = editMenu.Append(wx.ID_COPY, 'Copiar', 'Copiar')
        pasteItem = editMenu.Append(wx.ID_PASTE, 'Colar', 'Colar')
        helpItem = aboutMenu.Append(wx.ID_ABOUT, 'Ajuda', 'Ajuda')
        versionItem = aboutMenu.Append(wx.ID_DEFAULT, 'Versão', 'Informações sobre a versão')

        menuBar.Append(fileMenu, '&Arquivo')
        menuBar.Append(editMenu, '&Editar')
        menuBar.Append(aboutMenu, '&Sobre')

        c = CubeCanvas(self)
        c.SetMinSize((1280, 720))
        box.Add(c, 0, wx.ALIGN_CENTER | wx.EXPAND, 15)

        boxMain.Add(box, 0, wx.ALIGN_LEFT | wx.EXPAND,15)
        boxMain.Add(boxBtn,1, wx.ALIGN_RIGHT | wx.EXPAND, 15)

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.onQuit, exitItem)
        self.Bind(wx.EVT_MENU, self.onEdit, editItem)
        self.Bind(wx.EVT_MENU, self.onHelp, helpItem)
        self.Bind(wx.EVT_MENU, self.version, versionItem)

        self.SetSizer(boxMain)
        self.SetTitle("Janela de Teste")
        self.Centre()
        #self.SetAutoLayout(True)
        self.Layout()
        self.Show()


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

        ver = wx.MessageDialog(None, "Versão: " + version + "\nData de modificação: " + dateModificacao, "Versão",  wx.OK)
        ver.ShowModal()
        ver.Destroy()


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
        self.AddPage(tabOne, "TabOne")

        # Create and add the second tab
        tabTwo = TabPanel(self)
        self.AddPage(tabTwo, "TabTwo")

        # Create and add the third tab
        self.AddPage(TabPanel(self), "TabThree")

        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)

    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        #print('OnPageChanged,  old:%d, new:%d, sel:%d\n' % (old, new, sel))
        event.Skip()

    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        #print('OnPageChanging, old:%d, new:%d, sel:%d\n' % (old, new, sel))
        event.Skip()


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
        """"""

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        #sizer = wx.BoxSizer(wx.VERTICAL)
        txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
        txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(txtOne, 0, wx.ALL, 5)
        sizer.Add(txtTwo, 0, wx.ALL, 5)

        self.SetSizer(sizer)
