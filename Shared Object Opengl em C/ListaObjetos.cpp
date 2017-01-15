#include "ListaObjetos.h"
#include <iostream>
#include <fstream>

using namespace std;

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
void ListaObjetos::salvar(char* arquivo, char visionAxis, int visionOption){

    remove(arquivo);
    FILE *arq;
    arq = fopen(arquivo,"ab");
    cabecalhoKMP c;
    objeto obj;
    Objeto3D *aux = pri;
    c.numObj = size();
    c.visionAxis = visionAxis;
    c.visionOption = visionOption;
    fwrite(&c,sizeof(cabecalhoKMP),1,arq);
    while(aux != NULL){

        obj.obj = aux->getObjeto();
        obj.centro = *aux->getCentro();
        obj.MBR[0] = aux->getMBR()[0];
        obj.MBR[1] = aux->getMBR()[1];
        obj.extremidades[0] = aux->getExtremidades()[0];
        obj.extremidades[1] = aux->getExtremidades()[1];
        fwrite(&obj,sizeof(objeto),1,arq);
        aux = aux->getProx();
    }
    fclose(arq);

}
cabecalhoKMP* ListaObjetos::abrir(char* arquivo){

    FILE *arq;
    arq = fopen(arquivo,"a+b");
    cabecalhoKMP *c = new cabecalhoKMP;
    fread(c,sizeof(cabecalhoKMP),1,arq);
    objeto obj;
    Objeto3D *ant;
    if(c->numObj != 0){

        fread(&obj,sizeof(objeto),1,arq);
        pri = new Objeto3D();
        pri->setCentro(obj.centro.x,obj.centro.y,obj.centro.z);
        pri->setMBR(obj.MBR[0].x,obj.MBR[0].y,obj.MBR[0].z,obj.MBR[1].x,obj.MBR[1].y,obj.MBR[1].z);
        pri->setExtremidades(obj.extremidades[0].x,obj.extremidades[0].y,obj.extremidades[0].z,obj.extremidades[1].x,obj.extremidades[1].y,obj.extremidades[1].z);
        ant = pri;

    }for(int i = 1; i < c->numObj; i++){

        fread(&obj,sizeof(objeto),1,arq);
        ant->setProx(new Objeto3D());
        ant = ant->getProx();
        ant->setCentro(obj.centro.x,obj.centro.y,obj.centro.z);
        ant->setMBR(obj.MBR[0].x,obj.MBR[0].y,obj.MBR[0].z,obj.MBR[1].x,obj.MBR[1].y,obj.MBR[1].z);
        ant->setExtremidades(obj.extremidades[0].x,obj.extremidades[0].y,obj.extremidades[0].z,obj.extremidades[1].x,obj.extremidades[1].y,obj.extremidades[1].z);

    }
    fclose(arq);
    return c;

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
