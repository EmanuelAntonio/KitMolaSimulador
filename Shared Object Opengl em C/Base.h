#ifndef BASE_H
#define BASE_H
#include "Objeto3D.h"

class Base : public Objeto3D
{
    public:
        Base();
        void draw(float meshQual, bool wireframe, char visionAxis, int visionOption);
        virtual ~Base();
    private:
        void drawSphereZero(float meshQual, bool wireframe);
        void drawBarZero(float meshQual, bool wireframe, char visionAxis, int visionOption,float radius, Ponto *p1, Ponto *p2);
};

#endif // BASE_H
