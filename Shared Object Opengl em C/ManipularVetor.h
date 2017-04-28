#ifndef MANIPULARVETOR_H
#define MANIPULARVETOR_H
#include "Ponto.h"
#include <math.h>


namespace ManipularVetor
{

    float distancia(Ponto p, Ponto n){

        return sqrt(pow(p.x - n.x,2) + pow(p.y - n.y,2) + pow(p.z - n.z,2));

    }
    Ponto prodVetorial(Ponto vetp, Ponto vetn){

        Ponto p;
        p.x = vetp.y * vetn.z - vetp.z * vetn.y;
        p.y = vetp.z * vetn.x - vetp.x * vetn.z;
        p.z = vetp.x * vetn.y - vetp.y * vetn.x;
        return p;

    }
    float normaVet(Ponto vetp){

        return sqrt(pow(vetp.x,2) + pow(vetp.y,2) + pow(vetp.z,2));

    }
    float prodEscalar(Ponto vetp, Ponto vetn){

        return vetp.x*vetn.x + vetp.y*vetn.y + vetp.z*vetn.z;

    }
    Ponto somaVetorial(Ponto vetp, Ponto vetn){

        Ponto p;
        p.x = vetp.x + vetn.x;
        p.y = vetp.y + vetn.y;
        p.z = vetp.z + vetn.z;
        return p;

    }
    Ponto inverteSentido(Ponto vetp){

        Ponto p;
        p.x = -vetp.x;
        p.y = -vetp.y;
        p.z = -vetp.z;
        return p;

    }
    Ponto prodPorEscalar(float t, Ponto vetn){

        Ponto p;
        p.x = t*vetn.x;
        p.y = t*vetn.y;
        p.z = t*vetn.z;
        return p;

    }
    Ponto normalizarVet(Ponto vetp){

        Ponto p;
        float norma = normaVet(vetp);
        p.x = vetp.x / norma;
        p.y = vetp.y / norma;
        p.z = vetp.z / norma;
        return p;

    }
    Ponto maiorXYZ(Ponto p1, Ponto p2){

        Ponto p;
        if(p1.x > p2.x){

            p.x = p1.x;

        }else{

            p.x = p2.x;

        }if(p1.y > p2.y){

            p.y = p1.y;

        }else{

            p.y = p2.y;

        }if(p1.z > p2.z){

            p.z = p1.z;

        }else{

            p.z = p2.z;

        }
        return p;
    }
    Ponto menorXYZ(Ponto p1, Ponto p2){

        Ponto p;
        if(p1.x < p2.x){

            p.x = p1.x;

        }else{

            p.x = p2.x;

        }if(p1.y < p2.y){

            p.y = p1.y;

        }else{

            p.y = p2.y;

        }if(p1.z < p2.z){

            p.z = p1.z;

        }else{

            p.z = p2.z;

        }
        return p;
    }

};

#endif // MANIPULARVETOR_H
