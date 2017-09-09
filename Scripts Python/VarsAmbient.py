# -*- coding: UTF-8 -*-

import math
from CStructs import *
import wx
from wx import glcanvas
import wx.lib.scrolledpanel
import wx.adv
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

import warnings
warnings.filterwarnings("ignore")

#Arquivo para armazenar todas as variáveis de ambiente utilizadas no programa

class Vars(object):

    thema = "dark"
    corThema = (50,50,50)
    reset = True
    lineUp = None # Variável que armazena uma referência para a linha que separa a drawArea0 e a drawArea1
    lineDown = None  # Variável que armazena uma referência para a linha que separa a drawArea2 e a drawArea3
    boxUp = None # Variável que armazena o sizer que engloba drawArea0 e drawArea1
    boxDown = None  # Variável que armazena o sizer que engloba drawArea2 e drawArea3
    lineBox = None # Variável que armazena uma referência para a linha que separa a boxUp e a boxDown
    boxDraw = None # variável que armazena uma referência ao sizer que contêm toda a parte de draw
    drawPrincipal = -1 #Variável que armazena qual das drawAreas foi selecionado como principal
    posLuz = (0.0,0.0,0.0,1.0) # variável que armazena a posição da luz na cena
    visionModes = ("Perspectiva", "Frente Ortho", "Atrás Ortho", "Direita Ortho", "Esquerda Ortho", "Cima Ortho")  # Variável que armazena os modos de visão(Perspectiva, direita, esquerda, frente, atrás, cima, baixo)
    visionItem = None  # Variável que armazena o label que mostra na janela qual o tipo de visão que estamos utilizando
    rightMouse = (0,0,0) #Variável que armazena a ultima posição do mouse ao clicar com o botao direito
    shiftPress = False #Variável que armazena se o shift está sendo pressionado nesse exato momento
    ctrlPress = False #Variável que armazena se o control está sendo pressionado nesse exato momento

    dirExec = '' # Variável que armazena o diretorio de execução do programa, necessário para abrir arquivos do sistema
    openFile = False #Variável que armazena o diretório da abertura de um arquivo, usado para abrir um arquivo ao iniciar o programa

    # Constantes
    SPHERE = 1
    BAR_SMALL = 2
    BAR_LARGE = 3
    BASE = 4
    LAJE = 5
    DIAGONAL_SMALL = 6
    DIAGONAL_LARGE = 7
    SPHERE_RADIUS = 0.75 # em centimetros
    BASE_RADIUS = 2.2 # em centimetros
    BAR_RADIUS = 0.3 # em centimetros
    BAR_LENGTH_SMALL = 7.5 # em Centrimetros
    BAR_LENGTH_LARGE = 16.5 # em centrimetros
    LAJE_LENGTH = 17.3 # em centimetros
    LAJE_WIDTH = 8.3 # em centimetros
    LAJE_THICKNESS = 0.6 # em centimetros
    LAJE_LEG = 0.0 # em centimetros - catetos que formam o tringulo faltante nas bordas da laje
    DIAGONAL_LENGTH_SMALL = 11.22 # em centimetros
    DIAGONAL_LENGTH_LARGE = 18.625 # em centimetros
    ASCII_0 = 48
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
    X_PRESS = 88
    Y_PRESS = 89
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
    R_PRESS = 82
    NUM_PLUS = 388
    NUM_LESS = 390
    LESS_PRESS = 45
    F1_PRESS = 340
    F2_PRESS = 341
    F3_PRESS = 342
    SPHERE_SELECIONADO = 0
    BAR9_SELECIONADO = 1
    BAR18_SELECIONADO = 2
    BASE_SELECIONADO = 3
    LAJE_SELECIONADO = 4
    MOVETELA_SELECIONADO = 5
    TIRANTE9_SELECIONADO = 6
    TIRANTE18_SELECIONADO = 7
    ADDFORCA_SELECIONADO = 8
    LIVRE_SELECIONADO = -1
    ENTER_PRESS = 13
    BASE_LIVRE = 9
    BASE_BLOQUEADA_X = 10
    BASE_BLOQUEADA_Y = 11
    BASE_BLOQUEADA_XY = 12

    @staticmethod
    def __init__():
        ctypes.WinDLL(
            Vars.dirExec + 'libs/freeglut.dll')  # Importa a dll freeglut.dll, usado apenas no windows, a versão para linux não terá esta linha
        ctypes.WinDLL(
            Vars.dirExec + 'libs/glew32.dll')  # Importa a dll glew32.dll, usado apenas no windows, a versão para linux não terá esta linha
        Vars.KitLib = ctypes.CDLL(
            Vars.dirExec + 'libs/KitLib.dll')  # Variável que armazena uma referência ao núcleo do programa em C
        Vars.KitLib.distObjsSelect.restype = Vars.KitLib.getEspacoGrid.restype = c_float  # define o tipo de retorno da funcao
        Vars.KitLib.getObjById.restype = POINTER(CObjeto3D)  # define o tipo de retorno da funcao
        Vars.KitLib.getCentroMBRSelect.restype = POINTER(CPonto)  # define o tipo de retorno da funcao
        Vars.KitSim = ctypes.CDLL(
            Vars.dirExec + 'libs/ksim.dll')  # Variável que armazena uma referencia ao núcleo da simulacao em C
        Vars.KitSim.getTempoTotal.restype = c_float


