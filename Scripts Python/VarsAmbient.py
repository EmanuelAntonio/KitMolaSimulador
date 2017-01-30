# -*- coding: UTF-8 -*-

import math
from ctypes import *

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

    version = "0.5.1"  # Variável de controle de versão
    dateModificacao = "30/01/2017"  # Data da última atualização do programa
    tamJanela = (0, 0)  # Tupla respomsável por guardar o tamanho atual da janela
    drawArea = None  # Variável que armazena uma referência a área de desenho do OpenGL, usado para corrigir o tamanho da área de desenho após um resize
    posLuz = (0.0,0.0,0.0,1.0) # variável que armazena a posição da luz na cena
    toolBar = None # Variável que armazena uma refência para a toolbar
    toolBox = None # Variável que armazena uma referencia ao menu do lado direito da tela
    drawSize = 0.8  # Variável que armazena a porcentagem, normalizada de 0 a 1, do quanto que a drawArea irá pegar do tamanho da janela
    status = None # Varável que armazena uma referência ao 'status bar', pode ser utilizado em usos futuros
    visionModes = ("Perspectiva", "Frente Ortho", "Atrás Ortho", "Direita Ortho", "Esquerda Ortho", "Cima Ortho")  # Variável que armazena os modos de visão(Perspectiva, direita, esquerda, frente, atrás, cima, baixo)
    visionItem = None  # Variável que armazena o label que mostra na janela qual o tipo de visão que estamos utilizando
    camZoom = 16  # Variável que armazena o raio da coordenada esférica correspondente ao zoom da câmera
    theta = math.pi / 4  # Variável que armazena em radianos o ângulo XY da câmera
    phi = math.pi / 3  # Variável que armazena em radianos o ângulo do eixo Z com o plano XY
    centro = (0,0,0) #Variável que armazena a posição do foco da cãmera
    orthoCenter = (0,0) #Tupla que armazena o ponto central da visão ortho
    orthoZoom = 5 #Variável que armazena a distancia do centro para visao ortho
    rightMouse = (0,0,0) #Variável que armazena a ultima posição do mouse ao clicar com o botao direito
    arquivoProjeto = "" #Variável que armazena o diretorio com o nome do projeto que está aberto atualmente
    shiftPress = False #Variável que armazena se o shift está sendo pressionado nesse exato momento
    ctrlPress = False #Variável que armazena se o control está sendo pressionado nesse exato momento
    moveObjetos = False #Variável que armazena se a opção de mover objetos está ativa
    moveObjetosEixo = -1 #Variável que armazena qual eixo a seleção irá se mover, apenas usado quando clica-se em cima da seta de movimento
    ctypes.WinDLL('libs/freeglut.dll') #Importa a dll freeglut.dll, usado apenas no windows, a versão para linux não terá esta linha
    KitLib = ctypes.CDLL('libs/kitmola.dll')  # Variável que armazena uma referência ao núcleo do programa em C

