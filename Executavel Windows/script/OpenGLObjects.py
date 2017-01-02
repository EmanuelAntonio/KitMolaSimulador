from OpenGLCanvas import *

"""
    -> Classe CubeCanvas:
        Classe para desenhar em OpenGL futuramente será substituida.

"""

class CubeCanvas(MyCanvasBase):

    def InitGL(self):

        glClearColor(0.5, 0.5, 0.5, 0.0)
        # set viewing projection
        glMatrixMode(GL_PROJECTION)
        #glFrustum(-0.5, 0.5, -0.5, 0.5, 1.0, 3.0)

        # position viewer
        #glMatrixMode(GL_MODELVIEW)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

    def OnDraw(self):
        global tamJanela
        # clear color and depth buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        if tamJanela[1] != 0:
            gluPerspective(60.0, tamJanela[0] / tamJanela[1], 1.0, 5)
        else:
            print("janela ta com zero " + str(tamJanela))
        glMatrixMode(GL_MODELVIEW)
        gluLookAt(5, 5, 5, 0, 0, 0.0, 0.0, 0.0, 1.0)
        glLoadIdentity()

        drawSphere((0.2, 0, 0), 1, 32)

        if self.size is None:
            self.size = self.GetClientSize()
        w, h = self.size
        #print("largura e altura: " + str(w) + ", " + str(h))

        self.SwapBuffers()


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
        glVertex(raio * math.cos(theta * i) + centro[0], raio * math.sin(theta * i)+ centro[1], centro[2])
        glVertex(raio * math.cos(theta * (i+1))+ centro[0], raio * math.sin(theta * (i+1))+ centro[1], centro[2])

    glEnd()

    glEnable(GL_LIGHTING)