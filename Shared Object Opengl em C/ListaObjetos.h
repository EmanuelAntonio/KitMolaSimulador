#ifndef LISTAOBJETOS_H
#define LISTAOBJETOS_H
#include "Objeto3D.h"

class ListaObjetos
{
    public:
        ListaObjetos();
        void addCubo(float x, float y, float z);/**
                                                *   Fun��o addCubo: Adiciona um cubo � lista de objetos na cena
                                                *   Par�metros: 'x','y','z', coordenadas do centro do cubo
                                                *   Retorno: vazio
                                                **/
        Objeto3D* get();/**
                        *   Fun��o addCubo: retorna uma refer�ncia para o primeiro no da lista
                        *   Par�metro: vazio
                        *   Retorno: vazio
                        **/
        void salvar(char* arquivo,char visionAxis, int visionOption);/**
                                                    *   Fun��o salvar: Salva a lista de objetos em um arquivo binario .kmp
                                                    *   Par�metros: 'arquivo' string com o diret�rio do arquivo a ser salvo, 'visionAxis' qual o tipo de visao
                                                    *   Retorno: vazio
                                                    **/
        cabecalhoKMP* abrir(char* arquivo);/**
                                            *   Fun��o abrir: abre um projeto salvo em um arquivo binario .kmp
                                            *   Par�metros: 'arquivo' string com o diret�rio do arquivo a ser aberto
                                            *   Retorno: 'cabecalhoKMP' retorna parametros adicionais salvos no cabecalho do arquivo .KMP
                                            **/
        int size();/**
                    *   Fun��o size: retorna o tamanho da lista de objetos em um arquivo binario .kmp
                    *   Par�metros: vazio
                    *   Retorno: vazio
                    **/
        ~ListaObjetos();
    private:
        Objeto3D *pri;
};

#endif // LISTAOBJETOS_H
