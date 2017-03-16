#include "include/GL/glut.h"
#include "ListaObjetos.cpp"


extern "C"{

    int tamGrid; ///Define o tamanho do grid a ser exibido na tela
    Ponto MBRSelect[2]; ///MBR que engloba todos os objetos que estao selecionados
    ListaObjetos *l;
    Ponto MBRMoveX[4]; ///MBR que engloba as setas de movimento no eixo X(posicoes 0 e 1 para positivo, 2 e 3 para negativo)
    Ponto MBRMoveY[4]; ///MBR que engloba as setas de movimento no eixo Y(posicoes 0 e 1 para positivo, 2 e 3 para negativo)
    Ponto MBRMoveZ[4]; ///MBR que engloba as setas de movimento no eixo Z(posicoes 0 e 1 para positivo, 2 e 3 para negativo)
    float espacoGrid; /// Espaçamento das marcações do grid
    GLfloat object_ambient[] = {0.5,0.5,0.5,1.0};
    GLfloat object_brilho[]    = { 128.0 };
    GLfloat object_especular[] = { 1.0, 1.0, 1.0, 1.0 };
    GLfloat object_select[] = {0.0, 0.5, 1.0};
    float meshQual; /// Qualidade da malha
    bool wireframe; /// Variavel que armazena se será exibido em modo wireframe


    /**
	*	->Função init:
	*		Inicializa todos as variaveis do kit
	*	->Parâmetros: vazio
	*	->Retorno: vazio
	**/
    void init();

    void initGL();
	/**
	*	->Função drawAxis:
	*		Desenha os eixos cartesianos no centro do espaco R^3
	*	->Parâmetros: vazio
	*	->Retorno: vazio
	**/
	void drawAxis(char visionAxis);
    /**
	*	->Função drawAxisZero:
	*		Desenha os eixos cartesianos no centro do espaco R^3 na posicão original
	*	->Parâmetros: vazio
	*	->Retorno: vazio
	**/
	void drawAxisZero();
	/**
	*	->Função drawAxisX:
	*		Desenha os eixos cartesianos no centro do espaco R^3 quando o eixo 'pra cima' selecionado é o X
	*	->Parâmetros: vazio
	*	->Retorno: vazio
	**/
    void drawGrid(char visionAxis);
    /**
	*   ->Função drawSphere:
	*		Desenha uma esfera de ligacao em uma posicao do espaco
	*	->Parâmetros: 'x','y','z' é a posição do centro da esfera e 'selected' se esta selecionada
	*	->Retorno: vazio
	**/
    void drawSphere(float x, float y, float z, bool selected,char visionAxis);
    /**
	*   ->Função drawSphereZero:
	*		Desenha uma esfera de ligacao na origem
	*	->Parâmetros: 'bool', se a esfera está selecionada, se estiver desenha de uma outra cor
	*	->Retorno: vazio
	**/
    void drawSphereZero(bool selected, GLfloat *object_difusa);
    /**
	*   ->Função drawBar:
	*		Desenha uma barra entre duas esferas de id1 e id2
	*	->Parâmetros: 'id1' 'id2', ids das esferas que ligam as  duas pontas da barra
	*	->Retorno: 'vazio'
	**/
    void drawBar(int id1, int id2, bool selecionado,char visionAxis);
    /**
	*   ->Função drawBarZero:
	*		Desenha uma barra na origem
	*	->Parâmetros: 'tamBar' tamanho da barra a ser desenhada
    *	->Retorno: 'vazio'
	**/
    void drawBarZero(Ponto *p1, Ponto *p2,float radius,int subdivisions,GLUquadricObj *quadric, bool selecionado, GLfloat *object_difusa);
    /**
	*   ->Função drawSphere:
	*		Desenha uma base em uma posicao do espaco
	*	->Parâmetros: 'x','y','z' é a posição do centro da semi-esfera e 'selected' se esta selecionada
	*	->Retorno: vazio
	**/
    void drawBase(float x, float y, float z, bool selected,char visionAxis);
    /**
	*   ->Função setTamGrid:
	*		Altera a variável tamGrid
	*	->Parâmetros: 'int', novo valor da variável tamGrid
	*	->Retorno: 'int', retorna o modo de visao armazenado em tamGrid
	**/
    void setTamGrid(int p);
    /**
	*   ->Função getTamGrid:
	*		Retorna a variável tamGrid
	*	->Parâmetros: vazio
	*	->Retorno: 'int', valor da variável tamGrid
	**/
    int getTamGrid();
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
    void drawCena(char visionAxis,int visionOption);
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
    int select(double *ponto, char visionAxis);
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
    void drawMoveAxis(char visionAxis, int visionOption, float zoom);
    /**
    *   Função drawMoveAxisZero: desenha os eixos de movimento dos objetos na cena na origem, eh usado em na funcao drawMoveAxis
    *   Parâmetros: 'vazio'
    *   Retorno: 'vazio'
    **/
    void drawMoveAxisZero(int visionOption, float zoom);
    /**
    *   Função drawSetaMove: desenha uma parte
    *   Parâmetros: 'vazio'
    *   Retorno: 'vazio'
    **/
    void drawSetaMove(float zoom);
    /**
    *   Função resetMBRSelect: inicializa todos os parametros de MBRSelect com os valores maximos e minimos
    *   Parâmetros: 'vazio'
    *   Retorno: 'vazio'
    **/
    void resetMBRSelect();
    /**
    *   Função selectMoveSeta: retorna se o ponto pertence a alguma seta de movimento
    *   Parâmetros: (x,y,z) ponto em R^3
    *   Retorno: 'int' -1 -> nao pertence a nenhuma seta
    *                   0 -> pertence a X positivo
    *                   1 -> pertence a X negativo
    *                   2 -> pertence a Y positivo
    *                   3 -> pertence a Y negativo
    *                   4 -> pertence a Z positivo
    *                   5 -> pertence a Z negativo
    **/
    int selectMoveSeta(double *ponto, char visionAxis);
    /**
	*   ->Função addSphere:
	*		Adiciona uma esfera de ligação na lista de objetos com o centro em x,y,z
	*	->Parâmetros: x,y,z, centro da esfera
	*	->Retorno: 'vazio'
	**/
    void addSphere(float x, float y, float z);
    /**
	*   ->Função addSphere:
	*		verifica se o ponto pertence a MBRSelect
	*	->Parâmetros: 'double*', vetor de 3 posições que representa ponto a ser verificado
	*	->Retorno: 'bool' se pertence ou não à MBR
	**/
    bool MBRSelectPonto(double *ponto);
    /**
	*   ->Função addBar:
	*		Adiciona uma barra na lista de objetos ligando duas eferas com ids 'id1' e 'id2'
	*	->Parâmetros: 'id1', 'id2' ids das esferas
	*	->Retorno: 'bool' se a adição foi realizada
	**/
    bool addBar(int tipoBar);
    /**
	*   ->Função setEspacoGrid:
	*		Altera o espaçamento entre o grid
	*	->Parâmetros: 'tam' novo valor da variavel
	*	->Retorno: 'vazio'
	**/
    void setEspacoGrid(float tam);
    /**
	*   ->Função getEspacoGrid:
	*		Retorna o valor da variéavel espacoGrid
	*	->Parâmetros: 'vazio'
	*	->Retorno: 'float' valor da variável
	**/
    float getEspacoGrid();
    /**
	*   ->Função distObjsSelect:
	*		Retorna o valor da distância entre dois objetos selecionados
	*	->Parâmetros: 'vazio'
	*	->Retorno: 'float' valor da distâcia
	**/
    float distObjsSelect();
    /**
	*   ->Função setWireframe:
	*		Altera o valor da variavel wireframe
	*	->Parâmetros: 'vazio'
	*	->Retorno: 'vazio'
	**/
    void setWireframe(bool w);
    /**
	*   ->Função getWireframe:
	*		Retorna o valor da variavel wireframe
	*	->Parâmetros: 'vazio'
	*	->Retorno: 'bool' o valor da variável
	**/
    bool getWireframe();
    /**
	*   ->Função setMeshQual:
	*		Altera o valor da variavel meshQual
	*	->Parâmetros: 'vazio'
	*	->Retorno: 'vazio'
	**/
    void setMeshQual(float p);
    /**
	*   ->Função getMeshQual:
	*		Retorna o valor da variável meshQual
	*	->Parâmetros: 'vazio'
	*	->Retorno: 'float' valor da variável
	**/
    int getMeshQual();
    /**
	*   ->Função getObjById:
	*		Retorna um struct do tipo objeto com o 'id' passado como parâmetro
	*	->Parâmetros: 'id' parâmetro do objeto a ser retornado
	*	->Retorno: 'Objeto' struct que representa um objeto da classe Objeto3D
	**/
    Objeto *getObjById(int id);
    /**
    *   Função moveObj: move todos os objetos selecionados
    *   Parâmetros: (x,y,z) a quantidade que sera movido por eixo e 'id' é o ID do objeto a ser movido
    *   Retorno: 'vazio'
    **/
    void moveObj(int id, float x, float y, float z);
    /**
    *   Função moveObjSelect: move todos os objetos selecionados
    *   Parâmetros: (x,y,z) a quantidade que sera movido por eixo
    *   Retorno: 'vazio'
    **/
    void moveObjSelect(float x, float y, float z);
    /**
    *   Função duplicaSelect: duplica objetos da cena
    *   Parâmetros: (x,y,z) a quantidade que sera movido por eixo
    *   Retorno: 'vazio'
    **/
    bool duplicaSelect();
    /**
	*   ->Função addBase:
	*		Adiciona uma base na lista de objetos com o centro da semi-esfera em x,y,z
	*	->Parâmetros: x,y,z, centro da semi-esfera
	*	->Retorno: 'vazio'
	**/
    void addBase(float x, float y, float z);
    /**
	*   ->Função getCentroMBRSelect:
	*		Retorna o centro do MBRSelect
	*	->Parâmetros: 'vazio'
	*	->Retorno: 'Ponto*' centro do MBRSelect
	**/
    Ponto* getCentroMBRSelect();
    /**
	*   ->Função addBase:
	*		Adiciona uma laje na lista de objetos
	*	->Parâmetros: 'vazio'
	*	->Retorno: 'bool' se o objeto foi adicionado na lista de objetos
	**/
    bool addLaje();
    /**
	*   ->Função drawLaje:
	*		Desenha uma laje entre p1 até p4, onde esses pontos são centros das esferas que ligam essa laje
	*	->Parâmetros: 'p1','p2,'p3','p4', pontos dos "vertices" na laje
	*	->Retorno: 'vazio'
	**/
    void drawLaje(Ponto *p1, Ponto *p2, Ponto *p3, Ponto *p4, bool selected);

}
