#ifndef BAR_H
#define BAR_H
#include "Objeto3D.h"


class Bar : public Objeto3D
{
    public:
        Bar();
        void draw(float meshQual, bool wireframe, char visionAxis, int visionOption, Objeto3D *obj1, Objeto3D *obj2);
        virtual ~Bar();
        void drawZero(float meshQual, bool wireframe, char visionAxis, int visionOption, Ponto *p1, Ponto *p2);

};

#endif // BAR_H
