#ifndef LISTAOBJETOS_H
#define LISTAOBJETOS_H
#include "ListaAcao.cpp"
#include "AVL.cpp"
#include "ManipularVetor.h"
#include "Sphere.cpp"
#include "Bar.cpp"
#include "Base.cpp"
#include "Laje.cpp"
#include "Tirante.cpp"
#include "LigRigida.cpp"

class ListaObjetos
{
    public:
        ListaObjetos();
        /**
        *   Função addSphere: Adiciona uma esfera de ligacao à lista de objetos na cena
        *   Parâmetros: 'x','y','z', coordenadas do centro da esfera de ligacao
        *   Retorno: vazio
        **/
        void addSphere(float x, float y, float z);
        /**
        *   Função addBar: Adiciona uma barra na lista de objetos da cena
        *   Parâmetros: 'tipoBar' constante referente ao tipo da barra que irá ser inserida, BAR_SMALL ou BAR_LARGE
        *   Retorno: vazio
        **/
        bool addBar(int tipoBar);
        /**
        *   Função addBase: Adiciona uma base na cena
        *   Parâmetros: 'x','y','z', coordenadas do centro da semi-esfera da base
        *   Retorno: vazio
        **/
        void addBase(int subtipo, float x, float y, float z);
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
        void salvar(char* arquivo,int tamGrid, float meshQual, float espacoGrid);
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
        *   Parâmetros: (x,y,z), ponto que foi clicado na interface, 'MBRSelect' MBR que engloba todos os objetos selecionados
        *   Retorno: 'bool' se foi selecionado algum objeto
        **/
        int select(float x, float y, float z, Ponto* MBRSelect);
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
        /**
        *   Função getCenter: retorna o centro de um objeto que contem o ponto(x,y,z)
        *   Parâmetros: (x,y,z) ponto que pertence a um objeto, 'center' é o vetor de trez coordenadas que pertence ao objeto
        *   Retorno: 'vazio'
        **/
        bool getCenter(float x, float y, float z, float *center);
        /**
        *   Função desfazerAcao: desfaz a ultima ação feita pelo usuario
        *   Parâmetros: 'vazio'
        *   Retorno: 'vazio'
        **/
        void desfazerAcao(Ponto *MBRSelect);
        /**
        *   Função refazerAcao: refaz uma ultima ação desfeita
        *   Parâmetros: 'vazio'
        *   Retorno: 'vazio'
        **/
        void refazerAcao(Ponto *MBRSelect);
        /**
        *   Função desfazerSize: retorna o tamanho da lista de desfazerAcao
        *   Parâmetros: 'vazio'
        *   Retorno: 'int' tamanho da lista desfazerAcao
        **/
        int desfazerSize();
        /**
        *   Função refazerSize: retorna o tamanho da lista de refazerAcao
        *   Parâmetros: 'vazio'
        *   Retorno: 'int' tamanho da lista refazerAcao
        **/
        int refazerSize();
        /**
        *   Função selectAll: seleciona todos os objetos
        *   Parâmetros: 'MBRSelect' MBR que engloba todos os objetos selecionados
        *   Retorno: 'vazio'
        **/
        void selectAll(Ponto* MBRSelect);
        /**
        *   Função setFocusToSelect: gera o centro gemometrico de todos os objetos selecionados
        *   Parâmetros: 'vazio'
        *   Retorno: 'Ponto' ponto onde se encontra o centro gemometrico dos objetos
        **/
        Ponto* setFocusToSelect();
        /**
        *   Função moveSelect: move todos os objetos selecionados
        *   Parâmetros: (x,y,z) a quantidade que sera movido por eixo
        *   Retorno: 'vazio'
        **/
        bool moveSelect(float x, float y, float z);
        /**
        *   Função recalculaMBRSelect: recalcula o MBRSelect
        *   Parâmetros: 'Ponto*' a MBR que armazena a MBR de todos os objetos selecionados
        *   Retorno: 'vazio'
        **/
        void recalculaMBRSelect(Ponto* MBRSelect);
        /**
        *   Função getById: retorna o objeto que tem id
        *   Parâmetros: 'id' ID do objeto a ser buscado
        *   Retorno: 'Objeto3D*' o objeto que contem o 'id'
        **/
        Objeto3D* getbyId(int id);
        /**
        *   ->Função distObjsSelect:
        *		retorna o valor da distância entre dois objetos selecionados
        *	->Parâmetros: 'vazio'
        *	->Retorno: 'float' valor da distâcia
        **/
        float distObjsSelect();
        /**
        *   ->Função getObj:
        *		Retorna o objeto cujo "*ponto" pertence
        *	->Parâmetros: '*ponto' vetor de 3 posições correspondente a XYZ
        *	->Retorno: 'Objeto3D' objeto que "*ponto" pertence
        **/
        Objeto3D* getObj(double *ponto);
        bool addLaje();
        /**
        *   Função moveObj: move todos os objetos selecionados
        *   Parâmetros: (x,y,z) a quantidade que sera movido por eixo e 'id' é o ID do objeto a ser movido
        *   Retorno: 'vazio'
        **/
        bool moveObj(int id, float x, float y, float z);
        /**
        *   Função duplicaSelect: duplica objetos da cena
        *   Parâmetros: (x,y,z) a quantidade que sera movido por eixo
        *   Retorno: 'vazio'
        **/
        bool duplicaSelect();
        /**
        *   Função terminaMovimentacao: termina a ação de movimentar objetos, ou seja, adiciona a ação na lista de desfazer
        *   Parâmetros: 'Ponto' vetor deslocamento de toda a movimentação feita até o momento
        *   Retorno: 'vazio'
        **/
        void terminaMovimentacao(Ponto vetDes);
        /**
        *   Função addDiagonal: Adiciona uma diagonal na lista de objetos da cena
        *   Parâmetros: 'tipoDiag' constante referente ao tipo da barra que irá ser inserida, DIAGONAL_SMALL ou DIAGONAL_LARGE
        *   Retorno: 'bool' se a diagonal foi adicionada a lista
        **/
        bool addDiagonal(int tipoDiag);
        /**
        *   ->Função addDiag:
        *		Adiciona uma ligação rígida quando há uma esfera e duas barras selecionadas ou uma barra e uma base
        *	->Parâmetros: 'vazio'
        *	->Retorno: 'bool' se a adição foi realizada
        **/
        bool addLigRigida();
        int getNumSelect(){return tamSelect;}
        ~ListaObjetos();
    private:

        /**
        *   Função duplicarOBJ: cria uma referência ao objeto original 'OBJ', usado nas listas de refazer e desfazer
        *   Parâmetros: 'Objeto3D*', objeto original que será criado uma referencia
        *   Retorno: 'Objeto3D*', referência ao objeto original
        **/
        Objeto3D *duplicarObj(Objeto3D *obj);
        /**
        *   Função deletar: deleta o objeto 'p' que foi passado como parâmetro
        *   Parâmetros: 'Objeto3D*', objeto que será deletado da lista
        *   Retorno: 'void'
        **/
        void deletar(Objeto3D *p, bool completo);
        Objeto3D *pri;
        int idDis; ///ID disponivel para a proxima inserção
        ListaAcao *desfazer;
        ListaAcao *refazer;
        AVL *indexId;
        int tam;
        int tamSelect;

};

#endif // LISTAOBJETOS_H
