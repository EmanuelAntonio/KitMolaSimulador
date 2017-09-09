#ifndef LIGRIGIDA_H
#define LIGRIGIDA_H
#include "Objeto3D.h"


class LigRigida : public Objeto3D{
    public:
        LigRigida();
        ~LigRigida();
        void draw(float mehQual, bool wireframe, char visionAxis, int visionOption, Objeto3D *obj1, Objeto3D *obj2, Objeto3D *obj3);

    private:
        void drawZero(float mehQual, bool wireframe, char visionAxis, int visionOption, Ponto *obj1, Ponto *obj2, Ponto *obj3);
};

#endif // LIGRIGIDA_H
