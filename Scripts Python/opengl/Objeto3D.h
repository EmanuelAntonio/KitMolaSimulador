#ifndef OBJETO3D_H
#define OBJETO3D_H
#include <stdlib.h>
#include <stdio.h>

class Ponto{

    public:
        float x;
        float y;
        float z;

};

class Objeto3D
{
    public:
        Objeto3D(){

            objeto = 0;
            prox = NULL;

        }
        void setObjeto(int p){objeto = p;}
        void setProx(Objeto3D *p){prox = p;}
        void setCentro(float x, float y, float z){

            centro.x = x;
            centro.y = y;
            centro.z = z;

        }
        void setExtremidades(float x1, float y1, float z1, float x2, float y2, float z2){

            extremidades[0].x = x1;
            extremidades[0].y = y1;
            extremidades[0].z = z1;
            extremidades[1].x = x2;
            extremidades[1].y = y2;
            extremidades[1].z = z2;

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
        Ponto *getExtremidades(){return extremidades;}
        ~Objeto3D(){}
    private:
        int objeto;/**Referência a qual objeto este nó da lista se refere
                        0 -> Cubo

                    **/
        Ponto centro;/**Parâmetro de desenho, para objetos que precisem**/
        Ponto extremidades[2];/**Parâmetro de desenho, para objetos que precisem**/
        Ponto MBR[2];/**Menor paralelepipedo que engloba todo o objeto**/
        Objeto3D *prox;/**Ponteiro para o proximo nó da lista**/
};
#endif // OBJETO3D_H
