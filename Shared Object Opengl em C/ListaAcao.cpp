#include "ListaAcao.h"
#include <iostream>
using namespace std;
ListaAcao::ListaAcao()
{
    pri = NULL;
    tam = 0;
}
void ListaAcao::insere(int acao, Objeto3D *objs, Ponto *vetDes){

    if(pri == NULL){

        pri = new Acao();
        pri->setAcao(acao);
        pri->setObjs(objs);

    }else{

        Acao *aux = new Acao();
        aux->setAcao(acao);
        aux->setObjs(objs);
        aux->setProx(pri);
        pri = aux;

    }
    if(vetDes != NULL){


        pri->setVetDes(vetDes->x, vetDes->y, vetDes->z);

    }
    tam++;

}
Acao* ListaAcao::get(){

    if(tam == 0){

        return NULL;

    }else{

        Acao *aux = pri;
        pri = pri->getProx();
        tam--;
        return aux;

    }

}
int ListaAcao::size(){

    return tam;

}
void ListaAcao::clear(){

    Acao *aux = pri;
    while(pri != NULL){

        aux = pri;
        pri = pri->getProx();
        delete aux;

    }
    pri = NULL;
    tam = 0;

}
ListaAcao::~ListaAcao()
{
    clear();
}
