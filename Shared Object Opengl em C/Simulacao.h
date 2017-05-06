#ifndef SIMULACAO_H
#define SIMULACAO_H
#include "ListaObjetos.h"
#include "ManipularVetor.h"


class Simulacao
{
    public:
        Simulacao();

        void start(ListaObjetos *p, float tempDecorrido, float tempTotal);

        void addForca(ListaObjetos *p, double *a, Ponto f);

        ~Simulacao();
    private:

        float centimetroMetro(float c);
        float deformadaBiapoiada(float x, Ponto forca);
        void addForcaEsfera(Objeto3D *e, Ponto forca);
        void addForcaBar(ListaObjetos *p, Objeto3D *b, double *ponto, Ponto forca);
        void drawForca(Ponto p1, Ponto p2);
        void drawForcaZero(float tam);

};

#endif // SIMULACAO_H
