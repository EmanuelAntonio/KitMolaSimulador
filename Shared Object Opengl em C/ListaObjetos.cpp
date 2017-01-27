#include "ListaObjetos.h"
#include <iostream>
#include <fstream>
#include <float.h>

using namespace std;

ListaObjetos::ListaObjetos()
{
    pri = NULL;
    idDis = 0;
    tam = 0;
    indexId = new AVL();
    desfazer = new ListaAcao();
    refazer = new ListaAcao();
}
Objeto3D *ListaObjetos::duplicarObj(Objeto3D *obj){

    Objeto3D *objOut = new Objeto3D();
    objOut->setCentro(obj->getCentro()->x,obj->getCentro()->y,obj->getCentro()->z);
    objOut->setExtremidades(obj->getExtremidades()[0],obj->getExtremidades()[1]);
    objOut->setMBR(obj->getMBR()[0].x,obj->getMBR()[0].y,obj->getMBR()[0].z,obj->getMBR()[1].x,obj->getMBR()[1].y,obj->getMBR()[1].z);
    objOut->setId(obj->getId());
    objOut->setProx(NULL);
    objOut->setAnt(NULL);
    return objOut;

}
void ListaObjetos::addCubo(float x, float y, float z){

    if(pri == NULL){

        pri = new Objeto3D();
        pri->setObjeto(0);
        pri->setCentro(x,y,z);
        pri->setMBR(-0.5+x,-0.5+y,-0.5+z,0.5+x,0.5+y,0.5+z);

    }else{

        Objeto3D *aux = new Objeto3D();
        aux->setObjeto(0);
        aux->setCentro(x,y,z);
        aux->setProx(pri);
        pri->setAnt(aux);
        aux->setMBR(-0.5+x,-0.5+y,-0.5+z,0.5+x,0.5+y,0.5+z);
        pri = aux;

    }
    pri->setId(idDis);
    idDis++;
    indexId->insere(pri->getId(),pri);
    desfazer->insere(ADICAO_OBJETOS,duplicarObj(pri));
    refazer->clear();
    tam++;

}
Objeto3D* ListaObjetos::get(){

    return pri;

}
int ListaObjetos::size(){

    return tam;
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
    arq = fopen(arquivo,"rb");
    cabecalhoKMP *c = new cabecalhoKMP;
    fread(c,sizeof(cabecalhoKMP),1,arq);
    objeto obj;
    Objeto3D *ant;
    int idMax = 0;
    clear();
    desfazer = new ListaAcao();
    refazer = new ListaAcao();
    indexId = new AVL();
    if(c->numObj != 0){

        fread(&obj,sizeof(objeto),1,arq);
        pri = new Objeto3D();
        pri->setCentro(obj.centro.x,obj.centro.y,obj.centro.z);
        pri->setMBR(obj.MBR[0].x,obj.MBR[0].y,obj.MBR[0].z,obj.MBR[1].x,obj.MBR[1].y,obj.MBR[1].z);
        pri->setExtremidades(obj.idExtremidades[0], obj.idExtremidades[1]);
        ant = pri;
        pri->setAnt(NULL);
        pri->setProx(NULL);
        indexId->insere(pri->getId(),pri);
        if(pri->getId() > idMax){

            idMax = pri->getId();

        }
        tam++;

    }for(int i = 1; i < c->numObj; i++){

        fread(&obj,sizeof(objeto),1,arq);
        ant->setProx(new Objeto3D());
        ant->getProx()->setAnt(ant);
        ant = ant->getProx();
        ant->setCentro(obj.centro.x,obj.centro.y,obj.centro.z);
        ant->setMBR(obj.MBR[0].x,obj.MBR[0].y,obj.MBR[0].z,obj.MBR[1].x,obj.MBR[1].y,obj.MBR[1].z);
        ant->setExtremidades(obj.idExtremidades[0], obj.idExtremidades[1]);
        tam++;
        if(ant->getId() > idMax){

            idMax = ant->getId();

        }
        indexId->insere(ant->getId(),ant);

    }
    idDis = idMax + 1;
    fclose(arq);
    return c;

}
ListaObjetos::~ListaObjetos()
{
    clear();

}
void ListaObjetos::clear(){

    Objeto3D *aux = NULL;
    tam = 0;
    delete desfazer;
    delete refazer;
    delete indexId;
    while(pri != NULL){

        aux = pri;
        pri = pri->getProx();
        delete aux;

    }

}
bool ListaObjetos::select(float x, float y, float z, Ponto* MBRSelect){

    Objeto3D *aux = pri;
    while(aux != NULL){

        if((aux->getMBR()[0].x - 0.05 <= x) && (aux->getMBR()[0].y - 0.05 <= y) && (aux->getMBR()[0].z - 0.05 <= z)){

            if((aux->getMBR()[1].x + 0.05>= x) && (aux->getMBR()[1].y + 0.05 >= y) && (aux->getMBR()[1].z + 0.05 >= z)){

                aux->setSelecionado(!aux->getSelecionado());
                if(aux->getSelecionado()){

                    if(MBRSelect[0].x > aux->getMBR()[0].x){

                        MBRSelect[0].x = aux->getMBR()[0].x;

                    }
                    if(MBRSelect[0].y > aux->getMBR()[0].y){

                        MBRSelect[0].y = aux->getMBR()[0].y;

                    }
                    if(MBRSelect[0].z > aux->getMBR()[0].z){

                        MBRSelect[0].z = aux->getMBR()[0].z;

                    }
                    if(MBRSelect[1].x < aux->getMBR()[1].x){

                        MBRSelect[1].x = aux->getMBR()[1].x;

                    }
                    if(MBRSelect[1].y < aux->getMBR()[1].y){

                        MBRSelect[1].y = aux->getMBR()[1].y;

                    }
                    if(MBRSelect[1].z < aux->getMBR()[1].z){

                        MBRSelect[1].z = aux->getMBR()[1].z;

                    }

                }else{

                    recalculaMBRSelect(MBRSelect);

                }
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
void ListaObjetos::selectAll(Ponto* MBRSelect){

    Objeto3D *aux = pri;
    while(aux != NULL){

        aux->setSelecionado(true);
        if(MBRSelect[0].x > aux->getMBR()[0].x){

            MBRSelect[0].x = aux->getMBR()[0].x;

        }
        if(MBRSelect[0].y > aux->getMBR()[0].y){

            MBRSelect[0].y = aux->getMBR()[0].y;

        }
        if(MBRSelect[0].z > aux->getMBR()[0].z){

            MBRSelect[0].z = aux->getMBR()[0].z;

        }
        if(MBRSelect[1].x < aux->getMBR()[1].x){

            MBRSelect[1].x = aux->getMBR()[1].x;

        }
        if(MBRSelect[1].y < aux->getMBR()[1].y){

            MBRSelect[1].y = aux->getMBR()[1].y;

        }
        if(MBRSelect[1].z < aux->getMBR()[1].z){

            MBRSelect[1].z = aux->getMBR()[1].z;

        }
        aux = aux->getProx();

    }

}
bool ListaObjetos::remover(float x, float y, float z){
    /**Esta função devera usar uma Arvore R para aumentar o desempenho**/
    Objeto3D *aux = pri;
    while(aux != NULL){

        if((aux->getMBR()[0].x - 0.05 <= x) && (aux->getMBR()[0].y - 0.05 <= y) && (aux->getMBR()[0].z - 0.05 <= z)){

            if((aux->getMBR()[1].x + 0.05>= x) && (aux->getMBR()[1].y + 0.05 >= y) && (aux->getMBR()[1].z + 0.05 >= z)){

                indexId->remover(aux->getId());
                if(aux->getAnt() == NULL){

                    pri = aux->getProx();
                    if(pri != NULL){

                        pri->setAnt(NULL);

                    }

                }else if(aux->getProx() == NULL){

                    aux->getAnt()->setProx(NULL);

                }else{

                    aux->getAnt()->setProx(aux->getProx());
                    aux->getProx()->setAnt(aux->getAnt());

                }
                desfazer->insere(REMOCAO_OBJETOS,duplicarObj(aux));
                delete aux;
                tam--;
                return true;

            }

        }
        aux = aux->getProx();
    }
    return false;

}
void ListaObjetos::removeAll(){

    Objeto3D *aux = pri;
    Objeto3D *refOut = NULL;
    while(aux != NULL){

        if(aux->getSelecionado()){

            indexId->remover(aux->getId());
            if(aux->getAnt() == NULL && aux->getProx() != NULL){

                pri = aux->getProx();
                if(refOut == NULL){

                    refOut = duplicarObj(aux);
                    refOut->setProx(NULL);
                    refOut->setAnt(NULL);

                }else{

                    Objeto3D *ant = duplicarObj(aux);
                    ant->setProx(refOut);
                    refOut->setAnt(ant);
                    refOut = ant;

                }
                delete aux;
                if(pri != NULL){

                    pri->setAnt(NULL);

                }
                aux = pri;

            }else if(aux->getProx() == NULL && aux->getAnt() != NULL){

                aux->getAnt()->setProx(NULL);
                if(refOut == NULL){

                    refOut = duplicarObj(aux);
                    refOut->setProx(NULL);
                    refOut->setAnt(NULL);

                }else{

                    Objeto3D *ant = duplicarObj(aux);
                    ant->setProx(refOut);
                    refOut->setAnt(ant);
                    refOut = ant;

                }
                delete aux;
                aux = NULL;

            }else if(aux->getProx() == NULL && aux->getAnt() == NULL){

                pri = NULL;
                if(refOut == NULL){

                    refOut = duplicarObj(aux);
                    refOut->setProx(NULL);
                    refOut->setAnt(NULL);

                }else{

                    Objeto3D *ant = duplicarObj(aux);
                    ant->setProx(refOut);
                    refOut->setAnt(ant);
                    refOut = ant;

                }
                delete aux;
                aux = NULL;

            }else{

                Objeto3D *prox;
                prox = aux->getProx();
                aux->getAnt()->setProx(aux->getProx());
                aux->getProx()->setAnt(aux->getAnt());
                if(refOut == NULL){

                    refOut = duplicarObj(aux);
                    refOut->setProx(NULL);
                    refOut->setAnt(NULL);

                }else{

                    Objeto3D *ant = duplicarObj(aux);
                    ant->setProx(refOut);
                    refOut->setAnt(ant);
                    refOut = ant;

                }
                delete aux;
                aux = prox;

            }
            tam--;

        }else{

            aux = aux->getProx();

        }
    }
    desfazer->insere(REMOCAO_OBJETOS,refOut);

}
bool ListaObjetos::getCenter(float x, float y, float z, float *center){

    Objeto3D *aux = pri;
    while(aux != NULL){

        if((aux->getMBR()[0].x - 0.05 <= x) && (aux->getMBR()[0].y - 0.05 <= y) && (aux->getMBR()[0].z - 0.05 <= z)){

            if((aux->getMBR()[1].x + 0.05>= x) && (aux->getMBR()[1].y + 0.05 >= y) && (aux->getMBR()[1].z + 0.05 >= z)){

                center[0] = aux->getCentro()->x;
                center[1] = aux->getCentro()->y;
                center[2] = aux->getCentro()->z;
                return true;

            }

        }
        aux = aux->getProx();
    }
    return false;

}
int ListaObjetos::desfazerSize(){

    return desfazer->size();

}
int ListaObjetos::refazerSize(){

    return refazer->size();

}
void ListaObjetos::desfazerAcao(){

    Acao *aux = NULL;
    if(desfazerSize() <= 0){

        return;

    }else{

        aux = desfazer->get();

    }
    if(aux->getAcao() == ADICAO_OBJETOS){

        /**Trata para desfazer a acao de adicionar objetos, ou seja, os remove**/
        Objeto3D *refObj = aux->getObjs();
        Objeto3D *obj = NULL;
        while(refObj != NULL){

            obj = indexId->busca(refObj->getId());
            indexId->remover(refObj->getId());
            if(obj->getAnt() == NULL && obj->getProx() != NULL){

                delete obj;
                pri = pri->getProx();
                if(pri != NULL){

                    pri->setAnt(NULL);

                }

            }else if(obj->getProx() == NULL && obj->getAnt() != NULL){

                obj->getAnt()->setProx(NULL);
                delete obj;

            }else if(obj->getProx() == NULL && obj->getAnt() == NULL){

                pri = NULL;
                delete obj;

            }else{

                obj->getAnt()->setProx(obj->getProx());
                obj->getProx()->setAnt(obj->getAnt());
                delete obj;

            }

            tam--;
            refObj = refObj->getProx();

        }
        refazer->insere(REMOCAO_OBJETOS, aux->getObjs());

    }else if(aux->getAcao() == REMOCAO_OBJETOS){

        /**Trata para desfazer a acao de remover objetos selecionados, ou seja, os adiciona**/
        Objeto3D *refObj = aux->getObjs();
        Objeto3D *obj = NULL;
        while(refObj != NULL){

            obj = duplicarObj(refObj);
            obj->setProx(pri);
            if(pri != NULL){

                pri->setAnt(obj);

            }
            pri = obj;
            indexId->insere(obj->getId(),obj);
            tam++;

            refObj = refObj->getProx();

        }
        refazer->insere(ADICAO_OBJETOS,aux->getObjs());

    }else if(aux->getAcao() == SELECAO_OBJETOS){

        printf("SELECAO_OBJETOS\n");

    }else if(aux->getAcao() == DESELECAO_OBJETOS){

        printf("DESELECAO_OBJETOS\n");

    }

}
void ListaObjetos::refazerAcao(){

    Acao *aux = refazer->get();

    if(aux->getAcao() == ADICAO_OBJETOS){

        /**Trata para refazer a acao de remover objetos que vieram da opcao de desfazer anteriormente**/
        Objeto3D *refObj = aux->getObjs();
        Objeto3D *obj = NULL;
        while(refObj != NULL){

            obj = indexId->busca(refObj->getId());
            indexId->remover(refObj->getId());
            if(obj->getAnt() == NULL && obj->getProx() != NULL){

                delete obj;
                pri = pri->getProx();
                if(pri != NULL){

                    pri->setAnt(NULL);

                }

            }else if(obj->getProx() == NULL && obj->getAnt() != NULL){

                obj->getAnt()->setProx(NULL);
                delete obj;

            }else if(obj->getProx() == NULL && obj->getAnt() == NULL){

                pri = NULL;
                delete obj;

            }else{

                obj->getAnt()->setProx(obj->getProx());
                obj->getProx()->setAnt(obj->getAnt());
                delete obj;

            }

            tam--;
            refObj = refObj->getProx();

        }
        desfazer->insere(REMOCAO_OBJETOS, aux->getObjs());

    }else if(aux->getAcao() == REMOCAO_OBJETOS){

        /**Trata da opcao de reinserir um objeto, quando foi removido por uma acao de desfazer**/
        Objeto3D *refObj = aux->getObjs();
        Objeto3D *obj = NULL;
        while(refObj != NULL){

            obj = duplicarObj(refObj);
            obj->setProx(pri);
            if(pri != NULL){

                pri->setAnt(obj);

            }
            pri = obj;
            indexId->insere(obj->getId(),obj);
            tam++;

            refObj = refObj->getProx();
        }
        desfazer->insere(ADICAO_OBJETOS, aux->getObjs());

    }else if(aux->getAcao() == SELECAO_OBJETOS){

        printf("SELECAO_OBJETOS\n");

    }else if(aux->getAcao() == DESELECAO_OBJETOS){

        printf("DESELECAO_OBJETOS\n");

    }

}
Ponto* ListaObjetos::setFocusToSelect(){

    Ponto *saida = new Ponto();
    saida->x = 0;
    saida->x = 0;
    saida->x = 0;
    Objeto3D *it = pri;
    int cont = 0;
    while(it != NULL){

        if(it->getSelecionado()){

            saida->x += (it->getMBR()[0].x + it->getMBR()[1].x)/2.0;
            saida->y += (it->getMBR()[0].y + it->getMBR()[1].y)/2.0;
            saida->z += (it->getMBR()[0].z + it->getMBR()[1].z)/2.0;
            cont++;

        }
        it = it->getProx();
    }
    if(cont != 0){

        saida->x /= cont;
        saida->y /= cont;
        saida->z /= cont;

    }else{

        delete saida;
        return NULL;

    }
    return saida;

}
void ListaObjetos::moveSelect(float x, float y, float z){

    Objeto3D *aux = pri;
    while(aux != NULL){

        if(aux->getSelecionado()){

            if(aux->getObjeto() == 0){

                aux->setCentro(aux->getCentro()->x + x,aux->getCentro()->y + y,aux->getCentro()->z + z);

            }

        }
        aux = aux->getProx();
    }

}
void ListaObjetos::recalculaMBRSelect(Ponto* MBRSelect){

    MBRSelect[0].x = FLT_MAX;
    MBRSelect[0].y = FLT_MAX;
    MBRSelect[0].z = FLT_MAX;
    MBRSelect[1].x = -FLT_MAX;
    MBRSelect[1].y = -FLT_MAX;
    MBRSelect[1].z = -FLT_MAX;

    Objeto3D *aux = pri;
    while(aux != NULL){

        if(aux->getSelecionado()){
            if(MBRSelect[0].x > aux->getMBR()[0].x){

                MBRSelect[0].x = aux->getMBR()[0].x;

            }
            if(MBRSelect[0].y > aux->getMBR()[0].y){

                MBRSelect[0].y = aux->getMBR()[0].y;

            }
            if(MBRSelect[0].z > aux->getMBR()[0].z){

                MBRSelect[0].z = aux->getMBR()[0].z;

            }
            if(MBRSelect[1].x < aux->getMBR()[1].x){

                MBRSelect[1].x = aux->getMBR()[1].x;

            }
            if(MBRSelect[1].y < aux->getMBR()[1].y){

                MBRSelect[1].y = aux->getMBR()[1].y;

            }
            if(MBRSelect[1].z < aux->getMBR()[1].z){

                MBRSelect[1].z = aux->getMBR()[1].z;

            }

        }
        aux = aux->getProx();
    }

}
