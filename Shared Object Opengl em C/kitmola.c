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

	void drawAxisY(){

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

	void drawAxisX(){

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
        float iniGrid = -tamGrid/(2/espacoGrid);

        glDisable(GL_LIGHTING);
        glColor3f(0.8,0.8,0.8);
        for(int i = 0; i <= tamGrid; i++){

            if (i == tamGrid/2){
                if (visionAxis == 'z'){
                    glColor3f(0.0, 1.0, 0.0);
                }else if (visionAxis == 'y'){
                    glColor3f(0.0, 0.0, 1.0);
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
                }else if (visionAxis == 'y'){
                    glColor3f(1.0, 0.0, 0.0);
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
    void drawCubeZero(bool selected){

        GLfloat object_difusa[] = {0.0,1.0,0.0};
        if(selected){

            object_difusa[0] = 1.0;
            object_difusa[1] = 0.3;
            object_difusa[2] = 0.3;
            if(visionOption == 0){

                glColor3f(0.0,0.0,1.0);

                glDisable(GL_LIGHTING);

                glBegin(GL_LINE_STRIP);

                    glVertex3f(0.501,0.501,0.501);
                    glVertex3f(-0.501,0.501,0.501);
                    glVertex3f(-0.501,-0.501,0.501);
                    glVertex3f(0.501,-0.501,0.501);
                    glVertex3f(0.501,0.501,0.501);
                    glVertex3f(0.501,0.501,-0.501);
                    glVertex3f(0.501,-0.501,-0.501);
                    glVertex3f(-0.501,-0.501,-0.501);
                    glVertex3f(-0.501,0.501,-0.501);
                    glVertex3f(0.501,0.501,-0.501);

                glEnd();
                glBegin(GL_LINES);

                    glVertex3f(-0.501,-0.501,-0.501);
                    glVertex3f(-0.501,-0.501,0.501);

                    glVertex3f(0.501,-0.501,0.501);
                    glVertex3f(0.501,-0.501,-0.501);

                    glVertex3f(-0.501,0.501,0.501);
                    glVertex3f(-0.501,0.501,-0.501);

                glEnd();

                glEnable(GL_LIGHTING);

            }


        }else{

            object_difusa[0] = 1.0;
            object_difusa[1] = 1.0;
            object_difusa[2] = 1.0;

        }
        glBegin(GL_QUADS);

            glMaterialfv(GL_FRONT, GL_DIFFUSE,object_difusa);
            //z+
            glNormal3f(0.0,0.0,1.0);
            glVertex3f(0.5,0.5,0.5);
            glVertex3f(-0.5,0.5,0.5);
            glVertex3f(-0.5,-0.5,0.5);
            glVertex3f(0.5,-0.5,0.5);

            //z-
            glNormal3f(0.0,0.0,1.0);
            glVertex3f(0.5,0.5,-0.5);
            glVertex3f(0.5,-0.5,-0.5);
            glVertex3f(-0.5,-0.5,-0.5);
            glVertex3f(-0.5,0.5,-0.5);

            //x+
            glNormal3f(1.0,0.0,0.0);
            glVertex3f(0.5,0.5,0.5);
            glVertex3f(0.5,-0.5,0.5);
            glVertex3f(0.5,-0.5,-0.5);
            glVertex3f(0.5,0.5,-0.5);

            //x-
            glNormal3f(-1.0,0.0,0.0);
            glVertex3f(-0.5,0.5,0.5);
            glVertex3f(-0.5,0.5,-0.5);
            glVertex3f(-0.5,-0.5,-0.5);
            glVertex3f(-0.5,-0.5,0.5);

            //y+
            glNormal3f(0.0,1.0,0.0);
            glVertex3f(0.5,0.5,0.5);
            glVertex3f(0.5,0.5,-0.5);
            glVertex3f(-0.5,0.5,-0.5);
            glVertex3f(-0.5,0.5,0.5);

            //y-
            glNormal3f(0.0,-1.0,0.0);
            glVertex3f(0.5,-0.5,0.5);
            glVertex3f(-0.5,-0.5,0.5);
            glVertex3f(-0.5,-0.5,-0.5);
            glVertex3f(0.5,-0.5,-0.5);

        glEnd();

    }
    void drawCube(float x, float y, float z, bool selected){

        glPushMatrix();

            if(visionAxis == 'z'){

                glTranslatef(x,y,z);

            }else if(visionAxis == 'x'){

                glTranslatef(y,z,x);

            }else{

                glTranslatef(x,z,y);

            }
            drawCubeZero(selected);

        glPopMatrix();

    }
    void drawCena(){

        Objeto3D *aux = l->get();
        while(aux != NULL){

            if(aux->getObjeto() == 0){

                drawCube(aux->getCentro()->x, aux->getCentro()->y, aux->getCentro()->z, aux->getSelecionado());

            }
            aux = aux->getProx();

        }

    }
    void save(char* arquivo){

        l->salvar(arquivo, visionAxis,visionOption);

    }
    void open(char* arquivo){

        cabecalhoKMP *c = l->abrir(arquivo);
        visionAxis = c->visionAxis;

    }
    int getVisionOption(){

        return visionOption;

    }
    void setVisionOption(int p){

        visionOption = p;

    }
    void setTamGrid(int p){

        tamGrid = p;

    }
    int getTamGrid(){

        return tamGrid;

    }
    double* getPonto3D(int x, int y){

        double modelview[16], projection[16];
        int viewport[4];
        float z = 1;
        double *ponto = new double[3];
        glGetDoublev( GL_PROJECTION_MATRIX, projection );
        glGetDoublev( GL_MODELVIEW_MATRIX, modelview );
        glGetIntegerv( GL_VIEWPORT, viewport );
        glReadPixels( x, viewport[3]-y, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT, &z );
        gluUnProject( x, viewport[3]-y, z, modelview, projection, viewport, &ponto[0], &ponto[1], &ponto[2]);

        if(visionAxis == 'x'){

            double X,Y,Z;
            X = ponto[0];
            Y = ponto[1];
            Z = ponto[2];

            ponto[0] = Z;
            ponto[1] = X;
            ponto[2] = Y;

        }else if(visionAxis == 'y'){

            double X,Y,Z;
            X = ponto[0];
            Y = ponto[1];
            Z = ponto[2];

            ponto[0] = X;
            ponto[1] = Z;
            ponto[2] = Y;

        }
        return ponto;

    }
    void getPonto3DFloat(int x, int y, float *ponto){

        double *p = getPonto3D(x,y);
        ponto[0] = p[0];
        ponto[1] = p[1];
        ponto[2] = p[2];

    }
    bool select(double *ponto){

        return l->select(ponto[0], ponto[1], ponto[2]);

    }
    void deSelectAll(){

        l->deSelectAll();

    }
    bool remover(double *ponto){

        return l->remover(ponto[0], ponto[1], ponto[2]);

    }
    void removeAll(){

        l->removeAll();

    }
    void clear(){

        l->clear();

    }
    bool getCenter(double *ponto, float *center){

        return l->getCenter(ponto[0],ponto[1],ponto[2], center);

    }
    void desfazer(){

        l->desfazerAcao();

    }
    void refazer(){

        l->refazerAcao();

    }
    int desfazerSize(){

        return l->desfazerSize();

    }
    int refazerSize(){

        return l->refazerSize();

    }
    void selectAll(){

        l->selectAll();

    }
}
