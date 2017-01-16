#ifndef LISTAOBJETOS_H
#define LISTAOBJETOS_H
#include "Objeto3D.h"

class ListaObjetos
{
    public:
        ListaObjetos();
        void addCubo(float x, float y, float z);/**
                                                *   Função addCubo: Adiciona um cubo à lista de objetos na cena
                                                *   Parâmetros: 'x','y','z', coordenadas do centro do cubo
                                                *   Retorno: vazio
                                                **/
        Objeto3D* get();/**
                        *   Função addCubo: retorna uma referência para o primeiro no da lista
                        *   Parâmetro: vazio
                        *   Retorno: vazio
                        **/
        void salvar(char* arquivo,char visionAxis, int visionOption);/**
                                                    *   Função salvar: Salva a lista de objetos em um arquivo binario .kmp
                                                    *   Parâmetros: 'arquivo' string com o diretório do arquivo a ser salvo, 'visionAxis' qual o tipo de visao
                                                    *   Retorno: vazio
                                                    **/
        cabecalhoKMP* abrir(char* arquivo);/**
                                            *   Função abrir: abre um projeto salvo em um arquivo binario .kmp
                                            *   Parâmetros: 'arquivo' string com o diretório do arquivo a ser aberto
                                            *   Retorno: 'cabecalhoKMP' retorna parametros adicionais salvos no cabecalho do arquivo .KMP
                                            **/
        int size();/**
                    *   Função size: retorna o tamanho da lista de objetos em um arquivo binario .kmp
                    *   Parâmetros: vazio
                    *   Retorno: vazio
                    **/
        void clear();/**
                        *   Função clear: apaga a lista de objetos
                        *   Parâmetros: vazio
                        *   Retorno: vazio
                        **/
        bool select(float x, float y, float z);/**
                                                *   Função select: seleciona o objeto que contêm o ponto (x,y,z)
                                                *   Parâmetros: (x,y,z), ponto que foi clicado na interface
                                                *   Retorno: 'bool' se foi selecionado algum objeto
                                                **/
        void deSelectAll();/**
                            *   Função deSelectAll: deseleciona todos os objetos que estavam selecionados
                            *   Parâmetros: vazio
                            *   Retorno: vazio
                            **/

        ~ListaObjetos();
    private:
        Objeto3D *pri;
};

#endif // LISTAOBJETOS_H
