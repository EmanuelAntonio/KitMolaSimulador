#ifndef LISTAOBJETOS_H
#define LISTAOBJETOS_H
#include "Objeto3D.h"
#include "heapEsq.cpp"

class ListaObjetos
{
    public:
        ListaObjetos();
        /**
        *   Função addCubo: Adiciona um cubo à lista de objetos na cena
        *   Parâmetros: 'x','y','z', coordenadas do centro do cubo
        *   Retorno: vazio
        **/
        void addCubo(float x, float y, float z);
        /**
        *   Função get: retorna uma referência para o primeiro no da lista
        *   Parâmetro: vazio
        *   Retorno: vazio
        **/
        Objeto3D* get();
        /**
        *   Função salvar: Salva a lista de objetos em um arquivo binario .kmp
        *   Parâmetros: 'arquivo' string com o diretório do arquivo a ser salvo, 'visionAxis' qual o tipo de visao
        *   Retorno: vazio
        **/
        void salvar(char* arquivo,char visionAxis, int visionOption);
        /**
        *   Função abrir: abre um projeto salvo em um arquivo binario .kmp
        *   Parâmetros: 'arquivo' string com o diretório do arquivo a ser aberto
        *   Retorno: 'cabecalhoKMP' retorna parametros adicionais salvos no cabecalho do arquivo .KMP
        **/
        cabecalhoKMP* abrir(char* arquivo);
        /**
        *   Função size: retorna o tamanho da lista de objetos em um arquivo binario .kmp
        *   Parâmetros: vazio
        *   Retorno: vazio
        **/
        int size();
        /**
        *   Função clear: apaga a lista de objetos
        *   Parâmetros: vazio
        *   Retorno: vazio
        **/
        void clear();
        /**
        *   Função select: seleciona o objeto que contêm o ponto (x,y,z)
        *   Parâmetros: (x,y,z), ponto que foi clicado na interface
        *   Retorno: 'bool' se foi selecionado algum objeto
        **/
        bool select(float x, float y, float z);
        /**
        *   Função deSelectAll: deseleciona todos os objetos que estavam selecionados
        *   Parâmetros: vazio
        *   Retorno: vazio
        **/
        void deSelectAll();
        /**
        *   Função remove: apaga o objeto que contem o ponto
        *   Parâmetros: (x,y,z) ponto que pertence ao objeto a ser removido
        *   Retorno: 'bool' se removeu algum objeto
        **/
        bool remover(float x, float y, float z);
        /**
        *   Função removeAll: apaga todos os objetos que estao selecionados
        *   Parâmetros: 'vazio'
        *   Retorno: 'vazio'
        **/
        void removeAll();
        ~ListaObjetos();
    private:
        Objeto3D *pri;
        heapEsq *indexId;
        int idDis;

};

#endif // LISTAOBJETOS_H
