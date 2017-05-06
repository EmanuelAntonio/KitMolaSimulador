#ifndef OBJETO3D_H
#define OBJETO3D_H
#include <stdlib.h>
#include <stdio.h>
#include "ManipularVetor.h"

#define SPHERE 1
#define BAR_SMALL 2
#define BAR_LARGE 3
#define BASE 4
#define LAJE 5
#define DIAGONAL_SMALL 6
#define DIAGONAL_LARGE 7
#define LIGACAO_RIGIDA 8
#define BASE_LIVRE 9
#define BASE_BLOQUEADA_X 10
#define BASE_BLOQUEADA_Y 11
#define BASE_BLOQUEADA_XY 12

#define SPHERE_RADIUS 0.75 /// em centimetros
#define BAR_RADIUS 0.3 /// em centimetros
#define BAR_LENGTH_SMALL 7.5 /// em Centimetros
#define BAR_LENGTH_LARGE 16.5 /// em centimetros
#define BASE_RADIUS 2.2 /// em centimetros
#define LAJE_LENGTH 17.3 /// em centimetros
#define LAJE_WIDTH 8.3 /// em centimetros
#define LAJE_THICKNESS 0.6 /// em centimetros
#define LAJE_LEG 0.0 /// em centimetros - catetos que formam o tringulo faltante nas bordas da laje
#define DIAGONAL_LENGTH_SMALL 11.22 /// em centimetros
#define DIAGONAL_LENGTH_LARGE 18.625 /// em centimetros
#define LIGACAO_RIGIDA_ALTURA 1.0 ///em centimetros
#define LIGACAO_RIGIDA_BASE_MAIOR 2.6 ///em centimetros
#define LIGACAO_RIGIDA_BASE_MENOR 0.8 ///em centímetros


/**Struct cabecalhoKMP: cabeçalho do arquivo binario do projeto .kmp**/
struct cabecalhoKMP{

    int numObj;
    int tamGrid;
    float meshQual;
    float espacoGrid;

};

/**Struct objeto: armazena um objeto3d para armazenamento no arquivo binario do projeto .kmp**/
typedef struct objeto{

    int obj;
    int id;
    Ponto centro;
    Ponto MBR[2];
    int idExtremidades[16];
    int tamExtremidades;
    int subObjeto;

}Objeto;

/** Classe Objeto3D: um nó da lista de objetos, armazena informacoes essenciais sobre um objeto da cena**/
class Objeto3D
{
    public:
        Objeto3D();
        void setObjeto(int p);
        void setProx(Objeto3D *p);
        void setSelecionado(bool sel);
        void setCentro(float x, float y, float z);
        void setMBR(float x1, float y1, float z1, float x2, float y2, float z2);
        int getObjeto();
        Objeto3D* getProx();
        Ponto *getMBR();
        Ponto *getCentro();
        int *getExtremidades();
        int getTamExtremidades();
        void setTamExtremidades(int tam);
        bool getSelecionado();
        int getId();
        void setId(int i);
        Objeto3D *getAnt();
        void setAnt(Objeto3D *o);
        void addExtremidades(int id);
        void removeExtremidades(int id);
        void swapExtremidades(int id1, int id2);
        bool buscaIdExtremidades(int id);
        Ponto *getForca();
        void setForca(Ponto f, Ponto aplicacao);

        virtual void draw(float meshQual, bool wireframe, char visionAxis, int visionOption);
        virtual void draw(float meshQual, bool wireframe, char visionAxis, int visionOption, Objeto3D *obj1, Objeto3D *obj2);
        virtual void draw(float meshQual, bool wireframe, char visionAxis, int visionOption, Ponto *p1, Ponto *p2, Ponto *p3, Ponto *p4);
        virtual void draw(float mehQual, bool wireframe, char visionAxis, int visionOption, Objeto3D *obj1, Objeto3D *obj2, Objeto3D *obj3);

        virtual ~Objeto3D();
    private:

        int objeto;/**Referência a qual objeto este nó da lista se refere
                        0 -> Cubo
                        1 -> Esfera
                        3 -> Barra Pequena
                        4 -> Barra Grande
                        ...
                    **/
        int idExtremidades[16];/**Parâmetro de desenho, para objetos que precisem**/
        int tamExtremidades;
        int id;
        Ponto MBR[2];/**Menor paralelepipedo que engloba todo o objeto, menor ponto e maior ponto repectivamente**/
        Objeto3D *prox;/**Ponteiro para o proximo nó da lista**/
        Objeto3D *ant;/**Ponteiro para o nó anterior da lista**/

    protected:
        GLfloat *object_difusa;
        bool selecionado;/**Variavel que armazena se este objeto está selecionado**/
        GLfloat *object_ambient;
        GLfloat *object_brilho;
        GLfloat *object_especular;
        GLfloat *object_select;
        Ponto centro;/**Parâmetro de desenho, para objetos que precisem**/
        Ponto forca[2];///vetor forca e ponto de aplicação respectivamente
};
#endif // OBJETO3D_H
