#include "ListaObjetos.h"

ListaObjetos::ListaObjetos()
{
    pri = NULL;
}
void ListaObjetos::addCubo(float x, float y, float z){

    if(pri == NULL){

        pri = new Objeto3D();
        pri->setObjeto(0);
        pri->setCentro(x,y,z);

    }else{

        Objeto3D *aux = new Objeto3D();
        aux->setObjeto(0);
        aux->setCentro(x,y,z);
        aux->setProx(pri);
        pri = aux;

    }

}
Objeto3D* ListaObjetos::get(){

    return pri;

}
int ListaObjetos::size(){

    int cont = 0;
    Objeto3D *aux = pri;
    while(aux != NULL){

        cont++;
        aux= aux->getProx();

    }
    return cont;
}
ListaObjetos::~ListaObjetos()
{
    Objeto3D *aux = NULL;
    while(pri != NULL){

        aux = pri;
        pri = pri->getProx();
        delete aux;

    }

}
