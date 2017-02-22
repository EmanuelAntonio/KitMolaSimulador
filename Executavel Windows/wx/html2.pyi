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
# Copyright: (c) 2017 by Total Control Software
# License:   wxWindows License
#---------------------------------------------------------------------------


"""
The ``wx.html2`` module includes a widget class and supporting classes that
wraps native browser components on the system, therefore providing a fully
featured HTML rendering component including the latest HTML, Javascript and
CSS standards. Since platform-specific back-ends are used (Microsoft Trident,
WebKit webView, etc.) there will be some difference in ability and behaviors,
but these classes will minimize those differences as much as possible.
"""
#-- begin-_html2 --#

import wx
#-- end-_html2 --#
#-- begin-webview --#
WEBVIEW_ZOOM_TINY = 0
WEBVIEW_ZOOM_SMALL = 0
WEBVIEW_ZOOM_MEDIUM = 0
WEBVIEW_ZOOM_LARGE = 0
WEBVIEW_ZOOM_LARGEST = 0
WEBVIEW_ZOOM_TYPE_LAYOUT = 0
WEBVIEW_ZOOM_TYPE_TEXT = 0
WEBVIEW_NAV_ERR_CONNECTION = 0
WEBVIEW_NAV_ERR_CERTIFICATE = 0
WEBVIEW_NAV_ERR_AUTH = 0
WEBVIEW_NAV_ERR_SECURITY = 0
WEBVIEW_NAV_ERR_NOT_FOUND = 0
WEBVIEW_NAV_ERR_REQUEST = 0
WEBVIEW_NAV_ERR_USER_CANCELLED = 0
WEBVIEW_NAV_ERR_OTHER = 0
WEBVIEW_RELOAD_DEFAULT = 0
WEBVIEW_RELOAD_NO_CACHE = 0
WEBVIEW_FIND_WRAP = 0
WEBVIEW_FIND_ENTIRE_WORD = 0
WEBVIEW_FIND_MATCH_CASE = 0
WEBVIEW_FIND_HIGHLIGHT_RESULT = 0
WEBVIEW_FIND_BACKWARDS = 0
WEBVIEW_FIND_DEFAULT = 0
wxEVT_WEBVIEW_NAVIGATING = 0
wxEVT_WEBVIEW_NAVIGATED = 0
wxEVT_WEBVIEW_LOADED = 0
wxEVT_WEBVIEW_ERROR = 0
wxEVT_WEBVIEW_NEWWINDOW = 0
wxEVT_WEBVIEW_TITLE_CHANGED = 0

class WebViewHistoryItem(object):
    """
    WebViewHistoryItem(url, title)
    
    A simple class that contains the URL and title of an element of the
    history of a wxWebView.
    """

    def __init__(self, url, title):
        """
        WebViewHistoryItem(url, title)
        
        A simple class that contains the URL and title of an element of the
        history of a wxWebView.
        """

    def GetUrl(self):
        """
        GetUrl() -> String
        """

    def GetTitle(self):
        """
        GetTitle() -> String
        """
    Title = property(None, None)
    Url = property(None, None)
# end of class WebViewHistoryItem


class WebViewHandler(object):
    """
    WebViewHandler(scheme)
    
    The base class for handling custom schemes in wxWebView, for example
    to allow virtual file system support.
    """

    def __init__(self, scheme):
        """
        WebViewHandler(scheme)
        
        The base class for handling custom schemes in wxWebView, for example
        to allow virtual file system support.
        """

    def GetFile(self, uri):
        """
        GetFile(uri) -> wx.FSFile
        """

    def GetName(self):
        """
        GetName() -> String
        """
    Name = property(None, None)
# end of class WebViewHandler


class WebViewArchiveHandler(WebViewHandler):
    """
    WebViewArchiveHandler(scheme)
    
    A custom handler for the file scheme which also supports loading from
    archives.
    """

    def __init__(self, scheme):
        """
        WebViewArchiveHandler(scheme)
        
        A custom handler for the file scheme which also supports loading from
        archives.
        """

    def GetFile(self, uri):
        """
        GetFile(uri) -> wx.FSFile
        """
# end of class WebViewArchiveHandler


class WebViewFSHandler(WebViewHandler):
    """
    WebViewFSHandler(scheme)
    
    A wxWebView file system handler to support standard wxFileSystem
    protocols of the form  example:page.htm  The handler allows wxWebView
    to use wxFileSystem in a similar fashion to its use with wxHtml.
    """

    def __init__(self, scheme):
        """
        WebViewFSHandler(scheme)
        
        A wxWebView file system handler to support standard wxFileSystem
        protocols of the form  example:page.htm  The handler allows wxWebView
        to use wxFileSystem in a similar fashion to its use with wxHtml.
        """

    def GetFile(self, uri):
        """
        GetFile(uri) -> wx.FSFile
        """
# end of class WebViewFSHandler

WebViewNameStr = ""
WebViewDefaultURLStr = ""

class WebView(wx.Control):
    """
    This control may be used to render web (HTML / CSS / javascript)
    documents.
    """

    def CanCopy(self):
        """
        CanCopy() -> bool
        
        Returns true if the current selection can be copied.
        """

    def CanCut(self):
        """
        CanCut() -> bool
        
        Returns true if the current selection can be cut.
        """

    def CanPaste(self):
        """
        CanPaste() -> bool
        
        Returns true if data can be pasted.
        """

    def Copy(self):
        """
        Copy()
        
        Copies the current selection.
        """

    def Cut(self):
        """
        Cut()
        
        Cuts the current selection.
        """

    def Paste(self):
        """
        Paste()
        
        Pastes the current data.
        """

    def EnableContextMenu(self, enable=True):
        """
        EnableContextMenu(enable=True)
        
        Enable or disable the right click context menu.
        """

    def IsContextMenuEnabled(self):
        """
        IsContextMenuEnabled() -> bool
        
        Returns true if a context menu will be shown on right click.
        """

    def CanGoBack(self):
        """
        CanGoBack() -> bool
        
        Returns true if it is possible to navigate backward in the history of
        visited pages.
        """

    def CanGoForward(self):
        """
        CanGoForward() -> bool
        
        Returns true if it is possible to navigate forward in the history of
        visited pages.
        """

    def ClearHistory(self):
        """
        ClearHistory()
        
        Clear the history, this will also remove the visible page.
        """

    def EnableHistory(self, enable=True):
        """
        EnableHistory(enable=True)
        
        Enable or disable the history.
        """

    def GetBackwardHistory(self):
        """
        GetBackwardHistory() -> PyObject
        
        Returns a list of items in the back history.
        """

    def GetForwardHistory(self):
        """
        GetForwardHistory() -> PyObject
        
        Returns a list of items in the forward history.
        """

    def GoBack(self):
        """
        GoBack()
        
        Navigate back in the history of visited pages.
        """

    def GoForward(self):
        """
        GoForward()
        
        Navigate forward in the history of visited pages.
        """

    def ClearSelection(self):
        """
        ClearSelection()
        
        Clears the current selection.
        """

    def DeleteSelection(self):
        """
        DeleteSelection()
        
        Deletes the current selection.
        """

    def GetSelectedSource(self):
        """
        GetSelectedSource() -> String
        
        Returns the currently selected source, if any.
        """

    def GetSelectedText(self):
        """
        GetSelectedText() -> String
        
        Returns the currently selected text, if any.
        """

    def HasSelection(self):
        """
        HasSelection() -> bool
        
        Returns true if there is a current selection.
        """

    def SelectAll(self):
        """
        SelectAll()
        
        Selects the entire page.
        """

    def CanRedo(self):
        """
        CanRedo() -> bool
        
        Returns true if there is an action to redo.
        """

    def CanUndo(self):
        """
        CanUndo() -> bool
        
        Returns true if there is an action to undo.
        """

    def Redo(self):
        """
        Redo()
        
        Redos the last action.
        """

    def Undo(self):
        """
        Undo()
        
        Undos the last action.
        """

    def Find(self, text, flags=WEBVIEW_FIND_DEFAULT):
        """
        Find(text, flags=WEBVIEW_FIND_DEFAULT) -> long
        
        Finds a phrase on the current page and if found, the control will
        scroll the phrase into view and select it.
        """

    def CanSetZoomType(self, type):
        """
        CanSetZoomType(type) -> bool
        
        Retrieve whether the current HTML engine supports a zoom type.
        """

    def GetZoom(self):
        """
        GetZoom() -> WebViewZoom
        
        Get the zoom factor of the page.
        """

    def GetZoomType(self):
        """
        GetZoomType() -> WebViewZoomType
        
        Get how the zoom factor is currently interpreted.
        """

    def SetZoom(self, zoom):
        """
        SetZoom(zoom)
        
        Set the zoom factor of the page.
        """

    def SetZoomType(self, zoomType):
        """
        SetZoomType(zoomType)
        
        Set how to interpret the zoom factor.
        """

    def Create(self, parent, id=wx.ID_ANY, url=WebViewDefaultURLStr, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, name=WebViewNameStr):
        """
        Create(parent, id=wx.ID_ANY, url=WebViewDefaultURLStr, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, name=WebViewNameStr) -> bool
        
        Creation function for two-step creation.
        """

    def GetCurrentTitle(self):
        """
        GetCurrentTitle() -> String
        
        Get the title of the current web page, or its URL/path if title is not
        available.
        """

    def GetCurrentURL(self):
        """
        GetCurrentURL() -> String
        
        Get the URL of the currently displayed document.
        """

    def GetNativeBackend(self):
        """
        GetNativeBackend() -> void
        
        Return the pointer to the native backend used by this control.
        """

    def GetPageSource(self):
        """
        GetPageSource() -> String
        
        Get the HTML source code of the currently displayed document.
        """

    def GetPageText(self):
        """
        GetPageText() -> String
        
        Get the text of the current page.
        """

    def IsBusy(self):
        """
        IsBusy() -> bool
        
        Returns whether the web control is currently busy (e.g. loading a
        page).
        """

    def IsEditable(self):
        """
        IsEditable() -> bool
        
        Returns whether the web control is currently editable.
        """

    def LoadURL(self, url):
        """
        LoadURL(url)
        
        Load a web page from a URL.
        """

    def Print(self):
        """
        Print()
        
        Opens a print dialog so that the user may print the currently
        displayed page.
        """

    def RegisterHandler(self, handler):
        """
        RegisterHandler(handler)
        
        Registers a custom scheme handler.
        """

    def Reload(self, flags=WEBVIEW_RELOAD_DEFAULT):
        """
        Reload(flags=WEBVIEW_RELOAD_DEFAULT)
        
        Reload the currently displayed URL.
        """

    def RunScript(self, javascript):
        """
        RunScript(javascript)
        
        Runs the given javascript code.
        """

    def SetEditable(self, enable=True):
        """
        SetEditable(enable=True)
        
        Set the editable property of the web control.
        """

    def SetPage(self, *args, **kw):
        """
        SetPage(html, baseUrl)
        SetPage(html, baseUrl)
        
        Set the displayed page source to the contents of the given string.
        """

    def Stop(self):
        """
        Stop()
        
        Stop the current page loading process, if any.
        """

    @staticmethod
    def New(*args, **kw):
        """
        New(backend=WebViewBackendDefault) -> WebView
        New(parent, id=wx.ID_ANY, url=WebViewDefaultURLStr, pos=wx.DefaultPosition, size=wx.DefaultSize, backend=WebViewBackendDefault, style=0, name=WebViewNameStr) -> WebView
        
        Factory function to create a new wxWebView with two-step creation,
        wxWebView::Create should be called on the returned object.
        """

    @staticmethod
    def RegisterFactory(backend, factory):
        """
        RegisterFactory(backend, factory)
        
        Allows the registering of new backend for wxWebView.
        """
    BackwardHistory = property(None, None)
    CurrentTitle = property(None, None)
    CurrentURL = property(None, None)
    ForwardHistory = property(None, None)
    NativeBackend = property(None, None)
    PageSource = property(None, None)
    PageText = property(None, None)
    SelectedSource = property(None, None)
    SelectedText = property(None, None)
    Zoom = property(None, None)
    ZoomType = property(None, None)
# end of class WebView


class WebViewEvent(wx.NotifyEvent):
    """
    WebViewEvent()
    WebViewEvent(type, id, href, target)
    
    A navigation event holds information about events associated with
    wxWebView objects.
    """

    def __init__(self, *args, **kw):
        """
        WebViewEvent()
        WebViewEvent(type, id, href, target)
        
        A navigation event holds information about events associated with
        wxWebView objects.
        """

    def GetTarget(self):
        """
        GetTarget() -> String
        
        Get the name of the target frame which the url of this event has been
        or will be loaded into.
        """

    def GetURL(self):
        """
        GetURL() -> String
        
        Get the URL being visited.
        """
    Target = property(None, None)
    URL = property(None, None)
# end of class WebViewEvent


class WebViewFactory(wx.Object):
    """
    An abstract factory class for creating wxWebView backends.
    """

    def Create(self, *args, **kw):
        """
        Create() -> WebView
        Create(parent, id, url=WebViewDefaultURLStr, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, name=WebViewNameStr) -> WebView
        
        Function to create a new wxWebView with two-step creation,
        wxWebView::Create should be called on the returned object.
        """
# end of class WebViewFactory

WebViewBackendDefault = ""
WebViewBackendIE = ""
WebViewBackendWebKit = ""

EVT_WEBVIEW_NAVIGATING = wx.PyEventBinder( wxEVT_WEBVIEW_NAVIGATING, 1 )
EVT_WEBVIEW_NAVIGATED = wx.PyEventBinder( wxEVT_WEBVIEW_NAVIGATED, 1 )
EVT_WEBVIEW_LOADED = wx.PyEventBinder( wxEVT_WEBVIEW_LOADED, 1 )
EVT_WEBVIEW_ERROR = wx.PyEventBinder( wxEVT_WEBVIEW_ERROR, 1 )
EVT_WEBVIEW_NEWWINDOW = wx.PyEventBinder( wxEVT_WEBVIEW_NEWWINDOW, 1 )
EVT_WEBVIEW_TITLE_CHANGED = wx.PyEventBinder( wxEVT_WEBVIEW_TITLE_CHANGED, 1 )

# deprecated wxEVT aliases
wxEVT_COMMAND_WEBVIEW_NAVIGATING     = wxEVT_WEBVIEW_NAVIGATING
wxEVT_COMMAND_WEBVIEW_NAVIGATED      = wxEVT_WEBVIEW_NAVIGATED
wxEVT_COMMAND_WEBVIEW_LOADED         = wxEVT_WEBVIEW_LOADED
wxEVT_COMMAND_WEBVIEW_ERROR          = wxEVT_WEBVIEW_ERROR
wxEVT_COMMAND_WEBVIEW_NEWWINDOW      = wxEVT_WEBVIEW_NEWWINDOW
wxEVT_COMMAND_WEBVIEW_TITLE_CHANGED  = wxEVT_WEBVIEW_TITLE_CHANGED
#-- end-webview --#
