#include "AVL.h"

AVL::AVL()
{
    raiz = NULL;
}
void AVL::deletaH(No* p){

    if(p != NULL){

        deletaH(p->getAnt());
        deletaH(p->getProx());
        delete p;

    }

}
int AVL::Altura (No* p){

	int Alt_Esq, Alt_Dir;
	if (p == NULL) return 0;
	else
	{
		Alt_Esq = Altura (p->getAnt());
		Alt_Dir = Altura (p->getProx());
		if (Alt_Esq > Alt_Dir)
		{
			return (1 + Alt_Esq);
		}
		else
		{
			return (1 + Alt_Dir);
		}
	}
}

int AVL::Calcula_FB(No* p){

    if(p == NULL)return 0;
    return (Altura(p->getAnt())- Altura(p->getProx()));
}

void AVL::Seta_FB(No* p){

     if (p!= NULL)
     {
         p->setMarca(Altura(p->getAnt())- Altura(p->getProx()));
		 Seta_FB(p->getAnt());
		 Seta_FB(p->getProx());
     }
}
No* AVL::rotacao_direita(No* N3){

       No* N2= N3->getAnt();
       if(N2->getProx()) N3->setAnt(N2->getProx());
       else N3->setAnt(NULL);
       N2->setProx(N3);
       return N2;
}

No* AVL::rotacao_esquerda(No* N1){

       No* N2= N1->getProx();
       if(N2->getAnt()) N1->setProx(N2->getAnt());
       else N1->setProx(NULL);
       N2->setAnt(N1);
       return N2;
}

No* AVL::rotacao_dupla_direita (No* N3){

       No* N1= N3->getAnt();
       No* N2= N1->getProx();

       if(N2->getAnt()) N1->setAnt(N2->getAnt());
       else N1->setProx(NULL);

       if(N2->getProx()) N3->setAnt(N2->getProx());
       else N3->setAnt(NULL);

       N2->setAnt(N1);
       N2->setProx(N3);

       return N2;
}

No* AVL::rotacao_dupla_esquerda (No* N1){

       No* N3= N1->getProx();
       No* N2= N3->getAnt();

       if(N2->getAnt()) N1->setProx(N2->getAnt());
       else N1->setProx(NULL);

       if(N2->getProx()) N3->setAnt(N2->getProx());
       else N3->setAnt(NULL);

       N2->setAnt(N1);
       N2->setProx(N3);

       return N2;
}

No* AVL::CorrigeAVL(No* p){
	if(p != NULL)
	{
		p->setMarca(Calcula_FB(p));
		if(p->getMarca() == 2)
		{
			p->getAnt()->setMarca(Calcula_FB(p->getAnt()));
			if(p->getAnt()->getMarca() > 0)
			{
				p = rotacao_direita(p);
			}
			else
			{
				p =  rotacao_dupla_direita(p);
			}
		}
		else if(p->getMarca() == -2)
		{
			p->getProx()->setMarca(Calcula_FB(p->getProx()));
			if(p->getProx()->getMarca() < 0)
			{
				p = rotacao_esquerda(p);
			}
			else
			{
				p =  rotacao_dupla_esquerda(p);
			}
		}
		p->setAnt(CorrigeAVL(p->getAnt()));
		p->setProx(CorrigeAVL(p->getProx()));
    }
    return p;
}


No* AVL::InsereAVL(No* p, int ch, Objeto3D* obj){
	if (p == NULL)
	{
		p = new No();
		p->setValor(ch);
		p->setMarca(0);
		p->setObj(obj);
		return p;
	}
	else
	{
		if(ch < p->getValor())
		{
			p->setAnt(InsereAVL(p->getAnt(),ch,obj));
		}
		else
		{
			p->setProx(InsereAVL(p->getProx(),ch,obj));
		}
	}
	return p;
}


No* AVL::Consulta(No* p, int ch){

    while (p != NULL)
    {
		if(ch == p->getValor())
		{
			return p;
		}
		else
		{
			if(ch < p->getValor())
			{
				p = p->getAnt();
			}
			else
			{
				p = p->getProx();
			}
		}
	}
	return NULL;
}

No* AVL::RemoveAVL(No* p){
	No* pAux;
	No* pAuxPai;

	if((p->getAnt() == NULL) && (p->getProx() == NULL))
	{
        delete p;
    	return NULL;
	}
	else if((p->getAnt() == NULL) && (p->getProx() != NULL))
	{
		pAux = p->getProx();
        delete p;
    	return pAux;
	}
	else if((p->getAnt() != NULL) && (p->getProx() == NULL))
	{
		pAux = p->getAnt();
		delete p;
		return pAux;
	}
	else
	{
		if(p->getAnt()->getProx() == NULL)
        {
			pAux = p->getAnt();
    	    p->getAnt()->setProx(p->getProx());
            delete p;
    		return pAux;
        }
        else
        {
    		pAux = p->getAnt();

    		while (pAux->getProx() != NULL)
    		{
    			pAuxPai = pAux;
                pAux = pAux->getProx();
    		}

    		if(pAux->getAnt() != NULL) pAuxPai->setProx(pAux->getAnt());
    		else pAuxPai->setProx(NULL);

            pAux->setProx(p->getProx());
    	    pAux->setAnt(p->getAnt());

    		delete p;
    		return pAux;
        }
	}

	return NULL;
}

No* AVL::Remove(No* p, int ch){

	No* pAux = p;
	No* pPai;
	bool bdir = false;

	if(ch == p->getValor()) return RemoveAVL(pAux);

    while (pAux != NULL)
    {
		if(ch == pAux->getValor())
		{
			if(bdir) pPai->setProx(RemoveAVL(pAux));
			else pPai->setAnt(RemoveAVL(pAux));
			return p;
		}
		else
		{
			if(ch < pAux->getValor())
			{
				bdir = false;
				pPai = pAux;
				pAux = pAux->getAnt();
			}
			else
			{
				bdir = true;
				pPai = pAux;
				pAux = pAux->getProx();
			}
		}
	}
	return p;
}
void AVL::insere(int p, Objeto3D *obj){

    raiz = InsereAVL(raiz, p, obj);
    raiz = CorrigeAVL(raiz);
    Seta_FB(raiz);

}
void AVL::remover(int p){

    raiz=  Remove(raiz, p);
    raiz = CorrigeAVL(raiz);
    Seta_FB(raiz);

}
Objeto3D *AVL::busca(int p){

    No* aux = Consulta(raiz, p);
    return aux->getObj();

}
AVL::~AVL()
{
    deletaH(raiz);
}
