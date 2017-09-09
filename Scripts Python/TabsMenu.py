# -*- coding: UTF-8 -*-

from TabConfig import *
from TabTools import *
from TabInfo import *
from TabSim import *

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
                            wx.NB_DEFAULT

        )
        if(Vars.thema == "dark"):
            self.SetBackgroundColour(Vars.corThema)

        # Create the first tab and add it to the notebook
        self.tabInfo = TabInfo(self)
        self.tabInfo.Layout()
        self.AddPage(self.tabInfo,"")
        imL = wx.ImageList(32,32)

        # Create and add the second tab
        self.tabTools = TabTools(self)
        self.tabTools.Layout()
        self.AddPage(self.tabTools, "")

        # Create and add the third tab
        self.tabConfig = TabConfig(self)
        self.tabConfig.Layout()
        self.AddPage(self.tabConfig, "")

        #self.tabSim = TabSim(self)
        #self.tabSim.Layout()
        #self.AddPage(self.tabSim, "")

        # Adiciona os icones nas tabs
        imgObj = imL.Add(wx.Bitmap(Vars.dirExec + 'icones/obj.ico'))
        imgTool = imL.Add(wx.Bitmap(Vars.dirExec + 'icones/tool.ico'))
        imgConfig = imL.Add(wx.Bitmap(Vars.dirExec + 'icones/config.ico'))
        #imgSim = imL.Add(wx.Bitmap('Vars.dirExec + icones/obj16.ico'))
        self.AssignImageList(imL)
        self.SetPageImage(0, imgObj)
        self.SetPageImage(1, imgTool)
        self.SetPageImage(2, imgConfig)
        #self.SetPageImage(3, imgSim)