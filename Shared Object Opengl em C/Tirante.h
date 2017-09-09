#ifndef TIRANTE_H
#define TIRANTE_H
#include "Objeto3D.h"


class Tirante : public Objeto3D
{
    public:
        Tirante();
        void draw(float meshQual, bool wireframe, char visionAxis, int visionOption, Objeto3D *obj1, Objeto3D *obj2);
        void recalculaMBR(Ponto *p1, Ponto *p2);
        ~Tirante();
    private:
        void drawZero(float meshQual, bool wireframe, char visionAxis, int visionOption,float radius, Ponto *p1, Ponto *p2);
};

#endif // TIRANTE_H
