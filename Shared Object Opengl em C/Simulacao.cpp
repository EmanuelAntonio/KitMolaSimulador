#include "Simulacao.h"
#define E 20000

using namespace ManipularVetor;

Simulacao::Simulacao()
{
    //ctor
}
void Simulacao::start(ListaObjetos *p, float tempDecorrido, float tempTotal){


    Base b1,b2;
    Sphere e1,e2;
    Bar br1, br2, br3;
    float L, b, a, I, t, taux, meshQual, deltaL, forca;
    int n;
    Ponto vetDir, p1, p2;
    LigRigida l;
    Tirante t1;
    t1.setObjeto(DIAGONAL_LENGTH_SMALL);
    l.setObjeto(LIGACAO_RIGIDA);

    b1.setSubObjeto(BASE_LIVRE);
    b2.setSubObjeto(BASE_LIVRE);
    b1.setObjeto(BASE);
    b2.setObjeto(BASE);
    e1.setObjeto(SPHERE);
    e2.setObjeto(SPHERE);
    b1.setCentro(9.0,0.0,0.0);
    b2.setCentro(18.0,0.0,0.0);
    e1.setCentro(b1.getCentro()->x, b1.getCentro()->y, b1.getCentro()->z + 9.0);
    e2.setCentro(b2.getCentro()->x, b2.getCentro()->y, b2.getCentro()->z + 9.0);


    meshQual = 100;
    n = 1;
    forca = 6.0;//Newtons

    ///Barra vertical esquerda

    vetDir = somaVetorial(*e1.getCentro(), inverteSentido(*b1.getCentro()));
    L = normaVet(vetDir);
    deltaL = compressao(forca/2,L);///forca no centro da barra horizontal
    e1.setCentro(e1.getCentro()->x,e1.getCentro()->y,e1.getCentro()->z - deltaL);

    vetDir = somaVetorial(*e1.getCentro(), inverteSentido(*b1.getCentro()));
    L = normaVet(vetDir);
    I = M_PI*pow(BAR_RADIUS,4)/4.0;
    t = 0;
    taux = 1/meshQual;


    for(int i = 1; i <= meshQual; i++){

        p1 = somaVetorial(*b1.getCentro(), prodPorEscalar(t,vetDir));
        p1.x -= flambagem(p1.z,forca/2.0,L,I,n);

        t += taux;

        p2 = somaVetorial(*b1.getCentro(), prodPorEscalar(t,vetDir));
        p2.x -= flambagem(p2.z,forca/2.0,L,I,n);

        br1.drawZero(1.0,false,'z',0,&p1,&p2);

    }

    e1.setCentro(e1.getCentro()->x + flambagem(9,forca/2.0,L,I,n),e1.getCentro()->y,e1.getCentro()->z);


    ///Barra vertical direita

    vetDir = somaVetorial(*e2.getCentro(), inverteSentido(*b2.getCentro()));
    L = normaVet(vetDir);
    deltaL = compressao(forca/2,L);///forca no centro da barra horizontal
    e2.setCentro(e2.getCentro()->x,e2.getCentro()->y,e2.getCentro()->z - deltaL);

    vetDir = somaVetorial(*e2.getCentro(), inverteSentido(*b2.getCentro()));
    L = normaVet(vetDir);
    I = M_PI*pow(BAR_RADIUS,4)/4.0;
    t = 0;
    taux = 1/meshQual;


    for(int i = 1; i <= meshQual; i++){

        p1 = somaVetorial(*b2.getCentro(), prodPorEscalar(t,vetDir));
        p1.x += flambagem(p1.z,forca/2.0,L,I,n);

        t += taux;

        p2 = somaVetorial(*b2.getCentro(), prodPorEscalar(t,vetDir));
        p2.x += flambagem(p2.z,forca/2.0,L,I,n);

        br1.drawZero(1.0,false,'z',0,&p1,&p2);

    }

    e2.setCentro(e2.getCentro()->x - flambagem(e2.getCentro()->z,forca/2.0,L,I,n),e2.getCentro()->y,e2.getCentro()->z);


    ///barra horizontal

    vetDir = somaVetorial(*e2.getCentro(), inverteSentido(*e1.getCentro()));
    L = normaVet(vetDir);
    a = L/2.0;///Metade da barra horizontal
    b = L - a;
    I = M_PI*pow(BAR_RADIUS,4)/4.0;
    t = 0;
    taux = 1/meshQual;


    for(int i = 1; i <= meshQual*a/L; i++){

        p1 = somaVetorial(*e1.getCentro(), prodPorEscalar(t,vetDir));
        p1.z += deformadaBiapoiada(normaVet(somaVetorial(p1, inverteSentido(*e1.getCentro()))),forca,I,b,L);

        t += taux;

        p2 = somaVetorial(*e1.getCentro(), prodPorEscalar(t,vetDir));
        p2.z += deformadaBiapoiada(normaVet(somaVetorial(p2, inverteSentido(*e1.getCentro()))),forca,I,b,L);

        br1.drawZero(1.0,false,'z',0,&p1,&p2);

    }
    float aux = b;
    b = a;
    a = aux;

    for(int i = meshQual*b/L; i <= meshQual; i++){

        p1 = somaVetorial(*e1.getCentro(), prodPorEscalar(t,vetDir));
        p1.z += deformadaBiapoiada(normaVet(somaVetorial(p1, inverteSentido(*e2.getCentro()))),forca,I,b,L);

        t += taux;

        p2 = somaVetorial(*e1.getCentro(), prodPorEscalar(t,vetDir));
        p2.z += deformadaBiapoiada(normaVet(somaVetorial(p2, inverteSentido(*e2.getCentro()))),forca,I,b,L);

        br1.drawZero(1.0,false,'z',0,&p1,&p2);

    }

    aux = b;
    b = a;
    a = aux;

    t1.draw(1.0,false,'z',0.0, (Objeto3D*)(&b1), (Objeto3D*)(&e2));
    t1.draw(1.0,false,'z',0.0, (Objeto3D*)(&b2), (Objeto3D*)(&e1));

    b1.draw(1.0,0.0,'z',0.0);
    b2.draw(1.0,0.0,'z',0.0);

    e1.draw(1.0,0.0,'z',0.0);
    e2.draw(1.0,0.0,'z',0.0);

    ///draw forca

    Ponto f, apl;
    f.x = 0;
    f.y = 0;
    f.z = -forca;

    apl = somaVetorial(*e2.getCentro(),inverteSentido(*e1.getCentro()));
    apl = somaVetorial(*e1.getCentro(),prodPorEscalar(a/normaVet(apl),apl));

    apl.z += deformadaBiapoiada(a,forca,I,b,L);
    drawForca(f,apl);


    /*********************************Segunda extrutura a ser montada**********************************/


    b1.setCentro(27.0,0.0,0.0);
    b2.setCentro(36.0,0.0,0.0);
    e1.setCentro(b1.getCentro()->x, b1.getCentro()->y, b1.getCentro()->z + 9.0);
    e2.setCentro(b2.getCentro()->x, b2.getCentro()->y, b2.getCentro()->z + 9.0);

    meshQual = 100;
    n = 1;
    forca = 6.0;//Newtons

    ///Barra vertical esquerda

    vetDir = somaVetorial(*e1.getCentro(), inverteSentido(*b1.getCentro()));
    L = normaVet(vetDir);
    I = M_PI*pow(BAR_RADIUS,4)/4.0;
    t = 0;
    taux = 1/meshQual;


    for(int i = 1; i <= meshQual; i++){

        p1 = somaVetorial(*b1.getCentro(), prodPorEscalar(t,vetDir));
        p1.x -= deformadaMonoapoiada(p1.z, forca, L, I);

        t += taux;

        p2 = somaVetorial(*b1.getCentro(), prodPorEscalar(t,vetDir));
        p2.x -= deformadaMonoapoiada(p2.z, forca, L, I);

        br1.drawZero(1.0,false,'z',0,&p1,&p2);

    }

    e1.setCentro(e1.getCentro()->x - deformadaMonoapoiada(9.0,forca,L,I),e1.getCentro()->y ,e1.getCentro()->z);


    ///Barra vertical direita


    vetDir = somaVetorial(*e2.getCentro(), inverteSentido(*b2.getCentro()));
    L = normaVet(vetDir);
    I = M_PI*pow(BAR_RADIUS,4)/4.0;
    t = 0;
    taux = 1/meshQual;


    for(int i = 1; i <= meshQual; i++){

        p1 = somaVetorial(*b2.getCentro(), prodPorEscalar(t,vetDir));
        p1.x -= deformadaMonoapoiada(p1.z, forca, L, I);

        t += taux;

        p2 = somaVetorial(*b2.getCentro(), prodPorEscalar(t,vetDir));
        p2.x -= deformadaMonoapoiada(p2.z, forca, L, I);

        br1.drawZero(1.0,false,'z',0,&p1,&p2);

    }

    e2.setCentro(e2.getCentro()->x - deformadaMonoapoiada(e2.getCentro()->z, forca, L, I),e2.getCentro()->y,e2.getCentro()->z);


    ///barra horizontal

    vetDir = somaVetorial(*e2.getCentro(), inverteSentido(*e1.getCentro()));
    L = normaVet(vetDir);
    I = M_PI*pow(BAR_RADIUS,4)/4.0;
    n = 1;
    t = 0;
    taux = 1/meshQual;


    for(int i = 0; i <= meshQual; i++){

        p1 = somaVetorial(*e1.getCentro(), prodPorEscalar(t,vetDir));
        p1.z += flambagem(normaVet(somaVetorial(p1, inverteSentido(*e1.getCentro()))),forca,L,I,n);

        t += taux;

        p2 = somaVetorial(*e1.getCentro(), prodPorEscalar(t,vetDir));
        p2.z += flambagem(normaVet(somaVetorial(p2, inverteSentido(*e1.getCentro()))),forca,L,I,n);

        br1.drawZero(1.0,false,'z',0,&p1,&p2);

    }

    aux = b;
    b = a;
    a = aux;

    Sphere ea1, ea2;
    ea1.setObjeto(SPHERE);
    ea2.setObjeto(SPHERE);

    ea1.setCentro(36,0.0,0.0);
    ea2.setCentro(27.0,0.0,9.0);

    l.draw(1.0,false,'z',0.0, (Objeto3D*)(&b1),(Objeto3D*)(&ea1),(Objeto3D*)(&ea2));

    ea1.setCentro(18,0.0,0.0);

    l.draw(1.0,false,'z',0.0, (Objeto3D*)(&b1),(Objeto3D*)(&ea1),(Objeto3D*)(&ea2));


    ea1.setCentro(45,0.0,0.0);
    ea2.setCentro(36.0,0.0,9.0);

    l.draw(1.0,false,'z',0.0, (Objeto3D*)(&b2),(Objeto3D*)(&ea1),(Objeto3D*)(&ea2));

    ea1.setCentro(27,0.0,0.0);

    l.draw(1.0,false,'z',0.0, (Objeto3D*)(&b2),(Objeto3D*)(&ea1),(Objeto3D*)(&ea2));

    b1.draw(1.0,0.0,'z',0.0);
    b2.draw(1.0,0.0,'z',0.0);

    e1.draw(1.0,0.0,'z',0.0);
    e2.draw(1.0,0.0,'z',0.0);

    ///draw forca

    f.x = forca;
    f.y = 0;
    f.z = 0;

    apl = *e1.getCentro();

    drawForca(f,apl);

}
float Simulacao::centimetroMetro(float c){

    return c/100.0;

}
float Simulacao::deformadaBiapoiada(float x, float P, float I, float b, float L){

    return ((-P*b*x)/(6.0*E*I*L)) * (pow(L,2) - pow(b,2) - pow(x,2));

}
void Simulacao::addForca(ListaObjetos *p, double *ponto, Ponto forca){

    /*Objeto3D *obj = p->getObj(ponto);

    if(obj == NULL){

        return;

    }

    if(obj->getObjeto() == SPHERE){

        addForcaEsfera(obj, forca);

    }else if(obj->getObjeto() == BAR_LARGE || obj->getObjeto() == BAR_SMALL){

        addForcaBar(p, obj, ponto, forca);

    }*/

}
void Simulacao::addForcaEsfera(Objeto3D *e, Ponto forca){

    //e->setForca(forca, *e->getCentro());

}
void Simulacao::addForcaBar(ListaObjetos *p, Objeto3D *b, double *ponto, Ponto forca){

    /*Objeto3D *sph0 = p->getbyId(b->getExtremidades()[0]);
    Objeto3D *sph1 = p->getbyId(b->getExtremidades()[1]);
    Ponto p1;

    p1.x = ponto[0];
    p1.y = ponto[1];
    p1.z = ponto[2];

    Ponto vetAux = somaVetorial(p1,inverteSentido(*sph0->getCentro()));
    Ponto vetDir = somaVetorial(*sph1->getCentro(), inverteSentido(*sph0->getCentro()));

    float angulo = anguloVetores(vetAux, vetDir);
    float t = normaVet(prodPorEscalar(cos(angulo)*normaVet(vetAux), normalizarVet(vetAux)))/normaVet(vetDir);
    p1 = somaVetorial(*sph0->getCentro(), prodPorEscalar(t,vetDir));

    b->setForca(forca, p1);*/

}
void Simulacao::drawForca(Ponto forca, Ponto aplicacao){

    if(forca.x == 0 && forca.y == 0 && forca.z == 0){

        return;

    }

    glDisable(GL_LIGHTING);

    glPushMatrix();

        glTranslatef(aplicacao.x,aplicacao.y,aplicacao.z);
        glBegin(GL_LINES);

            glColor3f(0.0,0.0,1.0);
            glVertex3f(0,0,0);
            glVertex3f(forca.x,forca.y,forca.z);

        glEnd();

    glPopMatrix();

    glPushMatrix();

        glTranslatef(forca.x,forca.y,forca.z);
        glPushMatrix();

            float vx = forca.x;
            float vy = forca.y;
            float vz = forca.z;

            //handle the degenerate case of z1 == z2 with an approximation
            if(vz == 0)
                vz = .0001;

            float v = sqrt( vx*vx + vy*vy + vz*vz );
            float ax = 57.2957795*acos( vz/v );
            if ( vz < 0.0 )
                ax = -ax;
            float rx = -vy*vz;
            float ry = vx*vz;

            glTranslatef(aplicacao.x,aplicacao.y,aplicacao.z);
            glRotatef(ax, rx, ry, 0.0);
            drawSetaForca();

        glPopMatrix();
    glPopMatrix();

    glEnable(GL_LIGHTING);

}
void Simulacao::drawSetaForca(){

    float tamSeta = 1.0;
    float dxyz = 0.1;
    glBegin(GL_TRIANGLE_FAN);

        glColor3f(0.0,0.0,1.0);
        glVertex3f(0.0, 0.0, tamSeta);
        glVertex3f(dxyz, dxyz, 0.0);
        glVertex3f(-dxyz, dxyz, 0.0);
        glVertex3f(-dxyz, -dxyz, 0.0);
        glVertex3f(dxyz, -dxyz, 0.0);
        glVertex3f(dxyz, dxyz, 0.0);

    glEnd();


}
float Simulacao::compressao(float P, float L){

    return P*L/(M_PI*pow(BAR_RADIUS,2)*E);

}
float Simulacao::flambagem(float x, float P, float L, float I, float n){

    float C1 = sqrt(pow(L/10,2)/4 - (M_PI*E*I/10000)/4*P);

    return C1*sin((n*M_PI*x)/L);

}
float Simulacao::deformadaMonoapoiada(float x, float P, float L, float I){

    return -((P*x*x/(6*(E*10)*(I)))*(3*L-x));

}
Simulacao::~Simulacao()
{
    //dtor
}
