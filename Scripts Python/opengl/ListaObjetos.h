#ifndef LISTAOBJETOS_H
#define LISTAOBJETOS_H
#include "Objeto3D.h"

class ListaObjetos
{
    public:
        ListaObjetos();
        void addCubo(float x, float y, float z);/**
                                                *   Fun��o addCubo: Adiciona um cubo � lista de objetos na cena
                                                *   Par�metro: 'x','y','z', coordenadas do centro do cubo
                                                *   Retorno: vazio
                                                **/
        Objeto3D* get();/**
                        *   Fun��o addCubo: retorna uma refer�ncia para o primeiro no da lista
                        *   Par�metro: vazio
                        *   Retorno: vazio
                        **/
        int size();
        ~ListaObjetos();
    private:
        Objeto3D *pri;
};

#endif // LISTAOBJETOS_H
