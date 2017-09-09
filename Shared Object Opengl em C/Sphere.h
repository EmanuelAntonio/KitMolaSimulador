#ifndef SPHERE_H
#define SPHERE_H
#include "Objeto3D.h"

class Sphere : public Objeto3D
{
    public:
        Sphere();
        void draw(float meshQual, bool wireframe, char visionAxis, int visionOption);
        void recalculaMBR();
        static void initBuffer();
        ~Sphere();
    private:
        void drawZero(float meshQual, bool wireframe);
        static GLuint sph64;
        static GLuint sph64n;
        static GLuint sphVao;

};

#endif // SPHERE_H
