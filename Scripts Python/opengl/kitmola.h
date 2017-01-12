#include "include/GL/glut.h"
#include "ListaObjetos.cpp"

extern "C"{

    char visionAxis = 'z';
    ListaObjetos *l = new ListaObjetos();
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
	*	->Parâmetros: 'x','y','z' é a posição do centro do cubo
	*	->Retorno: vazio
	**/
    void drawCube(float x, float y, float z);
    /**
	*   ->Função drawCubeZero:
	*		Desenha um cubo na origem
	*	->Parâmetros: vazio
	*	->Retorno: vazio
	**/
    void drawCubeZero();
    /**
	*   ->Função setVisionAxis:
	*		Altera a variável visionAxis
	*	->Parâmetros: 'c' é o novo valor da variavel visionAxis
	*	->Retorno: vazio
	**/
    void setVisionAxis(char c);
    /**
	*   ->Função setVisionAxis:
	*		Retorna a variável visionAxis
	*	->Parâmetros: 'char', retorna o caracter armazenado em visionAxis
	*	->Retorno: vazio
	**/
    char getVisionAxis();
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


}
