import math

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

    version = "0.1.2"  # Variável de controle de versão
    dateModificacao = "04/01/2017"  # Data da última atualização do programa
    tamJanela = (0, 0)  # Tupla respomsável por guardar o tamanho atual da janela
    drawArea = None  # Variável que armazena uma referência a área de desenho do OpenGL, usado para corrigir o tamanho da área de desenho após um resize
    drawSize = 0.88  # Variável que armazena a porcentagem, normalizada de 0 a 1, do quanto que a drawArea irá pegar do tamanho da janela
    visionModes = ("Perspectiva", "orthoX", "ortho-X", "orthoY", "ortho-Y", "orthoZ",
                        "ortho-Z")  # Variável que armazna os modos de visão
    visionItem = None  # Variável que armazena o label que mostra na janela qual o tipo de visão que estamos utilizando
    camZoom = 5  # Variável que armazena o raio da coordenada esférica correspondente ao zoom da câmera
    theta = math.pi / 4  # Variável que armazena em radianos o ângulo XY da câmera
    phi = math.pi / 3  # Variável que armazena em radianos o ângulo do eixo Z com o plano XY
    cube = False #Variável temporaria, que define o se irá ser desenhado um cubo na drawArea
