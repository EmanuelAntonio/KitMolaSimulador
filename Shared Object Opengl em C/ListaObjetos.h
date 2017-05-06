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
        *   Fun��o addSphere: Adiciona uma esfera de ligacao � lista de objetos na cena
        *   Par�metros: 'x','y','z', coordenadas do centro da esfera de ligacao
        *   Retorno: vazio
        **/
        void addSphere(float x, float y, float z);
        /**
        *   Fun��o addBar: Adiciona uma barra na lista de objetos da cena
        *   Par�metros: 'tipoBar' constante referente ao tipo da barra que ir� ser inserida, BAR_SMALL ou BAR_LARGE
        *   Retorno: vazio
        **/
        bool addBar(int tipoBar);
        /**
        *   Fun��o addBase: Adiciona uma base na cena
        *   Par�metros: 'x','y','z', coordenadas do centro da semi-esfera da base
        *   Retorno: vazio
        **/
        void addBase(int subtipo, float x, float y, float z);
        /**
        *   Fun��o get: retorna uma refer�ncia para o primeiro no da lista
        *   Par�metro: vazio
        *   Retorno: vazio
        **/
        Objeto3D* get();
        /**
        *   Fun��o salvar: Salva a lista de objetos em um arquivo binario .kmp
        *   Par�metros: 'arquivo' string com o diret�rio do arquivo a ser salvo, 'visionAxis' qual o tipo de visao
        *   Retorno: vazio
        **/
        void salvar(char* arquivo,int tamGrid, float meshQual, float espacoGrid);
        /**
        *   Fun��o abrir: abre um projeto salvo em um arquivo binario .kmp
        *   Par�metros: 'arquivo' string com o diret�rio do arquivo a ser aberto
        *   Retorno: 'cabecalhoKMP' retorna parametros adicionais salvos no cabecalho do arquivo .KMP
        **/
        cabecalhoKMP* abrir(char* arquivo);
        /**
        *   Fun��o size: retorna o tamanho da lista de objetos em um arquivo binario .kmp
        *   Par�metros: vazio
        *   Retorno: vazio
        **/
        int size();
        /**
        *   Fun��o clear: apaga a lista de objetos
        *   Par�metros: vazio
        *   Retorno: vazio
        **/
        void clear();
        /**
        *   Fun��o select: seleciona o objeto que cont�m o ponto (x,y,z)
        *   Par�metros: (x,y,z), ponto que foi clicado na interface, 'MBRSelect' MBR que engloba todos os objetos selecionados
        *   Retorno: 'bool' se foi selecionado algum objeto
        **/
        int select(float x, float y, float z, Ponto* MBRSelect);
        /**
        *   Fun��o deSelectAll: deseleciona todos os objetos que estavam selecionados
        *   Par�metros: vazio
        *   Retorno: vazio
        **/
        void deSelectAll();
        /**
        *   Fun��o remove: apaga o objeto que contem o ponto
        *   Par�metros: (x,y,z) ponto que pertence ao objeto a ser removido
        *   Retorno: 'bool' se removeu algum objeto
        **/
        bool remover(float x, float y, float z);
        /**
        *   Fun��o removeAll: apaga todos os objetos que estao selecionados
        *   Par�metros: 'vazio'
        *   Retorno: 'vazio'
        **/
        void removeAll();
        /**
        *   Fun��o getCenter: retorna o centro de um objeto que contem o ponto(x,y,z)
        *   Par�metros: (x,y,z) ponto que pertence a um objeto, 'center' � o vetor de trez coordenadas que pertence ao objeto
        *   Retorno: 'vazio'
        **/
        bool getCenter(float x, float y, float z, float *center);
        /**
        *   Fun��o desfazerAcao: desfaz a ultima a��o feita pelo usuario
        *   Par�metros: 'vazio'
        *   Retorno: 'vazio'
        **/
        void desfazerAcao(Ponto *MBRSelect);
        /**
        *   Fun��o refazerAcao: refaz uma ultima a��o desfeita
        *   Par�metros: 'vazio'
        *   Retorno: 'vazio'
        **/
        void refazerAcao(Ponto *MBRSelect);
        /**
        *   Fun��o desfazerSize: retorna o tamanho da lista de desfazerAcao
        *   Par�metros: 'vazio'
        *   Retorno: 'int' tamanho da lista desfazerAcao
        **/
        int desfazerSize();
        /**
        *   Fun��o refazerSize: retorna o tamanho da lista de refazerAcao
        *   Par�metros: 'vazio'
        *   Retorno: 'int' tamanho da lista refazerAcao
        **/
        int refazerSize();
        /**
        *   Fun��o selectAll: seleciona todos os objetos
        *   Par�metros: 'MBRSelect' MBR que engloba todos os objetos selecionados
        *   Retorno: 'vazio'
        **/
        void selectAll(Ponto* MBRSelect);
        /**
        *   Fun��o setFocusToSelect: gera o centro gemometrico de todos os objetos selecionados
        *   Par�metros: 'vazio'
        *   Retorno: 'Ponto' ponto onde se encontra o centro gemometrico dos objetos
        **/
        Ponto* setFocusToSelect();
        /**
        *   Fun��o moveSelect: move todos os objetos selecionados
        *   Par�metros: (x,y,z) a quantidade que sera movido por eixo
        *   Retorno: 'vazio'
        **/
        bool moveSelect(float x, float y, float z);
        /**
        *   Fun��o recalculaMBRSelect: recalcula o MBRSelect
        *   Par�metros: 'Ponto*' a MBR que armazena a MBR de todos os objetos selecionados
        *   Retorno: 'vazio'
        **/
        void recalculaMBRSelect(Ponto* MBRSelect);
        /**
        *   Fun��o getById: retorna o objeto que tem id
        *   Par�metros: 'id' ID do objeto a ser buscado
        *   Retorno: 'Objeto3D*' o objeto que contem o 'id'
        **/
        Objeto3D* getbyId(int id);
        /**
        *   ->Fun��o distObjsSelect:
        *		retorna o valor da dist�ncia entre dois objetos selecionados
        *	->Par�metros: 'vazio'
        *	->Retorno: 'float' valor da dist�cia
        **/
        float distObjsSelect();
        /**
        *   ->Fun��o getObj:
        *		Retorna o objeto cujo "*ponto" pertence
        *	->Par�metros: '*ponto' vetor de 3 posi��es correspondente a XYZ
        *	->Retorno: 'Objeto3D' objeto que "*ponto" pertence
        **/
        Objeto3D* getObj(double *ponto);
        bool addLaje();
        /**
        *   Fun��o moveObj: move todos os objetos selecionados
        *   Par�metros: (x,y,z) a quantidade que sera movido por eixo e 'id' � o ID do objeto a ser movido
        *   Retorno: 'vazio'
        **/
        bool moveObj(int id, float x, float y, float z);
        /**
        *   Fun��o duplicaSelect: duplica objetos da cena
        *   Par�metros: (x,y,z) a quantidade que sera movido por eixo
        *   Retorno: 'vazio'
        **/
        bool duplicaSelect();
        /**
        *   Fun��o terminaMovimentacao: termina a a��o de movimentar objetos, ou seja, adiciona a a��o na lista de desfazer
        *   Par�metros: 'Ponto' vetor deslocamento de toda a movimenta��o feita at� o momento
        *   Retorno: 'vazio'
        **/
        void terminaMovimentacao(Ponto vetDes);
        /**
        *   Fun��o addDiagonal: Adiciona uma diagonal na lista de objetos da cena
        *   Par�metros: 'tipoDiag' constante referente ao tipo da barra que ir� ser inserida, DIAGONAL_SMALL ou DIAGONAL_LARGE
        *   Retorno: 'bool' se a diagonal foi adicionada a lista
        **/
        bool addDiagonal(int tipoDiag);
        /**
        *   ->Fun��o addDiag:
        *		Adiciona uma liga��o r�gida quando h� uma esfera e duas barras selecionadas ou uma barra e uma base
        *	->Par�metros: 'vazio'
        *	->Retorno: 'bool' se a adi��o foi realizada
        **/
        bool addLigRigida();
        int getNumSelect(){return tamSelect;}
        ~ListaObjetos();
    private:

        /**
        *   Fun��o duplicarOBJ: cria uma refer�ncia ao objeto original 'OBJ', usado nas listas de refazer e desfazer
        *   Par�metros: 'Objeto3D*', objeto original que ser� criado uma referencia
        *   Retorno: 'Objeto3D*', refer�ncia ao objeto original
        **/
        Objeto3D *duplicarObj(Objeto3D *obj);
        /**
        *   Fun��o deletar: deleta o objeto 'p' que foi passado como par�metro
        *   Par�metros: 'Objeto3D*', objeto que ser� deletado da lista
        *   Retorno: 'void'
        **/
        void deletar(Objeto3D *p, bool completo);
        Objeto3D *pri;
        int idDis; ///ID disponivel para a proxima inser��o
        ListaAcao *desfazer;
        ListaAcao *refazer;
        AVL *indexId;
        int tam;
        int tamSelect;

};

#endif // LISTAOBJETOS_H
