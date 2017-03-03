#include "kitmola.h"

extern "C"{
    void init(){

        tamGrid = 16;
        resetMBRSelect();
        l = new ListaObjetos();
        espacoGrid = 1.0;
        meshQual = 1.0;
        wireframe = false;

    }
    void drawAxisZero(){

        glDisable(GL_LIGHTING);
        glLineWidth(0.5);
        float tamSeta = espacoGrid * 0.2;
        float dxyz = espacoGrid * 0.05;
        // X-axis
        glColor3f(1.0, 0.0, 0.0);
        glBegin(GL_LINES);

        glVertex3f(0.0, 0.0, 0.0);
        glVertex3f(espacoGrid, 0.0, 0.0);

        glEnd();

        glBegin(GL_QUADS);

        glNormal3f(-1.0, 0.0, 0.0);
        glVertex3f(espacoGrid, -dxyz, -dxyz);
        glVertex3f(espacoGrid, -dxyz, dxyz);
        glVertex3f(espacoGrid, dxyz, dxyz);
        glVertex3f(espacoGrid, dxyz, -dxyz);

        glEnd();

        glBegin(GL_TRIANGLE_FAN);

        glVertex3f(espacoGrid + tamSeta, 0.0, 0.0);
        glVertex3f(espacoGrid, dxyz, dxyz);
        glVertex3f(espacoGrid, -dxyz, dxyz);
        glVertex3f(espacoGrid, -dxyz, -dxyz);
        glVertex3f(espacoGrid, dxyz, -dxyz);
        glVertex3f(espacoGrid, dxyz, dxyz);

        glEnd();

        // Y-axis
        glColor3f(0.0, 1.0, 0.0);
        glBegin(GL_LINES);

        glVertex3f(0.0, 0.0, 0.0);
        glVertex3f(0.0, espacoGrid, 0.0);

        glEnd();

        glBegin(GL_QUADS);

        glNormal3f(0.0, -1.0, 0.0);
        glVertex3f(dxyz, espacoGrid, dxyz);
        glVertex3f(-dxyz, espacoGrid, dxyz);
        glVertex3f(-dxyz, espacoGrid, -dxyz);
        glVertex3f(dxyz, espacoGrid, -dxyz);

        glEnd();

        glBegin(GL_TRIANGLE_FAN);

        glVertex3f(0.0, espacoGrid + tamSeta, 0.0);
        glVertex3f(-dxyz, espacoGrid, -dxyz);
        glVertex3f(-dxyz, espacoGrid, dxyz);
        glVertex3f(dxyz, espacoGrid, dxyz);
        glVertex3f(dxyz, espacoGrid, -dxyz);
        glVertex3f(-dxyz, espacoGrid, -dxyz);

        glEnd();

        // Z-axis
        glColor3f(0.0, 0.0, 1.0);
        glBegin(GL_LINES);

        glVertex3f(0.0, 0.0, 0.0);
        glVertex3f(0.0, 0.0, espacoGrid);

        glEnd();

        glBegin(GL_QUADS);

        glNormal3f(0.0, 0.0, 1.0);
        glVertex3f(-dxyz, -dxyz, espacoGrid);
        glVertex3f(-dxyz, dxyz, espacoGrid);
        glVertex3f(dxyz, dxyz, espacoGrid);
        glVertex3f(dxyz, -dxyz, espacoGrid);

        glEnd();

        glBegin(GL_TRIANGLE_FAN);

        glVertex3f(0.0, 0.0, espacoGrid + tamSeta);
        glVertex3f(dxyz, dxyz, espacoGrid);
        glVertex3f(-dxyz, dxyz, espacoGrid);
        glVertex3f(-dxyz, -dxyz, espacoGrid);
        glVertex3f(dxyz, -dxyz, espacoGrid);
        glVertex3f(dxyz, dxyz, espacoGrid);

        glEnd();

        glEnable(GL_LIGHTING);

    }
	void drawAxis(char visionAxis){

        glPushMatrix();
            if(visionAxis == 'x'){

                glRotatef(-90.0,1.0,0.0,0.0);
                glRotatef(-90.0,0.0,0.0,1.0);


            }else if(visionAxis == 'y'){

                glRotatef(180.0,0.0,1.0,0.0);
                glRotatef(-90.0,1.0,0.0,0.0);
                glRotatef(180.0,0.0,0.0,1.0);

            }
            drawAxisZero();
        glPopMatrix();

	}

	void drawGrid(char visionAxis){

        float iniGrid = -tamGrid/(2/espacoGrid);

        glDisable(GL_LIGHTING);

        if(espacoGrid != 1.0){

            glPushMatrix();

                glColor3f(0.65,0.65,0.65);
                glBegin(GL_LINES);
                for(int i = 0; i <= tamGrid; i++){

                    if(i != tamGrid/2){

                        glVertex3f(iniGrid + (i * espacoGrid), iniGrid, 0.0);
                        glVertex3f(iniGrid + (i * espacoGrid), iniGrid + (tamGrid * espacoGrid), 0.0);

                        glVertex3f(iniGrid, iniGrid + (i * espacoGrid), 0.0);
                        glVertex3f(iniGrid + (tamGrid * espacoGrid), iniGrid + (i * espacoGrid), 0.0);

                    }

                }
                glEnd();

            glPopMatrix();
            if(espacoGrid == 18.0){

                glPushMatrix();

                    glColor3f(0.55,0.55,0.55);
                    glBegin(GL_LINES);
                    for(int i = 0; i <= tamGrid*2; i++){

                        if(i != tamGrid){

                            glVertex3f(iniGrid + (i * espacoGrid/2.0), iniGrid, 0.0);
                            glVertex3f(iniGrid + (i * espacoGrid/2.0), iniGrid + (tamGrid * espacoGrid), 0.0);

                            glVertex3f(iniGrid, iniGrid + (i * espacoGrid/2.0), 0.0);
                            glVertex3f(iniGrid + (tamGrid * espacoGrid), iniGrid + (i * espacoGrid/2.0), 0.0);

                        }

                    }
                    glEnd();

                glPopMatrix();

            }

        }

        int tGrid = tamGrid*espacoGrid;
        iniGrid = -tGrid/(2.0);

        glBegin(GL_LINES);
            if(espacoGrid > 1.0){

                glColor3f(0.45,0.45,0.45);

            }else{

                glColor3f(0.65,0.65,0.65);

            }
            for(int i = 0; i <= tGrid; i++){

                if (i == tGrid/2){
                    if (visionAxis == 'z'){
                        glColor3f(0.0, 1.0, 0.0);
                    }else if (visionAxis == 'y'){
                        glColor3f(0.0, 0.0, 1.0);
                    }
                    else{
                        glColor3f(0.0, 0.0, 1.0);
                    }

                    glVertex3f(iniGrid + (i), iniGrid, 0.0);
                    glVertex3f(iniGrid + (i), iniGrid + (tGrid), 0.0);

                    if (visionAxis == 'z'){
                        glColor3f(1.0, 0.0, 0.0);
                    }else if (visionAxis == 'y'){
                        glColor3f(1.0, 0.0, 0.0);
                    }else{
                        glColor3d(0.0, 1.0, 0.0);
                    }

                    glVertex3f(iniGrid, iniGrid + (i), 0.0);
                    glVertex3f(iniGrid + (tGrid), iniGrid + (i), 0.0);

                    if(espacoGrid > 1.0){

                        glColor3f(0.45,0.45,0.45);

                    }else{

                        glColor3f(0.65,0.65,0.65);

                    }

                }else{


                    glVertex3f(iniGrid + (i), iniGrid, 0.0);
                    glVertex3f(iniGrid + (i), iniGrid + (tGrid), 0.0);

                    glVertex3f(iniGrid, iniGrid + (i), 0.0);
                    glVertex3f(iniGrid + (tGrid), iniGrid + (i), 0.0);

                }

        }
        glEnd();
        glLineWidth(0.5);
        glEnable(GL_LIGHTING);
	}
    int tamanhoListaObjetos(){

        return l->size();

    }
    void drawSphereZero(bool selected){

        GLfloat object_difusa[] = {1.0,1.0,1.0,0.5};
        float resolucao = meshQual * 32;
        if(selected){

            object_difusa[0] = 1.0;
            object_difusa[1] = 0.3;
            object_difusa[2] = 0.3;

        }
        if(wireframe){

            if(!selected){

                object_difusa[0] = 0.0;
                object_difusa[1] = 0.0;
                object_difusa[2] = 1.0;

            }
            glPushMatrix();
                glPolygonMode(GL_FRONT,GL_LINE);
                glMaterialfv(GL_FRONT, GL_DIFFUSE,object_difusa);
                glMaterialfv(GL_FRONT,GL_AMBIENT, object_ambient);
                glMaterialfv(GL_FRONT, GL_SHININESS, object_brilho);
                glMaterialfv(GL_FRONT, GL_SPECULAR, object_especular);
                GLUquadricObj *quadric;
                quadric = gluNewQuadric();
                gluSphere( quadric , SPHERE_RADIUS + 0.015, 16, 16);
                gluDeleteQuadric(quadric);
                glPolygonMode(GL_FRONT, GL_FILL);
            glPopMatrix();

            object_difusa[0] = 1.0;
            object_difusa[1] = 0.3;
            object_difusa[2] = 0.3;

        }
        if(!wireframe){

            glPushMatrix();
                glMaterialfv(GL_FRONT, GL_DIFFUSE,object_difusa);
                glMaterialfv(GL_FRONT,GL_AMBIENT, object_ambient);
                glMaterialfv(GL_FRONT, GL_SHININESS, object_brilho);
                glMaterialfv(GL_FRONT, GL_SPECULAR, object_especular);
                GLUquadricObj *quadric;
                quadric = gluNewQuadric();
                gluSphere( quadric , SPHERE_RADIUS , resolucao, resolucao);
                gluDeleteQuadric(quadric);
            glPopMatrix();

        }

    }
    void drawSphere(float x, float y, float z, bool selected,char visionAxis){

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
    void drawCena(char visionAxis,int visionOption){

        Objeto3D *aux = l->get();
        while(aux != NULL){

            if(aux->getObjeto() == SPHERE){

                drawSphere(aux->getCentro()->x, aux->getCentro()->y, aux->getCentro()->z, aux->getSelecionado(),visionAxis);

            }else if(aux->getObjeto() == BAR_SMALL || aux->getObjeto() == BAR_LARGE){

                drawBar(aux->getExtremidades()[0],aux->getExtremidades()[1], aux->getSelecionado(),visionAxis);

            }else if(aux->getObjeto() == BASE){

                drawBase(aux->getCentro()->x, aux->getCentro()->y, aux->getCentro()->z, aux->getSelecionado(),visionAxis);

            }
            aux = aux->getProx();

        }

    }
    void save(char* arquivo){

        l->salvar(arquivo, tamGrid, meshQual, espacoGrid);

    }
    void open(char* arquivo){

        cabecalhoKMP *c = l->abrir(arquivo);
        meshQual = c->meshQual;
        tamGrid = c->tamGrid;
        espacoGrid = c->espacoGrid;
        delete c;

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

        return ponto;

    }
    void getPonto3DFloat(int x, int y, float *ponto){

        double *p = getPonto3D(x,y);
        ponto[0] = p[0];
        ponto[1] = p[1];
        ponto[2] = p[2];
        delete p;

    }
    int select(double *ponto, char visionAxis){

        if(visionAxis == 'z'){

            return l->select(ponto[0], ponto[1], ponto[2], MBRSelect);

        }else if(visionAxis == 'x'){

            return l->select(ponto[2], ponto[0], ponto[1], MBRSelect);

        }
        return l->select(ponto[0], ponto[2], ponto[1], MBRSelect);

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

        l->desfazerAcao(MBRSelect);

    }
    void refazer(){

        l->refazerAcao(MBRSelect);

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
    void drawMoveAxis(char visionAxis){

        Ponto centro;
        centro.x = (MBRSelect[1].x + MBRSelect[0].x)/2.0;
        centro.y = (MBRSelect[1].y + MBRSelect[0].y)/2.0;
        centro.z = (MBRSelect[1].z + MBRSelect[0].z)/2.0;

        float dx = 1.25;
        float dy = 0.5;
        float dz = 0.5;

        ///MBR para X
        MBRMoveX[0].x = MBRSelect[1].x + dx;
        MBRMoveX[0].y = centro.y - dy ;
        MBRMoveX[0].z = centro.z - dz;

        MBRMoveX[1].x = MBRSelect[1].x + 5.0;
        MBRMoveX[1].y = centro.y + dy;
        MBRMoveX[1].z = centro.z + dz;

        MBRMoveX[2].x = MBRSelect[0].x - 5.0;
        MBRMoveX[2].y = centro.y - dy;
        MBRMoveX[2].z = centro.z - dz;

        MBRMoveX[3].x = MBRSelect[0].x - dx;
        MBRMoveX[3].y = centro.y + dy;
        MBRMoveX[3].z = centro.z + dz;

        ///MBR para Y
        dx = 0.5;
        dy = 1.25;

        MBRMoveY[0].x = centro.x - dx;
        MBRMoveY[0].y = MBRSelect[1].y + dy ;
        MBRMoveY[0].z = centro.z - dz;

        MBRMoveY[1].x = centro.x + dx;
        MBRMoveY[1].y = MBRSelect[1].y + 5.0;
        MBRMoveY[1].z = centro.z + dz;

        MBRMoveY[2].x = centro.x - dx;
        MBRMoveY[2].y = MBRSelect[0].y - 5.0;
        MBRMoveY[2].z = centro.z - dz;

        MBRMoveY[3].x = centro.x + dx;
        MBRMoveY[3].y = MBRSelect[0].y - dy;
        MBRMoveY[3].z = centro.z + dz;

        ///MBR para Z
        dy = 0.5;
        dz = 1.25;

        MBRMoveZ[0].x = centro.x - dx;
        MBRMoveZ[0].y = centro.y - dy ;
        MBRMoveZ[0].z = MBRSelect[1].z + dz;

        MBRMoveZ[1].x = centro.x + dx;
        MBRMoveZ[1].y = centro.y + dy;
        MBRMoveZ[1].z = MBRSelect[1].z + 5.0;


        MBRMoveZ[2].x = centro.x - dx;
        MBRMoveZ[2].y = centro.y - dy;
        MBRMoveZ[2].z = MBRSelect[0].z - 5.0;

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

        float dx = 1.25;
        float dy = 0.5;
        float dz = 0.5;
        ///X
        glColor3f(0.69,0.933333,0.933333);
        glBegin(GL_TRIANGLE_FAN);

            glVertex3f(5.0, 0, 0);
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

            glVertex3f(5, 0, 0);
            glVertex3f(dx, dy, dz);
            glVertex3f(5, 0, 0);
            glVertex3f(dx,-dy, dz);
            glVertex3f(5, 0, 0);
            glVertex3f(dx,-dy,-dz);
            glVertex3f(5, 0, 0);
            glVertex3f(dx, dy,-dz);
            glVertex3f(5, 0, 0);
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
    int selectMoveSeta(double *ponto, char visionAxis){

        double x,y,z;
        if(visionAxis == 'z'){

            x = ponto[0];
            y = ponto[1];
            z = ponto[2];

        }else if(visionAxis == 'x'){

            x = ponto[2];
            y = ponto[0];
            z = ponto[1];

        }else{

            x = ponto[0];
            y = ponto[2];
            z = ponto[1];

        }

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
    void drawBar(int id1, int id2, bool selecionado,char visionAxis){

        float resolucao = meshQual * 32;

        Objeto3D *objId1 = l->getbyId(id1);
        Objeto3D *objId2 = l->getbyId(id2);
        Ponto p1,p2;
        if(visionAxis == 'z'){

            p1.x = objId1->getCentro()->x;
            p1.y = objId1->getCentro()->y;
            p1.z = objId1->getCentro()->z;
            p2.x = objId2->getCentro()->x;
            p2.y = objId2->getCentro()->y;
            p2.z = objId2->getCentro()->z;

        }else if(visionAxis == 'x'){

            p1.x = objId1->getCentro()->y;
            p1.y = objId1->getCentro()->z;
            p1.z = objId1->getCentro()->x;
            p2.x = objId2->getCentro()->y;
            p2.y = objId2->getCentro()->z;
            p2.z = objId2->getCentro()->x;


        }else{

            p1.x = objId1->getCentro()->x;
            p1.y = objId1->getCentro()->z;
            p1.z = objId1->getCentro()->y;
            p2.x = objId2->getCentro()->x;
            p2.y = objId2->getCentro()->z;
            p2.z = objId2->getCentro()->y;

        }
        GLUquadricObj *quadric=gluNewQuadric();
        gluQuadricNormals(quadric, GLU_SMOOTH);
        drawBarZero(&p1,&p2, BAR_RADIUS, resolucao, quadric, selecionado);
        gluDeleteQuadric(quadric);

    }
    void drawBarZero(Ponto *p1, Ponto *p2,float radius,int subdivisions,GLUquadricObj *quadric,bool selecionado){

        if(p1->z > p2->z){

            Ponto *aux = p1;
            p1 = p2;
            p2 = aux;

        }

        GLfloat object_difusa[] = {1.0,1.0,1.0,0.5};
        float vx = p2->x - p1->x;
        float vy = p2->y - p1->y;
        float vz = p2->z - p1->z;

        //handle the degenerate case of z1 == z2 with an approximation
        if(vz == 0)
            vz = .0001;

        float v = sqrt( vx*vx + vy*vy + vz*vz );
        float ax = 57.2957795*acos( vz/v );
        if ( vz < 0.0 )
            ax = -ax;
        float rx = -vy*vz;
        float ry = vx*vz;
        if(selecionado){

            object_difusa[0] = 1.0;
            object_difusa[1] = 0.3;
            object_difusa[2] = 0.3;

        }
        if(wireframe){
            if(!selecionado){

                object_difusa[0] = 0.0;
                object_difusa[1] = 0.0;
                object_difusa[2] = 1.0;

            }
            glPushMatrix();

                glPolygonMode(GL_FRONT,GL_LINE);
                glMaterialfv(GL_FRONT, GL_DIFFUSE,object_difusa);
                glMaterialfv(GL_FRONT,GL_AMBIENT, object_ambient);
                glMaterialfv(GL_FRONT, GL_SHININESS, object_brilho);
                glMaterialfv(GL_FRONT, GL_SPECULAR, object_especular);
                //draw the cylinder body
                glTranslatef( p1->x,p1->y,p1->z );
                glRotatef(ax, rx, ry, 0.0);
                gluQuadricOrientation(quadric,GLU_OUTSIDE);
                gluCylinder(quadric, radius, radius, v, 16, 1);

                glPolygonMode(GL_FRONT,GL_FILL);

            glPopMatrix();
            object_difusa[0] = 1.0;
            object_difusa[1] = 0.3;
            object_difusa[2] = 0.3;

        }
        if(!wireframe){
            glPushMatrix();

                glMaterialfv(GL_FRONT, GL_DIFFUSE,object_difusa);
                glMaterialfv(GL_FRONT,GL_AMBIENT, object_ambient);
                glMaterialfv(GL_FRONT, GL_SHININESS, object_brilho);
                glMaterialfv(GL_FRONT, GL_SPECULAR, object_especular);
                //draw the cylinder body
                glTranslatef( p1->x,p1->y,p1->z );
                glRotatef(ax, rx, ry, 0.0);
                gluQuadricOrientation(quadric,GLU_OUTSIDE);
                gluCylinder(quadric, radius, radius, v, subdivisions, 1);

                //draw the first cap
                gluQuadricOrientation(quadric,GLU_INSIDE);
                gluDisk( quadric, 0.0, radius, subdivisions, 1);
                glTranslatef( 0,0,v );

                //draw the second cap
                gluQuadricOrientation(quadric,GLU_OUTSIDE);
                gluDisk( quadric, 0.0, radius, subdivisions, 1);

            glPopMatrix();
        }


    }
    void setEspacoGrid(float tam){

        espacoGrid = tam;

    }
    float getEspacoGrid(){

        return espacoGrid;

    }
    float distObjsSelect(){

        return l->distObjsSelect();

    }
    void setWireframe(bool w){

        wireframe = w;

    }
    bool getWireframe(){

        return wireframe;

    }
    void setMeshQual(float p){

        meshQual = p;

    }
    float getMeshQual(){

        return meshQual;

    }
    Objeto *getObjById(int id){

        Objeto3D *aux = l->getbyId(id);
        Objeto *obj = new Objeto;
        obj->obj = aux->getObjeto();
        obj->id = aux->getId();
        obj->centro = *aux->getCentro();
        obj->MBR[0] = aux->getMBR()[0];
        obj->MBR[1] = aux->getMBR()[1];
        obj->idExtremidades[0] = aux->getExtremidades()[0];
        obj->idExtremidades[1] = aux->getExtremidades()[1];
        return obj;

    }
    void moveObj(int id, float x, float y, float z){

        if(l->moveObj(id,x,y,z)){

            MBRSelect[0].x += x;
            MBRSelect[0].y += y;
            MBRSelect[0].z += z;
            MBRSelect[1].x += x;
            MBRSelect[1].y += y;
            MBRSelect[1].z += z;

        }

    }
    void moveObjSelect(float x, float y, float z){

        if(l->getNumSelect() > 0){

            Ponto vetDeslocamento;
            vetDeslocamento.x = x - (MBRSelect[1].x + MBRSelect[0].x)/2.0;
            vetDeslocamento.y = y - (MBRSelect[1].y + MBRSelect[0].y)/2.0;
            vetDeslocamento.z = z - (MBRSelect[1].z + MBRSelect[0].z)/2.0;
            if(l->moveSelect(vetDeslocamento.x, vetDeslocamento.y, vetDeslocamento.z)){

                MBRSelect[0].x += vetDeslocamento.x;
                MBRSelect[0].y += vetDeslocamento.y;
                MBRSelect[0].z += vetDeslocamento.z;
                MBRSelect[1].x += vetDeslocamento.x;
                MBRSelect[1].y += vetDeslocamento.y;
                MBRSelect[1].z += vetDeslocamento.z;

            }

        }

    }
    bool duplicaSelect(){

        return l->duplicaSelect();

    }
    void drawBase(float x, float y, float z, bool selected, char visionAxis){

        float resolucao = 64*meshQual;

        Ponto p1,p2;
        if(visionAxis == 'z'){

            p2.x = x;
            p2.y = y;
            p2.z = z;
            p1.x = x;
            p1.y = y;
            p1.z = z - SPHERE_RADIUS/2;

        }else if(visionAxis == 'x'){

            p2.x = y;
            p2.y = z;
            p2.z = x;
            p1.x = y;
            p1.y = z - SPHERE_RADIUS/2;
            p1.z = x;

        }else{

            p2.x = x;
            p2.y = z;
            p2.z = y;
            p1.x = x;
            p1.y = z - SPHERE_RADIUS/2;
            p1.z = y;

        }
        GLdouble eq[] = {0.0,0.0,1.0,z};
        if(visionAxis == 'y' || visionAxis == 'x'){

            eq[1] = 1.0;
            eq[2] = 0.0;

        }
        glClipPlane(GL_CLIP_PLANE0,eq);
        glEnable(GL_CLIP_PLANE0);
        drawSphere(x,y,z,selected,visionAxis);
        glDisable(GL_CLIP_PLANE0);

        GLUquadricObj *quadric=gluNewQuadric();
        gluQuadricOrientation(quadric,GLU_INSIDE);
        gluQuadricNormals(quadric, GLU_SMOOTH);
        drawBarZero(&p1,&p2,BASE_RADIUS,resolucao,quadric,selected);
        gluDeleteQuadric(quadric);

    }
    void addBase(float x, float y, float z){

        l->addBase(x,y,z);

    }
    Ponto* getCentroMBRSelect(){

        Ponto *c = new Ponto;
        c->x = (MBRSelect[1].x + MBRSelect[0].x)/2.0;
        c->y = (MBRSelect[1].y + MBRSelect[0].y)/2.0;
        c->z = (MBRSelect[1].z + MBRSelect[0].z)/2.0;
        return c;

    }
}
