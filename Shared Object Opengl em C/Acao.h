#ifndef ACAO_H
#define ACAO_H
#include "Objeto3D.h"

#define ADICAO_OBJETOS 0
#define REMOCAO_OBJETOS 1

/**Classe Acao: acao feita no projeto**/

class Acao
{
    public:
        Acao(){

            prox = NULL;

        }
        void setProx(Acao *p){prox = p;}
        Acao* getProx(){return prox;}
        void setAcao(int a){acao = a;}
        int getAcao(){return acao;}
        Objeto3D *getObjs(){return objs;}
        void setObjs(Objeto3D *o){objs = o;}
        ~Acao(){}
    private:
        Acao *prox;
        Objeto3D *objs;
        int acao;/**
                    * 0 -> adicao de objetos
                    * 1 -> remocao de objetos
                    * 2 -> selecao de objetos
                    * 3 -> deselecao de objetos
                    **/
};

#endif // ACAO_H
