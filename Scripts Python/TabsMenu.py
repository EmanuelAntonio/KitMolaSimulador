# -*- coding: UTF-8 -*-

from TabConfig import *
from TabCam import *


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
        self.AddPage(self.tabOne, "Objetos")
        imL = wx.ImageList(32,32)

        # Create and add the second tab
        self.tabTwo = TabPanel(self)
        self.AddPage(self.tabTwo, "Ferramentas")

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

#########################################################################################################################################################################################
"""
    ->Classe TabPanel:
        Classe utilizada para instânciar uma das abas, será substituida futuramente por classes específicas para cada aba.

"""
class TabPanel(wx.lib.scrolledpanel.ScrolledPanel):
    """
    This will be the first notebook tab
    """

    # ----------------------------------------------------------------------
    def __init__(self, parent):



        wx.lib.scrolledpanel.ScrolledPanel.__init__(self, parent=parent,size=(100,0), id=wx.ID_ANY,style=wx.DOUBLE_BORDER)
        self.SetupScrolling()

        sizer = wx.BoxSizer(wx.VERTICAL)
        txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
        txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")

        sizer.Add(txtOne, 0, wx.ALIGN_CENTER, 5)
        sizer.Add(txtTwo, 0, wx.ALIGN_CENTER, 5)

        self.SetSizer(sizer)


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

