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
These classes enable viewing and interacting with an OpenGL context in a wx.Window.
"""
#-- begin-_glcanvas --#

import wx
WX_GL_RGBA = 0
WX_GL_BUFFER_SIZE = 0
WX_GL_LEVEL = 0
WX_GL_DOUBLEBUFFER = 0
WX_GL_STEREO = 0
WX_GL_AUX_BUFFERS = 0
WX_GL_MIN_RED = 0
WX_GL_MIN_GREEN = 0
WX_GL_MIN_BLUE = 0
WX_GL_MIN_ALPHA = 0
WX_GL_DEPTH_SIZE = 0
WX_GL_STENCIL_SIZE = 0
WX_GL_MIN_ACCUM_RED = 0
WX_GL_MIN_ACCUM_GREEN = 0
WX_GL_MIN_ACCUM_BLUE = 0
WX_GL_MIN_ACCUM_ALPHA = 0
WX_GL_SAMPLE_BUFFERS = 0
WX_GL_SAMPLES = 0
WX_GL_CORE_PROFILE = 0
WX_GL_MAJOR_VERSION = 0
WX_GL_MINOR_VERSION = 0

class GLContext(Object):
    """
    GLContext(win, other=None)
    
    An instance of a wxGLContext represents the state of an OpenGL state
    machine and the connection between OpenGL and the system.
    """

    def __init__(self, win, other=None):
        """
        GLContext(win, other=None)
        
        An instance of a wxGLContext represents the state of an OpenGL state
        machine and the connection between OpenGL and the system.
        """

    def SetCurrent(self, win):
        """
        SetCurrent(win) -> bool
        
        Makes the OpenGL state that is represented by this rendering context
        current with the wxGLCanvas win.
        """
# end of class GLContext


class GLCanvas(Window):
    """
    GLCanvas(self, parent, id=ID_ANY, attribList=None, pos=DefaultPosition, size=DefaultSize, style=0, name='GLCanvas', palette=NullPalette)
    
    wxGLCanvas is a class for displaying OpenGL graphics.
    """

    def __init__(self, self, parent, id=ID_ANY, attribList=None, pos=DefaultPosition, size=DefaultSize, style=0, name='GLCanvas', palette=NullPalette):
        """
        GLCanvas(self, parent, id=ID_ANY, attribList=None, pos=DefaultPosition, size=DefaultSize, style=0, name='GLCanvas', palette=NullPalette)
        
        wxGLCanvas is a class for displaying OpenGL graphics.
        """

    def SetColour(self, colour):
        """
        SetColour(colour) -> bool
        
        Sets the current colour for this window (using glcolor3f()), using the
        wxWidgets colour database to find a named colour.
        """

    def SetCurrent(self, context):
        """
        SetCurrent(context) -> bool
        
        Makes the OpenGL state that is represented by the OpenGL rendering
        context context current, i.e.
        """

    def SwapBuffers(self):
        """
        SwapBuffers() -> bool
        
        Swaps the double-buffer of this window, making the back-buffer the
        front-buffer and vice versa, so that the output of the previous OpenGL
        commands is displayed on the window.
        """

    @staticmethod
    def IsDisplaySupported(attribList):
        """
        IsDisplaySupported(attribList) -> bool
        
        Determines if a canvas having the specified attributes is available.
        """

    @staticmethod
    def IsExtensionSupported(extension):
        """
        IsExtensionSupported(extension) -> bool
        
        Returns true if the extension with given name is supported.
        """
# end of class GLCanvas

#-- end-_glcanvas --#