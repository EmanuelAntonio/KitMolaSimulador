#ifndef BAR_H
#define BAR_H
#include "Objeto3D.h"


class Bar : public Objeto3D
{
    public:
        Bar();
        void draw(float meshQual, bool wireframe, char visionAxis, int visionOption, Objeto3D *obj1, Objeto3D *obj2);
        void recalculaMBR(Ponto *p1, Ponto *p2);
        virtual ~Bar();
        void drawZero(float meshQual, bool wireframe, char visionAxis, int visionOption, Ponto *p1, Ponto *p2);
        static void initBuffer();
    private:
        static GLuint bar64;
        static GLuint bar64n;
        static int split;


};

#endif // BAR_H
