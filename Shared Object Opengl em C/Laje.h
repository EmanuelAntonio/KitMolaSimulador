#ifndef LAJE_H
#define LAJE_H
#include "Objeto3D.h"

class Laje : public Objeto3D
{
    public:
        Laje();
        ~Laje();
        void draw(float meshQual, bool wireframe, char visionAxis, int visionOption, Ponto *p1, Ponto *p2, Ponto *p3, Ponto *p4);

    private:
        void drawZero(float meshQual, bool wireframe, char visionAxis, int visionOption, Ponto *p1, Ponto *p2, Ponto *p3, Ponto *p4);
};

#endif // LAJE_H
