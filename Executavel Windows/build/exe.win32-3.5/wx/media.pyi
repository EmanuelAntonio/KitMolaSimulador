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
The ``wx.media`` module provides a widget class that allows displaying various
types of media, such as video and audio files and streaming, using native
system components.  The wxWidgets media classes are an optional part of the
build so it may not always be available on your build of wxPython.
"""
#-- begin-_media --#

import wx
#-- end-_media --#
#-- begin-mediactrl --#
MEDIASTATE_STOPPED = 0
MEDIASTATE_PAUSED = 0
MEDIASTATE_PLAYING = 0
MEDIACTRLPLAYERCONTROLS_NONE = 0
MEDIACTRLPLAYERCONTROLS_STEP = 0
MEDIACTRLPLAYERCONTROLS_VOLUME = 0
MEDIACTRLPLAYERCONTROLS_DEFAULT = 0
wxEVT_MEDIA_LOADED = 0
wxEVT_MEDIA_STOP = 0
wxEVT_MEDIA_FINISHED = 0
wxEVT_MEDIA_STATECHANGED = 0
wxEVT_MEDIA_PLAY = 0
wxEVT_MEDIA_PAUSE = 0

class MediaCtrl(wx.Control):
    """
    MediaCtrl()
    MediaCtrl(parent, id=-1, fileName=wx.EmptyString, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, szBackend=wx.EmptyString, validator=wx.DefaultValidator, name="mediaCtrl")
    
    wxMediaCtrl is a class for displaying types of media, such as videos,
    audio files, natively through native codecs.
    """

    def __init__(self, *args, **kw):
        """
        MediaCtrl()
        MediaCtrl(parent, id=-1, fileName=wx.EmptyString, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, szBackend=wx.EmptyString, validator=wx.DefaultValidator, name="mediaCtrl")
        
        wxMediaCtrl is a class for displaying types of media, such as videos,
        audio files, natively through native codecs.
        """

    def Create(self, parent, id=-1, fileName=wx.EmptyString, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, szBackend=wx.EmptyString, validator=wx.DefaultValidator, name="mediaCtrl"):
        """
        Create(parent, id=-1, fileName=wx.EmptyString, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, szBackend=wx.EmptyString, validator=wx.DefaultValidator, name="mediaCtrl") -> bool
        
        Creates this control.
        """

    def GetBestSize(self):
        """
        GetBestSize() -> wx.Size
        
        Obtains the best size relative to the original/natural size of the
        video, if there is any.
        """

    def GetPlaybackRate(self):
        """
        GetPlaybackRate() -> double
        
        Obtains the playback rate, or speed of the media.
        """

    def GetState(self):
        """
        GetState() -> MediaState
        
        Obtains the state the playback of the media is in.
        """

    def GetVolume(self):
        """
        GetVolume() -> double
        
        Gets the volume of the media from a 0.0 to 1.0 range.
        """

    def Length(self):
        """
        Length() -> FileOffset
        
        Obtains the length - the total amount of time the movie has in
        milliseconds.
        """

    def Load(self, fileName):
        """
        Load(fileName) -> bool
        
        Loads the file that fileName refers to.
        """

    def LoadURI(self, uri):
        """
        LoadURI(uri) -> bool
        
        Loads the location that uri refers to.
        """

    def LoadURIWithProxy(self, uri, proxy):
        """
        LoadURIWithProxy(uri, proxy) -> bool
        
        Loads the location that uri refers to with the proxy proxy.
        """

    def Pause(self):
        """
        Pause() -> bool
        
        Pauses playback of the movie.
        """

    def Play(self):
        """
        Play() -> bool
        
        Resumes playback of the movie.
        """

    def Seek(self, where, mode=wx.FromStart):
        """
        Seek(where, mode=wx.FromStart) -> FileOffset
        
        Seeks to a position within the movie.
        """

    def SetPlaybackRate(self, dRate):
        """
        SetPlaybackRate(dRate) -> bool
        
        Sets the playback rate, or speed of the media, to that referred by
        dRate.
        """

    def SetVolume(self, dVolume):
        """
        SetVolume(dVolume) -> bool
        
        Sets the volume of the media from a 0.0 to 1.0 range to that referred
        by dVolume.
        """

    def ShowPlayerControls(self, flags=MEDIACTRLPLAYERCONTROLS_DEFAULT):
        """
        ShowPlayerControls(flags=MEDIACTRLPLAYERCONTROLS_DEFAULT) -> bool
        
        A special feature to wxMediaCtrl.
        """

    def Stop(self):
        """
        Stop() -> bool
        
        Stops the media.
        """

    def Tell(self):
        """
        Tell() -> FileOffset
        
        Obtains the current position in time within the movie in milliseconds.
        """
    BestSize = property(None, None)
    PlaybackRate = property(None, None)
    State = property(None, None)
    Volume = property(None, None)
# end of class MediaCtrl


class MediaEvent(wx.NotifyEvent):
    """
    MediaEvent(commandType=wx.wxEVT_NULL, winid=0)
    
    Event wxMediaCtrl uses.
    """

    def __init__(self, commandType=wx.wxEVT_NULL, winid=0):
        """
        MediaEvent(commandType=wx.wxEVT_NULL, winid=0)
        
        Event wxMediaCtrl uses.
        """

    EVT_MEDIA_LOADED = wx.PyEventBinder( wxEVT_MEDIA_LOADED )
    EVT_MEDIA_STOP = wx.PyEventBinder( wxEVT_MEDIA_STOP )
    EVT_MEDIA_FINISHED = wx.PyEventBinder( wxEVT_MEDIA_FINISHED )
    EVT_MEDIA_STATECHANGED = wx.PyEventBinder( wxEVT_MEDIA_STATECHANGED )
    EVT_MEDIA_PLAY = wx.PyEventBinder( wxEVT_MEDIA_PLAY )
    EVT_MEDIA_PAUSE = wx.PyEventBinder( wxEVT_MEDIA_PAUSE )
# end of class MediaEvent


MEDIABACKEND_DIRECTSHOW = "wxAMMediaBackend"
MEDIABACKEND_MCI        = "wxMCIMediaBackend"
MEDIABACKEND_QUICKTIME  = "wxQTMediaBackend"
MEDIABACKEND_GSTREAMER  = "wxGStreamerMediaBackend"
MEDIABACKEND_REALPLAYER = "wxRealPlayerMediaBackend"
MEDIABACKEND_WMP10      = "wxWMP10MediaBackend"
#-- end-mediactrl --#
