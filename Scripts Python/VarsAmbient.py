import math
from ctypes import c_void_p

try:
    import wx
    from wx import glcanvas

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

    version = "0.1.4"  # Variável de controle de versão
    dateModificacao = "09/01/2017"  # Data da última atualização do programa
    tamJanela = (0, 0)  # Tupla respomsável por guardar o tamanho atual da janela
    drawArea = None  # Variável que armazena uma referência a área de desenho do OpenGL, usado para corrigir o tamanho da área de desenho após um resize
    drawSize = 0.88  # Variável que armazena a porcentagem, normalizada de 0 a 1, do quanto que a drawArea irá pegar do tamanho da janela
    status = None # Varável que armazena uma referência ao 'status bar', pode ser utilizado em usos futuros
    visionModes = ("Perspectiva", "Frente Ortho", "Atrás Ortho", "Direita Ortho", "Esquerda Ortho", "Cima Ortho")  # Variável que armazena os modos de visão(Perspectiva, direita, esquerda, frente, atrás, cima, baixo)
    visionItem = None  # Variável que armazena o label que mostra na janela qual o tipo de visão que estamos utilizando
    visionOption = 0 # Variável que armazena qual a o tipo de visão que está selecionado
    visionAxis = 'z' # Variável que armazena qual o eixo principal para visão, o eixo 'que está para cima', é definido a partir do visionOption
    camZoom = 5  # Variável que armazena o raio da coordenada esférica correspondente ao zoom da câmera
    theta = math.pi / 4  # Variável que armazena em radianos o ângulo XY da câmera
    phi = math.pi / 3  # Variável que armazena em radianos o ângulo do eixo Z com o plano XY
    orthoCenter = (0,0) #Tupla que armazena o ponto central da visão ortho
    orthoZoom = 5 #Variável que armazena a distancia do centro para visao ortho
    rightMouse = (0,0,0) #Variável que armazena a ultima posição do mouse ao clicar com o botao direito
    cube = None #Variável temporaria, que define o se irá ser desenhado um cubo na drawArea

