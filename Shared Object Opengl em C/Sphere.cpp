#include "Sphere.h"

using namespace ManipularVetor;

GLuint Sphere::sph64;
GLuint Sphere::sph64n;
GLuint Sphere::sphVao;


Sphere::Sphere():Objeto3D()
{

    object_difusa = new GLfloat[4];
    object_difusa[0] = 1.0;
    object_difusa[1] = 0.2;
    object_difusa[2] = 0.2;
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

            /*glEnableClientState(GL_NORMAL_ARRAY);
            glEnableClientState(GL_VERTEX_ARRAY);

            glBindBuffer(GL_ARRAY_BUFFER, sph64n);
            //glNormalPointer(GL_FLOAT, 64*64*4, NULL);
            glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 0, NULL);
            glNormalPointer(GL_FLOAT, 32*32*4, NULL);
            glBindBuffer(GL_ARRAY_BUFFER, sphVao);
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, NULL);
            glDrawArrays(GL_QUADS,0,32*32*4);

            glDisableClientState(GL_VERTEX_ARRAY);
            glDisableClientState(GL_NORMAL_ARRAY);*/

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

            /*glEnableClientState(GL_NORMAL_ARRAY);
            glEnableClientState(GL_VERTEX_ARRAY);

            glBindBuffer(GL_ARRAY_BUFFER, sph64n);
            //glNormalPointer(GL_FLOAT, 32*32*4, NULL);
            glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 0, NULL);

            glBindBuffer(GL_ARRAY_BUFFER, sphVao);
            //glVertexPointer(3, GL_FLOAT, 0, 0);
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, NULL);

            glDrawArrays(GL_QUADS,0,32*32*4);

            glDisableClientState(GL_VERTEX_ARRAY);
            glDisableClientState(GL_NORMAL_ARRAY);*/

        glPopMatrix();

    }

}
void Sphere::initBuffer(){

    int split = 32;
    float s64[split*split*3*4];///numero de faces: split*split, numero de vertices em cada uma: 4, numero de coordenadas: 3;
    float s64n[split*split*3*4];///numero de faces: split*split, numero de vertices em cada uma: 4, numero de coordenadas da normal: 3;

    int num = 0;
    int numNormal = 0;
    float norma = 0.0;
    float theta = 0.0;
    float phi = 0.0;

    for(int k = 0; k < split; k++){

        for(int i = 0; i < split; i++){

            ///vertice
            s64[num] = SPHERE_RADIUS*sin(phi)*cos(theta);
            num++;
            s64[num] = SPHERE_RADIUS*sin(phi)*sin(theta);
            num++;
            s64[num] = SPHERE_RADIUS*cos(phi);
            num++;

            ///normal

            s64n[numNormal] = s64[num-3];
            numNormal++;
            s64n[numNormal] = s64[num-2];
            numNormal++;
            s64n[numNormal] = s64[num-1];
            numNormal++;

            norma = s64n[numNormal-3]*s64n[numNormal-3] + s64n[numNormal-2]*s64n[numNormal-2] + s64n[numNormal-1]*s64n[numNormal-1];
            norma = sqrt(norma);
            s64n[numNormal-3] /= norma;
            s64n[numNormal-2] /= norma;
            s64n[numNormal-1] /= norma;

            ///vertice
            s64[num] = SPHERE_RADIUS*sin(phi + M_PI/(float)split)*cos(theta);
            num++;
            s64[num] = SPHERE_RADIUS*sin(phi + M_PI/(float)split)*sin(theta);
            num++;
            s64[num] = SPHERE_RADIUS*cos(phi + M_PI/(float)split);
            num++;


            ///normal

            s64n[numNormal] = s64[num-3];
            numNormal++;
            s64n[numNormal] = s64[num-2];
            numNormal++;
            s64n[numNormal] = s64[num-1];
            numNormal++;

            norma = s64n[numNormal-3]*s64n[numNormal-3] + s64n[numNormal-2]*s64n[numNormal-2] + s64n[numNormal-1]*s64n[numNormal-1];
            norma = sqrt(norma);
            s64n[numNormal-3] /= norma;
            s64n[numNormal-2] /= norma;
            s64n[numNormal-1] /= norma;


            ///vertice
            s64[num] = SPHERE_RADIUS*sin(phi + M_PI/(float)split)*cos(theta + 2*M_PI/(float)split);
            num++;
            s64[num] = SPHERE_RADIUS*sin(phi + M_PI/(float)split)*sin(theta + 2*M_PI/(float)split);
            num++;
            s64[num] = SPHERE_RADIUS*cos(phi + M_PI/(float)split);
            num++;


            ///normal

            s64n[numNormal] = s64[num-3];
            numNormal++;
            s64n[numNormal] = s64[num-2];
            numNormal++;
            s64n[numNormal] = s64[num-1];
            numNormal++;

            norma = s64n[numNormal-3]*s64n[numNormal-3] + s64n[numNormal-2]*s64n[numNormal-2] + s64n[numNormal-1]*s64n[numNormal-1];
            norma = sqrt(norma);
            s64n[numNormal-3] /= norma;
            s64n[numNormal-2] /= norma;
            s64n[numNormal-1] /= norma;


            ///vertice
            s64[num] = SPHERE_RADIUS*sin(phi)*cos(theta + 2*M_PI/(float)split);
            num++;
            s64[num] = SPHERE_RADIUS*sin(phi)*sin(theta + 2*M_PI/(float)split);
            num++;
            s64[num] = SPHERE_RADIUS*cos(phi);
            num++;

            theta += 2*M_PI/(float)split;

            ///normal

            s64n[numNormal] = s64[num-3];
            numNormal++;
            s64n[numNormal] = s64[num-2];
            numNormal++;
            s64n[numNormal] = s64[num-1];
            numNormal++;

            norma = s64n[numNormal-3]*s64n[numNormal-3] + s64n[numNormal-2]*s64n[numNormal-2] + s64n[numNormal-1]*s64n[numNormal-1];
            norma = sqrt(norma);
            s64n[numNormal-3] /= norma;
            s64n[numNormal-2] /= norma;
            s64n[numNormal-1] /= norma;

        }
        theta = 0;
        phi += M_PI/(float)split;

    }


    glGenBuffers(1, &sph64);
    glBindBuffer(GL_ARRAY_BUFFER, sph64);
    glBufferData(GL_ARRAY_BUFFER, sizeof(s64), s64, GL_STATIC_DRAW);

    glGenVertexArrays(1, &sphVao);
    glBindVertexArray(sphVao);
    glBindBuffer(GL_ARRAY_BUFFER, sph64);
    glEnableVertexAttribArray(0);

    glGenBuffers(1, &sph64n);
    glBindBuffer(GL_ARRAY_BUFFER, sph64n);
    glBufferData(GL_ARRAY_BUFFER, sizeof(s64), s64, GL_STATIC_DRAW);
    glEnableVertexAttribArray(2);

}
void Sphere::recalculaMBR(){

    setMBR(-SPHERE_RADIUS + centro.x,-SPHERE_RADIUS + centro.y,-SPHERE_RADIUS + centro.z,SPHERE_RADIUS + centro.x,SPHERE_RADIUS + centro.y,SPHERE_RADIUS + centro.z);

}
Sphere::~Sphere()
{
    delete []object_difusa;
}
