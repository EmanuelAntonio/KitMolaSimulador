#include "include/GL/glut.h"
#include "ListaObjetos.cpp"


extern "C"{

    char visionAxis = 'z';
    int visionOption = 0;

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

}
