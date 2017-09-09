#include "kitlib.h"

extern "C"{

    using namespace ManipularVetor;
    void init(){

        tamGrid = 8;
        resetMBRSelect();
        listObj = new ListaObjetos();
        espacoGrid = 9.0;
        meshQual = 1.0;
        wireframe = false;
        MBRAtivo = true;
        initBuffer = false;
        idRotCenter = -1; ///Nenhum objeto selecionado

    }
    void initGL(float r, float g, float b, bool dark){

        GLfloat object_difusa[] = {0.5,0.5,0.5,1.0};
        GLfloat posLuz[] = {0.0,0.0,0.0,1.0};
        glClearColor(r, g, b, 1.0);

        glEnable(GL_DEPTH_TEST);
        glEnable(GL_CULL_FACE);
        glEnable(GL_NORMALIZE);
        glEnable(GL_LIGHTING);

        glEnable(GL_MULTISAMPLE);
        glShadeModel(GL_SMOOTH);

        /*glEnable( GL_LINE_SMOOTH );
        glEnable(GL_BLEND);
        glEnable( GL_POLYGON_SMOOTH );
        glHint( GL_LINE_SMOOTH_HINT, GL_NICEST );
        glHint( GL_POLYGON_SMOOTH_HINT, GL_NICEST );
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

        glDisable(GL_BLEND);*/

        glLightfv(GL_LIGHT0, GL_AMBIENT, object_ambient);
        glLightfv(GL_LIGHT0, GL_DIFFUSE, object_difusa);
        glLightfv(GL_LIGHT0, GL_POSITION, posLuz);
        glEnable(GL_LIGHT0);

        if(!initBuffer){

            glewInit();
            Sphere::initBuffer();
            Bar::initBuffer();

        }


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

        glEnable(GL_BLEND);
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

                glColor3f(0.25,0.25,0.25);

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

                        glColor3f(0.25,0.25,0.25);

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
        glDisable(GL_BLEND);
	}
    int tamanhoListaObjetos(){

        return listObj->size();

    }
    void drawCena(char visionAxis,int visionOption){

        Objeto3D *aux = listObj->get();
        while(aux != NULL){

            if(aux->getObjeto() == SPHERE){

                aux->draw(meshQual,wireframe,visionAxis,visionOption);

            }else if(aux->getObjeto() == BAR_SMALL || aux->getObjeto() == BAR_LARGE){

                aux->draw(meshQual,wireframe,visionAxis,visionOption,
                          listObj->getbyId(aux->getExtremidades()[0]),
                          listObj->getbyId(aux->getExtremidades()[1]));

            }else if(aux->getObjeto() == BASE){

                aux->draw(meshQual, wireframe, visionAxis, visionOption);
                if(((Base*)aux)->getSubObjeto() == BASE_BLOQUEADA_X || ((Base*)aux)->getSubObjeto() == BASE_BLOQUEADA_XY){

                    LigRigida a;
                    Objeto3D sph0;
                    Objeto3D sph1;
                    sph0.setCentro(aux->getCentro()->x,aux->getCentro()->y,aux->getCentro()->z + 9.0);
                    sph1.setCentro(aux->getCentro()->x + 9.0,aux->getCentro()->y,aux->getCentro()->z);
                    a.draw(meshQual,wireframe,visionAxis, visionOption, aux, &sph1, &sph0);
                    sph1.setCentro(aux->getCentro()->x - 9.0,aux->getCentro()->y,aux->getCentro()->z);
                    a.draw(meshQual,wireframe,visionAxis, visionOption, aux, &sph1, &sph0);

                }
                if(((Base*)aux)->getSubObjeto() == BASE_BLOQUEADA_Y || ((Base*)aux)->getSubObjeto() == BASE_BLOQUEADA_XY){

                    LigRigida a;
                    Objeto3D sph0;
                    Objeto3D sph1;
                    sph0.setCentro(aux->getCentro()->x,aux->getCentro()->y,aux->getCentro()->z + 9.0);
                    sph1.setCentro(aux->getCentro()->x, aux->getCentro()->y + 9.0, aux->getCentro()->z);
                    a.draw(meshQual,wireframe,visionAxis, visionOption, aux, &sph0, &sph1);
                    sph1.setCentro(aux->getCentro()->x,aux->getCentro()->y - 9.0, aux->getCentro()->z);
                    a.draw(meshQual,wireframe,visionAxis, visionOption, aux, &sph0, &sph1);

                }

            }else if(aux->getObjeto() == LAJE){

                aux->draw(meshQual,wireframe,visionAxis,visionOption,
                        listObj->getbyId(aux->getExtremidades()[0])->getCentro(),
                        listObj->getbyId(aux->getExtremidades()[1])->getCentro(),
                        listObj->getbyId(aux->getExtremidades()[2])->getCentro(),
                        listObj->getbyId(aux->getExtremidades()[3])->getCentro());


            }else if(aux->getObjeto() == DIAGONAL_SMALL || aux->getObjeto() == DIAGONAL_LARGE){

                aux->draw(meshQual,wireframe,visionAxis,visionOption,
                          listObj->getbyId(aux->getExtremidades()[0]),
                          listObj->getbyId(aux->getExtremidades()[1]));

            }else if(aux->getObjeto() == LIGACAO_RIGIDA){

                Objeto3D *sph1 = listObj->getbyId(aux->getExtremidades()[0]);
                Objeto3D *sph2 = listObj->getbyId(aux->getExtremidades()[1]);
                if(sph2->getExtremidades()[0] == sph1->getId()){

                    sph2 = listObj->getbyId((sph2->getExtremidades()[1]));

                }else{

                    sph2 = listObj->getbyId((sph2->getExtremidades()[0]));

                }
                Objeto3D *sph3 = listObj->getbyId(aux->getExtremidades()[2]);
                if(sph3->getExtremidades()[0] == sph1->getId()){

                    sph3 = listObj->getbyId((sph3->getExtremidades()[1]));

                }else{

                    sph3 = listObj->getbyId((sph3->getExtremidades()[0]));

                }
                aux->draw(meshQual, wireframe, visionAxis,visionOption,sph1,sph2,sph3);

            }
            if(MBRAtivo){

                drawMBR(aux->getMBR()[0],aux->getMBR()[1]);

            }
            aux = aux->getProx();

        }
    }
    void save(char* arquivo){

        listObj->salvar(arquivo, tamGrid, meshQual, espacoGrid);

    }
    void open(char* arquivo){

        cabecalhoKMP *c = listObj->abrir(arquivo);
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
    int select(double *ponto, char visionAxis, int visionOption){

        if(visionAxis == 'z'){

            return listObj->select(ponto[0], ponto[1], ponto[2], MBRSelect);

        }else if(visionAxis == 'x'){

            if(visionOption == 1){


                return listObj->select(ponto[2], ponto[0], ponto[1], MBRSelect);

            }else{

                return listObj->select(ponto[2], ponto[0], ponto[1], MBRSelect);

            }

        }
        if(visionOption == 3){

            return listObj->select(ponto[0], -ponto[2], ponto[1], MBRSelect);

        }else{

            return listObj->select(ponto[0], ponto[2], -ponto[1], MBRSelect);

        }

    }
    void deSelectAll(){

        listObj->deSelectAll();
        resetMBRSelect();

    }
    bool remover(double *ponto){

        return listObj->remover(ponto[0], ponto[1], ponto[2]);

    }
    void removeAll(){

        listObj->removeAll();
        resetMBRSelect();

    }
    void clear(){

        listObj->clear();

    }
    bool getCenter(double *ponto, float *center){

        return listObj->getCenter(ponto[0],ponto[1],ponto[2], center);

    }
    void desfazer(){

        listObj->desfazerAcao(MBRSelect);

    }
    void refazer(){

        listObj->refazerAcao(MBRSelect);

    }
    int desfazerSize(){

        return listObj->desfazerSize();

    }
    int refazerSize(){

        return listObj->refazerSize();

    }
    void selectAll(){

        resetMBRSelect();
        listObj->selectAll(MBRSelect);

    }
    bool setFocusToSelect(float* centro){

        Ponto* aux = listObj->setFocusToSelect();
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

        listObj->moveSelect(x,y,z);
        MBRSelect[0].x += x;
        MBRSelect[0].y += y;
        MBRSelect[0].z += z;

        MBRSelect[1].x += x;
        MBRSelect[1].y += y;
        MBRSelect[1].z += z;

        vetDeslocamento.x += x;
        vetDeslocamento.y += y;
        vetDeslocamento.z += z;

    }
    void resetMBRSelect(){

        MBRSelect[0].x = FLT_MAX;
        MBRSelect[0].y = FLT_MAX;
        MBRSelect[0].z = FLT_MAX;
        MBRSelect[1].x = -FLT_MAX;
        MBRSelect[1].y = -FLT_MAX;
        MBRSelect[1].z = -FLT_MAX;

    }
    void drawMoveAxis(char visionAxis, int visionOption, char eixo){

        Ponto centro;
        float max = 10000.0;
        centro.x = (MBRSelect[1].x + MBRSelect[0].x)/2.0;
        centro.y = (MBRSelect[1].y + MBRSelect[0].y)/2.0;
        centro.z = (MBRSelect[1].z + MBRSelect[0].z)/2.0;

        if(listObj->getNumSelect() == 0){

            return;

        }
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
            glDisable(GL_LIGHTING);

            glLineWidth(3);
            ///Eixo X
            if(eixo == '0' || eixo == 'x'){

                glColor3f(1.0,0.0,0.0);
                glBegin(GL_LINES);

                    glVertex3f(-max,0.0,0.0);
                    glVertex3f(max,0.0,0.0);

                glEnd();

            }

            ///Eixo Y
            if(eixo == '0' || eixo == 'y'){

                glColor3f(0.0,1.0,0.0);
                glBegin(GL_LINES);

                    glVertex3f(0.0,-max,0.0);
                    glVertex3f(0.0,max,0.0);

                glEnd();

            }
            ///Eixo Z
            if(eixo == '0' || eixo == 'z'){

                glColor3f(0.0,0.0,1.0);
                glBegin(GL_LINES);

                    glVertex3f(0.0,0.0,-max);
                    glVertex3f(0.0,0.0,max);

                glEnd();

            }
            glLineWidth(1);
            glEnable(GL_LIGHTING);
        glPopMatrix();

    }
    int selectMoveSeta(double *ponto, char visionAxis){

        double x,y,z;
        float erro = 0.2;
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

        if((x >= MBRMoveX[0].x - erro) && (y >= MBRMoveX[0].y - erro) && (z >= MBRMoveX[0].z - erro)){

            if((x <= MBRMoveX[1].x + erro) && (y <= MBRMoveX[1].y + erro) && (z <= MBRMoveX[1].z + erro)){

                return 0;

            }

        }else if((x >= MBRMoveX[2].x - erro) && (y >= MBRMoveX[2].y - erro) && (z >= MBRMoveX[2].z - erro)){

            if((x <= MBRMoveX[3].x + erro) && (y <= MBRMoveX[3].y + erro) && (z <= MBRMoveX[3].z + erro)){

                return 1;

            }

        }if((x >= MBRMoveY[0].x - erro ) && (y >= MBRMoveY[0].y - erro) && (z >= MBRMoveY[0].z - erro)){

            if((x <= MBRMoveY[1].x + erro) && (y <= MBRMoveY[1].y + erro) && (z <= MBRMoveY[1].z + erro)){

                return 2;

            }

        }else if((x >= MBRMoveY[2].x - erro) && (y >= MBRMoveY[2].y - erro) && (z >= MBRMoveY[2].z) - erro){

            if((x <= MBRMoveY[3].x + erro) && (y <= MBRMoveY[3].y + erro) && (z <= MBRMoveY[3].z + erro)){

                return 3;

            }

        }if((x >= MBRMoveZ[0].x - erro) && (y >= MBRMoveZ[0].y - erro) && (z >= MBRMoveZ[0].z) - erro){

            if((x <= MBRMoveZ[1].x + erro) && (y <= MBRMoveZ[1].y + erro) && (z <= MBRMoveZ[1].z + erro)){

                return 4;

            }

        }else if((x >= MBRMoveZ[2].x - erro ) && (y >= MBRMoveZ[2].y - erro) && (z >= MBRMoveZ[2].z - erro)){

            if((x <= MBRMoveZ[3].x + erro) && (y <= MBRMoveZ[3].y + erro) && (z <= MBRMoveZ[3].z + erro)){

                return 5;

            }

        }

        return -1;
    }
    void addSphere(float x, float y, float z){

        listObj->addSphere(x,y,z);

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

        return listObj->addBar(tipoBar);

    }
    void setEspacoGrid(float tam){

        espacoGrid = tam;

    }
    float getEspacoGrid(){

        return espacoGrid;

    }
    float distObjsSelect(){

        return listObj->distObjsSelect();

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
    int getMeshQual(){

        return meshQual*100;

    }
    Objeto *getObjById(int id){

        Objeto3D *aux = listObj->getbyId(id);
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

        if(listObj->moveObj(id,x,y,z)){

            MBRSelect[0].x += x;
            MBRSelect[0].y += y;
            MBRSelect[0].z += z;
            MBRSelect[1].x += x;
            MBRSelect[1].y += y;
            MBRSelect[1].z += z;

        }

    }
    void moveObjSelect(float x, float y, float z){

        if(listObj->getNumSelect() > 0){

            Ponto vetDes;
            vetDes.x = x - (MBRSelect[1].x + MBRSelect[0].x)/2.0;
            vetDes.y = y - (MBRSelect[1].y + MBRSelect[0].y)/2.0;
            vetDes.z = z - (MBRSelect[1].z + MBRSelect[0].z)/2.0;
            if(listObj->moveSelect(vetDes.x, vetDes.y, vetDes.z)){

                MBRSelect[0].x += vetDes.x;
                MBRSelect[0].y += vetDes.y;
                MBRSelect[0].z += vetDes.z;
                MBRSelect[1].x += vetDes.x;
                MBRSelect[1].y += vetDes.y;
                MBRSelect[1].z += vetDes.z;
                vetDeslocamento.x += vetDes.x;
                vetDeslocamento.y += vetDes.y;
                vetDeslocamento.z += vetDes.z;

            }

        }

    }
    bool duplicaSelect(){

        return listObj->duplicaSelect();

    }
    void addBase(int tipo, float x, float y, float z){

        listObj->addBase(tipo, x,y,z);

    }
    Ponto* getCentroMBRSelect(){

        Ponto *c = new Ponto;
        c->x = (MBRSelect[1].x + MBRSelect[0].x)/2.0;
        c->y = (MBRSelect[1].y + MBRSelect[0].y)/2.0;
        c->z = (MBRSelect[1].z + MBRSelect[0].z)/2.0;
        return c;

    }
    bool addLaje(){

        return listObj->addLaje();

    }
    void drawMBR(Ponto p1, Ponto p2){

        glDisable(GL_LIGHTING);

        glPushMatrix();

            glBegin(GL_LINES);

                glColor3f(0.0,0.0,1.0);
                ///parte de baixo
                glVertex3f(p1.x,p1.y,p1.z);
                glVertex3f(p2.x,p1.y,p1.z);

                glVertex3f(p2.x,p1.y,p1.z);
                glVertex3f(p2.x,p2.y,p1.z);

                glVertex3f(p2.x,p2.y,p1.z);
                glVertex3f(p1.x,p2.y,p1.z);

                glVertex3f(p1.x,p2.y,p1.z);
                glVertex3f(p1.x,p1.y,p1.z);

                ///laterais

                glVertex3f(p1.x,p1.y,p1.z);
                glVertex3f(p1.x,p1.y,p2.z);

                glVertex3f(p1.x,p2.y,p1.z);
                glVertex3f(p1.x,p2.y,p2.z);

                glVertex3f(p2.x,p2.y,p1.z);
                glVertex3f(p2.x,p2.y,p2.z);

                glVertex3f(p2.x,p1.y,p1.z);
                glVertex3f(p2.x,p1.y,p2.z);

                ///parte de cima
                glVertex3f(p1.x,p1.y,p2.z);
                glVertex3f(p2.x,p1.y,p2.z);

                glVertex3f(p2.x,p1.y,p2.z);
                glVertex3f(p2.x,p2.y,p2.z);

                glVertex3f(p2.x,p2.y,p2.z);
                glVertex3f(p1.x,p2.y,p2.z);

                glVertex3f(p1.x,p2.y,p2.z);
                glVertex3f(p1.x,p1.y,p2.z);


            glEnd();

        glPopMatrix();

        glEnable(GL_LIGHTING);
    }
    void terminaMovimentacao(){

        listObj->terminaMovimentacao(vetDeslocamento);
        vetDeslocamento = prodPorEscalar(0,vetDeslocamento);

    }
    void cancelarMovimentacao(){

        listObj->moveSelect(-vetDeslocamento.x,-vetDeslocamento.y,-vetDeslocamento.z);
        vetDeslocamento = prodPorEscalar(0,vetDeslocamento);
    }
    bool addDiag(int tipoDiag){

        return listObj->addDiagonal(tipoDiag);

    }
    bool addLigRigida(){

        return listObj->addLigRigida();

    }
    ListaObjetos *getObjList(){

        return listObj;

    }
    void drawRotAxis(char visionAxis, int visionOption, char axis){

        drawMoveAxis(visionAxis, visionOption, axis);

    }
    bool rotacionaSelect(bool x, bool y, bool z, float angle){

        if(idRotCenter == -1){

            Ponto centro;
            centro.x = (MBRSelect[1].x + MBRSelect[0].x)/2.0;
            centro.y = (MBRSelect[1].y + MBRSelect[0].y)/2.0;
            centro.z = (MBRSelect[1].z + MBRSelect[0].z)/2.0;
            return listObj->rotacionaObjSelect(angle,x,y,z,centro);

        }else{

            return listObj->rotacionaObjSelect(angle,x,y,z,rotCenter);

        }


    }
    void selectRotCenter(double *ponto, char visionAxis, int visionOption){

        Objeto3D *p = listObj->getObj(ponto);
        if(p != NULL){

            idRotCenter = p->getId();
            rotCenter = *p->getCentro();

        }

    }
    void terminaRotacao(){

        idRotCenter = -1;
        rotCenter = iniVet();

    }
}
