#ifndef LISTAACAO_H
#define LISTAACAO_H
#include "Acao.h"

/** Classe ListaAcao: Lista de Ações, armazena as acões feitas no programa kitmola, usado as operações de desfazer e refazer.**/
class ListaAcao
{
    public:
        ListaAcao();
        /**
        *   Função insere: insere uma acao na lista em forma de pilha
        *   Parâmetros: 'acao', inteiro referente a qual acao ocorreu,'objs' lista de objetos que estao associados a esta acao
        *   Retorno: 'vazio'
        **/
        void insere(int acao, Objeto3D *objs);
        /**
        *   Função get: retorna a primeira posicao da pilha
        *   Parâmetros: 'vazio'
        *   Retorno: primeira posicao da pilha
        **/
        Acao* get();
        /**
        *   Função size: retorna o tamanho da pilha
        *   Parâmetros: 'vazio'
        *   Retorno: tamanho da pilha
        **/
        int size();
        /**
        *   Função clear: limpa os parametros e apaga a pilha
        *   Parâmetros: 'vazio'
        *   Retorno: primeira posicao da pilha
        **/
        void clear();
        ~ListaAcao();

    private:
        Acao *pri;
        int tam;
};

#endif // LISTAACAO_H
