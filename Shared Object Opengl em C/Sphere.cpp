#include "Sphere.h"

using namespace ManipularVetor;

Sphere::Sphere():Objeto3D()
{

    object_difusa = new GLfloat[4];
    object_difusa[0] = 1.0;
    object_difusa[1] = 0.397;
    object_difusa[2] = 0.397;
    object_difusa[3]  = 1.0;

}
void Sphere::draw(float meshQual, bool wireframe, char visionAxis, int visionOption){

    glPushMatrix();

            if(visionAxis == 'z'){

                glTranslatef(centro.x,centro.y,centro.z);

            }else if(visionAxis == 'x'){

                if(visionOption == 1){


                    glTranslatef(centro.y,centro.z,centro.x);

                }else{

                    glTranslatef(centro.y,centro.z,-centro.x);

                }

            }else{

                if(visionOption == 3){

                    glTranslatef(centro.x,centro.z,-centro.y);

                }else{

                    glTranslatef(centro.x,centro.z,centro.y);

                }

            }
            drawZero(meshQual, wireframe);

        glPopMatrix();

}void Sphere::drawZero(float meshQual, bool wireframe){

    float resolucao = meshQual * 32;
    GLUquadricObj *quadric=gluNewQuadric();
    gluQuadricNormals(quadric, GLU_SMOOTH);

    GLfloat difuse[4];
    difuse[0] = object_difusa[0];
    difuse[1] = object_difusa[1];
    difuse[2] = object_difusa[2];
    difuse[3] = object_difusa[3];

    if(selecionado){

        difuse[0] = object_select[0];
        difuse[1] = object_select[1];
        difuse[2] = object_select[2];

    }
    if(wireframe){

        if(!selecionado){

            difuse[0] = 0.0;
            difuse[1] = 0.0;
            difuse[2] = 1.0;

        }
        glPushMatrix();
            glPolygonMode(GL_FRONT,GL_LINE);
            glMaterialfv(GL_FRONT, GL_DIFFUSE,difuse);
            glMaterialfv(GL_FRONT, GL_AMBIENT,object_ambient);
            glMaterialfv(GL_FRONT, GL_SHININESS, object_brilho);
            glMaterialfv(GL_FRONT, GL_SPECULAR, object_especular);
            GLUquadricObj *quadric;
            quadric = gluNewQuadric();
            gluQuadricOrientation(quadric, GLU_OUTSIDE);
            gluSphere( quadric , SPHERE_RADIUS, 16, 16);
            gluDeleteQuadric(quadric);
            glPolygonMode(GL_FRONT, GL_FILL);
        glPopMatrix();

        difuse[0] = object_select[0];
        difuse[1] = object_select[1];
        difuse[2] = object_select[2];

    }
    if(!wireframe){

        glPushMatrix();
            glMaterialfv(GL_FRONT, GL_DIFFUSE,difuse);
            glMaterialfv(GL_FRONT, GL_AMBIENT,object_ambient);
            glMaterialfv(GL_FRONT, GL_SHININESS, object_brilho);
            glMaterialfv(GL_FRONT, GL_SPECULAR, object_especular);
            GLUquadricObj *quadric;
            quadric = gluNewQuadric();
            gluQuadricOrientation(quadric, GLU_OUTSIDE);
            gluSphere( quadric , SPHERE_RADIUS , resolucao, resolucao);
            gluDeleteQuadric(quadric);
        glPopMatrix();

    }

}
Sphere::~Sphere()
{
    delete []object_difusa;
}
