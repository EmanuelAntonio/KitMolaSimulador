#include "kitmola.h"

extern "C"{

	void drawAxis(){

		if(visionAxis == 'z'){

			glDisable(GL_LIGHTING);

			// X-axis
			glColor3f(1.0, 0.0, 0.0);
			glBegin(GL_LINES);

			glVertex3f(0.0, 0.0, 0.0);
			glVertex3f(1.0, 0.0, 0.0);

			glEnd();

			glBegin(GL_QUADS);

			glNormal3f(-1.0, 0.0, 0.0);
			glVertex3f(1.0, -0.05, -0.05);
			glVertex3f(1.0, -0.05, 0.05);
			glVertex3f(1.0, 0.05, 0.05);
			glVertex3f(1.0, 0.05, -0.05);

			glEnd();

			glBegin(GL_TRIANGLE_FAN);

			glVertex3f(1.2, 0.0, 0.0);
			glVertex3f(1.0, 0.05, 0.05);
			glVertex3f(1.0, -0.05, 0.05);
			glVertex3f(1.0, -0.05, -0.05);
			glVertex3f(1.0, 0.05, -0.05);
			glVertex3f(1.0, 0.05, 0.05);

			glEnd();

			// Y-axis
			glColor3f(0.0, 1.0, 0.0);
			glBegin(GL_LINES);

			glVertex3f(0.0, 0.0, 0.0);
			glVertex3f(0.0, 1.0, 0.0);

			glEnd();

			glBegin(GL_QUADS);

			glNormal3f(0.0, -1.0, 0.0);
			glVertex3f(0.05, 1.0, 0.05);
			glVertex3f(-0.05, 1.0, 0.05);
			glVertex3f(-0.05, 1.0, -0.05);
			glVertex3f(0.05, 1.0, -0.05);

			glEnd();

			glBegin(GL_TRIANGLE_FAN);

			glVertex3f(0.0, 1.2, 0.0);
			glVertex3f(-0.05, 1.0, -0.05);
			glVertex3f(-0.05, 1.0, 0.05);
			glVertex3f(0.05, 1.0, 0.05);
			glVertex3f(0.05, 1.0, -0.05);
			glVertex3f(-0.05, 1.0, -0.05);

			glEnd();

			// Z-axis
			glColor3f(0.0, 0.0, 1.0);
			glBegin(GL_LINES);

			glVertex3f(0.0, 0.0, 0.0);
			glVertex3f(0.0, 0.0, 1.0);

			glEnd();

			glBegin(GL_QUADS);

			glNormal3f(0.0, 0.0, 1.0);
			glVertex3f(-0.05, -0.05, 1.0);
			glVertex3f(-0.05, 0.05, 1.0);
			glVertex3f(0.05, 0.05, 1.0);
			glVertex3f(0.05, -0.05, 1.0);

			glEnd();

			glBegin(GL_TRIANGLE_FAN);

			glVertex3f(0.0, 0.0, 1.2);
			glVertex3f(0.05, 0.05, 1.0);
			glVertex3f(-0.05, 0.05, 1.0);
			glVertex3f(-0.05, -0.05, 1.0);
			glVertex3f(0.05, -0.05, 1.0);
			glVertex3f(0.05, 0.05, 1.0);

			glEnd();

			glEnable(GL_LIGHTING);

		}else if(visionAxis == 'x'){

			drawAxisX();

		}else{

			drawAxisY();

		}

	}

	void drawAxisX(){

		glDisable(GL_LIGHTING);

		// X-axis
		glColor3f(1.0, 0.0, 0.0);
		glBegin(GL_LINES);

		glVertex3f(0.0, 0.0, 0.0);
		glVertex3f(1.0, 0.0, 0.0);

		glEnd();

		glBegin(GL_QUADS);

		glNormal3f(-1.0, 0.0, 0.0);
		glVertex3f(1.0, -0.05, -0.05);
		glVertex3f(1.0, -0.05, 0.05);
		glVertex3f(1.0, 0.05, 0.05);
		glVertex3f(1.0, 0.05, -0.05);

		glEnd();

		glBegin(GL_TRIANGLE_FAN);

		glVertex3f(1.2, 0.0, 0.0);
		glVertex3f(1.0, 0.05, 0.05);
		glVertex3f(1.0, -0.05, 0.05);
		glVertex3f(1.0, -0.05, -0.05);
		glVertex3f(1.0, 0.05, -0.05);
		glVertex3f(1.0, 0.05, 0.05);

		glEnd();

		// Y-axis
		glColor3f(0.0, 0.0, 1.0);
		glBegin(GL_LINES);

		glVertex3f(0.0, 0.0, 0.0);
		glVertex3f(0.0, 1.0, 0.0);

		glEnd();

		glBegin(GL_QUADS);

		glNormal3f(0.0, -1.0, 0.0);
		glVertex3f(0.05, 1.0, 0.05);
		glVertex3f(-0.05, 1.0, 0.05);
		glVertex3f(-0.05, 1.0, -0.05);
		glVertex3f(0.05, 1.0, -0.05);

		glEnd();

		glBegin(GL_TRIANGLE_FAN);

		glVertex3f(0.0, 1.2, 0.0);
		glVertex3f(-0.05, 1.0, -0.05);
		glVertex3f(-0.05, 1.0, 0.05);
		glVertex3f(0.05, 1.0, 0.05);
		glVertex3f(0.05, 1.0, -0.05);
		glVertex3f(-0.05, 1.0, -0.05);

		glEnd();

		// Z-axis
		glColor3f(0.0, 1.0, 0.0);
		glBegin(GL_LINES);

		glVertex3f(0.0, 0.0, 0.0);
		glVertex3f(0.0, 0.0, 1.0);

		glEnd();

		glBegin(GL_QUADS);

		glNormal3f(0.0, 0.0, 1.0);
		glVertex3f(-0.05, -0.05, 1.0);
		glVertex3f(-0.05, 0.05, 1.0);
		glVertex3f(0.05, 0.05, 1.0);
		glVertex3f(0.05, -0.05, 1.0);

		glEnd();

		glBegin(GL_TRIANGLE_FAN);

		glVertex3f(0.0, 0.0, 1.2);
		glVertex3f(0.05, 0.05, 1.0);
		glVertex3f(-0.05, 0.05, 1.0);
		glVertex3f(-0.05, -0.05, 1.0);
		glVertex3f(0.05, -0.05, 1.0);
		glVertex3f(0.05, 0.05, 1.0);

		glEnd();

		glEnable(GL_LIGHTING);


	}

	void drawAxisY(){

		glDisable(GL_LIGHTING);

		// X-axis
		glColor3f(0.0, 1.0, 0.0);
		glBegin(GL_LINES);

		glVertex3f(0.0, 0.0, 0.0);
		glVertex3f(1.0, 0.0, 0.0);

		glEnd();

		glBegin(GL_QUADS);

		glNormal3f(-1.0, 0.0, 0.0);
		glVertex3f(1.0, -0.05, -0.05);
		glVertex3f(1.0, -0.05, 0.05);
		glVertex3f(1.0, 0.05, 0.05);
		glVertex3f(1.0, 0.05, -0.05);

		glEnd();

		glBegin(GL_TRIANGLE_FAN);

		glVertex3f(1.2, 0.0, 0.0);
		glVertex3f(1.0, 0.05, 0.05);
		glVertex3f(1.0, -0.05, 0.05);
		glVertex3f(1.0, -0.05, -0.05);
		glVertex3f(1.0, 0.05, -0.05);
		glVertex3f(1.0, 0.05, 0.05);

		glEnd();

		// Y-axis
		glColor3f(0.0, 0.0, 1.0);
		glBegin(GL_LINES);

		glVertex3f(0.0, 0.0, 0.0);
		glVertex3f(0.0, 1.0, 0.0);

		glEnd();

		glBegin(GL_QUADS);

		glNormal3f(0.0, -1.0, 0.0);
		glVertex3f(0.05, 1.0, 0.05);
		glVertex3f(-0.05, 1.0, 0.05);
		glVertex3f(-0.05, 1.0, -0.05);
		glVertex3f(0.05, 1.0, -0.05);

		glEnd();

		glBegin(GL_TRIANGLE_FAN);

		glVertex3f(0.0, 1.2, 0.0);
		glVertex3f(-0.05, 1.0, -0.05);
		glVertex3f(-0.05, 1.0, 0.05);
		glVertex3f(0.05, 1.0, 0.05);
		glVertex3f(0.05, 1.0, -0.05);
		glVertex3f(-0.05, 1.0, -0.05);

		glEnd();

		// Z-axis
		glColor3f(1.0, 0.0, 0.0);
		glBegin(GL_LINES);

		glVertex3f(0.0, 0.0, 0.0);
		glVertex3f(0.0, 0.0, 1.0);

		glEnd();

		glBegin(GL_QUADS);

		glNormal3f(0.0, 0.0, 1.0);
		glVertex3f(-0.05, -0.05, 1.0);
		glVertex3f(-0.05, 0.05, 1.0);
		glVertex3f(0.05, 0.05, 1.0);
		glVertex3f(0.05, -0.05, 1.0);

		glEnd();

		glBegin(GL_TRIANGLE_FAN);

		glVertex3f(0.0, 0.0, 1.2);
		glVertex3f(0.05, 0.05, 1.0);
		glVertex3f(-0.05, 0.05, 1.0);
		glVertex3f(-0.05, -0.05, 1.0);
		glVertex3f(0.05, -0.05, 1.0);
		glVertex3f(0.05, 0.05, 1.0);

		glEnd();

		glEnable(GL_LIGHTING);

	}

	void drawGrid(){

        float espacoGrid = 1;
        int tamGrid = 10;
        float iniGrid = -tamGrid/(2/espacoGrid);

        glDisable(GL_LIGHTING);
        glColor3f(0.8,0.8,0.8);
        for(int i = 0; i <= tamGrid; i++){

            if (i == tamGrid/2){
                if (visionAxis == 'z'){
                    glColor3f(0.0, 1.0, 0.0);
                }else if (visionAxis == 'x'){
                    glColor3f(1.0, 0.0, 0.0);
                }
                else{
                    glColor3f(0.0, 0.0, 1.0);
                }

                glBegin(GL_LINES);

                glVertex3f(iniGrid + (i * espacoGrid), iniGrid, 0.0);
                glVertex3f(iniGrid + (i * espacoGrid), iniGrid + (tamGrid * espacoGrid), 0.0);

                glEnd();

                if (visionAxis == 'z'){
                    glColor3f(1.0, 0.0, 0.0);
                }else if (visionAxis == 'x'){
                    glColor3f(0.0, 0.0, 1.0);
                }else{
                    glColor3d(0.0, 1.0, 0.0);
                }
                glBegin(GL_LINES);

                glVertex3f(iniGrid, iniGrid + (i * espacoGrid), 0.0);
                glVertex3f(iniGrid + (tamGrid * espacoGrid), iniGrid + (i * espacoGrid), 0.0);

                glEnd();
                glColor3f(0.8, 0.8, 0.8);

            }else{
                glBegin(GL_LINES);

                glVertex3f(iniGrid + (i * espacoGrid), iniGrid, 0.0);
                glVertex3f(iniGrid + (i * espacoGrid), iniGrid + (tamGrid * espacoGrid), 0.0);

                glEnd();

                glBegin(GL_LINES);

                glVertex3f(iniGrid, iniGrid + (i * espacoGrid), 0.0);
                glVertex3f(iniGrid + (tamGrid * espacoGrid), iniGrid + (i * espacoGrid), 0.0);

                glEnd();
            }

        }
        glEnable(GL_LIGHTING);

	}
    void setVisionAxis(char c){

        visionAxis = c;

    }
    char getVisionAxis(){

        return visionAxis;

    }
    void addCubo(float x, float y, float z){

        l->addCubo(x,y,z);

    }
    int tamanhoListaObjetos(){

        return l->size();

    }
    void drawCubeZero(){

        glBegin(GL_QUADS);

            glNormal3f(0.0,0.0,1.0);
            glVertex3f(0.5,0.5,0.5);
            glVertex3f(-0.5,0.5,0.5);
            glVertex3f(-0.5,-0.5,0.5);
            glVertex3f(0.5,-0.5,0.5);

            glNormal3f(0.0,0.0,-1.0);
            glVertex3f(0.5,0.5,-0.5);
            glVertex3f(0.5,-0.5,-0.5);
            glVertex3f(-0.5,-0.5,-0.5);
            glVertex3f(-0.5,0.5,-0.5);

            glNormal3f(1.0,0.0,0.0);
            glVertex3f(0.5,0.5,0.5);
            glVertex3f(0.5,-0.5,0.5);
            glVertex3f(0.5,-0.5,-0.5);
            glVertex3f(0.5,0.5,-0.5);

            glNormal3f(-1.0,0.0,0.0);
            glVertex3f(-0.5,0.5,0.5);
            glVertex3f(-0.5,0.5,-0.5);
            glVertex3f(-0.5,-0.5,-0.5);
            glVertex3f(-0.5,-0.5,0.5);

            glNormal3f(0.0,1.0,0.0);
            glVertex3f(0.5,0.5,0.5);
            glVertex3f(0.5,0.5,-0.5);
            glVertex3f(-0.5,0.5,-0.5);
            glVertex3f(-0.5,0.5,0.5);

            glNormal3f(0.0,-1.0,0.0);
            glVertex3f(0.5,-0.5,0.5);
            glVertex3f(-0.5,-0.5,0.5);
            glVertex3f(-0.5,-0.5,-0.5);
            glVertex3f(0.5,-0.5,-0.5);

        glEnd();

    }
    void drawCube(float x, float y, float z){

        glPushMatrix();

            if(visionAxis == 'z'){

                glTranslatef(x,y,z);

            }else if(visionAxis == 'x'){

                glTranslatef(z,y,x);

            }else{

                glTranslatef(x,z,y);

            }
            drawCubeZero();

        glPopMatrix();

    }
    void drawCena(){

        Objeto3D *aux = l->get();
        while(aux != NULL){

            if(aux->getObjeto() == 0){

                drawCube(aux->getCentro()->x,aux->getCentro()->y,aux->getCentro()->z);

            }
            aux = aux->getProx();

        }

    }

}
