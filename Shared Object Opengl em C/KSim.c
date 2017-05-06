#include "KSim.h"


extern "C"{

    void init(ListaObjetos *l){

        tempo = 0;
        sSim = false;
        lObj = l;
        tempoTotal = 5; ///Em segundos

    }
    void start(){

        tempo = clock();
        sSim = true;

    }
    void stop(){

        tempo = 0;
        sSim = false;

    }
    void setListaObjetos(ListaObjetos *p){

        lObj = p;

    }
    bool getSSim(){

        return sSim;

    }
    void drawSim(){

        sim.start(lObj,(clock() - tempo)/(float)CLOCKS_PER_SEC,tempoTotal);

    }
    void setTempoTotal(float t){

        tempoTotal = t;

    }
    float getTempoTotal(){

        return tempoTotal;

    }
    void addForca(double* ponto, float x, float y, float z){

        Ponto forca;

        forca.x = x;
        forca.y = y;
        forca.z = z;
        sim.addForca(lObj, ponto,forca);


    }
}
