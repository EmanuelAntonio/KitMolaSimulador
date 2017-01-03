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

        eye = (Vars.camZoom*math.cos(Vars.theta)*math.sin(Vars.phi), Vars.camZoom*math.sin(Vars.theta)*math.sin(Vars.phi), Vars.camZoom*math.cos(Vars.phi))
        up = (0, 0, 1)
        center = (0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glViewport(0, 0, self.GetClientSize()[0], self.GetClientSize()[1])
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, self.GetClientSize()[0] / self.GetClientSize()[1], 0.1, 50)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(eye[0], eye[1], eye[2], center[0], center[1], center[2], up[0],up[1],up[2])
        #gluLookAt(2, 2, 2, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0)


        #drawSphere((0, 0, 0), 1, 32)
        drawCubeZero()

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

def drawCubeZero():

    #up
    glBegin(GL_QUADS)

    glNormal3f(0,0,1)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)

    glEnd()

    #down
    glBegin(GL_QUADS)

    glNormal3f(0, 0, -1)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)

    glEnd()

    #left
    glBegin(GL_QUADS)

    glNormal3f(-1, 0, 0)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5,- 0.5)
    glVertex3f(-0.5, 0.5, -0.5)

    glEnd()

    #right
    glBegin(GL_QUADS)

    glNormal3f(1, 0, 0)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)

    glEnd()

    #front
    glBegin(GL_QUADS)

    glNormal3f(0, -1, 0)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)

    glEnd()


    #botton
    glBegin(GL_QUADS)

    glNormal3f(0, 1, 0)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)

    glEnd()
