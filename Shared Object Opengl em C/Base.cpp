#include "Base.h"

using namespace ManipularVetor;

Base::Base() : Objeto3D()
{
    object_difusa = new GLfloat[4];
    object_difusa[0] = 0.528;
    object_difusa[1] = 0.8;
    object_difusa[2] = 0.514;
    object_difusa[3]  = 1.0;
}
void Base::draw(float meshQual, bool wireframe, char visionAxis, int visionOption){

    Ponto p1,p2;
    if(visionAxis == 'z'){

        p2.x = centro.x;
        p2.y = centro.y;
        p2.z = centro.z + SPHERE_RADIUS/2;
        p1.x = centro.x;
        p1.y = centro.y;
        p1.z = centro.z - SPHERE_RADIUS/2;

    }else if(visionAxis == 'x'){

        p2.x = centro.y;
        p2.y = centro.z + SPHERE_RADIUS/2;
        p1.x = centro.y;
        p1.y = centro.z - SPHERE_RADIUS/2;
        if(visionOption == 1){

            p1.z = centro.x;
            p2.z = centro.x;

        }else{

            p1.z = -centro.x;
            p2.z = -centro.x;

        }

    }else{

        p2.x = centro.x;
        p2.y = centro.z + SPHERE_RADIUS/2;
        p1.x = centro.x;
        p1.y = centro.z - SPHERE_RADIUS/2;
        if(visionOption == 3){

            p2.z = -centro.y;
            p1.z = -centro.y;

        }else{

            p2.z = centro.y;
            p1.z = centro.y;

        }

    }
    GLdouble eq[] = {0.0,0.0,1.0,-centro.z};
    if(visionAxis == 'y' || visionAxis == 'x'){

        eq[1] = 1.0;
        eq[2] = 0.0;

    }
    glClipPlane(GL_CLIP_PLANE0,eq);
    glEnable(GL_CLIP_PLANE0);
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
        drawSphereZero(meshQual, wireframe);

    glPopMatrix();
    glDisable(GL_CLIP_PLANE0);
    drawBarZero(meshQual, wireframe, visionAxis, visionOption,BASE_RADIUS, &p1, &p2);


}
void Base::drawSphereZero(float meshQual, bool wireframe){

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
void Base::drawBarZero(float meshQual, bool wireframe, char visionAxis, int visionOption,float radius, Ponto *p1, Ponto *p2){

    float resolucao = meshQual * 32;
    GLUquadricObj *quadric=gluNewQuadric();
    gluQuadricNormals(quadric, GLU_SMOOTH);

    GLfloat difuse[4];
    difuse[0] = object_difusa[0];
    difuse[1] = object_difusa[1];
    difuse[2] = object_difusa[2];
    difuse[3] = object_difusa[3];

    if(p1->z > p2->z){

        Ponto *aux = p1;
        p1 = p2;
        p2 = aux;

    }

    float vx = p2->x - p1->x;
    float vy = p2->y - p1->y;
    float vz = p2->z - p1->z;

    //handle the degenerate case of z1 == z2 with an approximation
    if(vz == 0)
        vz = .0001;

    float v = sqrt( vx*vx + vy*vy + vz*vz );
    float ax = 57.2957795*acos( vz/v );
    if ( vz < 0.0 )
        ax = -ax;
    float rx = -vy*vz;
    float ry = vx*vz;
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
            //draw the cylinder body
            glTranslatef( p1->x,p1->y,p1->z );
            glRotatef(ax, rx, ry, 0.0);
            gluQuadricOrientation(quadric,GLU_OUTSIDE);
            gluCylinder(quadric, radius, radius, v, 16, 1);

            glPolygonMode(GL_FRONT,GL_FILL);

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
            //draw the cylinder body
            glTranslatef( p1->x,p1->y,p1->z );
            glRotatef(ax, rx, ry, 0.0);
            gluQuadricOrientation(quadric,GLU_OUTSIDE);
            gluCylinder(quadric, radius, radius, v, resolucao, 1);

            //draw the first cap
            gluQuadricOrientation(quadric,GLU_INSIDE);
            gluDisk( quadric, 0.0, radius, resolucao, 1);
            glTranslatef( 0,0,v );

            //draw the second cap
            gluQuadricOrientation(quadric,GLU_OUTSIDE);
            gluDisk( quadric, 0.0, radius, resolucao, 1);

        glPopMatrix();
    }
    gluDeleteQuadric(quadric);

}
void Base::setSubObjeto(int o){

    subObjeto = o;

}
int Base::getSubObjeto(){

    return subObjeto;

}
void Base::recalculaMBR(){

    setMBR(-BASE_RADIUS + centro.x,-BASE_RADIUS + centro.y,-SPHERE_RADIUS + centro.z,BASE_RADIUS + centro.x,BASE_RADIUS + centro.y,SPHERE_RADIUS + centro.z);

}
Base::~Base()
{
    delete []object_difusa;
}
