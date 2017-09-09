#ifndef MANIPULARVETOR_H
#define MANIPULARVETOR_H
#include "Ponto.h"
#include <math.h>


namespace ManipularVetor
{

    float distancia(Ponto p, Ponto n);
    Ponto prodVetorial(Ponto vetp, Ponto vetn);
    float normaVet(Ponto vetp);
    float prodEscalar(Ponto vetp, Ponto vetn);
    Ponto somaVetorial(Ponto vetp, Ponto vetn);
    Ponto inverteSentido(Ponto vetp);
    Ponto prodPorEscalar(float t, Ponto vetn);
    Ponto normalizarVet(Ponto vetp);
    Ponto maiorXYZ(Ponto p1, Ponto p2);
    Ponto menorXYZ(Ponto p1, Ponto p2);
    float anguloVetores(Ponto vet1, Ponto vet2);
    bool vetNulo(Ponto vet);
    Ponto iniVet();
    Ponto copiar(Ponto n);
};

#endif // MANIPULARVETOR_H
