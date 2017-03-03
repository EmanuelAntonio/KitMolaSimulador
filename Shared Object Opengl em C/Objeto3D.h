#ifndef OBJETO3D_H
#define OBJETO3D_H
#include <stdlib.h>
#include <stdio.h>

#define SPHERE 1
#define BAR_SMALL 2
#define BAR_LARGE 3
#define BASE 4
#define LAJE 5
#define DIAGONAL_SMALL 6
#define DIAGONAL_LARGE 7
#define LIGACAO_RIGIDA 8

#define SPHERE_RADIUS 0.75 /// em centimetros
#define BAR_RADIUS 0.3 /// em centimetros
#define BAR_LENGTH_SMALL 7.5 /// em Centrimetros
#define BAR_LENGTH_LARGE 16.5 /// em centrimetros
#define BASE_RADIUS 2.2 /// em centrimetros


/**Struct cabecalhoKMP: cabeçalho do arquivo binario do projeto .kmp**/
struct cabecalhoKMP{

    int numObj;
    int tamGrid;
    float meshQual;
    float espacoGrid;

};
/**Struct Ponto: armazena um ponto em R^3**/
struct Ponto{

    float x;
    float y;
    float z;

};
/**Struct objeto: armazena um objeto3d para armazenamento no arquivo binario do projeto .kmp**/
typedef struct objeto{

    int obj;
    int id;
    Ponto centro;
    Ponto MBR[2];
    int idExtremidades[16];
    int tamExtremidades;

}Objeto;
/** Classe Objeto3D: um nó da lista de objetos, armazena informacoes essenciais sobre um objeto da cena**/
class Objeto3D
{
    public:
        Objeto3D(){

            objeto = 0;
            prox = NULL;
            ant = NULL;
            selecionado = false;
            tamExtremidades = 0;

        }
        void setObjeto(int p){objeto = p;}
        void setProx(Objeto3D *p){prox = p;}
        void setSelecionado(bool sel){selecionado = sel;}
        void setCentro(float x, float y, float z){

            centro.x = x;
            centro.y = y;
            centro.z = z;

        }
        void setMBR(float x1, float y1, float z1, float x2, float y2, float z2){

            MBR[0].x = x1;
            MBR[0].y = y1;
            MBR[0].z = z1;
            MBR[1].x = x2;
            MBR[1].y = y2;
            MBR[1].z = z2;

        }
        int getObjeto(){return objeto;}
        Objeto3D* getProx(){return prox;}
        Ponto *getMBR(){return MBR;}
        Ponto *getCentro(){return &centro;}
        int *getExtremidades(){return idExtremidades;}
        int getTamExtremidades(){return tamExtremidades;}
        void setTamExtremidades(int tam){tamExtremidades = tam;}
        bool getSelecionado(){return selecionado;}
        int getId(){return id;}
        void setId(int i){id = i;}
        Objeto3D *getAnt(){return ant;}
        void setAnt(Objeto3D *o){ant = o;}
        void addExtremidades(int id){

            idExtremidades[tamExtremidades] = id;
            tamExtremidades++;

        }
        void removeExtremidades(int id){

            int idE = -1;
            for(int i = 0; i < tamExtremidades; i++){

                if(idExtremidades[i] == id){

                    idE = i;
                    break;

                }

            }
            if(idE != -1){

                for(int i = idE; i < tamExtremidades - 1; i++){

                    idExtremidades[i] = idExtremidades[i+1];

                }
                tamExtremidades--;
            }

        }
        bool buscaIdExtremidades(int id){

            for(int i = 0; i < tamExtremidades; i++){

                if(idExtremidades[i] == id){

                    return true;

                }

            }
            return false;
        }
        ~Objeto3D(){}
    private:
        int objeto;/**Referência a qual objeto este nó da lista se refere
                        0 -> Cubo
                        1 -> Esfera
                        3 -> Barra Pequena
                        4 -> Barra Grande
                    **/
        Ponto centro;/**Parâmetro de desenho, para objetos que precisem**/
        int idExtremidades[16];/**Parâmetro de desenho, para objetos que precisem**/
        int tamExtremidades;
        int id;
        Ponto MBR[2];/**Menor paralelepipedo que engloba todo o objeto, menor ponto e maior ponto repectivamente**/
        bool selecionado;/**Variavel que armazena se este objeto está selecionado**/
        Objeto3D *prox;/**Ponteiro para o proximo nó da lista**/
        Objeto3D *ant;/**Ponteiro para o nó anterior da lista**/
};
#endif // OBJETO3D_H
