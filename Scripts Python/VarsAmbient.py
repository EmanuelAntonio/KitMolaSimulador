# -*- coding: UTF-8 -*-

import math
from CStructs import *
import wx
from wx import glcanvas
import wx.lib.scrolledpanel
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

import warnings
warnings.filterwarnings("ignore")

#Arquivo para armazenar todas as variáveis de ambiente utilizadas no programa

class Vars(object):

    lineUp = None # Variável que armazena uma referência para a linha que separa a drawArea0 e a drawArea1
    lineDown = None  # Variável que armazena uma referência para a linha que separa a drawArea2 e a drawArea3
    boxUp = None # Variável que armazena o sizer que engloba drawArea0 e drawArea1
    boxDown = None  # Variável que armazena o sizer que engloba drawArea2 e drawArea3
    lineBox = None # Variável que armazena uma referência para a linha que separa a boxUp e a boxDown
    boxDraw = None # variável que armazena uma referência ao sizer que contêm toda a parte de draw
    drawPrincipal = -1 #Variável que armazena qual das drawAreas foi selecionado como principal
    posLuz = (0.0,0.0,0.0,1.0) # variável que armazena a posição da luz na cena
    toolBar = None # Variável que armazena uma refência para a toolbar
    toolBox = None # Variável que armazena uma referencia ao menu do lado direito da tela
    status = None # Varável que armazena uma referência ao 'status bar', pode ser utilizado em usos futuros
    visionModes = ("Perspectiva", "Frente Ortho", "Atrás Ortho", "Direita Ortho", "Esquerda Ortho", "Cima Ortho")  # Variável que armazena os modos de visão(Perspectiva, direita, esquerda, frente, atrás, cima, baixo)
    visionItem = None  # Variável que armazena o label que mostra na janela qual o tipo de visão que estamos utilizando
    rightMouse = (0,0,0) #Variável que armazena a ultima posição do mouse ao clicar com o botao direito
    shiftPress = False #Variável que armazena se o shift está sendo pressionado nesse exato momento
    ctrlPress = False #Variável que armazena se o control está sendo pressionado nesse exato momento

    ctypes.WinDLL('libs/freeglut.dll') #Importa a dll freeglut.dll, usado apenas no windows, a versão para linux não terá esta linha
    KitLib = ctypes.CDLL('libs/kitmola.dll')  # Variável que armazena uma referência ao núcleo do programa em C
    KitLib.distObjsSelect.restype = KitLib.getEspacoGrid.restype = c_float # define o tipo de retorno da funcao
    KitLib.getObjById.restype = POINTER(CObjeto3D) # define o tipo de retorno da funcao
    KitLib.getCentroMBRSelect.restype = POINTER(CPonto) # define o tipo de retorno da funcao

    # Constantes
    SPHERE = 1
    BAR_SMALL = 2
    BAR_LARGE = 3
    BASE = 4
    SPHERE_RADIUS = 0.75 # em centimetros
    BASE_RADIUS = 2.2 # em centimetros
    BAR_RADIUS = 0.3 # em centimetros
    BAR_LENGTH_SMALL = 7.5 # em Centrimetros
    BAR_LENGTH_LARGE = 16.5 # em centrimetros
    ASCII_X = 120
    ASCII_Y = 121
    ASCII_Z = 122
    VISION_Z_PERSP = 0
    VISION_Z_ORTHO = 5
    VISION_X_POS = 1
    VISION_X_NEG = 2
    VISION_Y_POS = 3
    VISION_Y_NEG = 4
    W_PRESS = 87
    S_PRESS = 83
    G_PRESS = 71
    A_PRESS = 65
    D_PRESS = 68
    Z_PRESS = 90
    T_PRESS = 84
    NUM_0_PRESS = 324
    NUM_1_PRESS = 325
    NUM_2_PRESS = 326
    NUM_3_PRESS = 327
    NUM_4_PRESS = 328
    NUM_5_PRESS = 329
    N_0_PRESS = 48
    N_1_PRESS = 49
    N_2_PRESS = 50
    N_3_PRESS = 51
    N_4_PRESS = 52
    N_5_PRESS = 53
    ESC_PRESS = 27
    NUM_PLUS = 388
    NUM_LESS = 390
    LESS_PRESS = 45
    SPHERE_SELECIONADO = 0
    BAR9_SELECIONADO = 1
    BAR18_SELECIONADO = 2
    BASE_SELECIONADO = 3
    LAJE_SELECIONADO = 4
    MOVETELA_SELECIONADO = 5
    LIVRE_SELECIONADO = -1
    ENTER_PRESS = 13


