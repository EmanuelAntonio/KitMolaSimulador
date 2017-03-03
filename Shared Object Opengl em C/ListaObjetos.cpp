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
    for(int i = 0; i < obj->getTamExtremidades(); i++){

        objOut->addExtremidades(obj->getExtremidades()[i]);

    }
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
void ListaObjetos::salvar(char* arquivo,int tamGrid, float meshQual, float espacoGrid){

    remove(arquivo);
    FILE *arq;
    arq = fopen(arquivo,"ab");
    cabecalhoKMP c;
    Objeto obj;
    Objeto3D *aux = pri;
    c.numObj = size();
    c.meshQual = meshQual;
    c.tamGrid = tamGrid;
    c.espacoGrid = espacoGrid;
    fwrite(&c,sizeof(cabecalhoKMP),1,arq);
    while(aux != NULL){

        obj.obj = aux->getObjeto();
        obj.id = aux->getId();
        obj.centro = *aux->getCentro();
        obj.MBR[0] = aux->getMBR()[0];
        obj.MBR[1] = aux->getMBR()[1];
        obj.tamExtremidades = aux->getTamExtremidades();
        for(int i = 0; i < aux->getTamExtremidades(); i++){

            obj.idExtremidades[i] = aux->getExtremidades()[i];

        }
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
        for(int i = 0; i < obj.tamExtremidades; i++){

            pri->addExtremidades(obj.idExtremidades[i]);

        }
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
        for(int i = 0; i < obj.tamExtremidades; i++){

            ant->addExtremidades(obj.idExtremidades[i]);

        }
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

                desfazer->insere(REMOCAO_OBJETOS,duplicarObj(aux),NULL);
                deletar(aux,true);
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
            deletar(aux,true);
            aux = prox;
        }else{

            aux = aux->getProx();

        }
    }
    desfazer->insere(REMOCAO_OBJETOS,refOut,NULL);
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
void ListaObjetos::desfazerAcao(Ponto *MBRSelect){

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
            if(obj != NULL){

                if(obj->getSelecionado()){

                    deletar(obj,false);
                    refObj = refObj->getProx();
                    recalculaMBRSelect(MBRSelect);
                }else{

                    deletar(obj,false);
                    refObj = refObj->getProx();

                }

            }

        }
        refazer->insere(REMOCAO_OBJETOS, aux->getObjs(),NULL);
        delete aux;

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
        refazer->insere(ADICAO_OBJETOS,aux->getObjs(),NULL);
        delete aux;

    }else if(aux->getAcao() == MOVIMENTACAO_OBJETOS){

        /**Trata para desfazer a acao de mover objetos selecionados, ou seja, os move no sentido oposto**/
        Objeto3D *refObj = aux->getObjs();
        float x,y,z;
        x = -aux->getVetDes()->x;
        y = -aux->getVetDes()->y;
        z = -aux->getVetDes()->z;
        Objeto3D *obj = NULL;
        while(refObj != NULL){

            obj = indexId->busca(refObj->getId());
            if(obj->getObjeto() == SPHERE || obj->getObjeto() == BASE){

                obj->setCentro(obj->getCentro()->x + x,obj->getCentro()->y + y,obj->getCentro()->z + z);
                obj->setMBR(obj->getMBR()[0].x + x,obj->getMBR()[0].y + y,obj->getMBR()[0].z + z,obj->getMBR()[1].x + x,obj->getMBR()[1].y + y,obj->getMBR()[1].z + z);


            }else{

                if(indexId->busca(obj->getExtremidades()[0])->getSelecionado() && indexId->busca(obj->getExtremidades()[1])->getSelecionado()){

                    obj->setMBR(obj->getMBR()[0].x + x,obj->getMBR()[0].y + y,obj->getMBR()[0].z + z,obj->getMBR()[1].x + x,obj->getMBR()[1].y + y,obj->getMBR()[1].z + z);

                }

            }

            refObj = refObj->getProx();

        }
        refazer->insere(MOVIMENTACAO_OBJETOS,aux->getObjs(),aux->getVetDes());
        delete aux;
    }

}
void ListaObjetos::refazerAcao(Ponto *MBRSelect){

    Acao *aux = refazer->get();

    if(aux->getAcao() == ADICAO_OBJETOS){

        /**Trata para refazer a acao de remover objetos que vieram da opcao de desfazer anteriormente**/
        Objeto3D *refObj = aux->getObjs();
        Objeto3D *obj = NULL;
        while(refObj != NULL){

            obj = indexId->busca(refObj->getId());
            if(obj->getSelecionado()){

                indexId->remover(refObj->getId());
                deletar(obj,false);
                recalculaMBRSelect(MBRSelect);

            }else{

                indexId->remover(refObj->getId());
                deletar(obj,false);

            }
            refObj = refObj->getProx();

        }
        desfazer->insere(REMOCAO_OBJETOS, aux->getObjs(),NULL);
        delete aux;

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
        desfazer->insere(ADICAO_OBJETOS, aux->getObjs(),NULL);
        delete aux;

    }else if(aux->getAcao() == MOVIMENTACAO_OBJETOS){

        /**Trata para refazer a acao de mover objetos selecionados, ou seja, os move novamente**/
        Objeto3D *refObj = aux->getObjs();
        float x,y,z;
        x = aux->getVetDes()->x;
        y = aux->getVetDes()->y;
        z = aux->getVetDes()->z;
        Objeto3D *obj = NULL;
        while(refObj != NULL){

            obj = indexId->busca(refObj->getId());
            if(obj->getObjeto() == SPHERE || obj->getObjeto() == BASE){

                obj->setCentro(obj->getCentro()->x + x,obj->getCentro()->y + y,obj->getCentro()->z + z);
                obj->setMBR(obj->getMBR()[0].x + x,obj->getMBR()[0].y + y,obj->getMBR()[0].z + z,obj->getMBR()[1].x + x,obj->getMBR()[1].y + y,obj->getMBR()[1].z + z);


            }else{

                if(indexId->busca(obj->getExtremidades()[0])->getSelecionado() && indexId->busca(obj->getExtremidades()[1])->getSelecionado()){

                    obj->setMBR(obj->getMBR()[0].x + x,obj->getMBR()[0].y + y,obj->getMBR()[0].z + z,obj->getMBR()[1].x + x,obj->getMBR()[1].y + y,obj->getMBR()[1].z + z);

                }

            }

            refObj = refObj->getProx();

        }
        desfazer->insere(MOVIMENTACAO_OBJETOS,aux->getObjs(),aux->getVetDes());
        delete aux;
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
    Objeto3D *refOut = NULL;
    Objeto3D *prox = NULL;
    if(tamSelect <= 0){

        return false;

    }
    while(aux != NULL){

        if(aux->getSelecionado()){

            if(aux->getObjeto() == SPHERE || aux->getObjeto() == BASE){

                aux->setCentro(aux->getCentro()->x + x,aux->getCentro()->y + y,aux->getCentro()->z + z);
                aux->setMBR(aux->getMBR()[0].x + x,aux->getMBR()[0].y + y,aux->getMBR()[0].z + z,aux->getMBR()[1].x + x,aux->getMBR()[1].y + y,aux->getMBR()[1].z + z);
                if(refOut == NULL){

                    refOut = duplicarObj(aux);

                }else{

                    prox = duplicarObj(aux);
                    refOut->setAnt(prox);
                    prox->setProx(refOut);
                    refOut = prox;

                }

            }else{

                if(indexId->busca(aux->getExtremidades()[0])->getSelecionado() && indexId->busca(aux->getExtremidades()[1])->getSelecionado()){

                    aux->setMBR(aux->getMBR()[0].x + x,aux->getMBR()[0].y + y,aux->getMBR()[0].z + z,aux->getMBR()[1].x + x,aux->getMBR()[1].y + y,aux->getMBR()[1].z + z);
                    if(refOut == NULL){

                        refOut = duplicarObj(aux);

                    }else{

                        prox = duplicarObj(aux);
                        refOut->setAnt(prox);
                        prox->setProx(refOut);
                        refOut = prox;

                    }

                }

            }

        }
        aux = aux->getProx();
    }
    Ponto vetDes;
    vetDes.x = x;
    vetDes.y = y;
    vetDes.z = z;
    desfazer->insere(MOVIMENTACAO_OBJETOS, refOut, &vetDes);
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
    desfazer->insere(ADICAO_OBJETOS,duplicarObj(pri),NULL);
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

                if(aux->getObjeto() != SPHERE && aux->getObjeto() != BASE){

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
        pri->addExtremidades(id1);
        pri->addExtremidades(id2);

    }else{

        Objeto3D *aux = new Objeto3D();
        aux->setObjeto(tipoBar);
        aux->setProx(pri);
        aux->addExtremidades(id1);
        aux->addExtremidades(id2);
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
    objId1->addExtremidades(idDis);
    objId2->addExtremidades(idDis);
    idDis++;
    indexId->insere(pri->getId(),pri);
    desfazer->insere(ADICAO_OBJETOS,duplicarObj(pri),NULL);
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
void ListaObjetos::deletar(Objeto3D *p, bool completo){

    if(p != NULL){

        if(p->getObjeto() == SPHERE && completo){

            if(p->getTamExtremidades() > 0){

                for(int i = 0; i < p->getTamExtremidades(); i++){

                    deletar(indexId->busca(p->getExtremidades()[i]),completo);///Como uma esfera nao se liga a outra esfera, a recursão não entrará em loop

                }

            }
            p->setObjeto(BAR_SMALL);///Usado apenas para que a chamada recursiva entre no else do primeiro if
            deletar(p, completo);

        }
        else{

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
            for(int i = 0; i < p->getTamExtremidades(); i++){

                indexId->busca(p->getExtremidades()[i])->removeExtremidades(p->getId());

            }
            delete p;
            tam--;

        }

    }

}
bool ListaObjetos::duplicaSelect(){

    Objeto3D *aux = pri;
    Objeto3D *prox = NULL;
    Objeto3D *refOut = NULL;
    Objeto3D *refDesfazer = NULL;
    refazer->clear();

    while(aux != NULL){

        if(aux->getSelecionado()){

            if(aux->getObjeto() == SPHERE || aux->getObjeto() == BASE){

                if(refOut == NULL){

                    refOut = duplicarObj(aux);

                }else{

                    prox = duplicarObj(aux);
                    refOut->setAnt(prox);
                    prox->setProx(refOut);
                    refOut = prox;

                }


            }else if(aux->getObjeto() == BAR_SMALL || aux->getObjeto() == BAR_LARGE){

                if(indexId->busca(aux->getExtremidades()[0])->getSelecionado() && indexId->busca(aux->getExtremidades()[1])->getSelecionado()){

                    if(refOut == NULL){

                        refOut = duplicarObj(aux);

                    }else{

                        prox = duplicarObj(aux);
                        refOut->setAnt(prox);
                        prox->setProx(refOut);
                        refOut = prox;

                    }

                }else{

                    while(refOut != NULL){

                        prox = refOut->getProx();
                        delete refOut;
                        refOut = prox;

                    }
                    return false;
                }

            }
            refOut->setTamExtremidades(0);
            for(int i = 0; i < aux->getTamExtremidades(); i++){

                if(indexId->busca(aux->getExtremidades()[i])->getSelecionado()){

                    refOut->addExtremidades(aux->getExtremidades()[i]);

                }

            }

        }
        aux = aux->getProx();
    }
    aux = refOut;
    while(aux != NULL){

        prox = refOut;
        while(prox != NULL){

            if(prox->buscaIdExtremidades(aux->getId())){

                prox->removeExtremidades(aux->getId());
                prox->addExtremidades(idDis);

            }
            prox = prox->getProx();
        }
        indexId->busca(aux->getId())->setSelecionado(false);
        aux->setId(idDis);
        idDis++;
        tam++;
        if(refDesfazer == NULL){

            refDesfazer = duplicarObj(aux);

        }else{

            prox = duplicarObj(aux);
            refDesfazer->setAnt(prox);
            prox->setProx(refDesfazer);
            refDesfazer = prox;

        }
        prox = duplicarObj(aux);
        prox->setProx(pri);
        pri->setAnt(prox);
        pri = prox;
        indexId->insere(pri->getId(), pri);
        pri->setSelecionado(true);
        aux = aux->getProx();
    }
    desfazer->insere(ADICAO_OBJETOS,refDesfazer,NULL);
    while(refOut != NULL){

        prox = refOut->getProx();
        delete refOut;
        refOut = prox;

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
    desfazer->insere(ADICAO_OBJETOS,duplicarObj(pri),NULL);
    refazer->clear();
    tam++;

}
bool ListaObjetos::addLaje(){

    if(tamSelect != 4){

        return false;

    }
    Objeto3D *obj0 = NULL;
    Objeto3D *obj1 = NULL;
    Objeto3D *obj2 = NULL;
    Objeto3D *obj3 = NULL;
    Objeto3D *sph0 = NULL;
    Objeto3D *sph1 = NULL;
    Objeto3D *sph2 = NULL;
    Objeto3D *sph3 = NULL;
    Objeto3D *aux = pri;

    while(aux != NULL){

        if(aux->getSelecionado()){

            if(obj0 == NULL && aux->getObjeto() == SPHERE){

                obj0 = aux;

            }else if(obj1 == NULL && aux->getObjeto() == SPHERE){

                obj1 = aux;

            }else if(obj2 == NULL && aux->getObjeto() == SPHERE){

                obj2 = aux;

            }else if(obj3 == NULL && aux->getObjeto() == SPHERE){

                obj3 = aux;
                break;

            }else{

                return false;

            }

        }
        aux = aux->getProx();
    }
    sph0 = obj0;
    ///Definir a posicao o segundo vertice nos
    if(distancia(obj0->getCentro(),obj1->getCentro()) >= (BAR_LENGTH_SMALL + 2*SPHERE_RADIUS - 0.01) && distancia(obj0->getCentro(),obj1->getCentro()) <= (BAR_LENGTH_SMALL + 2*SPHERE_RADIUS + 0.01)){

        sph1 = obj1;

    }else if(distancia(obj0->getCentro(),obj2->getCentro()) >= (BAR_LENGTH_SMALL + 2*SPHERE_RADIUS - 0.01) && distancia(obj0->getCentro(),obj2->getCentro()) <= (BAR_LENGTH_SMALL + 2*SPHERE_RADIUS + 0.01)){


        sph1 = obj2;

    }
    else if(distancia(obj0->getCentro(),obj3->getCentro()) >= (BAR_LENGTH_SMALL + 2*SPHERE_RADIUS - 0.01) && distancia(obj0->getCentro(),obj3->getCentro()) <= (BAR_LENGTH_SMALL + 2*SPHERE_RADIUS + 0.01)){

        sph1 = obj3;

    }else{

        return false;

    }
    ///Definindo o terceiro ponto
    if(distancia(sph1->getCentro(),obj1->getCentro()) >= (BAR_LENGTH_LARGE + 2*SPHERE_RADIUS - 0.01) && distancia(sph1->getCentro(),obj1->getCentro()) <= (BAR_LENGTH_LARGE + 2*SPHERE_RADIUS + 0.01)){

        sph2 = obj1;

    }else if(distancia(sph1->getCentro(),obj2->getCentro()) >= (BAR_LENGTH_LARGE + 2*SPHERE_RADIUS - 0.01) && distancia(sph1->getCentro(),obj2->getCentro()) <= (BAR_LENGTH_LARGE + 2*SPHERE_RADIUS + 0.01)){

        sph2 = obj2;

    }else if(distancia(sph1->getCentro(),obj3->getCentro()) >= (BAR_LENGTH_LARGE + 2*SPHERE_RADIUS - 0.01) && distancia(sph1->getCentro(),obj3->getCentro()) <= (BAR_LENGTH_LARGE + 2*SPHERE_RADIUS + 0.01)){

        sph2 = obj3;

    }else{

        return false;

    }
    ///Definindo o quarto ponto
    if(distancia(sph2->getCentro(),obj1->getCentro()) >= (BAR_LENGTH_SMALL + 2*SPHERE_RADIUS - 0.01) && distancia(sph2->getCentro(),obj1->getCentro()) <= (BAR_LENGTH_SMALL + 2*SPHERE_RADIUS + 0.01)){

        sph3 = obj1;

    }else if(distancia(sph2->getCentro(),obj2->getCentro()) >= (BAR_LENGTH_SMALL + 2*SPHERE_RADIUS - 0.01) && distancia(sph2->getCentro(),obj2->getCentro()) <= (BAR_LENGTH_SMALL + 2*SPHERE_RADIUS + 0.01)){

        sph3 = obj2;

    }else if(distancia(sph2->getCentro(),obj3->getCentro()) >= (BAR_LENGTH_SMALL + 2*SPHERE_RADIUS - 0.01) && distancia(sph2->getCentro(),obj3->getCentro()) <= (BAR_LENGTH_SMALL + 2*SPHERE_RADIUS + 0.01)){

        sph3 = obj3;

    }else{

        return false;

    }
    if(distancia(sph3->getCentro(),sph0->getCentro()) < (BAR_LENGTH_LARGE + 2*SPHERE_RADIUS - 0.01) || distancia(sph3->getCentro(),sph0->getCentro()) > (BAR_LENGTH_LARGE + 2*SPHERE_RADIUS + 0.01)){

        return false;

    }
    aux = new Objeto3D();
    aux->setProx(pri);
    pri->setAnt(aux);
    aux->setObjeto(LAJE);
    aux->addExtremidades(sph0->getId());
    aux->addExtremidades(sph1->getId());
    aux->addExtremidades(sph2->getId());
    aux->addExtremidades(sph3->getId());
    pri = aux;
    pri->setId(idDis);
    idDis++;
    tam++;
    desfazer->insere(ADICAO_OBJETOS, duplicarObj(pri),NULL);
    return true;
}
float ListaObjetos::distancia(Ponto *p, Ponto *n){

    return sqrt(pow(p->x - n->x,2) + pow(p->y - n->y,2) + pow(p->z - n->z,2));

}
