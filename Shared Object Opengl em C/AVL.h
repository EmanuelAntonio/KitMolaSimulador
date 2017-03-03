#include "No.h"

#ifndef AVL_H
#define AVL_H

class AVL
{
    public:
        AVL();
        void insere(int id, Objeto3D *obj);
        Objeto3D *busca(int p);
        void remover(int p);
        ~AVL();

    private:
        No *raiz;
        No* rotacao_direita(No* N3);
        No* rotacao_esquerda(No* N1);
        No* rotacao_dupla_direita(No* N3);
        No* rotacao_dupla_esquerda(No* N1);
        No* CorrigeAVL(No* p);
        No* InsereAVL(No* p, int ch, Objeto3D *obj);
        No* Consulta(No* p, int ch);
        No* RemoveAVL(No* p);
        No* Remove(No* p, int ch);
        int Altura (No* p);
        int Calcula_FB(No* p);
        void Seta_FB(No* p);
        void deletaH(No* p);
};

#endif // AVL_H
