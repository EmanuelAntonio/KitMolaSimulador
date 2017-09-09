#ifndef NO_H
#define NO_H
#include <stdlib.h>
#include "Objeto3D.h"

class No
{
    public:

        No(){
            proximo = NULL;
            anterior = NULL;
             obj = NULL;
        };
        ~No(){};
        No* getProx(){return proximo;}
        No* getAnt(){return anterior;}
        int getValor(){return valor;}
        int getMarca(){return marca;}
        void setProx(No* p){proximo = p;}
        void setAnt(No* a){anterior = a;}
        void setValor(int v){valor = v;}
        void setMarca(int m){marca = m;}
        int getAltura(){return altura;}
        void setAltura(int p){altura = p;}
        Objeto3D *getObj(){return obj;}
        void setObj(Objeto3D *o){obj = o;}
    private:
        No* proximo;
        No* anterior;
        int valor;
        int marca;
        int altura;
        Objeto3D *obj;

};

#endif // NO_H
