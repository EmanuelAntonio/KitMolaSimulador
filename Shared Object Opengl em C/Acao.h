#ifndef ACAO_H
#define ACAO_H
#include "Objeto3D.h"

#define ADICAO_OBJETOS 0
#define REMOCAO_OBJETOS 1
#define MOVIMENTACAO_OBJETOS 3

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
        void setVetDes(float x, float y, float z){

            vetDes.x = x;
            vetDes.y = y;
            vetDes.z = z;

        }
        Ponto* getVetDes(){

            return &vetDes;

        }
        ~Acao(){}
    private:
        Acao *prox;
        Objeto3D *objs;
        Ponto vetDes;
        int acao;/**
                    * 0 -> adicao de objetos
                    * 1 -> remocao de objetos
                    * 2 -> movimentacao de objetos
                    **/
};

#endif // ACAO_H
