#include "LigRigida.h"

using namespace ManipularVetor;

LigRigida::LigRigida() : Objeto3D()
{
    object_difusa = new GLfloat[4];
    object_difusa[0] = 0.0;
    object_difusa[1] = 1.0;
    object_difusa[2] = 0.94176;
    object_difusa[3] = 1.0;
}
void LigRigida::drawZero(float mehQual, bool wireframe, char visionAxis, int visionOption, Ponto *obj1, Ponto *obj2, Ponto *obj3){

    Ponto vetDir1 = somaVetorial(*obj2, inverteSentido(*obj1));
    Ponto vetDir2 = somaVetorial(*obj3, inverteSentido(*obj1));

    Ponto vetDir1Normalizado = prodPorEscalar(BAR_RADIUS,normalizarVet(vetDir1));
    Ponto vetDir2Normalizado = prodPorEscalar(BAR_RADIUS,normalizarVet(vetDir2));
    Ponto p1 = *obj1;

    float lado = (LIGACAO_RIGIDA_BASE_MAIOR - LIGACAO_RIGIDA_BASE_MENOR)/2.0;
    lado = sqrt(lado*lado + 1);
    ///triangulo equilátero na base menor, distancia de um lado até o centro da esfera é de 0.8cm
    float t2 = (0.8+lado) / normaVet(vetDir1);
    float t = 0.8 / normaVet(vetDir1);
    Ponto retangulo[4];
    Ponto normal = normalizarVet(prodVetorial(vetDir1,vetDir2));
    normal = prodPorEscalar(BAR_RADIUS, normal);
    Ponto normalRet;
    Ponto centro;
    Ponto centroRet;

    retangulo[0] = somaVetorial(p1, somaVetorial(prodPorEscalar(t,vetDir1), vetDir2Normalizado));
    retangulo[1] = somaVetorial(p1, somaVetorial(prodPorEscalar(t2,vetDir1), vetDir2Normalizado));

    t2 = (0.8+lado) / normaVet(vetDir2);
    t = 0.8 / normaVet(vetDir2);

    retangulo[2] = somaVetorial(p1, somaVetorial(prodPorEscalar(t2,vetDir2), vetDir1Normalizado));
    retangulo[3] = somaVetorial(p1, somaVetorial(prodPorEscalar(t,vetDir2), vetDir1Normalizado));

    centro = prodPorEscalar(0.25, somaVetorial(somaVetorial(retangulo[0],retangulo[1]),somaVetorial(retangulo[2],retangulo[3])));

    glBegin(GL_QUADS);

        glNormal3f(normal.x/0.3,normal.y/0.3,normal.z/0.3);
        for(int i = 0; i < 4; i++){

            glVertex3f(retangulo[i].x + normal.x,retangulo[i].y + normal.y,retangulo[i].z + normal.z);

        }
        glNormal3f(-normal.x/0.3,-normal.y/0.3,-normal.z/0.3);
        for(int i = 3; i >= 0; i--){

            glVertex3f(retangulo[i].x - normal.x,retangulo[i].y - normal.y,retangulo[i].z - normal.z);

        }

        vetDir1 = somaVetorial(somaVetorial(retangulo[0], normal), somaVetorial(retangulo[1], normal));
        vetDir2 = somaVetorial(somaVetorial(retangulo[0], normal), somaVetorial(retangulo[1], inverteSentido(normal)));
        normalRet = normalizarVet(prodVetorial(vetDir1,vetDir2));

        centroRet = prodPorEscalar(0.5,somaVetorial(retangulo[0],retangulo[1]));
        if(prodEscalar(normalRet, somaVetorial(centroRet, inverteSentido(centro))) < 0){

            glNormal3f(-normalRet.x,-normalRet.y,-normalRet.z);

        }else{

            glNormal3f(normalRet.x,normalRet.y,normalRet.z);

        }
        glVertex3f(retangulo[0].x + normal.x,retangulo[0].y + normal.y,retangulo[0].z + normal.z);
        glVertex3f(retangulo[0].x - normal.x,retangulo[0].y - normal.y,retangulo[0].z - normal.z);
        glVertex3f(retangulo[1].x - normal.x,retangulo[1].y - normal.y,retangulo[1].z - normal.z);
        glVertex3f(retangulo[1].x + normal.x,retangulo[1].y + normal.y,retangulo[1].z + normal.z);


        vetDir1 = somaVetorial(somaVetorial(retangulo[1], normal), somaVetorial(retangulo[2], normal));
        vetDir2 = somaVetorial(somaVetorial(retangulo[1], normal), somaVetorial(retangulo[2], inverteSentido(normal)));
        normalRet = normalizarVet(prodVetorial(vetDir1,vetDir2));


        centroRet = prodPorEscalar(0.5,somaVetorial(retangulo[1],retangulo[2]));
        if(prodEscalar(normalRet, somaVetorial(centroRet, inverteSentido(centro))) < 0){

            glNormal3f(-normalRet.x,-normalRet.y,-normalRet.z);

        }else{

            glNormal3f(normalRet.x,normalRet.y,normalRet.z);

        }

        glVertex3f(retangulo[1].x + normal.x,retangulo[1].y + normal.y,retangulo[1].z + normal.z);
        glVertex3f(retangulo[1].x - normal.x,retangulo[1].y - normal.y,retangulo[1].z - normal.z);
        glVertex3f(retangulo[2].x - normal.x,retangulo[2].y - normal.y,retangulo[2].z - normal.z);
        glVertex3f(retangulo[2].x + normal.x,retangulo[2].y + normal.y,retangulo[2].z + normal.z);


        vetDir1 = somaVetorial(somaVetorial(retangulo[2], normal), somaVetorial(retangulo[2], normal));
        vetDir2 = somaVetorial(somaVetorial(retangulo[3], normal), somaVetorial(retangulo[3], inverteSentido(normal)));
        normalRet = normalizarVet(prodVetorial(vetDir1,vetDir2));

        centroRet = prodPorEscalar(0.5,somaVetorial(retangulo[2],inverteSentido(retangulo[3])));
        if(prodEscalar(normalRet, somaVetorial(centroRet, inverteSentido(centro))) < 0){

            glNormal3f(-normalRet.x,-normalRet.y,-normalRet.z);

        }else{

            glNormal3f(normalRet.x,normalRet.y,normalRet.z);

        }
        glVertex3f(retangulo[2].x + normal.x,retangulo[2].y + normal.y,retangulo[2].z + normal.z);
        glVertex3f(retangulo[2].x - normal.x,retangulo[2].y - normal.y,retangulo[2].z - normal.z);
        glVertex3f(retangulo[3].x - normal.x,retangulo[3].y - normal.y,retangulo[3].z - normal.z);
        glVertex3f(retangulo[3].x + normal.x,retangulo[3].y + normal.y,retangulo[3].z + normal.z);

        vetDir1 = somaVetorial(somaVetorial(retangulo[3], normal), somaVetorial(retangulo[0], normal));
        vetDir2 = somaVetorial(somaVetorial(retangulo[3], normal), somaVetorial(retangulo[0], inverteSentido(normal)));
        normalRet = normalizarVet(prodVetorial(vetDir1,vetDir2));

        centroRet = prodPorEscalar(0.5,somaVetorial(retangulo[3],inverteSentido(retangulo[0])));
        if(prodEscalar(normalRet, somaVetorial(centroRet, inverteSentido(centro))) < 0){

            glNormal3f(-normalRet.x,-normalRet.y,-normalRet.z);

        }else{

            glNormal3f(normalRet.x,normalRet.y,normalRet.z);

        }

        glVertex3f(retangulo[3].x + normal.x,retangulo[3].y + normal.y,retangulo[3].z + normal.z);
        glVertex3f(retangulo[3].x - normal.x,retangulo[3].y - normal.y,retangulo[3].z - normal.z);
        glVertex3f(retangulo[0].x - normal.x,retangulo[0].y - normal.y,retangulo[0].z - normal.z);
        glVertex3f(retangulo[0].x + normal.x,retangulo[0].y + normal.y,retangulo[0].z + normal.z);

    glEnd();

}
void LigRigida::draw(float meshQual, bool wireframe, char visionAxis, int visionOption, Objeto3D *obj1, Objeto3D *obj2, Objeto3D *obj3){

    Ponto p1,p2,p3;
    p1 = *obj1->getCentro();
    p2 = *obj2->getCentro();
    p3 = *obj3->getCentro();
    if(visionAxis == 'z'){

        p1.x = obj1->getCentro()->x;
        p1.y = obj1->getCentro()->y;
        p1.z = obj1->getCentro()->z;
        p2.x = obj2->getCentro()->x;
        p2.y = obj2->getCentro()->y;
        p2.z = obj2->getCentro()->z;
        p3.x = obj3->getCentro()->x;
        p3.y = obj3->getCentro()->y;
        p3.z = obj3->getCentro()->z;

    }else if(visionAxis == 'x'){

        p1.x = obj1->getCentro()->y;
        p1.y = obj1->getCentro()->z;
        p2.x = obj2->getCentro()->y;
        p2.y = obj2->getCentro()->z;
        p3.x = obj3->getCentro()->y;
        p3.y = obj3->getCentro()->z;
        if(visionOption == 1){

            p2.z = obj2->getCentro()->x;
            p1.z = obj1->getCentro()->x;
            p3.z = obj3->getCentro()->x;

        }else{

            p2.z = -obj2->getCentro()->x;
            p1.z = -obj1->getCentro()->x;
            p3.z = -obj3->getCentro()->x;

        }


    }else{

        p1.x = obj1->getCentro()->x;
        p1.y = obj1->getCentro()->z;
        p2.x = obj2->getCentro()->x;
        p2.y = obj2->getCentro()->z;
        p3.x = obj3->getCentro()->x;
        p3.y = obj3->getCentro()->z;
        if(visionOption == 3){

            p1.z = -obj1->getCentro()->y;
            p2.z = -obj2->getCentro()->y;
            p3.z = -obj3->getCentro()->y;

        }else{

            p1.z = obj1->getCentro()->y;
            p2.z = obj2->getCentro()->y;
            p3.y = obj3->getCentro()->y;

        }

    }

    glPushMatrix();

        glMaterialfv(GL_FRONT, GL_DIFFUSE,object_difusa);
        glMaterialfv(GL_FRONT, GL_AMBIENT,object_ambient);
        glMaterialfv(GL_FRONT, GL_SHININESS, object_brilho);
        glMaterialfv(GL_FRONT, GL_SPECULAR, object_especular);
        drawZero(meshQual,wireframe,visionAxis,visionOption,&p1,&p2,&p3);

    glPopMatrix();

}
LigRigida::~LigRigida()
{
    delete []object_difusa;
}
