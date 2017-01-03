# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# This file is generated by wxPython's PI generator.  Do not edit by hand.
#
# The *.pyi files are used by PyCharm to provide more information than it is
# able to glean from introspection of extension types and methods.  They are
# not intended to be imported, executed or used for any other purpose other
# than providing info to the IDE.  If you don't use PyCharm you can safely
# ignore this file.
#
# See: https://www.jetbrains.com/help/pycharm/2016.1/type-hinting-in-pycharm.html
#
# Copyright: (c) 2011-2016 by Total Control Software
# License:   wxWindows License
#---------------------------------------------------------------------------


"""
This module contains a few classes that are only available on Windows.
"""
#-- begin-_msw --#

import wx
#-- end-_msw --#
#-- begin-metafile --#

class Metafile(wx.Object):
    """
    Metafile(filename=wx.EmptyString)
    
    A wxMetafile represents the MS Windows metafile object, so metafile
    operations have no effect in X.
    """

    def __init__(self, filename=wx.EmptyString):
        """
        Metafile(filename=wx.EmptyString)
        
        A wxMetafile represents the MS Windows metafile object, so metafile
        operations have no effect in X.
        """

    def IsOk(self):
        """
        IsOk() -> bool
        
        Returns true if the metafile is valid.
        """

    def Play(self, dc):
        """
        Play(dc) -> bool
        
        Plays the metafile into the given device context, returning true if
        successful.
        """

    def SetClipboard(self, width=0, height=0):
        """
        SetClipboard(width=0, height=0) -> bool
        
        Passes the metafile data to the clipboard.
        """
# end of class Metafile


class MetafileDC(wx.DC):
    """
    MetafileDC(filename=wx.EmptyString)
    
    This is a type of device context that allows a metafile object to be
    created (Windows only), and has most of the characteristics of a
    normal wxDC.
    """

    def __init__(self, filename=wx.EmptyString):
        """
        MetafileDC(filename=wx.EmptyString)
        
        This is a type of device context that allows a metafile object to be
        created (Windows only), and has most of the characteristics of a
        normal wxDC.
        """

    def Close(self):
        """
        Close() -> Metafile
        
        This must be called after the device context is finished with.
        """
# end of class MetafileDC

#-- end-metafile --#
#-- begin-axbase --#

class PyAxBaseWindow(wx.Window):
    """
    PyAxBaseWindow(parent, id=-1, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, name=wx.PanelNameStr)
    PyAxBaseWindow()
    
    A Window class for use with ActiveX controls.
    
    This Window class exposes some low-level Microsoft Windows
    specific methods which can be overridden in Python.  Intended for
    use as an ActiveX container, but could also be useful
    elsewhere.
    """

    def __init__(self, *args, **kw):
        """
        PyAxBaseWindow(parent, id=-1, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, name=wx.PanelNameStr)
        PyAxBaseWindow()
        
        A Window class for use with ActiveX controls.
        
        This Window class exposes some low-level Microsoft Windows
        specific methods which can be overridden in Python.  Intended for
        use as an ActiveX container, but could also be useful
        elsewhere.
        """

    def MSWTranslateMessage(self, msg):
        """
        MSWTranslateMessage(msg) -> bool
        """
# end of class PyAxBaseWindow

#-- end-axbase --#
