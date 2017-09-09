#include "Simulacao.h"
#include "ListaObjetos.h"
#include <time.h>

extern "C"{

    clock_t tempo;
    float tempoTotal;
    bool sSim;
    ListaObjetos *lObj;
    Simulacao sim;


    void init(ListaObjetos *l);
    void start();
    void drawSim();
    void stop();
    void setListaObjetos(ListaObjetos *p);
    bool getSSim();
    void setTempoTotal(float t);
    float getTempoTotal();
    void addForca(double* ponto, float x, float y, float z);


}
