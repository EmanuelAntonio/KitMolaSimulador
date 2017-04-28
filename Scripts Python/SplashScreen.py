from VarsAmbient import *
import wx.lib.agw.advancedsplash as AS

class Splash(AS.AdvancedSplash):

    def __init__(self,parent):
        imagePath = "icones\KitSim.jpg"
        bitmap = wx.Bitmap(imagePath, wx.BITMAP_TYPE_JPEG)
        AS.AdvancedSplash.__init__(self,parent, bitmap=bitmap, timeout=3000, agwStyle=AS.AS_TIMEOUT | AS.AS_CENTER_ON_SCREEN)