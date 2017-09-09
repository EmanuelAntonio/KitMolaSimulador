#ifndef BASE_H
#define BASE_H
#include "Objeto3D.h"

class Base : public Objeto3D
{
    public:
        Base();
        void draw(float meshQual, bool wireframe, char visionAxis, int visionOption);
        void recalculaMBR();
        void setSubObjeto(int o);
        int getSubObjeto();
        virtual ~Base();
    private:
        void drawSphereZero(float meshQual, bool wireframe);
        void drawBarZero(float meshQual, bool wireframe, char visionAxis, int visionOption,float radius, Ponto *p1, Ponto *p2);
        int subObjeto;
};

#endif // BASE_H
