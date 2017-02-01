#ifndef LISTAOBJETOS_H
#define LISTAOBJETOS_H
#include "ListaAcao.cpp"
#include "AVL.cpp"
#include <math.h>

class ListaObjetos
{
    public:
        ListaObjetos();
        /**
        *   Fun��o addCubo: Adiciona um cubo � lista de objetos na cena
        *   Par�metros: 'x','y','z', coordenadas do centro do cubo
        *   Retorno: vazio
        **/
        void addCubo(float x, float y, float z);
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
        void salvar(char* arquivo,char visionAxis, int visionOption);
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
        bool select(float x, float y, float z, Ponto* MBRSelect);
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
        void desfazerAcao();
        /**
        *   Fun��o refazerAcao: refaz uma ultima a��o desfeita
        *   Par�metros: 'vazio'
        *   Retorno: 'vazio'
        **/
        void refazerAcao();
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
        void moveSelect(float x, float y, float z);
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
        ~ListaObjetos();
    private:

        Objeto3D *duplicarObj(Objeto3D *obj);
        Objeto3D *pri;
        int idDis; ///ID disponivel para a proxima inser��o
        ListaAcao *desfazer;
        ListaAcao *refazer;
        AVL *indexId;
        int tam;
        int tamSelect;

};

#endif // LISTAOBJETOS_H
