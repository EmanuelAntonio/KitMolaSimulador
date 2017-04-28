#include "Laje.h"

using namespace ManipularVetor;

Laje::Laje():Objeto3D()
{

    object_difusa = new GLfloat[4];
    object_difusa[0] = 0.9296875;
    object_difusa[1] = 0.90625;
    object_difusa[2] = 0.6640625;
    object_difusa[3]  = 1.0;
}
void Laje::draw(float meshQual, bool wireframe, char visionAxis, int visionOption, Ponto *p1, Ponto *p2, Ponto *p3, Ponto *p4){

    GLfloat difuse[4];
    difuse[0] = object_difusa[0];
    difuse[1] = object_difusa[1];
    difuse[2] = object_difusa[2];
    difuse[3] = object_difusa[3];

    Ponto retangulo[4];
    Ponto retAux[4];
    retAux[0] = *p1;
    retAux[1] = *p2;
    retAux[2] = *p3;
    retAux[3] = *p4;

    if(selecionado){

        difuse[0] = object_select[0];
        difuse[1] = object_select[1];
        difuse[2] = object_select[2];

    }
    glPushMatrix();

        if(visionAxis == 'x'){

            for(int i = 0; i < 4; i++){

                retangulo[i].x = retAux[i].y;
                retangulo[i].y = retAux[i].z;
                if(visionOption == 1){

                    retangulo[i].z = retAux[i].x;

                }else{

                    retangulo[i].z = -retAux[i].x;

                }

            }

        }else if(visionAxis == 'y'){

            for(int i = 0; i < 4; i++){

                retangulo[i].x = retAux[i].x;
                retangulo[i].y = retAux[i].z;
                if(visionOption == 3){

                    retangulo[i].z = -retAux[i].y;

                }else{

                    retangulo[i].z = retAux[i].y;

                }

            }

        }else{

            for(int i = 0; i < 4; i++){

                retangulo[i].x = retAux[i].x;
                retangulo[i].y = retAux[i].y;
                retangulo[i].z = retAux[i].z;

            }

        }
        if(wireframe){

            if(!selecionado){

                difuse[0] = 0.0;
                difuse[1] = 0.0;
                difuse[2] = 1.0;

            }
            glPushMatrix();
                glPolygonMode(GL_FRONT,GL_LINE);
                glMaterialfv(GL_FRONT, GL_DIFFUSE,difuse);
                glMaterialfv(GL_FRONT, GL_AMBIENT,object_ambient);
                glMaterialfv(GL_FRONT, GL_SHININESS, object_brilho);
                glMaterialfv(GL_FRONT, GL_SPECULAR, object_especular);
                drawZero(meshQual,wireframe, visionAxis, visionOption, &retangulo[0],&retangulo[1],&retangulo[2],&retangulo[3]);
                glPolygonMode(GL_FRONT, GL_FILL);
            glPopMatrix();

            difuse[0] = object_select[0];
            difuse[1] = object_select[1];
            difuse[2] = object_select[2];

        }else{

            glPushMatrix();
                glMaterialfv(GL_FRONT, GL_DIFFUSE,difuse);
                glMaterialfv(GL_FRONT, GL_AMBIENT,object_ambient);
                glMaterialfv(GL_FRONT, GL_SHININESS, object_brilho);
                glMaterialfv(GL_FRONT, GL_SPECULAR, object_especular);
                drawZero(meshQual, wireframe, visionAxis, visionOption, &retangulo[0],&retangulo[1],&retangulo[2],&retangulo[3]);
            glPopMatrix();

        }

    glPopMatrix();

}
void Laje::drawZero(float meshQual,  bool wireframe, char visionAxis, int visionOption, Ponto *p1, Ponto *p2, Ponto *p3, Ponto *p4){

    Ponto vet1;
    Ponto vet2;
    Ponto normal;
    Ponto normalUnit;
    Ponto poligonoSuperior[8];
    Ponto poligonoInferior[8];
    Ponto retangulo[4];
    Ponto centroObj;
    Ponto normalRet;
    Ponto centroRet;

    ///Calcula o centro da laje

    centroObj.x = (p1->x + p2->x + p3->x + p4->x)/4.0;
    centroObj.y = (p1->y + p2->y + p3->y + p4->y)/4.0;
    centroObj.z = (p1->z + p2->z + p3->z + p4->z)/4.0;


    ///Acerta os pontos P1, P2, P3 e P4 para o tamanho correto da laje

    vet1 = somaVetorial(*p4,inverteSentido(*p1));
    vet2 = somaVetorial(*p2,inverteSentido(*p1));

    ///Vetor normal ao plano que passa pelos pontos coplanares p1,p2,p3 e p4
    normal = prodVetorial(vet1,vet2);
    normalUnit = normalizarVet(normal);

    ///Vetor deslocamento normal com o tamanho da metade da espessura da laje

    normal = prodPorEscalar(LAJE_THICKNESS/2.0,normalUnit);

    ///Definição do poligonoSuperior

    float dist1 = normaVet(vet1);
    float dist2 = normaVet(vet2);
    float t = (LAJE_LEG + ((BAR_LENGTH_LARGE + 2*SPHERE_RADIUS) - LAJE_LENGTH))/dist1;
    float t2 = (LAJE_LEG + ((BAR_LENGTH_SMALL + 2*SPHERE_RADIUS) - LAJE_WIDTH))/dist2;
    float taux;
    taux = ((BAR_LENGTH_SMALL + 2*SPHERE_RADIUS) - LAJE_WIDTH)/(2*dist2);

    poligonoSuperior[0] = somaVetorial(somaVetorial(*p1,prodPorEscalar(t,vet1)),
                                                       prodPorEscalar(taux,vet2));

    taux = ((BAR_LENGTH_LARGE + 2*SPHERE_RADIUS) - LAJE_LENGTH)/(2*dist1);
    poligonoSuperior[1] = somaVetorial(somaVetorial(*p1,prodPorEscalar(t2,vet2)),
                                                       prodPorEscalar(taux,vet1));

    ///Redefino os vetores vet1 e vet2 para o ponto p2

    vet1 = somaVetorial(*p1,inverteSentido(*p2));
    vet2 = somaVetorial(*p3,inverteSentido(*p2));

    dist1 = normaVet(vet1);
    dist2 = normaVet(vet2);

    t = (LAJE_LEG + ((BAR_LENGTH_SMALL + 2*SPHERE_RADIUS) - LAJE_WIDTH))/dist1;///Altera o comprimento da reta que liga estes dois pontos
    t2 = (LAJE_LEG + ((BAR_LENGTH_LARGE + 2*SPHERE_RADIUS) - LAJE_LENGTH))/dist2;
    taux = ((BAR_LENGTH_LARGE + 2*SPHERE_RADIUS) - LAJE_LENGTH)/(2*dist2);

    poligonoSuperior[2] = somaVetorial(somaVetorial(*p2,prodPorEscalar(t,vet1)),
                                                       prodPorEscalar(taux,vet2));

    taux = ((BAR_LENGTH_SMALL + 2*SPHERE_RADIUS) - LAJE_WIDTH)/(2*dist1);
    poligonoSuperior[3] = somaVetorial(somaVetorial(*p2,prodPorEscalar(t2,vet2)),
                                                       prodPorEscalar(taux,vet1));

    ///Redefino os vetores vet1 e vet2 para o ponto p3

    vet1 = somaVetorial(*p2,inverteSentido(*p3));
    vet2 = somaVetorial(*p4,inverteSentido(*p3));

    dist1 = normaVet(vet1);
    dist2 = normaVet(vet2);

    t = (LAJE_LEG + ((BAR_LENGTH_SMALL + 2*SPHERE_RADIUS) - LAJE_WIDTH))/dist1;
    t2 = (LAJE_LEG + ((BAR_LENGTH_LARGE + 2*SPHERE_RADIUS) - LAJE_LENGTH))/dist2;
    taux = ((BAR_LENGTH_LARGE + 2*SPHERE_RADIUS) - LAJE_LENGTH)/(2*dist2);

    poligonoSuperior[4] = somaVetorial(somaVetorial(*p3,prodPorEscalar(t,vet1)),
                                                       prodPorEscalar(taux,vet2));

    taux = ((BAR_LENGTH_SMALL + 2*SPHERE_RADIUS) - LAJE_WIDTH)/(2*dist1);

    poligonoSuperior[5] = somaVetorial(somaVetorial(*p3,prodPorEscalar(t2,vet2)),
                                                       prodPorEscalar(taux,vet1));

    ///Redefino os vetores vet1 e vet2 para o ponto p4

    vet1 = somaVetorial(*p3,inverteSentido(*p4));
    vet2 = somaVetorial(*p1,inverteSentido(*p4));

    dist1 = normaVet(vet1);
    dist2 = normaVet(vet2);

    t = (LAJE_LEG + ((BAR_LENGTH_SMALL + 2*SPHERE_RADIUS) - LAJE_WIDTH))/dist1;
    t2 = (LAJE_LEG + ((BAR_LENGTH_LARGE + 2*SPHERE_RADIUS) - LAJE_LENGTH))/dist2;
    taux = ((BAR_LENGTH_LARGE + 2*SPHERE_RADIUS) - LAJE_LENGTH)/(2*dist2);

    poligonoSuperior[6] = somaVetorial(somaVetorial(*p4,prodPorEscalar(t,vet1)),
                                                       prodPorEscalar(taux,vet2));

    taux = ((BAR_LENGTH_SMALL + 2*SPHERE_RADIUS) - LAJE_WIDTH)/(2*dist1);

    poligonoSuperior[7] = somaVetorial(somaVetorial(*p4,prodPorEscalar(t2,vet2)),
                                                       prodPorEscalar(taux,vet1));

    int j = 7;
    glPushMatrix();
        glBegin(GL_POLYGON);

            glNormal3f(normalUnit.x,normalUnit.y,normalUnit.z);
            for(int i = 7; i >= 0; i--){

                glVertex3f(poligonoSuperior[i].x + normal.x,
                           poligonoSuperior[i].y + normal.y,
                           poligonoSuperior[i].z + normal.z);
                poligonoInferior[j] = poligonoSuperior[i];
                j--;

            }

        glEnd();
        glBegin(GL_POLYGON);

            glNormal3f(-normalUnit.x,-normalUnit.y,-normalUnit.z);
            for(int i = 0; i < 8; i++){

                glVertex3f(poligonoInferior[i].x - normal.x,
                           poligonoInferior[i].y - normal.y,
                           poligonoInferior[i].z - normal.z);

            }

        glEnd();

    glPopMatrix();

    ///Calcula as faces laterais da laje

    for(int j = 0; j < 8; j++){

        if(j < 7){

            retangulo[0] = somaVetorial(poligonoSuperior[j],normal);
            retangulo[1] = somaVetorial(poligonoSuperior[j+1],normal);
            retangulo[2] = somaVetorial(poligonoInferior[j+1],inverteSentido(normal));
            retangulo[3] = somaVetorial(poligonoInferior[j],inverteSentido(normal));

        }else{

            retangulo[0] = somaVetorial(poligonoSuperior[j],normal);
            retangulo[1] = somaVetorial(poligonoSuperior[0],normal);
            retangulo[2] = somaVetorial(poligonoInferior[0],inverteSentido(normal));
            retangulo[3] = somaVetorial(poligonoInferior[j],inverteSentido(normal));

        }

        vet1 = somaVetorial(retangulo[1],inverteSentido(retangulo[0]));
        vet2 = somaVetorial(retangulo[3],inverteSentido(retangulo[0]));

        normalRet = prodVetorial(vet1,vet2);

        centroRet.x = (retangulo[0].x + retangulo[1].x + retangulo[2].x + retangulo[3].x)/4.0;
        centroRet.y = (retangulo[0].y + retangulo[1].y + retangulo[2].y + retangulo[3].y)/4.0;
        centroRet.z = (retangulo[0].z + retangulo[1].z + retangulo[2].z + retangulo[3].z)/4.0;

        normalUnit = somaVetorial(centroRet, inverteSentido(centroObj));

        if(prodEscalar(normalRet, normalUnit) >= 0){

            glBegin(GL_QUADS);

                glNormal3f(normalRet.x,normalRet.y,normalRet.z);
                for(int i = 0; i < 4; i++){

                    glVertex3f(retangulo[i].x,retangulo[i].y,retangulo[i].z);

                }

            glEnd();


        }else{

            glBegin(GL_QUADS);

                normalRet = inverteSentido(normalRet);
                glNormal3f(normalRet.x,normalRet.y,normalRet.z);
                for(int i = 3; i >= 0; i--){

                    glVertex3f(retangulo[i].x,retangulo[i].y,retangulo[i].z);

                }

            glEnd();

        }

    }


}

Laje::~Laje()
{
    delete []object_difusa;
}
