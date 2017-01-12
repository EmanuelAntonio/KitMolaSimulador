# -*- coding: UTF-8 -*-

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