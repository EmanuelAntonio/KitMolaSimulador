# -*- coding: UTF-8 -*-

from TabConfig import *
from TabCam import *
from TabTools import *
from TabInfo import *


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
        self.parent = parent
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=
                            # wx.BK_DEFAULT
                            # wx.BK_TOP
                            # wx.BK_BOTTOM
                              wx.BK_LEFT
                            # wx.BK_RIGHT

        )

        # Create the first tab and add it to the notebook
        self.tabInfo = TabInfo(self)
        self.AddPage(self.tabInfo, "Objetos")
        imL = wx.ImageList(32,32)

        # Create and add the second tab
        self.tabTools = TabTools(self)
        self.AddPage(self.tabTools, "Ferramentas")

        # Create and add the third tab
        self.tabConfig = TabConfig(self)
        self.AddPage(self.tabConfig, "Configurações")

        # Adiciona os icones nas tabs
        imgObj = imL.Add(wx.Bitmap('icones/obj.ico'))
        imgTool = imL.Add(wx.Bitmap('icones/tool.ico'))
        imgConfig = imL.Add(wx.Bitmap('icones/config.ico'))
        self.AssignImageList(imL)
        self.SetPageImage(0, imgObj)
        self.SetPageImage(1, imgTool)
        self.SetPageImage(2, imgConfig)

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
        self.tabCam = CamPanel(self)
        #tabOne.SetBackgroundColour("Gray")
        self.AddPage(self.tabCam, "Câmera")
        imL = wx.ImageList(32,32)
        # Adiciona os icones nas tabs
        imgObj = imL.Add(wx.Bitmap('icones/cam.ico'))
        self.AssignImageList(imL)
        self.SetPageImage(0, imgObj)

