#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:54:11 2020

@author: Sébastien LECLERCQ
SNT/NSI Lycée Louis Bertrand - Briey
"""
import random

##########  SLIDE n°20  #############
def creerNoeud(val,fg=None,fd=None):
    return((val,fg,fd))

def fg(v):
    return(v[1])
    
def fd(v):
    return(v[2])
    
def val(v):
    return(v[0])

'''Pour éviter de les resaisir à chaque fois, le rendu de 2 arbres
Le premier demandé, le second un ABR
'''
a=(8, (1, (2, None, None), (3, None, None)), (5, None, None))
b=(8, (1, (0, None, None), (3, None, None)), (10, None, None))
c=(10, (5, (3, None, None), (11, None, None)), (12, None, None))


##########  SLIDE n°22 bis, erreur de lecture de consigne  #############

def comptElt(arbre):
    ''' Compte le nombre de feuille d'un arbre'''
    h=1
    if fg(arbre) == None :
        if fd(arbre) ==None :
            return(h)
        else :
            return(h+comptElt(fd(arbre)))
    elif (fd(arbre)==None) :
        return(h+comptElt(fg(arbre)))
    else :
        return(h+comptElt(fg(arbre))+comptElt(fd(arbre)))

##########  SLIDE n°22  #############

def hauteur(arbre):
    ''' Détermine la hauteur d'un arbre'''
    if arbre == None :
        return(0)
    else :
        h = max(hauteur(fg(arbre)),hauteur(fd(arbre)))
    return(h+1)


        
##########  SLIDE n°25  #############

def sommeElt(arbre):
    ''' Fait la somme des entier contenus dans l'arbre'''
    if arbre == None:
        return(0)
    else :
        return(val(arbre)+sommeElt(fg(arbre))+sommeElt(fd(arbre)))
        

def prefixe(arbre):
    ''' affichage racine, sous-arbre gauche, sous-arbre droit '''
    if arbre != None :
        print(val(arbre))
        prefixe(fg(arbre))
        prefixe(fd(arbre))
        
        
def postfixe(arbre):
    ''' affichage sous-arbre gauche, sous-arbre droit, racine'''
    if arbre != None :
        postfixe(fg(arbre))
        postfixe(fd(arbre))
        print(val(arbre))

def infixe(arbre):
    ''' affichage sous-arbre gauche, racine, sous-arbre droit, racine'''
    if arbre != None :
        infixe(fg(arbre))
        print(val(arbre))
        infixe(fd(arbre))



##########  SLIDE n°27 #############

def minArbre(arbre):
    '''Recherche le min d'un abre par un parcourt récursif'''
    if fg(arbre)==None:
        if fd(arbre)==None :
            return(val(arbre))
        else :
            return(min(minArbre(fd(arbre)),val(arbre)))
    else :
        if fd(arbre)==None :
            return(min(minArbre(fg(arbre)),val(arbre)))
        else :
            return(min(minArbre(fg(arbre)),val(arbre),minArbre(fd(arbre))))

def maxArbre(arbre):
    '''Recherche le min d'un abre par un parcourt récursif'''
    if fg(arbre)==None:
        if fd(arbre)==None :
            return(val(arbre))
        else :
            return(max(maxArbre(fd(arbre)),val(arbre)))
    else :
        if fd(arbre)==None :
            return(max(maxArbre(fg(arbre)),val(arbre)))
        else :
            return(max(maxArbre(fg(arbre)),val(arbre),maxArbre(fd(arbre))))

def arbreBinRe(arbre):
    '''Vérification que ce soit un arbre binaire de recherche
    Très très lourd. Il vaut mieux passer par infixe(arbre) qui affiche les valeurs dans l'ordre croissant.'''
    if arbre == None : 
        return(True)
    elif fg(arbre) ==None :
        if fd(arbre)==None :
            return(True)
        else :
            if val(arbre)<minArbre(fd(arbre)) :
                return(True)
            else : 
                return(False)
    elif fd(arbre)==None:
        if maxArbre(fg(arbre))<val(arbre) :
            return(True)
        else :
            return(False)
    else :
        return(maxArbre(fg(arbre))<val(arbre) and  val(arbre)<minArbre(fd(arbre)) and arbreBinRe(fg(arbre)) and arbreBinRe(fd(arbre)) )
    
##########  SLIDE n°29 #############

def rechArbreBinRe(arbre,k):
    '''Recherche d'un élément dans un ABR'''
    if arbreBinRe(arbre) != True :
        print("Ce n'est pas un arbre binaire de recherche !")
    else :
        if arbre==None :
            return(False)
        elif k==val(arbre):
            return(True)
        elif k>val(arbre):
            return(rechArbreBinRe(fd(arbre),k))
        else :
            return(rechArbreBinRe(fg(arbre),k))
            
##########  SLIDE n°31 #############

def inserer(arbre,k):
    '''Insertion d'un élément dans un ABR
    if arbreBinRe(arbre) != True :
        print("Ce n'est pas un arbre binaire de recherche !")
    '''
    if arbre == None:
        return(creerNoeud(k))
    elif (k < val(arbre) and fg(arbre) == None):
        return(creerNoeud(val(arbre),creerNoeud(k),fd(arbre)))
    elif (k > val(arbre) and fd(arbre) ==None) :
        return(creerNoeud(val(arbre),fg(arbre),creerNoeud(k)))
    elif(k < val(arbre)):
        return(creerNoeud(val(arbre),inserer(fg(arbre),k),fd(arbre)))
    elif(k > val(arbre)):
        return(creerNoeud(val(arbre),fg(arbre),inserer(fd(arbre),k)))

'''Les 3 listes demandées'''
l=[5, 9, 7, 8, 4, 2, 6, 3, 1]
ll=[1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
lll=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''Construction des 3 arbres'''
al=None
for i in l :
    al=inserer(al,i)
all=None
for i in ll :
    all=inserer(all,i)
alll=None
for i in lll :
    alll=inserer(alll,i)


def constArbre(n):
    '''Construction d'un ABR où on aurait insèrer les n 
    premiers entiers dans un ordre aléatoire'''
    arbre=None
    liste=[i for i in range(n)]
    listeAlea=random.sample(liste, n)
    for i in listeAlea :
        arbre=inserer(arbre,i)
    return(arbre)
    



def miniArbreRe(arbre):
    '''Recherche du minimum dans un arbre'''
    if fg(arbre)!=None :
        return(miniArbreRe(fg(arbre)))
    else :
        return(val(arbre))
'''
for nbVal in [10,100,1000,10000]:
    """Test demandé"""
    TotalHauteur=0
    for i in range(100):
        arbre=constArbre(nbVal)
        TotalHauteur+=hauteur(arbre)
    print('Moyenne des hauteurs pour n=',nbVal,' : ',TotalHauteur/100)
'''