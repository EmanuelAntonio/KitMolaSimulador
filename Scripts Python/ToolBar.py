from VarsAmbient import *
from KeyboardEvent import *


class ToolBar(object):

    @staticmethod
    def CreateToolBar(window):
        """
        Create a toolbar.
        """

        window.toolbar = window.CreateToolBar()
        window.toolbar.SetToolBitmapSize((32, 32))  # sets icon size

        # Use wx.ArtProvider for default icons
        open_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, (32, 32))
        openTool = window.toolbar.AddTool(wx.ID_OPEN, "Abre um Projeto Existente", open_ico, "Abrir")
        window.Bind(wx.EVT_MENU, window.OnOpen, openTool)

        save_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, (32, 32))
        saveTool = window.toolbar.AddTool(wx.ID_SAVE, "Salva o Projeto Corrente", save_ico, "Salvar")
        window.Bind(wx.EVT_MENU, window.OnSave, saveTool)

        saveAs_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_TOOLBAR, (32, 32))
        saveAsTool = window.toolbar.AddTool(wx.ID_SAVEAS, "Salva o Projeto Corrente em um Novo Arquivo", saveAs_ico,
                                          "Salvar Como...")
        window.Bind(wx.EVT_MENU, window.OnSaveAs, saveAsTool)

        window.toolbar.AddSeparator()

        undo_ico = wx.ArtProvider.GetBitmap(wx.ART_UNDO, wx.ART_TOOLBAR, (32, 32))
        window.undoTool = window.toolbar.AddTool(wx.ID_UNDO, "Desfazer", undo_ico, "Desfazer")
        window.toolbar.EnableTool(wx.ID_UNDO, False)
        window.Bind(wx.EVT_TOOL, window.OnUndo, window.undoTool)

        redo_ico = wx.ArtProvider.GetBitmap(wx.ART_REDO, wx.ART_TOOLBAR, (32, 32))
        window.redoTool = window.toolbar.AddTool(wx.ID_REDO, "Refazer", redo_ico, "Refazer")
        window.toolbar.EnableTool(wx.ID_REDO, False)
        window.Bind(wx.EVT_TOOL, window.OnRedo, window.redoTool)

        window.toolbar.AddSeparator()

        imgCopiar = wx.Bitmap('icones/copiar.ico')

        window.copiarSelect = window.toolbar.AddTool(wx.ID_ANY, "Copiar Seleção", imgCopiar, "Copiar Seleção")
        window.Bind(wx.EVT_TOOL, window.OnCopiarSelectToolbar, window.copiarSelect)

        imgMoverObj = wx.Bitmap('icones/moverObj.ico')

        window.copiarSelect = window.toolbar.AddTool(wx.ID_ANY, "Mover Seleção", imgMoverObj, "Mover Seleção")
        window.Bind(wx.EVT_TOOL, window.OnMoverSelectToolbar, window.copiarSelect)

        window.toolbar.AddSeparator()

        imgEsfera = wx.Bitmap('icones/esfera.ico')
        imgBase = wx.Bitmap('icones/base.ico')
        imgBarra9 = wx.Bitmap('icones/barra9.ico')
        imgBarra18 = wx.Bitmap('icones/barra18.ico')
        imgLaje = wx.Bitmap('icones/laje.ico')

        window.addEsfera = window.toolbar.AddTool(wx.ID_ANY, "Adicionar Esfera", imgEsfera, "Esfera")
        window.Bind(wx.EVT_TOOL, window.OnAddEsferaToolbar, window.addEsfera)
        window.addBase = window.toolbar.AddTool(wx.ID_ANY, "Adicionar Base", imgBase, "Base")
        window.Bind(wx.EVT_TOOL, window.OnAddBaseToolbar, window.addBase)
        window.addBarra9 = window.toolbar.AddTool(wx.ID_ANY, "Adicionar Barra de 9cm", imgBarra9, "Barra de 9cm")
        window.Bind(wx.EVT_TOOL, window.OnAddBarra9Toolbar, window.addBarra9)
        window.addBarra18 = window.toolbar.AddTool(wx.ID_ANY, "Adicionar Barra de 18cm", imgBarra18, "Barra de 18cm")
        window.Bind(wx.EVT_TOOL, window.OnAddBarra18Toolbar, window.addBarra18)
        window.addLaje = window.toolbar.AddTool(wx.ID_ANY, "Adicionar Laje", imgLaje, "Laje")
        window.Bind(wx.EVT_TOOL, window.OnAddLajeToolbar, window.addLaje)

        window.toolbar.AddSeparator()

        imgMoveTela = wx.Bitmap('icones/move.ico')

        window.moveTela = window.toolbar.AddTool(wx.ID_ANY, "Mover Tela", imgMoveTela, "Mover Tela")
        window.Bind(wx.EVT_TOOL, window.OnMoveTelaToolbar, window.moveTela)

        window.toolbar.Realize()

    @staticmethod
    def OnMoveSelectToolBar(window):
        window.moveObjetos = True
        window.drawArea0.Refresh(True)
        window.drawArea1.Refresh(True)
        window.drawArea2.Refresh(True)
        window.drawArea3.Refresh(True)

    @staticmethod
    def OnAddLajeToolBar(window):

        myCursor = wx.Cursor(r"icones/lajeCursor.cur",
                             wx.BITMAP_TYPE_CUR)
        window.botaoSelecionado = Vars.LAJE_SELECIONADO
        window.SetCursor(myCursor)

    @staticmethod
    def OnCopiarSelectToolBar(window):
        if Vars.KitLib.duplicaSelect():
            window.moveObjetos = True
            window.atualizaPrecisaSalvar(True)
        window.OnRefreshAll()

    @staticmethod
    def OnMoveTelaToolbar(window):
        myCursor = wx.Cursor(r"icones/cursorMoveTela.cur",
                             wx.BITMAP_TYPE_CUR)

        window.botaoSelecionado = Vars.MOVETELA_SELECIONADO

        window.SetCursor(myCursor)

    @staticmethod
    def OnAddEsferaToolbar(window):

        myCursor = wx.Cursor(r"icones/cursorEsfera.cur",
                             wx.BITMAP_TYPE_CUR)

        window.botaoSelecionado = Vars.SPHERE_SELECIONADO

        window.SetCursor(myCursor)

    @staticmethod
    def OnAddBaseToolbar(window):

        myCursor = wx.Cursor(r"icones/baseCursor.cur",
                             wx.BITMAP_TYPE_CUR)

        window.botaoSelecionado = Vars.BASE_SELECIONADO
        window.SetCursor(myCursor)



    @staticmethod
    def OnAddBarra9Toolbar(window):

        myCursor = wx.Cursor(r"icones/cursorBarra.cur",
                             wx.BITMAP_TYPE_CUR)

        window.botaoSelecionado = Vars.BAR9_SELECIONADO

        window.SetCursor(myCursor)

    @staticmethod
    def OnAddBarra18Toolbar(window):
        myCursor = wx.Cursor(r"icones/cursorBarra.cur",
                             wx.BITMAP_TYPE_CUR)

        window.botaoSelecionado = Vars.BAR18_SELECIONADO

        window.SetCursor(myCursor)