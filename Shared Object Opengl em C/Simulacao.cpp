#include "Simulacao.h"


using namespace ManipularVetor;

Simulacao::Simulacao()
{
    //ctor
}
void Simulacao::start(ListaObjetos *p, float tempDecorrido, float tempTotal){

    Objeto3D *inicio = p->get();
    Objeto3D *barra = NULL;
    Objeto3D *sph0 = NULL, *sph1 = NULL;
    Ponto p1,p2, vetDir;
    float t, taux;
    float norma;
    int meshQual = 100;
    Ponto forca;
    forca.x = 0;
    forca.y = 0;
    if(tempDecorrido < tempTotal){
        forca.z = 6 * (tempDecorrido/tempTotal);
    }else{

        forca.z = 6;

    }
    while(inicio != NULL){

        if(inicio->getObjeto() == BAR_LARGE || inicio->getObjeto() == BAR_SMALL){

            drawForca(inicio->getForca()[1], inicio->getForca()[0]);

            barra = inicio;

            sph0 = p->getbyId(barra->getExtremidades()[0]);
            sph1 = p->getbyId(barra->getExtremidades()[1]);
            vetDir = somaVetorial(*sph1->getCentro(), inverteSentido(*sph0->getCentro()));
            norma = normaVet(vetDir);
            t = SPHERE_RADIUS/norma;
            taux = t;
            for(int x = 1; x < meshQual/2; x++){

                p1 = somaVetorial(*sph0->getCentro(),prodPorEscalar(t,vetDir));
                p1.z += deformadaBiapoiada(normaVet(somaVetorial(p1, inverteSentido(*sph0->getCentro()))),forca);
                t += (1 - 2*taux)/meshQual;
                p2 = somaVetorial(*sph0->getCentro(),prodPorEscalar(t,vetDir));
                p2.z += deformadaBiapoiada(normaVet(somaVetorial(p2, inverteSentido(*sph0->getCentro()))),forca);

                ((Bar*)barra)->drawZero(1.0, false, 'z', 0, &p1, &p2);

            }
            for(int x = (meshQual-1)/2; x < meshQual; x++){

                p1 = somaVetorial(*sph0->getCentro(),prodPorEscalar(t,vetDir));
                p1.z += deformadaBiapoiada(normaVet(somaVetorial(p1, inverteSentido(*sph1->getCentro()))),forca);
                t += (1 - 2*taux)/meshQual;
                p2 = somaVetorial(*sph0->getCentro(),prodPorEscalar(t,vetDir));
                p2.z += deformadaBiapoiada(normaVet(somaVetorial(p2, inverteSentido(*sph1->getCentro()))),forca);

                ((Bar*)barra)->drawZero(1.0, false, 'z', 0, &p1, &p2);

            }

        }else if(inicio->getObjeto() == SPHERE || inicio->getObjeto() == BASE){

            (inicio)->draw(1.0, false, 'z', 0);

        }
        inicio = inicio->getProx();
    }



}
float Simulacao::centimetroMetro(float c){

    return c/100.0;

}
float Simulacao::deformadaBiapoiada(float x, Ponto forca){

    float I, b,L;
    float E;
    E = 20000;
    I = (M_PI*pow(BAR_RADIUS,4))/4.0;
    L = BAR_LENGTH_SMALL + (2*SPHERE_RADIUS);
    b = L/2.0;
    return ((-forca.z*b*x)/(6.0*E*I*L)) * (pow(L,2) - pow(b,2) - pow(x,2));

}
void Simulacao::addForca(ListaObjetos *p, double *ponto, Ponto forca){

    Objeto3D *obj = p->getObj(ponto);

    if(obj == NULL){

        return;

    }

    if(obj->getObjeto() == SPHERE){

        addForcaEsfera(obj, forca);

    }else if(obj->getObjeto() == BAR_LARGE || obj->getObjeto() == BAR_SMALL){

        addForcaBar(p, obj, ponto, forca);

    }

}
void Simulacao::addForcaEsfera(Objeto3D *e, Ponto forca){

    e->setForca(forca, *e->getCentro());

}
void Simulacao::addForcaBar(ListaObjetos *p, Objeto3D *b, double *ponto, Ponto forca){

    Objeto3D *sph0 = p->getbyId(b->getExtremidades()[0]);
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

    b->setForca(forca, p1);



}
void Simulacao::drawForca(Ponto p1, Ponto p2){

    float tam = normaVet(somaVetorial(p2, inverteSentido(p1)));

    if(p1.z > p2.z){

        Ponto aux = p1;
        p1 = p2;
        p2 = aux;

    }

    float vx = p2.x - p1.x;
    float vy = p2.y - p1.y;
    float vz = p2.z - p1.z;

    //handle the degenerate case of z1 == z2 with an approximation
    if(vz == 0)
        vz = .0001;

    float v = sqrt( vx*vx + vy*vy + vz*vz );
    float ax = 57.2957795*acos( vz/v );
    if ( vz < 0.0 )
        ax = -ax;
    float rx = -vy*vz;
    float ry = vx*vz;

    glPushMatrix();

        //draw the cylinder body
        glTranslatef( p1.x,p1.y,p1.z );
        glRotatef(ax, rx, ry, 0.0);
        drawForcaZero(tam);

    glPopMatrix();


}
void Simulacao::drawForcaZero(float tam){

    glDisable(GL_LIGHTING);

    glPushMatrix();

        glBegin(GL_LINES);

            glColor3f(0.0,0.0,1.0);
            glVertex3f(0.0,0.0,0.0);
            glVertex3f(tam,0.0,0.0);

        glEnd();

    glPopMatrix();

    glEnable(GL_LIGHTING);

}
Simulacao::~Simulacao()
{
    //dtor
}
