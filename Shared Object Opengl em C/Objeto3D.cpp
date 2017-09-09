#include "Objeto3D.h"

Objeto3D::Objeto3D()
{

    objeto = 0;
    prox = NULL;
    ant = NULL;
    selecionado = false;
    tamExtremidades = 0;
    object_ambient = new GLfloat[4];
    object_ambient[0] = 0.2;
    object_ambient[1] = 0.2;
    object_ambient[2] = 0.2;
    object_ambient[3] = 1.0;

    object_brilho = new GLfloat[1];
    object_brilho[0] = 25.6;


    object_especular = new GLfloat[4];
    object_especular[0] = 0.5;
    object_especular[1] = 0.5;
    object_especular[2] = 0.5;
    object_especular[3] = 1.0;

    object_select = new GLfloat[3];
    object_select[0] = 0.0;
    object_select[1] = 0.5;
    object_select[2] = 1.0;

}

void Objeto3D::setObjeto(int p){

    objeto = p;

}
void Objeto3D::setProx(Objeto3D *p){

    prox = p;

}
void Objeto3D::setSelecionado(bool sel){

    selecionado = sel;

}

void Objeto3D::setCentro(float x, float y, float z){

    centro.x = x;
    centro.y = y;
    centro.z = z;

}
void Objeto3D::setMBR(float x1, float y1, float z1, float x2, float y2, float z2){

    MBR[0].x = x1;
    MBR[0].y = y1;
    MBR[0].z = z1;
    MBR[1].x = x2;
    MBR[1].y = y2;
    MBR[1].z = z2;

}
int Objeto3D::getObjeto(){

    return objeto;

}
Objeto3D* Objeto3D::getProx(){

    return prox;

}
Ponto* Objeto3D::getMBR(){

    return MBR;

}
Ponto* Objeto3D::getCentro(){

    return &centro;

}
int* Objeto3D::getExtremidades(){

    return idExtremidades;

}
int Objeto3D::getTamExtremidades(){

    return tamExtremidades;

}
void Objeto3D::setTamExtremidades(int tam){

    tamExtremidades = tam;

}
bool Objeto3D::getSelecionado(){

    return selecionado;

}
int Objeto3D::getId(){

    return id;

}
void Objeto3D::setId(int i){

    id = i;

}
Objeto3D* Objeto3D::getAnt(){

    return ant;

}
void Objeto3D::setAnt(Objeto3D *o){

    ant = o;

}
void Objeto3D::addExtremidades(int id){

    idExtremidades[tamExtremidades] = id;
    tamExtremidades++;

}
void Objeto3D::removeExtremidades(int id){

    int idE = -1;
    for(int i = 0; i < tamExtremidades; i++){

        if(idExtremidades[i] == id){

            idE = i;
            break;

        }

    }
    if(idE != -1){

        for(int i = idE; i < tamExtremidades - 1; i++){

            idExtremidades[i] = idExtremidades[i+1];

        }
        tamExtremidades--;
    }

}
void Objeto3D::swapExtremidades(int id1, int id2){

    for(int i = 0; i < tamExtremidades; i++){

        if(idExtremidades[i] == id1){

           idExtremidades[i] = id2;
           return;

        }

    }

}
bool Objeto3D::buscaIdExtremidades(int id){

    for(int i = 0; i < tamExtremidades; i++){

        if(idExtremidades[i] == id){

            return true;

        }

    }
    return false;
}
void Objeto3D::draw(float meshQual, bool wireframe, char visionAxis, int visionOption){}
void Objeto3D::draw(float meshQual, bool wireframe, char visionAxis, int visionOption, Objeto3D *obj1, Objeto3D *obj2){}
void Objeto3D::draw(float meshQual, bool wireframe, char visionAxis, int visionOption, Ponto *p1, Ponto *p2, Ponto *p3, Ponto *p4){}
void Objeto3D::draw(float mehQual, bool wireframe, char visionAxis, int visionOption, Objeto3D *obj1, Objeto3D *obj2, Objeto3D *obj3){}
void Objeto3D::recalculaMBR(){}
void Objeto3D::recalculaMBR(Ponto *p1, Ponto *p2){}
void Objeto3D::recalculaMBR(Ponto *p1, Ponto *p2, Ponto *p3, Ponto *p4){}
Objeto3D::~Objeto3D(){}
