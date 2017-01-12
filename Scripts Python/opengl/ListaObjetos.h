#ifndef LISTAOBJETOS_H
#define LISTAOBJETOS_H
#include "Objeto3D.h"

class ListaObjetos
{
    public:
        ListaObjetos();
        void addCubo(float x, float y, float z);/**
                                                *   Função addCubo: Adiciona um cubo à lista de objetos na cena
                                                *   Parâmetro: 'x','y','z', coordenadas do centro do cubo
                                                *   Retorno: vazio
                                                **/
        Objeto3D* get();/**
                        *   Função addCubo: retorna uma referência para o primeiro no da lista
                        *   Parâmetro: vazio
                        *   Retorno: vazio
                        **/
        int size();
        ~ListaObjetos();
    private:
        Objeto3D *pri;
};

#endif // LISTAOBJETOS_H
