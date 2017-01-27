#include "include/GL/glut.h"
#include "ListaObjetos.cpp"


extern "C"{

    char visionAxis; ///Eixo principal para visao, usado na visao ortogonal
    int visionOption; ///Define qual visão estpa ativa no momento
    int tamGrid; ///Define o tamanho do grid a ser exibido na tela
    Ponto MBRSelect[2]; ///MBR que engloba todos os objetos que estao selecionados
    ListaObjetos *l;
    Ponto MBRMoveX[4]; ///MBR que engloba as setas de movimento no eixo X(posicoes 0 e 1 para positivo, 2 e 3 para negativo)
    Ponto MBRMoveY[4]; ///MBR que engloba as setas de movimento no eixo Y(posicoes 0 e 1 para positivo, 2 e 3 para negativo)
    Ponto MBRMoveZ[4]; ///MBR que engloba as setas de movimento no eixo Z(posicoes 0 e 1 para positivo, 2 e 3 para negativo)


    /**
	*	->Função init:
	*		Inicializa todos as variaveis do kit
	*	->Parâmetros: vazio
	*	->Retorno: vazio
	**/
    void init();
	/**
	*	->Função drawAxis:
	*		Desenha os eixos cartesianos no centro do espaco R^3
	*	->Parâmetros: vazio
	*	->Retorno: vazio
	**/
	void drawAxis();
	/**
	*	->Função drawAxisX:
	*		Desenha os eixos cartesianos no centro do espaco R^3 quando o eixo 'pra cima' selecionado é o X
	*	->Parâmetros: vazio
	*	->Retorno: vazio
	**/
	void drawAxisX();
	/**
	*   ->Função drawAxisY:
	*		Desenha os eixos cartesianos no centro do espaco R^3 quando o eixo 'pra cima' selecionado é o Y
	*	->Parâmetros: vazio
	*	->Retorno: vazio
	**/
    void drawAxisY();
    /**
	*   ->Função drawGrid:
	*		Desenha o grid no plano XY
	*	->Parâmetros: vazio
	*	->Retorno: vazio
	**/
    void drawGrid();
    /**
	*   ->Função drawCube:
	*		Desenha um cubo em uma posição do espaço
	*	->Parâmetros: 'x','y','z' é a posição do centro do cubo e 'selected' se o cubo está selecionado
	*	->Retorno: vazio
	**/
    void drawCube(float x, float y, float z, bool selected);
    /**
	*   ->Função drawCubeZero:
	*		Desenha um cubo na origem
	*	->Parâmetros: 'bool', se o cubo está selecionado, se estiver desenha de uma outra cor
	*	->Retorno: vazio
	**/
    void drawCubeZero(bool selected);
    /**
	*   ->Função setVisionAxis:
	*		Altera a variável visionAxis
	*	->Parâmetros: 'c' é o novo valor da variavel visionAxis
	*	->Retorno: vazio
	**/
    void setVisionAxis(char c);
    /**
	*   ->Função getVisionAxis:
	*		Retorna a variável visionAxis
	*	->Parâmetros: vazio
	*	->Retorno: 'char', retorna o caracter armazenado em visionAxis
	**/
    char getVisionAxis();
    /**
	*   ->Função setVisionOption:
	*		Altera a variável visionOption
	*	->Parâmetros: 'p' é o novo valor da variavel visionOption
	*	->Retorno: vazio
	**/
    void setVisionOption(int p);
    /**
	*   ->Função getVisionOption:
	*		Retorna a variável visionOption
	*	->Parâmetros: vazio
	*	->Retorno: 'int', retorna o modo de visao armazenado em visionAxis
	**/
    int getVisionOption();
    /**
	*   ->Função setTamGrid:
	*		Altera a variável tamGrid
	*	->Parâmetros: 'p' é o novo valor da variavel tamGrid
	*	->Retorno: vazio
	**/
    void setTamGrid(int p);
    /**
	*   ->Função getTamGrid:
	*		Retorna a variável visionOption
	*	->Parâmetros: vazio
	*	->Retorno: 'int', retorna o modo de visao armazenado em tamGrid
	**/
    int getTamGrid();
    /**
	*   ->Função addCubo:
	*		Adiciona um cubo na lista de objetos com o centro em x,y,z
	*	->Parâmetros: x,y,z, centro do cubo
	*	->Retorno: vazio
	**/
    void addCubo(float x, float y, float z);
    /**
	*   ->Função tamanhoListaObjetos:
	*		Retorna o tamanho da lista de objetos
	*	->Parâmetros: vazio
	*	->Retorno: 'int'
	**/
    int tamanhoListaObjetos();
    /**
	*   ->Função drawCena:
	*		Desenha todos os objetos da lista de objetos
	*	->Parâmetros: vazio
	*	->Retorno: 'int'
	**/
    void drawCena();
    /**
	*   ->Função save:
	*		Salva a lista de objetos em um arquivo .kmp
	*	->Parâmetros: "char* arquivo" é o arquivo de destino
	*	->Retorno: 'vazio'
	**/
    void save(char* arquivo);
    /**
	*   ->Função open:
	*		Abre um projeto em um arquivo .kmp
	*	->Parâmetros: "char*" é o arquivo a ser aberto
	*	->Retorno: 'vazio'
	**/
    void open(char* arquivo);
    /**
	*   ->Função getPonto3D:
	*		Converte um ponto da janela em seu respectivo ponto 3d da cena
	*	->Parâmetros: (x,y) ponto da janela
	*	->Retorno: (float[3])(x,y,z) ponto em 3d da cena
	**/
    double* getPonto3D(int x, int y);
    /**
	*   ->Função getPonto3DFloat:
	*		Converte um ponto da janela em seu respectivo ponto 3d da cena
	*	->Parâmetros: (x,y) ponto da janela, 'ponto' ponto em 3d da cena
	*	->Retorno: 'vazio'
	**/
    void getPonto3DFloat(int x, int y, float *ponto);
    /**
	*   ->Função select:
	*       Seleciona um objeto da cena de acordo com o ponto passado cmo parametro
	*	->Parâmetros: 'double*' um ponto em R^3
	*	->Retorno: 'bool' se o select encontrou algum objeto que corresponde ao ponto passado
	**/
    bool select(double *ponto);
    /**
	*   ->Função deSelectAll:
	*       Desseleciona todos os objetos da cena
	*	->Parâmetros: 'vazio'
	*	->Retorno: 'vazio'
	**/
    void deSelectAll();
    /**
	*   ->Função remove:
	*       Deleta um objeto da cena
	*	->Parâmetros: 'double*' um ponto em R^3 que pertence ao objeto
	*	->Retorno: 'bool' se o remove encontrou algum objeto que corresponde ao ponto passado
	**/
    bool remover(double *ponto);
    /**
    *   Função removeAll: apaga todos os objetos que estao selecionados
    *   Parâmetros: 'vazio'
    *   Retorno: 'vazio'
    **/
    void removeAll();
    /**
    *   Função selectAll: seleciona todos os objetos da cena
    *   Parâmetros: 'vazio'
    *   Retorno: 'vazio'
    **/
    void selectAll();
    /**
    *   Função Clear: apaga todos os objetos da cena
    *   Parâmetros: 'vazio'
    *   Retorno: 'vazio'
    **/
    void clear();
    /**
    *   Função getCenter: retorna o centro de um objeto que contem o ponto(x,y,z)
    *   Parâmetros: 'ponto' ponto que pertence a um objeto, 'center' é o vetor de trez coordenadas que pertence ao objeto
    *   Retorno: 'vazio'
    **/
    bool getCenter(double *ponto, float *center);
    /**
    *   Função desfazer: desfaz a ultima ação feita pelo usuario
    *   Parâmetros: 'vazio'
    *   Retorno: 'vazio'
    **/
    void desfazer();
    /**
    *   Função refazer: refaz uma ultima ação desfeita
    *   Parâmetros: 'vazio'
    *   Retorno: 'vazio'
    **/
    void refazer();
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
    *   Função setFocusToSelect: gera o centro geometrico de todos os objetos selecionados
    *   Parâmetros: 'float*' vetor de 3 posicoes que sera usado para retornar o "centro de massa"
    *   Retorno: 'bool' retorna se havia algum objeto selecionado, se sim, centro contem o centro geometrico, se nao, desconsidera centro
    **/
    bool setFocusToSelect(float* centro);
    /**
    *   Função moveSelect: move todos os objetos selecionados
    *   Parâmetros: (x,y,z) a quantidade que sera movido por eixo
    *   Retorno: 'vazio'
    **/
    void moveSelect(float x, float y, float z);
    /**
    *   Função drawMoveAxis: desenha os eixos de movimento dos objetos na cena, para isso utiliza a MBRSelect
    *   Parâmetros: 'vazio'
    *   Retorno: 'vazio'
    **/
    void drawMoveAxis();
    /**
    *   Função drawMoveAxisZero: desenha os eixos de movimento dos objetos na cena na origem, eh usado em na funcao drawMoveAxis
    *   Parâmetros: 'vazio'
    *   Retorno: 'vazio'
    **/
    void drawMoveAxisZero();
    /**
    *   Função drawSetaMove: desenha uma parte
    *   Parâmetros: 'vazio'
    *   Retorno: 'vazio'
    **/
    void drawSetaMove();
    /**
    *   Função resetMBRSelect: inicializa todos os parametros de MBRSelect com os valores maximos e minimos
    *   Parâmetros: 'vazio'
    *   Retorno: 'vazio'
    **/
    void resetMBRSelect();
    /**
    *   Função resetMBRSelect: retorna se o ponto pertence a alguma seta de movimento
    *   Parâmetros: (x,y,z) ponto em R^3
    *   Retorno: 'int' -1 -> nao pertence a nenhuma seta
    *                   0 -> pertence a X positivo
    *                   1 -> pertence a X negativo
    *                   2 -> pertence a Y positivo
    *                   3 -> pertence a Y negativo
    *                   4 -> pertence a Z positivo
    *                   5 -> pertence a Z negativo
    **/
    int selectMoveSeta(double *ponto);
    void drawMBRSeta();

}
