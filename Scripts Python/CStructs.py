from ctypes import *

class CPonto(Structure):
    _fields_= [("x", c_float),
               ("y", c_float),
               ("z", c_float)]

class CObjeto3D(Structure):
    _fields_ = [("obj", c_int),
                ("id", c_int),
                ("centro", CPonto),
                ("MBR", POINTER(CPonto)),
                ("idExtremidades", POINTER(c_int * 16))]


CObjeto3D.Extremidades = POINTER(c_int*16)