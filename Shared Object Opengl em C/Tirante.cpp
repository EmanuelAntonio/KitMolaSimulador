#include "Tirante.h"

using namespace ManipularVetor;

Tirante::Tirante():Objeto3D()
{
    object_difusa = new GLfloat[4];
    object_difusa[0] = 0.5;
    object_difusa[1] = 0.0;
    object_difusa[2] = 0.8;
    object_difusa[3] = 1.0;
}
void Tirante::draw(float meshQual, bool wireframe, char visionAxis, int visionOption, Objeto3D *obj1, Objeto3D *obj2){

    Ponto p1,p2,p3,p4;
    if(visionAxis == 'z'){

        p1.x = obj1->getCentro()->x;
        p1.y = obj1->getCentro()->y;
        p1.z = obj1->getCentro()->z;
        p2.x = obj2->getCentro()->x;
        p2.y = obj2->getCentro()->y;
        p2.z = obj2->getCentro()->z;

    }else if(visionAxis == 'x'){

        p1.x = obj1->getCentro()->y;
        p1.y = obj1->getCentro()->z;
        p2.x = obj2->getCentro()->y;
        p2.y = obj2->getCentro()->z;
        if(visionOption == 1){

            p2.z = obj2->getCentro()->x;
            p1.z = obj1->getCentro()->x;

        }else{

            p2.z = -obj2->getCentro()->x;
            p1.z = -obj1->getCentro()->x;

        }


    }else{

        p1.x = obj1->getCentro()->x;
        p1.y = obj1->getCentro()->z;
        p2.x = obj2->getCentro()->x;
        p2.y = obj2->getCentro()->z;
        if(visionOption == 3){

            p1.z = -obj1->getCentro()->y;
            p2.z = -obj2->getCentro()->y;

        }else{

            p1.z = obj1->getCentro()->y;
            p2.z = obj2->getCentro()->y;

        }

    }
    float t = (SPHERE_RADIUS - 0.1)/distancia(p1,p2);
    float t2 = (1.5*SPHERE_RADIUS)/distancia(p1,p2);
    Ponto vetDir;
    vetDir.x = p2.x - p1.x;
    vetDir.y = p2.y - p1.y;
    vetDir.z = p2.z - p1.z;
    Ponto pReta = p1;
    p1.x = pReta.x + vetDir.x*t;
    p1.y = pReta.y + vetDir.y*t;
    p1.z = pReta.z + vetDir.z*t;

    p2.x = pReta.x + vetDir.x*t2;
    p2.y = pReta.y + vetDir.y*t2;
    p2.z = pReta.z + vetDir.z*t2;

    t = 1.0 - t;
    t2 = 1.0 - t2;
    p3.x = pReta.x + vetDir.x*t;
    p3.y = pReta.y + vetDir.y*t;
    p3.z = pReta.z + vetDir.z*t;

    p4.x = pReta.x + vetDir.x*t2;
    p4.y = pReta.y + vetDir.y*t2;
    p4.z = pReta.z + vetDir.z*t2;

    GLUquadricObj *quadric=gluNewQuadric();
    gluQuadricNormals(quadric, GLU_SMOOTH);

    drawZero(meshQual, wireframe, visionAxis, visionOption,BAR_RADIUS, &p1,&p2);
    drawZero(meshQual, wireframe, visionAxis, visionOption,BAR_RADIUS, &p3,&p4);
    gluDeleteQuadric(quadric);
    drawZero(meshQual, wireframe, visionAxis, visionOption,BAR_RADIUS/4.0, &p2,&p3);

}
void Tirante::drawZero(float meshQual, bool wireframe, char visionAxis, int visionOption,float radius, Ponto *p1, Ponto *p2){

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
void Tirante::recalculaMBR(Ponto *p1, Ponto *p2){

    float xMBR, yMBR, zMBR, XMBR, YMBR, ZMBR;
    if(p1->x < p2->x){

        xMBR = p1->x - BAR_RADIUS;
        XMBR = p2->x + BAR_RADIUS;

    }else{

        XMBR = p1->x + BAR_RADIUS;
        xMBR = p2->x - BAR_RADIUS;

    }
    if(p1->y < p2->y){

        yMBR = p1->y - BAR_RADIUS;
        YMBR = p2->y + BAR_RADIUS;

    }else{

        YMBR = p1->y + BAR_RADIUS;
        yMBR = p2->y - BAR_RADIUS;

    }
    if(p1->z < p2->z){

        zMBR = p1->z - BAR_RADIUS;
        ZMBR = p2->z + BAR_RADIUS;

    }else{

        ZMBR = p1->z + BAR_RADIUS;
        zMBR = p2->z - BAR_RADIUS;

    }
    setMBR(xMBR, yMBR, zMBR, XMBR, YMBR, ZMBR);



}
Tirante::~Tirante()
{
    delete []object_difusa;
}
