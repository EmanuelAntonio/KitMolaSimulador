#include "ListaObjetos.h"
#include <iostream>
#include <fstream>
#include <float.h>

using namespace std;

ListaObjetos::ListaObjetos()
{
    pri = NULL;
    idDis = 1;
    tam = 0;
    indexId = new AVL();
    desfazer = new ListaAcao();
    refazer = new ListaAcao();
    tamSelect = 0;
}
Objeto3D *ListaObjetos::duplicarObj(Objeto3D *obj){

    Objeto3D *objOut = new Objeto3D();
    objOut->setObjeto(obj->getObjeto());
    objOut->setCentro(obj->getCentro()->x,obj->getCentro()->y,obj->getCentro()->z);
    objOut->setExtremidades(obj->getExtremidades()[0],obj->getExtremidades()[1]);
    objOut->setMBR(obj->getMBR()[0].x,obj->getMBR()[0].y,obj->getMBR()[0].z,obj->getMBR()[1].x,obj->getMBR()[1].y,obj->getMBR()[1].z);
    objOut->setId(obj->getId());
    objOut->setProx(NULL);
    objOut->setAnt(NULL);
    return objOut;

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
    Objeto obj;
    Objeto3D *aux = pri;
    c.numObj = size();
    c.visionAxis = visionAxis;
    c.visionOption = visionOption;
    fwrite(&c,sizeof(cabecalhoKMP),1,arq);
    while(aux != NULL){

        obj.obj = aux->getObjeto();
        obj.id = aux->getId();
        obj.centro = *aux->getCentro();
        obj.MBR[0] = aux->getMBR()[0];
        obj.MBR[1] = aux->getMBR()[1];
        obj.idExtremidades[0] = aux->getExtremidades()[0];
        obj.idExtremidades[1] = aux->getExtremidades()[1];
        fwrite(&obj,sizeof(Objeto),1,arq);
        aux = aux->getProx();
    }
    fclose(arq);

}
cabecalhoKMP* ListaObjetos::abrir(char* arquivo){

    FILE *arq;
    arq = fopen(arquivo,"rb");
    cabecalhoKMP *c = new cabecalhoKMP;
    fread(c,sizeof(cabecalhoKMP),1,arq);
    Objeto obj;
    Objeto3D *ant;
    int idMax = 0;
    clear();
    desfazer = new ListaAcao();
    refazer = new ListaAcao();
    indexId = new AVL();
    if(c->numObj != 0){

        fread(&obj,sizeof(Objeto),1,arq);
        pri = new Objeto3D();
        pri->setCentro(obj.centro.x,obj.centro.y,obj.centro.z);
        pri->setMBR(obj.MBR[0].x,obj.MBR[0].y,obj.MBR[0].z,obj.MBR[1].x,obj.MBR[1].y,obj.MBR[1].z);
        pri->setExtremidades(obj.idExtremidades[0], obj.idExtremidades[1]);
        pri->setObjeto(obj.obj);
        pri->setId(obj.id);
        ant = pri;
        pri->setAnt(NULL);
        pri->setProx(NULL);
        indexId->insere(pri->getId(),pri);
        if(pri->getId() > idMax){

            idMax = pri->getId();

        }
        tam++;

    }for(int i = 1; i < c->numObj; i++){

        fread(&obj,sizeof(Objeto),1,arq);
        ant->setProx(new Objeto3D());
        ant->getProx()->setAnt(ant);
        ant = ant->getProx();
        ant->setCentro(obj.centro.x,obj.centro.y,obj.centro.z);
        ant->setMBR(obj.MBR[0].x,obj.MBR[0].y,obj.MBR[0].z,obj.MBR[1].x,obj.MBR[1].y,obj.MBR[1].z);
        ant->setExtremidades(obj.idExtremidades[0], obj.idExtremidades[1]);
        ant->setObjeto(obj.obj);
        ant->setId(obj.id);
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
int ListaObjetos::select(float x, float y, float z, Ponto* MBRSelect){

    Objeto3D *aux = pri;
    while(aux != NULL){

        if((aux->getMBR()[0].x - 0.05 <= x) && (aux->getMBR()[0].y - 0.05 <= y) && (aux->getMBR()[0].z - 0.05 <= z)){

            if((aux->getMBR()[1].x + 0.05>= x) && (aux->getMBR()[1].y + 0.05 >= y) && (aux->getMBR()[1].z + 0.05 >= z)){

                aux->setSelecionado(!aux->getSelecionado());
                if(aux->getSelecionado()){

                    tamSelect++;
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

                    tamSelect--;
                    recalculaMBRSelect(MBRSelect);

                }
                return aux->getId();

            }

        }
        aux = aux->getProx();
    }
    return 0;
}
void ListaObjetos::deSelectAll(){

    Objeto3D *aux = pri;
    while(aux != NULL){

        aux->setSelecionado(false);
        aux = aux->getProx();

    }
    tamSelect = 0;

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
    tamSelect = tam;

}
bool ListaObjetos::remover(float x, float y, float z){
    /**Esta função devera usar uma Arvore R para aumentar o desempenho**/
    Objeto3D *aux = pri;
    while(aux != NULL){

        if((aux->getMBR()[0].x - 0.05 <= x) && (aux->getMBR()[0].y - 0.05 <= y) && (aux->getMBR()[0].z - 0.05 <= z)){

            if((aux->getMBR()[1].x + 0.05>= x) && (aux->getMBR()[1].y + 0.05 >= y) && (aux->getMBR()[1].z + 0.05 >= z)){

                desfazer->insere(REMOCAO_OBJETOS,duplicarObj(aux));
                deletar(aux);
                return true;

            }

        }
        aux = aux->getProx();
    }
    return false;

}
void ListaObjetos::removeAll(){

    Objeto3D *aux = pri;
    Objeto3D *prox = NULL;
    Objeto3D *refOut = NULL;
    while(aux != NULL){

        if(aux->getSelecionado()){

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
            prox = aux->getProx();
            deletar(aux);
            aux = prox;
        }else{

            aux = aux->getProx();

        }
    }
    desfazer->insere(REMOCAO_OBJETOS,refOut);
    tamSelect = 0;

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
            deletar(obj);
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
bool ListaObjetos::moveSelect(float x, float y, float z){

    Objeto3D *aux = pri;
    if(tamSelect <= 0){

        return false;

    }
    while(aux != NULL){

        if(aux->getSelecionado()){

            if(aux->getObjeto() == SPHERE || aux->getObjeto() == BASE){

                aux->setCentro(aux->getCentro()->x + x,aux->getCentro()->y + y,aux->getCentro()->z + z);
                aux->setMBR(aux->getMBR()[0].x + x,aux->getMBR()[0].y + y,aux->getMBR()[0].z + z,aux->getMBR()[1].x + x,aux->getMBR()[1].y + y,aux->getMBR()[1].z + z);

            }

        }
        aux = aux->getProx();
    }
    return true;
}
void ListaObjetos::recalculaMBRSelect(Ponto* MBRSelect){

    MBRSelect[0].x = FLT_MAX;
    MBRSelect[0].y = FLT_MAX;
    MBRSelect[0].z = FLT_MAX;
    MBRSelect[1].x = -FLT_MAX;
    MBRSelect[1].y = -FLT_MAX;
    MBRSelect[1].z = -FLT_MAX;

    if(tamSelect <= 0){

        return;

    }
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
void ListaObjetos::addSphere(float x, float y, float z){

    float erro = 0.0;
    if(pri == NULL){

        pri = new Objeto3D();
        pri->setObjeto(SPHERE);
        pri->setCentro(x,y,z);
        pri->setMBR(-SPHERE_RADIUS + erro + x,-SPHERE_RADIUS+ erro + y,-SPHERE_RADIUS + erro + z,SPHERE_RADIUS + erro + x,SPHERE_RADIUS + erro + y,SPHERE_RADIUS + erro + z);
        pri->setAnt(NULL);
        pri->setProx(NULL);

    }else{

        Objeto3D *aux = new Objeto3D();
        aux->setObjeto(SPHERE);
        aux->setCentro(x,y,z);
        aux->setProx(pri);
        pri->setAnt(aux);
        aux->setMBR(-SPHERE_RADIUS + erro + x,-SPHERE_RADIUS+ erro + y,-SPHERE_RADIUS + erro + z,SPHERE_RADIUS + erro + x,SPHERE_RADIUS + erro + y,SPHERE_RADIUS + erro + z);
        pri = aux;

    }
    pri->setId(idDis);
    idDis++;
    indexId->insere(pri->getId(),pri);
    desfazer->insere(ADICAO_OBJETOS,duplicarObj(pri));
    refazer->clear();
    tam++;

}
bool ListaObjetos::addBar(int tipoBar){

    int id1,id2;
    Objeto3D *objId1;
    Objeto3D *objId2;
    if(tamSelect != 2){

        return false;

    }else{

        Objeto3D *aux = pri;
        int cont = 0;
        while(cont < 2){

            if(aux->getSelecionado()){

                if(aux->getObjeto() != SPHERE){

                    return false;

                }else{
                    if(cont == 0){

                        id1 = aux->getId();
                        objId1 = aux;

                    }else{

                        id2 = aux->getId();
                        objId2 = aux;

                    }
                    cont++;

                }

            }
            aux = aux->getProx();

        }

    }
    if(tipoBar == BAR_SMALL){

        float dist = sqrt(pow(objId1->getCentro()->x - objId2->getCentro()->x,2)
                          + pow(objId1->getCentro()->y - objId2->getCentro()->y,2)
                          + pow(objId1->getCentro()->z - objId2->getCentro()->z,2)) - 2*SPHERE_RADIUS;
        if(dist < BAR_LENGTH_SMALL - 0.01 || dist > BAR_LENGTH_SMALL + 0.01){

            return false;

        }

    }else if(tipoBar == BAR_LARGE){

        float dist = sqrt(pow(objId1->getCentro()->x - objId2->getCentro()->x,2)
                          + pow(objId1->getCentro()->y - objId2->getCentro()->y,2)
                          + pow(objId1->getCentro()->z - objId2->getCentro()->z,2)) - 2*SPHERE_RADIUS;

        if(dist < BAR_LENGTH_LARGE - 0.01 || dist > BAR_LENGTH_LARGE + 0.01){

            return false;

        }

    }
    float xMBR, yMBR, zMBR, XMBR, YMBR, ZMBR;
    if(pri == NULL){

        pri = new Objeto3D();
        pri->setObjeto(tipoBar);
        pri->setExtremidades(id1,id2);


    }else{

        Objeto3D *aux = new Objeto3D();
        aux->setObjeto(tipoBar);
        aux->setProx(pri);
        aux->setExtremidades(id1,id2);
        pri->setAnt(aux);
        pri = aux;

    }
    if(objId1->getCentro()->x < objId2->getCentro()->x){

        xMBR = objId1->getCentro()->x - BAR_RADIUS;
        XMBR = objId2->getCentro()->x + BAR_RADIUS;

    }else{

        XMBR = objId1->getCentro()->x + BAR_RADIUS;
        xMBR = objId2->getCentro()->x - BAR_RADIUS;

    }
    if(objId1->getCentro()->y < objId2->getCentro()->y){

        yMBR = objId1->getCentro()->y - BAR_RADIUS;
        YMBR = objId2->getCentro()->y + BAR_RADIUS;

    }else{

        YMBR = objId1->getCentro()->y + BAR_RADIUS;
        yMBR = objId2->getCentro()->y - BAR_RADIUS;

    }
    if(objId1->getCentro()->z < objId2->getCentro()->z){

        zMBR = objId1->getCentro()->z - BAR_RADIUS;
        ZMBR = objId2->getCentro()->z + BAR_RADIUS;

    }else{

        ZMBR = objId1->getCentro()->z + BAR_RADIUS;
        zMBR = objId2->getCentro()->z - BAR_RADIUS;

    }
    pri->setMBR(xMBR, yMBR, zMBR, XMBR, YMBR, ZMBR);
    pri->setId(idDis);
    pri->setSelecionado(true);
    idDis++;
    indexId->insere(pri->getId(),pri);
    desfazer->insere(ADICAO_OBJETOS,duplicarObj(pri));
    refazer->clear();
    tam++;
    return true;

}
Objeto3D* ListaObjetos::getbyId(int id){

    return indexId->busca(id);

}
float ListaObjetos::distObjsSelect(){

    if(tamSelect != 2){

        return -1;

    }else{

        Objeto3D *aux = pri;
        Objeto3D *obj1 = NULL;
        while(aux != NULL){

            if(aux->getSelecionado()){

                if(obj1 == NULL){

                   obj1 = aux;

                }else{

                    return sqrt((pow(obj1->getCentro()->x - aux->getCentro()->x, 2))+
                                (pow(obj1->getCentro()->y - aux->getCentro()->y, 2))+
                                (pow(obj1->getCentro()->z - aux->getCentro()->z, 2))) - 2*SPHERE_RADIUS;

                }

            }

            aux = aux->getProx();

        }
        return -1;
    }

}
Objeto3D* ListaObjetos::getObj(double *ponto){

        Objeto3D *aux = pri;
        while(aux != NULL){


            if((aux->getMBR()[0].x - 0.05 <= ponto[0]) && (aux->getMBR()[0].y - 0.05 <= ponto[1]) && (aux->getMBR()[0].z - 0.05 <= ponto[2])){

                if((aux->getMBR()[1].x + 0.05>= ponto[0]) && (aux->getMBR()[1].y + 0.05 >= ponto[1]) && (aux->getMBR()[1].z + 0.05 >= ponto[2])){

                        return aux;

                }

            }

        }
        return NULL;

}
bool ListaObjetos::moveObj(int id, float x, float y, float z){

    Objeto3D *aux = indexId->busca(id);
    if(aux == NULL){

        return false;

    }
    if(aux->getObjeto() == SPHERE){

        aux->setCentro(x,y,z);
        aux->setMBR(-SPHERE_RADIUS + x,-SPHERE_RADIUS + y,-SPHERE_RADIUS + z,SPHERE_RADIUS + x,SPHERE_RADIUS + y,SPHERE_RADIUS + z);

    }
    return true;
}
void ListaObjetos::deletar(Objeto3D *p){

    if(p != NULL){

        indexId->remover(p->getId());
        if(p->getAnt() == NULL){

            pri = p->getProx();
            if(pri != NULL){

                pri->setAnt(NULL);

            }

        }else if(p->getProx() == NULL){

            p->getAnt()->setProx(NULL);

        }else{

            p->getAnt()->setProx(p->getProx());
            p->getProx()->setAnt(p->getAnt());

        }
        if(p->getSelecionado()){

            tamSelect--;

        }
        delete p;
        tam--;

    }

}
bool ListaObjetos::duplicaSelect(){

    Objeto3D *aux = pri;
    Objeto3D *prox = NULL;
    if(tamSelect <= 0){

        return false;

    }
    while(aux != NULL){

        if(aux->getSelecionado()){

            prox = duplicarObj(aux);
            prox->setProx(pri);
            prox->setSelecionado(true);
            pri->setAnt(prox);
            pri = prox;
            aux->setSelecionado(false);

        }
        aux = aux->getProx();
    }
    return true;
}
void ListaObjetos::addBase(float x, float y, float z){

    float erro = 0.0;
    if(pri == NULL){

        pri = new Objeto3D();
        pri->setObjeto(BASE);
        pri->setCentro(x,y,z);
        pri->setMBR(-BASE_RADIUS + erro + x,-BASE_RADIUS + erro + y,-SPHERE_RADIUS + erro + z,BASE_RADIUS + erro + x,BASE_RADIUS + erro + y,erro + z);
        pri->setAnt(NULL);
        pri->setProx(NULL);

    }else{

        Objeto3D *aux = new Objeto3D();
        aux->setObjeto(BASE);
        aux->setCentro(x,y,z);
        aux->setProx(pri);
        pri->setAnt(aux);
        aux->setMBR(-BASE_RADIUS + erro + x,-BASE_RADIUS + erro + y,-SPHERE_RADIUS + erro + z,BASE_RADIUS + erro + x,BASE_RADIUS + erro + y,erro + z);
        pri = aux;

    }
    pri->setId(idDis);
    idDis++;
    indexId->insere(pri->getId(),pri);
    desfazer->insere(ADICAO_OBJETOS,duplicarObj(pri));
    refazer->clear();
    tam++;

}
