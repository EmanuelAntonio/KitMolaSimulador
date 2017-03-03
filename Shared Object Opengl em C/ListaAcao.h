#ifndef LISTAACAO_H
#define LISTAACAO_H
#include "Acao.h"

/** Classe ListaAcao: Lista de A��es, armazena as ac�es feitas no programa kitmola, usado as opera��es de desfazer e refazer.**/
class ListaAcao
{
    public:
        ListaAcao();
        /**
        *   Fun��o insere: insere uma acao na lista em forma de pilha
        *   Par�metros: 'acao', inteiro referente a qual acao ocorreu,'objs' lista de objetos que estao associados a esta acao, vetDes � o vetor deslocamento que � usado para movimentar um grupo de objetos
        *   Retorno: 'vazio'
        **/
        void insere(int acao, Objeto3D *objs, Ponto *vetDes);
        /**
        *   Fun��o get: retorna a primeira posicao da pilha
        *   Par�metros: 'vazio'
        *   Retorno: primeira posicao da pilha
        **/
        Acao* get();
        /**
        *   Fun��o size: retorna o tamanho da pilha
        *   Par�metros: 'vazio'
        *   Retorno: tamanho da pilha
        **/
        int size();
        /**
        *   Fun��o clear: limpa os parametros e apaga a pilha
        *   Par�metros: 'vazio'
        *   Retorno: primeira posicao da pilha
        **/
        void clear();
        ~ListaAcao();

    private:
        Acao *pri;
        int tam;
};

#endif // LISTAACAO_H
