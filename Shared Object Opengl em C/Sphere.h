#ifndef SPHERE_H
#define SPHERE_H
#include "Objeto3D.h"

class Sphere : public Objeto3D
{
    public:
        Sphere();
        void draw(float meshQual, bool wireframe, char visionAxis, int visionOption);
        ~Sphere();
    private:
        void drawZero(float meshQual, bool wireframe);
};

#endif // SPHERE_H
