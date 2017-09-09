#include "Bar.h"

using namespace ManipularVetor;

GLuint Bar::bar64;
GLuint Bar::bar64n;
int Bar::split = 32;

Bar::Bar():Objeto3D(){
    object_difusa = new GLfloat[4];
    object_difusa[0] = 1.0;
    object_difusa[1] = 1.0;
    object_difusa[2] = 0.94176;
    object_difusa[3] = 1.0;
}
void Bar::draw(float meshQual, bool wireframe, char visionAxis, int visionOption, Objeto3D *obj1, Objeto3D *obj2){

    Ponto p1,p2;
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
    float t = (SPHERE_RADIUS - 0.1)/::distancia(p1,p2);
    Ponto vetDir;
    vetDir.x = p2.x - p1.x;
    vetDir.y = p2.y - p1.y;
    vetDir.z = p2.z - p1.z;
    Ponto pReta = p1;
    p1.x = pReta.x + vetDir.x*t;
    p1.y = pReta.y + vetDir.y*t;
    p1.z = pReta.z + vetDir.z*t;
    t = 1.0 - t;
    p2.x = pReta.x + vetDir.x*t;
    p2.y = pReta.y + vetDir.y*t;
    p2.z = pReta.z + vetDir.z*t;

    drawZero(meshQual, wireframe,visionAxis,visionOption, &p1,&p2);


}
void Bar::drawZero(float meshQual, bool wireframe, char visionAxis, int visionOption, Ponto *p1, Ponto *p2){

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
            gluCylinder(quadric, BAR_RADIUS, BAR_RADIUS, v, 16, 1);
            /*glPushMatrix();

                glScalef(BAR_RADIUS,BAR_RADIUS,v);
                glBindBuffer(GL_ARRAY_BUFFER, bar64n);
                glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 0, NULL);
                glBindBuffer(GL_ARRAY_BUFFER, bar64);
                glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, NULL);
                glDrawArrays(GL_QUADS,0,split*4);

            glPopMatrix();*/

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
            gluCylinder(quadric, BAR_RADIUS, BAR_RADIUS, v, resolucao, 1);

            /*glPushMatrix();

                glScalef(BAR_RADIUS,BAR_RADIUS,v);
                glBindBuffer(GL_ARRAY_BUFFER, bar64n);
                glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 0, NULL);
                glBindBuffer(GL_ARRAY_BUFFER, bar64);
                glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, NULL);
                glDrawArrays(GL_QUADS,0,split*4);

            glPopMatrix();*/

            //draw the first cap
            gluQuadricOrientation(quadric,GLU_INSIDE);
            gluDisk( quadric, 0.0, BAR_RADIUS, resolucao, 1);
            glTranslatef( 0,0,v );

            //draw the second cap
            gluQuadricOrientation(quadric,GLU_OUTSIDE);
            gluDisk( quadric, 0.0, BAR_RADIUS, resolucao, 1);

        glPopMatrix();
    }
    gluDeleteQuadric(quadric);
}
void Bar::initBuffer(){

    float b64[split*3*4];///numero de divisoes dabarra: split
    float b64n[split*3*4];
    int num = 0;
    float theta = 0;

    for(int i = 0; i < split; i++){

        ///vertice 1
        b64[num] = cos(theta);
        b64n[num] = cos(theta);
        num++;
        b64[num] = sin(theta);
        b64n[num] = sin(theta);
        num++;
        b64[num] = 1.0;
        b64n[num] = 0;
        num++;

        ///vertice 2
        b64[num] = cos(theta);
        b64n[num] = cos(theta);
        num++;
        b64[num] = sin(theta);
        b64n[num] = sin(theta);
        num++;
        b64[num] = 0.0;
        b64n[num] = 0.0;
        num++;

        ///vertice 3
        b64[num] = cos(theta + 2*M_PI/(float)split);
        b64n[num] = cos(theta + 2*M_PI/(float)split);
        num++;
        b64[num] = sin(theta + 2*M_PI/(float)split);
        b64n[num] = sin(theta + 2*M_PI/(float)split);
        num++;
        b64[num] = 0.0;
        b64n[num] = 0.0;
        num++;

        ///vertice 4
        b64[num] = cos(theta + 2*M_PI/(float)split);
        b64n[num] = cos(theta + 2*M_PI/(float)split);
        num++;
        b64[num] = sin(theta + 2*M_PI/(float)split);
        b64n[num] = sin(theta + 2*M_PI/(float)split);
        num++;
        b64[num] = 1.0;
        b64n[num] = 0.0;
        num++;

        theta += 2*M_PI/(float)split;


    }
    glGenBuffers(1, &bar64);
    glBindBuffer(GL_ARRAY_BUFFER, bar64);
    glBufferData(GL_ARRAY_BUFFER, sizeof(b64), b64, GL_STATIC_DRAW);

    glGenBuffers(1, &bar64n);
    glBindBuffer(GL_ARRAY_BUFFER, bar64n);
    glBufferData(GL_ARRAY_BUFFER, sizeof(float)*split*3*4, b64n, GL_STATIC_DRAW);
    glEnableVertexAttribArray(2);


}
void Bar::recalculaMBR(Ponto *p1, Ponto *p2){

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
Bar::~Bar()
{
    delete []object_difusa;
}
