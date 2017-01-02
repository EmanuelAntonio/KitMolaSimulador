from OpenGLCanvas import *

"""
    -> Classe CubeCanvas:
        Classe para desenhar em OpenGLm futuramente será substituida.

"""

class CubeCanvas(MyCanvasBase):
    def InitGL(self):

        glClearColor(0.5, 0.5, 0.5, 0.0)
        # set viewing projection
        glMatrixMode(GL_PROJECTION)
        glFrustum(-0.5, 0.5, -0.5, 0.5, 1.0, 3.0)

        # position viewer
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(0.0, 0.0, -2.0)

        # position object
        glRotatef(self.y, 1.0, 0.0, 0.0)
        glRotatef(self.x, 0.0, 1.0, 0.0)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

    def OnDraw(self):
        # clear color and depth buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        drawSphere((0.2,0,0),1,32)
        """
        # draw six faces of a cube
        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, 1.0)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(0.5, -0.5, 0.5)

        glNormal3f(0.0, 0.0, -1.0)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5, 0.5, -0.5)
        glVertex3f(0.5, 0.5, -0.5)
        glVertex3f(0.5, -0.5, -0.5)

        glNormal3f(0.0, 1.0, 0.0)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(0.5, 0.5, -0.5)
        glVertex3f(-0.5, 0.5, -0.5)
        glVertex3f(-0.5, 0.5, 0.5)

        glNormal3f(0.0, -1.0, 0.0)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glVertex3f(-0.5, -0.5, 0.5)

        glNormal3f(1.0, 0.0, 0.0)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5, 0.5, -0.5)

        glNormal3f(-1.0, 0.0, 0.0)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, -0.5)
        glEnd()

        if self.size is None:
            self.size = self.GetClientSize()
        w, h = self.size
        w = max(w, 1.0)
        h = max(h, 1.0)
        xScale = 180.0 / w
        yScale = 180.0 / h
        glRotatef((self.y - self.lasty) * yScale, 1.0, 0.0, 0.0);
        glRotatef((self.x - self.lastx) * xScale, 0.0, 1.0, 0.0);
        """
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
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_LINES)

    for i in range(resolucao):
        glVertex(raio * math.cos(theta * i) + centro[0], raio * math.sin(theta * i)+ centro[1], centro[2])
        glVertex(raio * math.cos(theta * (i+1))+ centro[0], raio * math.sin(theta * (i+1))+ centro[1], centro[2])

    glEnd()