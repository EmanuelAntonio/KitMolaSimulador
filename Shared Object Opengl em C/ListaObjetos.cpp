#include "ListaObjetos.h"
#include <iostream>
#include <fstream>

using namespace std;

ListaObjetos::ListaObjetos()
{
    pri = NULL;
    indexId = new heapEsq();
    idDis = 0;
}
void ListaObjetos::addCubo(float x, float y, float z){

    if(pri == NULL){

        pri = new Objeto3D();
        pri->setObjeto(0);
        pri->setCentro(x,y,z);
        pri->setMBR(-0.5+x,-0.5+y,-0.5+z,0.5+x,0.5+y,0.5+z);
        pri->setId(idDis);

    }else{

        Objeto3D *aux = new Objeto3D();
        aux->setObjeto(0);
        aux->setCentro(x,y,z);
        aux->setProx(pri);
        aux->setMBR(-0.5+x,-0.5+y,-0.5+z,0.5+x,0.5+y,0.5+z);
        pri = aux;

    }
    indexId->insere(idDis,pri);

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
        obj.idExtremidades[0] = aux->getExtremidades()[0];
        obj.idExtremidades[1] = aux->getExtremidades()[1];
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
    clear();
    indexId = new heapEsq();
    if(c->numObj != 0){

        fread(&obj,sizeof(objeto),1,arq);
        pri = new Objeto3D();
        pri->setCentro(obj.centro.x,obj.centro.y,obj.centro.z);
        pri->setMBR(obj.MBR[0].x,obj.MBR[0].y,obj.MBR[0].z,obj.MBR[1].x,obj.MBR[1].y,obj.MBR[1].z);
        pri->setExtremidades(obj.idExtremidades[0], obj.idExtremidades[1]);
        ant = pri;
        indexId->insere(pri->getId(),pri);

    }for(int i = 1; i < c->numObj; i++){

        fread(&obj,sizeof(objeto),1,arq);
        ant->setProx(new Objeto3D());
        ant = ant->getProx();
        ant->setCentro(obj.centro.x,obj.centro.y,obj.centro.z);
        ant->setMBR(obj.MBR[0].x,obj.MBR[0].y,obj.MBR[0].z,obj.MBR[1].x,obj.MBR[1].y,obj.MBR[1].z);
        ant->setExtremidades(obj.idExtremidades[0], obj.idExtremidades[1]);
        indexId->insere(ant->getId(),ant);

    }
    fclose(arq);
    return c;

}
ListaObjetos::~ListaObjetos()
{
    clear();


}
void ListaObjetos::clear(){

    Objeto3D *aux = NULL;
    while(pri != NULL){

        aux = pri;
        pri = pri->getProx();
        delete aux;

    }
    delete indexId;

}
bool ListaObjetos::select(float x, float y, float z){

    Objeto3D *aux = pri;
    while(aux != NULL){

        if((aux->getMBR()[0].x - 0.05 <= x) && (aux->getMBR()[0].y - 0.05 <= y) && (aux->getMBR()[0].z - 0.05 <= z)){

            if((aux->getMBR()[1].x + 0.05>= x) && (aux->getMBR()[1].y + 0.05 >= y) && (aux->getMBR()[1].z + 0.05 >= z)){

                aux->setSelecionado(!aux->getSelecionado());
                return true;

            }

        }
        aux = aux->getProx();
    }
    return false;
}
void ListaObjetos::deSelectAll(){

    Objeto3D *aux = pri;
    while(aux != NULL){

        aux->setSelecionado(false);
        aux = aux->getProx();

    }

}
bool ListaObjetos::remover(float x, float y, float z){

    Objeto3D *aux = pri;
    Objeto3D *ant = NULL;
    while(aux != NULL){

        if((aux->getMBR()[0].x - 0.05 <= x) && (aux->getMBR()[0].y - 0.05 <= y) && (aux->getMBR()[0].z - 0.05 <= z)){

            if((aux->getMBR()[1].x + 0.05>= x) && (aux->getMBR()[1].y + 0.05 >= y) && (aux->getMBR()[1].z + 0.05 >= z)){

                if(ant == NULL){

                    pri = aux->getProx();

                }else{

                    ant->setProx(aux->getProx());

                }
                indexId->remover(aux->getId());
                delete aux;
                return true;

            }

        }
        ant = aux;
        aux = aux->getProx();
    }
    return false;

}
void ListaObjetos::removeAll(){

    Objeto3D *aux = pri;
    Objeto3D *ant = NULL;
    while(aux != NULL){

        if(aux->getSelecionado()){

            if(ant == NULL){

                pri = aux->getProx();
                indexId->remover(aux->getId());
                delete aux;
                ant = NULL;
                aux = pri;

            }else{

                ant->setProx(aux->getProx());
                indexId->remover(aux->getId());
                delete aux;
                aux = ant->getProx();

            }

        }else{

            ant = aux;
            aux = aux->getProx();

        }
    }

}
