#include "ManipularVetor.h"


float ManipularVetor::distancia(Ponto p, Ponto n){

    return sqrt(pow(p.x - n.x,2) + pow(p.y - n.y,2) + pow(p.z - n.z,2));

}
Ponto ManipularVetor::prodVetorial(Ponto vetp, Ponto vetn){

    Ponto p;
    p.x = vetp.y * vetn.z - vetp.z * vetn.y;
    p.y = vetp.z * vetn.x - vetp.x * vetn.z;
    p.z = vetp.x * vetn.y - vetp.y * vetn.x;
    return p;

}
float ManipularVetor::normaVet(Ponto vetp){

    return sqrt(pow(vetp.x,2) + pow(vetp.y,2) + pow(vetp.z,2));

}
float ManipularVetor::prodEscalar(Ponto vetp, Ponto vetn){

    return vetp.x*vetn.x + vetp.y*vetn.y + vetp.z*vetn.z;

}
Ponto ManipularVetor::somaVetorial(Ponto vetp, Ponto vetn){

    Ponto p;
    p.x = vetp.x + vetn.x;
    p.y = vetp.y + vetn.y;
    p.z = vetp.z + vetn.z;
    return p;

}
Ponto ManipularVetor::inverteSentido(Ponto vetp){

    Ponto p;
    p.x = -vetp.x;
    p.y = -vetp.y;
    p.z = -vetp.z;
    return p;

}
Ponto ManipularVetor::prodPorEscalar(float t, Ponto vetn){

    Ponto p;
    p.x = t*vetn.x;
    p.y = t*vetn.y;
    p.z = t*vetn.z;
    return p;

}
Ponto ManipularVetor::normalizarVet(Ponto vetp){

    Ponto p;
    float norma = normaVet(vetp);
    p.x = vetp.x / norma;
    p.y = vetp.y / norma;
    p.z = vetp.z / norma;
    return p;

}
Ponto ManipularVetor::maiorXYZ(Ponto p1, Ponto p2){

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
Ponto ManipularVetor::menorXYZ(Ponto p1, Ponto p2){

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

float ManipularVetor::anguloVetores(Ponto vet1, Ponto vet2){

    return acos((prodEscalar(vet1,vet2))/(normaVet(vet1)*normaVet(vet2)));

}
bool ManipularVetor::vetNulo(Ponto vet){

    if(vet.x == 0 && vet.y == 0 && vet.z == 0){

        return true;

    }
    return false;

}
Ponto ManipularVetor::iniVet(){

    Ponto p;
    p.x = 0;
    p.y = 0;
    p.z = 0;
    return p;

}
Ponto ManipularVetor::copiar(Ponto n){

    Ponto p;
    p.x = n.x;
    p.y = n.y;
    p.z = n.z;

    return p;

}

