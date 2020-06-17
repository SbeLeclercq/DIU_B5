#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 21:24:26 2020

@author: Sébastien LECLERCQ
SNT/NSI Lycée Louis Bertrand - Briey
"""

def suivant(liste):
    return(liste[1])

def val(liste):
    return(liste[0])

def creerElt(k):
    return((k,()))

def insereTete(liste,k):
    if liste==():
        return(creerElt(k))
    else:
        return((k,liste))

def insereQueue(liste,k):
    if liste==() :
        return(creerElt(k))
    else :
        return(val(liste),insereQueue(suivant(liste),k))

def accesId(liste,id):
    if id==1 :
        return(val(liste))
    else :
        return(accesId(suivant(liste),id-1))

def supprimeTete(liste):
    return(suivant(liste))

def supprimeQueue(liste):
    if suivant(liste)==():
        return(())
    else:
        return((val(liste),supprimeQueue(suivant(liste))))

def affListe(liste):
    print(val(liste))
    if suivant(liste)!=():
        affListe(suivant(liste))

l=()
l=insereTete(l,5)
l=insereTete(l,4)
l=insereTete(l,3)
l=insereTete(l,2)
l=insereQueue(l,6)
l=insereQueue(l,7)
print("Liste complète :")
affListe(l)
print("Element 1 de la liste : ",accesId(l,1))
print("Element 5 de la liste : ",accesId(l,5))

l=supprimeTete(l)
print("SupprimerTete :")
affListe(l)
l=supprimeQueue(l)
print("Supprimer queue : ")
affListe(l)




