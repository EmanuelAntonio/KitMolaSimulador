#include "kitmola.h"

extern "C"{
    void init(){

        visionAxis = 'z';
        visionOption = 0;
        tamGrid = 16;
        resetMBRSelect();
        l = new ListaObjetos();

    }
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
        glColor3f(0.65,0.65,0.65);
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
                glColor3f(0.65, 0.65, 0.65);

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

                glPushMatrix();
                glLineWidth( 3.0 );
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
                 glLineWidth( 1.0 );
                glPopMatrix();
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
    void drawSphereZero(bool selected){

        GLfloat object_difusa[] = {1.0,1.0,1.0,0.5};
        GLfloat object_ambient[] = {0.5,0.5,0.5,1.0};
        if(selected){

            object_difusa[0] = 0.0;
            object_difusa[1] = 0.0;
            object_difusa[2] = 1.0;
            glPushMatrix();
                glLineWidth( 3.0 );
                glPolygonMode(GL_FRONT,GL_LINE);
                glMaterialfv(GL_FRONT,GL_AMBIENT, object_ambient);
                glMaterialfv(GL_FRONT, GL_DIFFUSE,object_difusa);
                GLUquadricObj *quadric;
                quadric = gluNewQuadric();
                gluSphere( quadric , SPHERE_RADIUS +0.015, 16, 16);
                gluDeleteQuadric(quadric);
                glPolygonMode(GL_FRONT, GL_FILL);
                glLineWidth( 1.0 );
            glPopMatrix();

            object_difusa[0] = 1.0;
            object_difusa[1] = 0.3;
            object_difusa[2] = 0.3;

        }
        glPushMatrix();
            glMaterialfv(GL_FRONT,GL_AMBIENT, object_ambient);
            glMaterialfv(GL_FRONT, GL_DIFFUSE,object_difusa);
            GLUquadricObj *quadric;
            quadric = gluNewQuadric();
            gluSphere( quadric , SPHERE_RADIUS , 64, 64);

            gluDeleteQuadric(quadric);
        glPopMatrix();

    }
    void drawSphere(float x, float y, float z, bool selected){

        glPushMatrix();

            if(visionAxis == 'z'){

                glTranslatef(x,y,z);

            }else if(visionAxis == 'x'){

                glTranslatef(y,z,x);

            }else{

                glTranslatef(x,z,y);

            }
            drawSphereZero(selected);

        glPopMatrix();

    }
    void drawCena(){

        Objeto3D *aux = l->get();
        while(aux != NULL){

            if(aux->getObjeto() == SPHERE){

                drawSphere(aux->getCentro()->x, aux->getCentro()->y, aux->getCentro()->z, aux->getSelecionado());

            }else if(aux->getObjeto() == BAR_SMALL || aux->getObjeto() == BAR_LARGE){

                drawBar(aux->getExtremidades()[0],aux->getExtremidades()[1]);

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

        return l->select(ponto[0], ponto[1], ponto[2], MBRSelect);

    }
    void deSelectAll(){

        l->deSelectAll();
        resetMBRSelect();

    }
    bool remover(double *ponto){

        return l->remover(ponto[0], ponto[1], ponto[2]);

    }
    void removeAll(){

        l->removeAll();
        resetMBRSelect();

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

        resetMBRSelect();
        l->selectAll(MBRSelect);

    }
    bool setFocusToSelect(float* centro){

        Ponto* aux = l->setFocusToSelect();
        if(aux != NULL){

            centro[0] = aux->x;
            centro[1] = aux->y;
            centro[2] = aux->z;
            delete aux;
            return true;

        }else{

            return false;

        }

    }
    void moveSelect(float x, float y, float z){

        l->moveSelect(x,y,z);
        MBRSelect[0].x += x;
        MBRSelect[0].y += y;
        MBRSelect[0].z += z;

        MBRSelect[1].x += x;
        MBRSelect[1].y += y;
        MBRSelect[1].z += z;

    }
    void resetMBRSelect(){

        MBRSelect[0].x = FLT_MAX;
        MBRSelect[0].y = FLT_MAX;
        MBRSelect[0].z = FLT_MAX;
        MBRSelect[1].x = -FLT_MAX;
        MBRSelect[1].y = -FLT_MAX;
        MBRSelect[1].z = -FLT_MAX;

    }
    void drawMoveAxis(){

        Ponto centro;
        centro.x = (MBRSelect[1].x + MBRSelect[0].x)/2.0;
        centro.y = (MBRSelect[1].y + MBRSelect[0].y)/2.0;
        centro.z = (MBRSelect[1].z + MBRSelect[0].z)/2.0;

        float dx = 0.3;
        float dy = 0.1;
        float dz = 0.1;

        ///MBR para X
        MBRMoveX[0].x = MBRSelect[1].x + dx;
        MBRMoveX[0].y = centro.y - dy ;
        MBRMoveX[0].z = centro.z - dz;

        MBRMoveX[1].x = MBRSelect[1].x + 1.2;
        MBRMoveX[1].y = centro.y + dy;
        MBRMoveX[1].z = centro.z + dz;

        MBRMoveX[2].x = MBRSelect[0].x - 1.2;
        MBRMoveX[2].y = centro.y - dy;
        MBRMoveX[2].z = centro.z - dz;

        MBRMoveX[3].x = MBRSelect[0].x - dx;
        MBRMoveX[3].y = centro.y + dy;
        MBRMoveX[3].z = centro.z + dz;

        ///MBR para Y
        dx = 0.1;
        dy = 0.3;

        MBRMoveY[0].x = centro.x - dx;
        MBRMoveY[0].y = MBRSelect[1].y + dy ;
        MBRMoveY[0].z = centro.z - dz;

        MBRMoveY[1].x = centro.x + dx;
        MBRMoveY[1].y = MBRSelect[1].y + 1.2;
        MBRMoveY[1].z = centro.z + dz;

        MBRMoveY[2].x = centro.x - dx;
        MBRMoveY[2].y = MBRSelect[0].y - 1.2;
        MBRMoveY[2].z = centro.z - dz;

        MBRMoveY[3].x = centro.x + dx;
        MBRMoveY[3].y = MBRSelect[0].y - dy;
        MBRMoveY[3].z = centro.z + dz;

        ///MBR para Z
        dy = 0.1;
        dz = 0.3;

        MBRMoveZ[0].x = centro.x - dx;
        MBRMoveZ[0].y = centro.y - dy ;
        MBRMoveZ[0].z = MBRSelect[1].z + dz;

        MBRMoveZ[1].x = centro.x + dx;
        MBRMoveZ[1].y = centro.y + dy;
        MBRMoveZ[1].z = MBRSelect[1].z + 1.2;


        MBRMoveZ[2].x = centro.x - dx;
        MBRMoveZ[2].y = centro.y - dy;
        MBRMoveZ[2].z = MBRSelect[0].z - 1.2;

        MBRMoveZ[3].x = centro.x + dx;
        MBRMoveZ[3].y = centro.y + dy;
        MBRMoveZ[3].z = MBRSelect[0].z - dz;

        glPushMatrix();
        if(visionAxis == 'z'){

            glTranslatef(centro.x, centro.y, centro.z);

        }
        else if(visionAxis == 'x'){

            glTranslatef(centro.y, centro.z, centro.x);
            glRotatef(90,1.0,0.0,0.0);
            glRotatef(90,0.0,0.0,1.0);

        }else if(visionAxis == 'y'){

            glTranslatef(centro.x, centro.z, centro.y);
            glRotatef(90,1.0,0.0,0.0);
            glRotatef(180,0.0,0.0,1.0);

        }
        drawMoveAxisZero();
        glPopMatrix();
    }
    void drawMoveAxisZero(){

        Ponto centro;
        centro.x = (MBRSelect[1].x - MBRSelect[0].x)/2.0;
        centro.y = (MBRSelect[1].y - MBRSelect[0].y)/2.0;
        centro.z = (MBRSelect[1].z - MBRSelect[0].z)/2.0;

        glDisable(GL_LIGHTING);

        ///X
        glPushMatrix();

            glTranslatef(centro.x,0,0);
            drawSetaMove();

            glTranslatef(-2*centro.x,0,0);
            glRotatef(180.0,0.0,1.0,0.0);
            drawSetaMove();

        glPopMatrix();

        ///Y
        glPushMatrix();

            glTranslatef(0,centro.y,0);
            glRotatef(90.0,0.0,0.0,1.0);
            drawSetaMove();

        glPopMatrix();

        glPushMatrix();

            glTranslatef(0,-centro.y,0);
            glRotatef(-90.0,0.0,0.0,1.0);
            drawSetaMove();

        glPopMatrix();

        ///Z
        glPushMatrix();

            glTranslatef(0,0,centro.z);
            glRotatef(-90.0,0.0,1.0,0.0);
            drawSetaMove();

        glPopMatrix();

        glPushMatrix();

            glTranslatef(0,0,-centro.z);
            glRotatef(90.0,0.0,1.0,0.0);
            drawSetaMove();

        glPopMatrix();

        glEnable(GL_LIGHTING);

    }
    void drawSetaMove(){

        float dx = 0.3;
        float dy = 0.1;
        float dz = 0.1;
        ///X
        glColor3f(0.69,0.933333,0.933333);
        glBegin(GL_TRIANGLE_FAN);

            glVertex3f(1.2, 0, 0);
            glVertex3f(dx, dy, dz);
            glVertex3f(dx,-dy, dz);
            glVertex3f(dx,-dy,-dz);
            glVertex3f(dx, dy,-dz);
            glVertex3f(dx, dy, dz);

        glEnd();

        glBegin(GL_QUADS);

            glVertex3f(dx, -dy, dz);
            glVertex3f(dx,dy, dz);
            glVertex3f(dx,dy,-dz);
            glVertex3f(dx, -dy,-dz);

        glEnd();

        glColor3f(1.0,0.0,0.0);
        glBegin(GL_LINES);

            glVertex3f(1.2, 0, 0);
            glVertex3f(dx, dy, dz);
            glVertex3f(1.2, 0, 0);
            glVertex3f(dx,-dy, dz);
            glVertex3f(1.2, 0, 0);
            glVertex3f(dx,-dy,-dz);
            glVertex3f(1.2, 0, 0);
            glVertex3f(dx, dy,-dz);
            glVertex3f(1.2, 0, 0);
            glVertex3f(dx, dy, dz);

            glVertex3f(dx, dy, dz);
            glVertex3f(dx, -dy, dz);

            glVertex3f(dx, -dy, dz);
            glVertex3f(dx, -dy, -dz);

            glVertex3f(dx, -dy, -dz);
            glVertex3f(dx, dy, -dz);

            glVertex3f(dx, dy, -dz);
            glVertex3f(dx, dy, dz);

        glEnd();

    }
    int selectMoveSeta(double *ponto){

        double x,y,z;
        x = ponto[0];
        y = ponto[1];
        z = ponto[2];

        if((x >= MBRMoveX[0].x) && (y >= MBRMoveX[0].y) && (z >= MBRMoveX[0].z)){

            if((x <= MBRMoveX[1].x) && (y <= MBRMoveX[1].y) && (z <= MBRMoveX[1].z)){

                return 0;

            }

        }else if((x >= MBRMoveX[2].x) && (y >= MBRMoveX[2].y) && (z >= MBRMoveX[2].z)){

            if((x <= MBRMoveX[3].x) && (y <= MBRMoveX[3].y) && (z <= MBRMoveX[3].z)){

                return 1;

            }

        }if((x >= MBRMoveY[0].x) && (y >= MBRMoveY[0].y) && (z >= MBRMoveY[0].z)){

            if((x <= MBRMoveY[1].x) && (y <= MBRMoveY[1].y) && (z <= MBRMoveY[1].z)){

                return 2;

            }

        }else if((x >= MBRMoveY[2].x) && (y >= MBRMoveY[2].y) && (z >= MBRMoveY[2].z)){

            if((x <= MBRMoveY[3].x) && (y <= MBRMoveY[3].y) && (z <= MBRMoveY[3].z)){

                return 3;

            }

        }if((x >= MBRMoveZ[0].x) && (y >= MBRMoveZ[0].y) && (z >= MBRMoveZ[0].z)){

            if((x <= MBRMoveZ[1].x) && (y <= MBRMoveZ[1].y) && (z <= MBRMoveZ[1].z)){

                return 4;

            }

        }else if((x >= MBRMoveZ[2].x) && (y >= MBRMoveZ[2].y) && (z >= MBRMoveZ[2].z)){

            if((x <= MBRMoveZ[3].x) && (y <= MBRMoveZ[3].y) && (z <= MBRMoveZ[3].z)){

                return 5;

            }

        }

        return -1;
    }
    void addSphere(float x, float y, float z){

        l->addSphere(x,y,z);

    }
    bool MBRSelectPonto(double *ponto){

        double x = ponto[0];
        double y = ponto[1];
        double z = ponto[2];

        if(MBRSelect[0].x <= x && MBRSelect[0].y <= y && MBRSelect[0].z <= z){

            if(MBRSelect[1].x >= x && MBRSelect[1].y >= y && MBRSelect[1].z >= z){

                return true;

            }

        }
        return false;
    }
    bool addBar(int tipoBar){

        return l->addBar(tipoBar);

    }
    void drawBar(int id1, int id2){

        Objeto3D *objId1 = l->getbyId(id1);
        Objeto3D *objId2 = l->getbyId(id2);
        float vetDir[3];
        vetDir[0] = objId2->getCentro()->x - objId1->getCentro()->x;
        vetDir[1] = objId2->getCentro()->y - objId1->getCentro()->y;
        vetDir[2] = objId2->getCentro()->z - objId1->getCentro()->z;

        float normaVetDir = sqrt(pow(vetDir[0],2) + pow(vetDir[1],2) + pow(vetDir[2],2));
        vetDir[0] /= normaVetDir;
        vetDir[1] /= normaVetDir;
        vetDir[2] /= normaVetDir;
        float angX = asin(vetDir[0]);
        float angY = asin(vetDir[1]);
        float angZ = asin(vetDir[2]);
        angX *= 180/M_PI;
        angY *= 180/M_PI;
        angZ *= 180/M_PI;
        float centro[3];
        centro[0] = (objId1->getCentro()->x + objId2->getCentro()->x)/2.0;
        centro[1] = (objId1->getCentro()->y + objId2->getCentro()->y)/2.0;
        centro[2] = (objId1->getCentro()->z + objId2->getCentro()->z)/2.0;
        glPushMatrix();

            glTranslatef(centro[0],centro[1],centro[2]);
            glRotatef(angX,1.0,0.0,0.0);
            glRotatef(angY,0.0,1.0,0.0);
            glRotatef(angZ,0.0,0.0,1.0);
            drawBarZero(normaVetDir);

        glPopMatrix();


    }
    void drawBarZero(float tamBar){

        float divTheta = 32;
        float divTam = 16;
        float dTheta = 2*M_PI/divTheta;
        float dTam = tamBar/divTam;

        GLfloat object_difusa[] = {1.0,1.0,1.0};

        glBegin(GL_QUADS);

            for(float i = -tamBar/2.0; i < tamBar/2.0; i = i + dTam){

                for(int j = 0; j < divTheta; j++){

                    glMaterialfv(GL_FRONT, GL_DIFFUSE,object_difusa);

                    glNormal3f(0,cos(j*dTheta),sin(j*dTheta));
                    glVertex3f(i,BAR_RADIUS*cos(j*dTheta),BAR_RADIUS*sin(j*dTheta));
                    glNormal3f(0,cos((j + 1)*dTheta),sin((j + 1)*dTheta));
                    glVertex3f(i,BAR_RADIUS*cos((j + 1)*dTheta),BAR_RADIUS*sin((j + 1)*dTheta));
                    glNormal3f(0,cos((j + 1)*dTheta),sin((j + 1)*dTheta));
                    glVertex3f(i + dTam,BAR_RADIUS*cos((j + 1)*dTheta),BAR_RADIUS*sin((j + 1)*dTheta));
                    glNormal3f(0,cos(j*dTheta),sin(j*dTheta));
                    glVertex3f(i + dTam,BAR_RADIUS*cos(j*dTheta),BAR_RADIUS*sin(j*dTheta));


                }

            }

        glEnd();

    }
}
