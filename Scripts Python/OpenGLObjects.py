from VarsAmbient import *

"""
    ->Função drawSphere:
        Desenha uma esfera em um local do R^3
    ->Parâmetros:
        ->centro: uma tupla (x,y,z), que contem a posição do centro da esfera
        ->raio: 'float' que armazena qual o raio da esfera a ser desenhada
         ->resolucao: valor responsável por definir a quantidade de poligonos que serão edsenhados para que se forme a esfera
    ->Retorno: vazio

"""

def drawSphere(centro, raio, resolucao):

    theta = 2*math.pi
    theta = theta/resolucao
    glDisable(GL_LIGHTING)
    glColor3f(1.0,1.0,1.0)


    glBegin(GL_LINES)

    for i in range(resolucao):
        if Vars.visionAxis == 'z':
            glVertex(raio * math.cos(theta * i) + centro[0], raio * math.sin(theta * i) + centro[1], centro[2])
            glVertex(raio * math.cos(theta * (i + 1)) + centro[0], raio * math.sin(theta * (i + 1)) + centro[1],
                     centro[2])

    glEnd()

    glEnable(GL_LIGHTING)

"""
    ->FUnção drawCubeZero:
        Desenha um cubo de aresta 1 sobre a origem
    ->Parâmetros: vazio
    ->Retorno: vazio

    *Será apagado após a fase de testes


"""

def drawCube(centro):

    glBegin(GL_QUADS)

    if Vars.visionAxis == 'z':
        glNormal3f(0, 0, 1)
        glVertex3f(0.5 + centro[0], 0.5 + centro[1], 0.5 + centro[2])
        glVertex3f(-0.5 + centro[0], 0.5 + centro[1], 0.5 + centro[2])
        glVertex3f(-0.5 + centro[0], -0.5 + centro[1], 0.5 + centro[2])
        glVertex3f(0.5 + centro[0], -0.5 + centro[1], 0.5 + centro[2])

        glNormal3f(0, 0, -1)
        glVertex3f(0.5 + centro[0], 0.5 + centro[1], -0.5 + centro[2])
        glVertex3f(-0.5 + centro[0], 0.5 + centro[1], -0.5 + centro[2])
        glVertex3f(-0.5 + centro[0], -0.5 + centro[1], -0.5 + centro[2])
        glVertex3f(0.5 + centro[0], -0.5 + centro[1], -0.5 + centro[2])

        glNormal3f(-1, 0, 0)
        glVertex3f(-0.5 + centro[0], -0.5 + centro[1], -0.5 + centro[2])
        glVertex3f(-0.5 + centro[0], -0.5 + centro[1], 0.5 + centro[2])
        glVertex3f(-0.5 + centro[0], 0.5 + centro[1], 0.5 + centro[2])
        glVertex3f(-0.5 + centro[0], 0.5 + centro[1], -0.5 + centro[2])

        glNormal3f(1, 0, 0)
        glVertex3f(0.5 + centro[0], 0.5 + centro[1], 0.5 + centro[2])
        glVertex3f(0.5 + centro[0], -0.5 + centro[1], 0.5 + centro[2])
        glVertex3f(0.5 + centro[0], -0.5 + centro[1], -0.5 + centro[2])
        glVertex3f(0.5 + centro[0], 0.5 + centro[1], -0.5 + centro[2])

        glNormal3f(0, -1, 0)
        glVertex3f(-0.5 + centro[0], -0.5 + centro[1], -0.5 + centro[2])
        glVertex3f(0.5 + centro[0], -0.5 + centro[1], -0.5 + centro[2])
        glVertex3f(0.5 + centro[0], -0.5 + centro[1], 0.5 + centro[2])
        glVertex3f(-0.5 + centro[0], -0.5 + centro[1], 0.5 + centro[2])

        glNormal3f(0, 1, 0)
        glVertex3f(0.5 + centro[0], 0.5 + centro[1], -0.5 + centro[2])
        glVertex3f(-0.5 + centro[0], 0.5 + centro[1], -0.5 + centro[2])
        glVertex3f(-0.5 + centro[0], 0.5 + centro[1], 0.5 + centro[2])
        glVertex3f(0.5 + centro[0], 0.5 + centro[1], 0.5 + centro[2])
    elif Vars.visionAxis == 'x':
        glNormal3f(1, 0, 0)
        glVertex3f(0.5 + centro[2], 0.5 + centro[1], 0.5 + centro[0])
        glVertex3f(0.5 + centro[2], 0.5 + centro[1], -0.5 + centro[0])
        glVertex3f( 0.5 + centro[2], -0.5 + centro[1], -0.5 + centro[0])
        glVertex3f(0.5 + centro[2], -0.5 + centro[1],0.5 + centro[0])

        glNormal3f(-1, 0, 0)
        glVertex3f(-0.5 + centro[2], 0.5 + centro[1], 0.5 + centro[0])
        glVertex3f(-0.5 + centro[2], 0.5 + centro[1], -0.5 + centro[0])
        glVertex3f(-0.5 + centro[2], -0.5 + centro[1], -0.5 + centro[0])
        glVertex3f(-0.5 + centro[2], -0.5 + centro[1], 0.5 + centro[0])

        glNormal3f(0, 0, -1)
        glVertex3f(-0.5 + centro[2], -0.5 + centro[1], -0.5 + centro[0])
        glVertex3f(0.5 + centro[2], -0.5 + centro[1], -0.5 + centro[0])
        glVertex3f(0.5 + centro[2], 0.5 + centro[1], -0.5 + centro[0])
        glVertex3f(-0.5 + centro[2], 0.5 + centro[1], -0.5 + centro[0])

        glNormal3f(0, 0, 1)
        glVertex3f(0.5 + centro[2], 0.5 + centro[1], 0.5 + centro[0])
        glVertex3f(0.5 + centro[2], -0.5 + centro[1], 0.5 + centro[0])
        glVertex3f(-0.5 + centro[2], -0.5 + centro[1], 0.5 + centro[0])
        glVertex3f(-0.5 + centro[2], 0.5 + centro[1], 0.5 + centro[0])

        glNormal3f(0, -1, 0)
        glVertex3f(-0.5 + centro[2], -0.5 + centro[1], -0.5 + centro[0])
        glVertex3f(-0.5 + centro[2], -0.5 + centro[1], 0.5 + centro[0])
        glVertex3f(0.5 + centro[2], -0.5 + centro[1], 0.5 + centro[0])
        glVertex3f(0.5 + centro[2], -0.5 + centro[1], -0.5 + centro[0])

        glNormal3f(0, 1, 0)
        glVertex3f(-0.5 + centro[2], 0.5 + centro[1], 0.5 + centro[0])
        glVertex3f(-0.5 + centro[2], 0.5 + centro[1], -0.5 + centro[0])
        glVertex3f(0.5 + centro[2], 0.5 + centro[1], -0.5 + centro[0])
        glVertex3f(0.5 + centro[2], 0.5 + centro[1], 0.5 + centro[0])
    else:
        glNormal3f(0, 1, 0)
        glVertex3f(0.5 + centro[0], 0.5 + centro[2], 0.5 + centro[1])
        glVertex3f(-0.5 + centro[0], 0.5 + centro[2], 0.5 + centro[1])
        glVertex3f(-0.5 + centro[0], 0.5 + centro[2], -0.5 + centro[1])
        glVertex3f(0.5 + centro[0], 0.5 + centro[2], -0.5 + centro[1])

        glNormal3f(0, -1, 0)
        glVertex3f(0.5 + centro[0], -0.5 + centro[2], 0.5 + centro[1])
        glVertex3f(-0.5 + centro[0], -0.5 + centro[2], 0.5 + centro[1])
        glVertex3f(-0.5 + centro[0], -0.5 + centro[2], -0.5 + centro[1])
        glVertex3f(0.5 + centro[0], -0.5 + centro[2], -0.5 + centro[1])

        glNormal3f(-1, 0, 0)
        glVertex3f(-0.5 + centro[0], -0.5 + centro[2], -0.5 + centro[1])
        glVertex3f(-0.5 + centro[0], 0.5 + centro[2], -0.5 + centro[1])
        glVertex3f(-0.5 + centro[0], 0.5 + centro[2], 0.5 + centro[1])
        glVertex3f(-0.5 + centro[0], -0.5 + centro[2], 0.5 + centro[1])

        glNormal3f(1, 0, 0)
        glVertex3f(0.5 + centro[0], 0.5 + centro[2], 0.5 + centro[1])
        glVertex3f(0.5 + centro[0], 0.5 + centro[2], -0.5 + centro[1])
        glVertex3f(0.5 + centro[0], -0.5 + centro[2], -0.5 + centro[1])
        glVertex3f(0.5 + centro[0], -0.5 + centro[2], 0.5 + centro[1])

        glNormal3f(0, 0, -1)
        glVertex3f(-0.5 + centro[0], -0.5 + centro[2], -0.5 + centro[1])
        glVertex3f(0.5 + centro[0], -0.5 + centro[2], -0.5 + centro[1])
        glVertex3f(0.5 + centro[0], 0.5 + centro[2], -0.5 + centro[1])
        glVertex3f(-0.5 + centro[0], 0.5 + centro[2], -0.5 + centro[1])

        glNormal3f(0, 0, 1)
        glVertex3f(0.5 + centro[0], -0.5 + centro[2], 0.5 + centro[1])
        glVertex3f(-0.5 + centro[0], -0.5 + centro[2], 0.5 + centro[1])
        glVertex3f(-0.5 + centro[0], 0.5 + centro[2], 0.5 + centro[1])
        glVertex3f(0.5 + centro[0], 0.5 + centro[2], 0.5 + centro[1])

    glEnd()


"""
    ->Função drawAxis:
        Desenha os eixos cartesianos no centro do espaco R^3
    ->Parâmetros: vazio
    ->Retorno: vazio


"""

def drawAxis():

    if Vars.visionAxis == 'z':
        glDisable(GL_LIGHTING)

        # X-axis
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_LINES)

        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(1.0, 0.0, 0.0)

        glEnd()

        glBegin(GL_QUADS)

        glNormal3f(-1.0, 0.0, 0.0)
        glVertex3f(1.0, -0.05, -0.05)
        glVertex3f(1.0, -0.05, 0.05)
        glVertex3f(1.0, 0.05, 0.05)
        glVertex3f(1.0, 0.05, -0.05)

        glEnd()

        glBegin(GL_TRIANGLE_FAN)

        glVertex3f(1.2, 0.0, 0.0)
        glVertex3f(1.0, 0.05, 0.05)
        glVertex3f(1.0, -0.05, 0.05)
        glVertex3f(1.0, -0.05, -0.05)
        glVertex3f(1.0, 0.05, -0.05)
        glVertex3f(1.0, 0.05, 0.05)

        glEnd()

        # Y-axis
        glColor3f(0.0, 1.0, 0.0)
        glBegin(GL_LINES)

        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 1.0, 0.0)

        glEnd()

        glBegin(GL_QUADS)

        glNormal3f(0.0, -1.0, 0.0)
        glVertex3f(0.05, 1.0, 0.05)
        glVertex3f(-0.05, 1.0, 0.05)
        glVertex3f(-0.05, 1.0, -0.05)
        glVertex3f(0.05, 1.0, -0.05)

        glEnd()

        glBegin(GL_TRIANGLE_FAN)

        glVertex3f(0.0, 1.2, 0.0)
        glVertex3f(-0.05, 1.0, -0.05)
        glVertex3f(-0.05, 1.0, 0.05)
        glVertex3f(0.05, 1.0, 0.05)
        glVertex3f(0.05, 1.0, -0.05)
        glVertex3f(-0.05, 1.0, -0.05)

        glEnd()

        # Z-axis
        glColor3f(0.0, 0.0, 1.0)
        glBegin(GL_LINES)

        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, 0.0, 1.0)

        glEnd()

        glBegin(GL_QUADS)

        glNormal3f(0.0, 0.0, 1.0)
        glVertex3f(-0.05, -0.05, 1.0)
        glVertex3f(-0.05, 0.05, 1.0)
        glVertex3f(0.05, 0.05, 1.0)
        glVertex3f(0.05, -0.05, 1.0)

        glEnd()

        glBegin(GL_TRIANGLE_FAN)

        glVertex3f(0.0, 0.0, 1.2)
        glVertex3f(0.05, 0.05, 1.0)
        glVertex3f(-0.05, 0.05, 1.0)
        glVertex3f(-0.05, -0.05, 1.0)
        glVertex3f(0.05, -0.05, 1.0)
        glVertex3f(0.05, 0.05, 1.0)

        glEnd()

        glDisable(GL_LIGHTING)
    elif Vars.visionAxis == 'x':
        drawAxisX()
    else:
        drawAxisY()

"""
    ->Função drawAxisX:
        Desenha os eixos cartesianos no centro do espaco R^3 quando o eixo 'pra cima' selecionado é o X
    ->Parâmetros: vazio
    ->Retorno: vazio


"""
def drawAxisX():
    glDisable(GL_LIGHTING)

    # X-axis
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)

    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)

    glEnd()

    glBegin(GL_QUADS)

    glNormal3f(-1.0, 0.0, 0.0)
    glVertex3f(1.0, -0.05, -0.05)
    glVertex3f(1.0, -0.05, 0.05)
    glVertex3f(1.0, 0.05, 0.05)
    glVertex3f(1.0, 0.05, -0.05)

    glEnd()

    glBegin(GL_TRIANGLE_FAN)

    glVertex3f(1.2, 0.0, 0.0)
    glVertex3f(1.0, 0.05, 0.05)
    glVertex3f(1.0, -0.05, 0.05)
    glVertex3f(1.0, -0.05, -0.05)
    glVertex3f(1.0, 0.05, -0.05)
    glVertex3f(1.0, 0.05, 0.05)

    glEnd()

    # Y-axis
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)

    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)

    glEnd()

    glBegin(GL_QUADS)

    glNormal3f(0.0, -1.0, 0.0)
    glVertex3f(0.05, 1.0, 0.05)
    glVertex3f(-0.05, 1.0, 0.05)
    glVertex3f(-0.05, 1.0, -0.05)
    glVertex3f(0.05, 1.0, -0.05)

    glEnd()

    glBegin(GL_TRIANGLE_FAN)

    glVertex3f(0.0, 1.2, 0.0)
    glVertex3f(-0.05, 1.0, -0.05)
    glVertex3f(-0.05, 1.0, 0.05)
    glVertex3f(0.05, 1.0, 0.05)
    glVertex3f(0.05, 1.0, -0.05)
    glVertex3f(-0.05, 1.0, -0.05)

    glEnd()

    # Z-axis
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)

    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 1.0)

    glEnd()

    glBegin(GL_QUADS)

    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(-0.05, -0.05, 1.0)
    glVertex3f(-0.05, 0.05, 1.0)
    glVertex3f(0.05, 0.05, 1.0)
    glVertex3f(0.05, -0.05, 1.0)

    glEnd()

    glBegin(GL_TRIANGLE_FAN)

    glVertex3f(0.0, 0.0, 1.2)
    glVertex3f(0.05, 0.05, 1.0)
    glVertex3f(-0.05, 0.05, 1.0)
    glVertex3f(-0.05, -0.05, 1.0)
    glVertex3f(0.05, -0.05, 1.0)
    glVertex3f(0.05, 0.05, 1.0)

    glEnd()

    glDisable(GL_LIGHTING)

"""
    ->Função drawAxisY:
        Desenha os eixos cartesianos no centro do espaco R^3 quando o eixo 'pra cima' selecionado é o Y
    ->Parâmetros: vazio
    ->Retorno: vazio


"""
def drawAxisY():
    glDisable(GL_LIGHTING)

    # X-axis
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)

    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)

    glEnd()

    glBegin(GL_QUADS)

    glNormal3f(-1.0, 0.0, 0.0)
    glVertex3f(1.0, -0.05, -0.05)
    glVertex3f(1.0, -0.05, 0.05)
    glVertex3f(1.0, 0.05, 0.05)
    glVertex3f(1.0, 0.05, -0.05)

    glEnd()

    glBegin(GL_TRIANGLE_FAN)

    glVertex3f(1.2, 0.0, 0.0)
    glVertex3f(1.0, 0.05, 0.05)
    glVertex3f(1.0, -0.05, 0.05)
    glVertex3f(1.0, -0.05, -0.05)
    glVertex3f(1.0, 0.05, -0.05)
    glVertex3f(1.0, 0.05, 0.05)

    glEnd()

    # Y-axis
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)

    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)

    glEnd()

    glBegin(GL_QUADS)

    glNormal3f(0.0, -1.0, 0.0)
    glVertex3f(0.05, 1.0, 0.05)
    glVertex3f(-0.05, 1.0, 0.05)
    glVertex3f(-0.05, 1.0, -0.05)
    glVertex3f(0.05, 1.0, -0.05)

    glEnd()

    glBegin(GL_TRIANGLE_FAN)

    glVertex3f(0.0, 1.2, 0.0)
    glVertex3f(-0.05, 1.0, -0.05)
    glVertex3f(-0.05, 1.0, 0.05)
    glVertex3f(0.05, 1.0, 0.05)
    glVertex3f(0.05, 1.0, -0.05)
    glVertex3f(-0.05, 1.0, -0.05)

    glEnd()

    # Z-axis
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)

    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 1.0)

    glEnd()

    glBegin(GL_QUADS)

    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(-0.05, -0.05, 1.0)
    glVertex3f(-0.05, 0.05, 1.0)
    glVertex3f(0.05, 0.05, 1.0)
    glVertex3f(0.05, -0.05, 1.0)

    glEnd()

    glBegin(GL_TRIANGLE_FAN)

    glVertex3f(0.0, 0.0, 1.2)
    glVertex3f(0.05, 0.05, 1.0)
    glVertex3f(-0.05, 0.05, 1.0)
    glVertex3f(-0.05, -0.05, 1.0)
    glVertex3f(0.05, -0.05, 1.0)
    glVertex3f(0.05, 0.05, 1.0)

    glEnd()

    glDisable(GL_LIGHTING)

def drawGrid():

    espacoGrid = 1
    tamGrid = 10
    iniGrid = -tamGrid/(2/espacoGrid)

    glDisable(GL_LIGHTING)
    glColor3f(0.8,0.8,0.8)
    for i in range(tamGrid+1):

        if i == tamGrid/2:
            if Vars.visionAxis == 'z':
                glColor3f(0.0, 1.0, 0.0)
            elif Vars.visionAxis == 'x':
                glColor3f(1.0, 0.0, 0.0)
            else:
                glColor3f(0.0, 0.0, 1.0)
            glBegin(GL_LINES)

            glVertex3f(iniGrid + (i * espacoGrid), iniGrid, 0.0)
            glVertex3f(iniGrid + (i * espacoGrid), iniGrid + (tamGrid * espacoGrid), 0.0)

            glEnd()

            if Vars.visionAxis == 'z':
                glColor3f(1.0, 0.0, 0.0)
            elif Vars.visionAxis == 'x':
                glColor3f(0.0, 0.0, 1.0)
            else:
                glColor3d(0.0, 1.0, 0.0)
            glBegin(GL_LINES)

            glVertex3f(iniGrid, iniGrid + (i * espacoGrid), 0.0)
            glVertex3f(iniGrid + (tamGrid * espacoGrid), iniGrid + (i * espacoGrid), 0.0)

            glEnd()
            glColor3f(0.8, 0.8, 0.8)
        else:
            glBegin(GL_LINES)

            glVertex3f(iniGrid + (i * espacoGrid), iniGrid, 0.0)
            glVertex3f(iniGrid + (i * espacoGrid), iniGrid + (tamGrid * espacoGrid), 0.0)

            glEnd()

            glBegin(GL_LINES)

            glVertex3f(iniGrid, iniGrid + (i * espacoGrid), 0.0)
            glVertex3f(iniGrid + (tamGrid * espacoGrid), iniGrid + (i * espacoGrid), 0.0)

            glEnd()

    glEnable(GL_LIGHTING)