
from VarsAmbient import *


class Camera(object):

    def __init__(self,ref,parent):
        self.camZoom = 16  # Variável que armazena o raio da coordenada esférica correspondente ao zoom da câmera
        self.theta = math.pi / 4  # Variável que armazena em radianos o ângulo XY da câmera
        self.phi = math.pi / 3  # Variável que armazena em radianos o ângulo do eixo Z com o plano XY
        self.centro = (0,0,0) #Variável que armazena a posição do foco da cãmera
        self.orthoCenter = (0,0) #Tupla que armazena o ponto central da visão ortho
        self.orthoZoom = 5 #Variável que armazena a distancia do centro para visao ortho
        self.parent = parent
        if ref == 0:
            self.visionAxis = Vars.ASCII_Z
            self.visionOption = Vars.VISION_Z_PERSP
        elif ref == 1:
            self.visionAxis = Vars.ASCII_Z
            self.visionOption = Vars.VISION_Z_PERSP
        elif ref == 2:
            self.visionAxis = Vars.ASCII_Z
            self.visionOption = Vars.VISION_Z_PERSP
        else:
            self.visionAxis = Vars.ASCII_Z
            self.visionOption = Vars.VISION_Z_PERSP

    def OnDrawCamera(self,canvas):

        size = canvas.GetClientSize()
        if self.visionOption == 0:
            zoom = self.camZoom * c_float(Vars.KitLib.getEspacoGrid()).value
            eye = (zoom * math.cos(self.theta) * math.sin(self.phi) + self.centro[0],
                   zoom * math.sin(self.theta) * math.sin(self.phi) + self.centro[1], zoom * math.cos(self.phi) + self.centro[2])
            up = (-zoom * math.cos(self.theta) * math.cos(self.phi),
                  -zoom * math.sin(self.theta) * math.cos(self.phi), zoom * math.sin(self.phi))


            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            Vars.posLuz = (eye[0], eye[1], eye[2], 1.0)
            glLightfv(GL_LIGHT0, GL_POSITION, Vars.posLuz)

            glViewport(0, 0, size[0], size[1])
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            #gluPerspective(60.0, size[0] / size[1], 0.01, 500*c_float(Vars.KitLib.getEspacoGrid()).value)
            gluPerspective(60.0, size[0] / size[1], 0.3,500*c_float(Vars.KitLib.getEspacoGrid()).value)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            gluLookAt(eye[0], eye[1], eye[2], self.centro[0], self.centro[1], self.centro[2], up[0], up[1], up[2])

        #Definições de câmera ortho positiva
        elif self.visionOption == 5 or self.visionOption == 1 or self.visionOption == 4:
            zoom = self.orthoZoom * c_float(Vars.KitLib.getEspacoGrid()).value
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            Vars.posLuz = (0,0,500000, 1.0)
            glLightfv(GL_LIGHT0, GL_POSITION, Vars.posLuz)
            glViewport(0, 0, size[0], size[1])
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(-zoom*size[0]/size[1] + self.orthoCenter[1],
                    zoom*size[0]/size[1] + self.orthoCenter[1],
                    -zoom - self.orthoCenter[0], zoom - self.orthoCenter[0], -10000, 10000.0)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
        #Definições de câmera ortho negativa
        elif self.visionOption == 2 or self.visionOption == 3:
            zoom = self.orthoZoom * c_float(Vars.KitLib.getEspacoGrid()).value
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            Vars.posLuz = (0, 0, -500000, 1.0)
            glLightfv(GL_LIGHT0, GL_POSITION, Vars.posLuz)
            glViewport(0, 0, size[0], size[1])
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(zoom*size[0]/size[1] - self.orthoCenter[1],
                    -zoom*size[0]/size[1] - self.orthoCenter[1],
                    -zoom - self.orthoCenter[0], zoom - self.orthoCenter[0], 10000, -10000.0)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

    def atualizaCentroFocus(self):

        if self.visionOption == Vars.VISION_Z_PERSP:
            self.parent.parent.tabs.tabConfig.txtFocusX.SetValue(str(round(self.centro[0], 3)))
            self.parent.parent.tabs.tabConfig.txtFocusY.SetValue(str(round(self.centro[1], 3)))
            self.parent.parent.tabs.tabConfig.txtFocusZ.SetValue(str(round(self.centro[2], 3)))
        elif self.visionOption == Vars.VISION_X_POS:
            self.parent.parent.tabs.tabConfig.txtFocusX.SetValue("0")
            self.parent.parent.tabs.tabConfig.txtFocusY.SetValue(str(round(self.orthoCenter[1], 3)))
            self.parent.parent.tabs.tabConfig.txtFocusZ.SetValue(str(round(-self.orthoCenter[0], 3)))
        elif self.visionOption == Vars.VISION_X_NEG:
            self.parent.parent.tabs.tabConfig.txtFocusX.SetValue("0")
            self.parent.parent.tabs.tabConfig.txtFocusY.SetValue(str(round(-self.orthoCenter[1], 3)))
            self.parent.parent.tabs.tabConfig.txtFocusZ.SetValue(str(round(-self.orthoCenter[0], 3)))
        elif self.visionOption == Vars.VISION_Y_POS:
            self.parent.parent.tabs.tabConfig.txtFocusX.SetValue(str(round(-self.orthoCenter[1], 3)))
            self.parent.parent.tabs.tabConfig.txtFocusY.SetValue("0")
            self.parent.parent.tabs.tabConfig.txtFocusZ.SetValue(str(round(-self.orthoCenter[0], 3)))
        elif self.visionOption == Vars.VISION_Y_NEG:
            self.parent.parent.tabs.tabConfig.txtFocusX.SetValue(str(round(self.orthoCenter[1], 3)))
            self.parent.parent.tabs.tabConfig.txtFocusY.SetValue("0")
            self.parent.parent.tabs.tabConfig.txtFocusZ.SetValue(str(round(-self.orthoCenter[1], 3)))
        else:
            self.parent.parent.tabs.tabConfig.txtFocusX.SetValue(str(round(self.orthoCenter[1], 3)))
            self.parent.parent.tabs.tabConfig.txtFocusY.SetValue(str(round(-self.orthoCenter[0], 3)))
            self.parent.parent.tabs.tabConfig.txtFocusZ.SetValue("0")