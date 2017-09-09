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
        float deformadaBiapoiada(float x, float P, float I, float b, float L);
        float compressao(float P, float L);
        float flambagem(float x, float P, float L, float I, float n);
        float deformadaMonoapoiada(float x, float P, float L, float I);
        void addForcaEsfera(Objeto3D *e, Ponto forca);
        void addForcaBar(ListaObjetos *p, Objeto3D *b, double *ponto, Ponto forca);
        void drawForca(Ponto forca, Ponto aplicacao);
        void drawSetaForca();

};

#endif // SIMULACAO_H
