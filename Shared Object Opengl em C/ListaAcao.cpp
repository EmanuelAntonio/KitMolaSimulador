#include "ListaAcao.h"

ListaAcao::ListaAcao()
{
    pri = NULL;
    tam = 0;
}
void ListaAcao::insere(int acao, Objeto3D *objs){

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
ListaAcao::~ListaAcao()
{
    Acao *aux = pri;
    while(pri != NULL){

        delete aux;
        aux = pri;
        pri = pri->getProx();

    }
}
