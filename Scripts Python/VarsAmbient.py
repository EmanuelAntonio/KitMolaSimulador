# -*- coding: UTF-8 -*-

import math
from CStructs import *
try:
    import wx
    from wx import glcanvas
    import wx.lib.scrolledpanel

    haveGLCanvas = True
except ImportError:
    haveGLCanvas = False

try:
    # The Python OpenGL package can be found at
    # http://PyOpenGL.sourceforge.net/
    from OpenGL.GLUT import *
    from OpenGL.GLU import *
    from OpenGL.GL import *

    haveOpenGL = True
except ImportError:
    haveOpenGL = False

#Arquivo para armazenar todas as variáveis de ambiente utilizadas no programa

class Vars(object):

    version = "0.6.8"  # Variável de controle de versão
    dateModificacao = "21/02/2017"  # Data da última atualização do programa
    drawArea0 = None  # Variável que armazena uma referência a área de desenho do OpenGL, usado para corrigir o tamanho da área de desenho após um resize
    drawArea1 = None  # Variável que armazena uma referência a área de desenho do OpenGL, usado para corrigir o tamanho da área de desenho após um resize
    drawArea2 = None  # Variável que armazena uma referência a área de desenho do OpenGL, usado para corrigir o tamanho da área de desenho após um resize
    drawArea3 = None  # Variável que armazena uma referência a área de desenho do OpenGL, usado para corrigir o tamanho da área de desenho após um resize
    ultimoDrawSelected = None #Variável que armazena uma referência para qual drawArea foi interagido por último
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
    #camZoom = 16  # Variável que armazena o raio da coordenada esférica correspondente ao zoom da câmera
    #theta = math.pi / 4  # Variável que armazena em radianos o ângulo XY da câmera
    #phi = math.pi / 3  # Variável que armazena em radianos o ângulo do eixo Z com o plano XY
    #centro = (0,0,0) #Variável que armazena a posição do foco da cãmera
    #orthoCenter = (0,0) #Tupla que armazena o ponto central da visão ortho
    #orthoZoom = 5 #Variável que armazena a distancia do centro para visao ortho
    rightMouse = (0,0,0) #Variável que armazena a ultima posição do mouse ao clicar com o botao direito
    arquivoProjeto = "" #Variável que armazena o diretorio com o nome do projeto que está aberto atualmente
    shiftPress = False #Variável que armazena se o shift está sendo pressionado nesse exato momento
    ctrlPress = False #Variável que armazena se o control está sendo pressionado nesse exato momento
    moveObjetos = False #Variável que armazena se a opção de mover objetos está ativa
    moveObjetosEixo = -1 #Variável que armazena qual eixo a seleção irá se mover, apenas usado quando clica-se em cima da seta de movimento

    ctypes.WinDLL('libs/freeglut.dll') #Importa a dll freeglut.dll, usado apenas no windows, a versão para linux não terá esta linha
    KitLib = ctypes.CDLL('libs/kitmola.dll')  # Variável que armazena uma referência ao núcleo do programa em C
    KitLib.distObjsSelect.restype = KitLib.getEspacoGrid.restype = c_float
    KitLib.getObjById.restype = POINTER(CObjeto3D)

    # Constantes
    SPHERE = 1
    BAR_SMALL = 2
    BAR_LARGE = 3
    SPHERE_RADIUS = 0.75 # em centimetros
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


