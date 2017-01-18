#ifndef HEAPESQ_H
#define HEAPESQ_H
#include "No.h"

class heapEsq
{
    public:
        heapEsq();
        No* criaHeapEsq(int ch, Objeto3D *obj);
        void insere(int x, Objeto3D *o);
        No* uniaoHeapEsq(No* H1, No* H2);
        void imprimeHeap();
        void remover(int x);
        No** getRaiz();
        ~heapEsq();
    private:
        No* H;
        No* HUniao;
        int menor(int a, int b);
        int calculaDist(No* p);
        void deletaH(No* H1);
        void imprime(No* H1);
        No* removerR(No* p, int x);
        No* buscaPai(No* H1, int x);

};

#endif // HEAPESQ_H
