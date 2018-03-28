from ctypes import *

class CPonto(Structure):
    _fields_= [("x", c_float),
               ("y", c_float),
               ("z", c_float)]

class CObjeto3D(Structure):
    _fields_ = [
                ("obj", c_int),
                ("id", c_int),
                ("Tx", c_bool),
                ("Ty", c_bool),
                ("Tz", c_bool),
                ("Rx", c_bool),
                ("Ry", c_bool),
                ("Rz", c_bool),
                ("E", c_float),
                ("poisson", c_float),
                ("termico", c_float),
                ("largura", c_float),
                ("altura", c_float),
                ("raio", c_float),
                ("secao", c_int),
                ("centro", CPonto),
                ("MBR", POINTER(CPonto*2)),
                ("idExtremidades", POINTER(c_int * 16)),
                ("tamExtremidades", c_int)
                ]