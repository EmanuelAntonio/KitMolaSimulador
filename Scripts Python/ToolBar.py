from VarsAmbient import *
from KeyboardEvent import *


class ToolBar(object):

    @staticmethod
    def CreateToolBar(window, sizer):

        window.toolbarside = wx.ToolBar(window,style=wx.TB_LEFT)

        imgEsfera = wx.Bitmap(Vars.dirExec + 'icones/esfera.ico')
        imgBase = wx.Bitmap(Vars.dirExec + 'icones/base.ico')
        imgLaje = wx.Bitmap(Vars.dirExec + 'icones/laje.ico')
        if (Vars.thema == "dark"):
            window.toolbarside.SetBackgroundColour(Vars.corThema)
            imgBarra9 = wx.Bitmap(Vars.dirExec + 'icones/barra9dark.ico')
            imgBarra18 = wx.Bitmap(Vars.dirExec + 'icones/barra18dark.ico')
            imgTirante9 = wx.Bitmap(Vars.dirExec + 'icones/tirante9dark.ico')
            imgTirante18 = wx.Bitmap(Vars.dirExec + 'icones/tirante18dark.ico')

        else:
            imgBarra9 = wx.Bitmap(Vars.dirExec + 'icones/barra9.ico')
            imgBarra18 = wx.Bitmap(Vars.dirExec + 'icones/barra18.ico')
            imgTirante9 = wx.Bitmap(Vars.dirExec + 'icones/tirante9.ico')
            imgTirante18 = wx.Bitmap(Vars.dirExec + 'icones/tirante18.ico')

        window.addEsfera = window.toolbarside.AddTool(wx.ID_ANY, "Adicionar Esfera", imgEsfera, "Esfera")
        window.Bind(wx.EVT_TOOL, window.OnAddEsferaToolbar, window.addEsfera)
        window.addBase = window.toolbarside.AddTool(wx.ID_ANY, "Adicionar Base", imgBase, "Base")
        window.Bind(wx.EVT_TOOL, window.OnAddBaseToolbar, window.addBase)
        window.addBarra9 = window.toolbarside.AddTool(wx.ID_ANY, "Adicionar Barra de 9cm", imgBarra9, "Barra de 9cm")
        window.Bind(wx.EVT_TOOL, window.OnAddBarra9Toolbar, window.addBarra9)
        window.addBarra18 = window.toolbarside.AddTool(wx.ID_ANY, "Adicionar Barra de 18cm", imgBarra18, "Barra de 18cm")
        window.Bind(wx.EVT_TOOL, window.OnAddBarra18Toolbar, window.addBarra18)
        window.addLaje = window.toolbarside.AddTool(wx.ID_ANY, "Adicionar Laje", imgLaje, "Laje")
        window.Bind(wx.EVT_TOOL, window.OnAddLajeToolbar, window.addLaje)
        window.addTirante9 = window.toolbarside.AddTool(wx.ID_ANY, "Adicionar Tirante de 9x9", imgTirante9, "Tirante de 9x9")
        window.Bind(wx.EVT_TOOL, window.OnAddTirante9Toolbar, window.addTirante9)
        window.addTirante18 = window.toolbarside.AddTool(wx.ID_ANY, "Adicionar Tirante de 18x9", imgTirante18, "Tirante de 18x18")
        window.Bind(wx.EVT_TOOL, window.OnAddTirante18Toolbar, window.addTirante18)

        window.toolbarside.Realize()

    @staticmethod
    def CreateToolBarTopo(window):

        window.toolbar = window.CreateToolBar()
        if(Vars.thema == "dark"):
            window.toolbar.SetBackgroundColour(Vars.corThema)
            imgMoveTela = wx.Bitmap(Vars.dirExec + 'icones/movedark.ico')
            imgCopiar = wx.Bitmap(Vars.dirExec + 'icones/copiardark.ico')
            open_ico = wx.Bitmap(Vars.dirExec + 'icones/openIcondark.ico')
            save_ico = wx.Bitmap(Vars.dirExec + 'icones/saveIcondark.ico')
            saveAs_ico = wx.Bitmap(Vars.dirExec + 'icones/saveasIcondark.ico')
            imgMoverObj = wx.Bitmap(Vars.dirExec + 'icones/moverObjdark.ico')

        else:
            imgMoveTela = wx.Bitmap(Vars.dirExec + 'icones/move.ico')
            imgCopiar = wx.Bitmap(Vars.dirExec + 'icones/copiar.ico')
            open_ico = wx.Bitmap(Vars.dirExec + 'icones/openIcon.ico')
            save_ico = wx.Bitmap(Vars.dirExec + 'icones/saveIcon.ico')
            saveAs_ico = wx.Bitmap(Vars.dirExec + 'icones/saveasIcon.ico')
            imgMoverObj = wx.Bitmap(Vars.dirExec + 'icones/moverObj.ico')

        window.toolbar.SetToolBitmapSize((32, 32))  # sets icon size

        # Use wx.ArtProvider for default icons

        openTool = window.toolbar.AddTool(wx.ID_OPEN, "Abre um Projeto Existente", open_ico, "Abrir")
        window.Bind(wx.EVT_MENU, window.OnOpen, openTool)


        saveTool = window.toolbar.AddTool(wx.ID_SAVE, "Salva o Projeto Corrente", save_ico, "Salvar")
        window.Bind(wx.EVT_MENU, window.OnSave, saveTool)

        saveAsTool = window.toolbar.AddTool(wx.ID_SAVEAS, "Salva o Projeto Corrente em um Novo Arquivo", saveAs_ico,
                                            "Salvar Como...")
        window.Bind(wx.EVT_MENU, window.OnSaveAs, saveAsTool)

        window.toolbar.AddSeparator()

        undo_ico = wx.Bitmap(Vars.dirExec + 'icones/undoIcon.ico')
        window.undoTool = window.toolbar.AddTool(wx.ID_UNDO, "Desfazer", undo_ico, "Desfazer")
        window.toolbar.EnableTool(wx.ID_UNDO, False)
        window.Bind(wx.EVT_TOOL, window.OnUndo, window.undoTool)

        redo_ico = wx.Bitmap(Vars.dirExec + 'icones/reundoIcon.ico')
        window.redoTool = window.toolbar.AddTool(wx.ID_REDO, "Refazer", redo_ico, "Refazer")
        window.toolbar.EnableTool(wx.ID_REDO, False)
        window.Bind(wx.EVT_TOOL, window.OnRedo, window.redoTool)

        window.moveTela = window.toolbar.AddTool(wx.ID_ANY, "Mover Tela", imgMoveTela, "Mover Tela")
        window.Bind(wx.EVT_TOOL, window.OnMoveTelaToolbar, window.moveTela)

        window.toolbar.AddSeparator()

        window.copiarSelect = window.toolbar.AddTool(wx.ID_ANY, "Copiar Seleção", imgCopiar, "Copiar Seleção")
        window.Bind(wx.EVT_TOOL, window.OnCopiarSelectToolbar, window.copiarSelect)

        window.copiarSelect = window.toolbar.AddTool(wx.ID_ANY, "Mover Seleção", imgMoverObj, "Mover Seleção")
        window.Bind(wx.EVT_TOOL, window.OnMoverSelectToolbar, window.copiarSelect)

        window.toolbar.AddSeparator()

        window.toolbar.Realize()

    @staticmethod
    def OnMoveSelectToolBar(window):
        window.moveObjetos = (True, Vars.ASCII_0)
        Msg.exibirStatusBar("Selecione um eixo de mivimentação precionando x, y ou z", 10)
        window.drawArea0.Refresh(True)
        window.drawArea1.Refresh(True)
        window.drawArea2.Refresh(True)
        window.drawArea3.Refresh(True)

    @staticmethod
    def OnAddLajeToolBar(window):

        myCursor = wx.Cursor(Vars.dirExec + "icones/lajeCursor.cur",
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

        if Vars.thema == "dark":
            myCursor = wx.Cursor(Vars.dirExec + "icones/cursorMoveTeladark.cur",
                                 wx.BITMAP_TYPE_CUR)
        else:
            myCursor = wx.Cursor(Vars.dirExec + "icones/cursorMoveTela.cur",
                                 wx.BITMAP_TYPE_CUR)

        window.botaoSelecionado = Vars.MOVETELA_SELECIONADO

        window.SetCursor(myCursor)

    @staticmethod
    def OnAddEsferaToolbar(window):

        myCursor = wx.Cursor(Vars.dirExec + "icones/cursorEsfera.cur",
                             wx.BITMAP_TYPE_CUR)

        window.botaoSelecionado = Vars.SPHERE_SELECIONADO

        window.SetCursor(myCursor)

    @staticmethod
    def OnAddBaseToolbar(window):

        myCursor = wx.Cursor(Vars.dirExec + "icones/baseCursor.cur",
                             wx.BITMAP_TYPE_CUR)

        window.botaoSelecionado = Vars.BASE_SELECIONADO
        window.SetCursor(myCursor)



    @staticmethod
    def OnAddBarra9Toolbar(window):

        myCursor = wx.Cursor(Vars.dirExec + "icones/cursorBarra.cur",
                             wx.BITMAP_TYPE_CUR)

        window.botaoSelecionado = Vars.BAR9_SELECIONADO

        window.SetCursor(myCursor)

    @staticmethod
    def OnAddBarra18Toolbar(window):
        myCursor = wx.Cursor(Vars.dirExec + "icones/cursorBarra.cur",
                             wx.BITMAP_TYPE_CUR)

        window.botaoSelecionado = Vars.BAR18_SELECIONADO

        window.SetCursor(myCursor)

    @staticmethod
    def OnAddTirante9Toolbar(window):
        myCursor = wx.Cursor(Vars.dirExec + "icones/tiranteCursor.cur",
                             wx.BITMAP_TYPE_CUR)

        window.botaoSelecionado = Vars.TIRANTE9_SELECIONADO

        window.SetCursor(myCursor)

    @staticmethod
    def OnAddTirante18Toolbar(window):
        myCursor = wx.Cursor(Vars.dirExec + "icones/tiranteCursor.cur",
                             wx.BITMAP_TYPE_CUR)

        window.botaoSelecionado = Vars.TIRANTE18_SELECIONADO

        window.SetCursor(myCursor)