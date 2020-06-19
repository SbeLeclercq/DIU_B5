#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:13:25 2020

@author: Sébastien LECLERCQ
SNT/NSI Lycée Louis Bertrand - Briey
"""
##################################################################
##Première remarque, j'ai travaillé mercredi ;) 
##Je ne mets pas les exercices "papier"
##################################################################
def ajoutNoeud(graphe,val,etat='I'):
    '''
    Effet : Création d'un noeud et ajout au graphe passé en paramètre
    Entrée : Une liste (le graphe), une valeur (l'ID du noeud, qui peut être de différents types),un état (de base 'I' pour inconnu)
    Sortie : aucune 
    '''
    graphe.append([val,etat,[]])
    
def accesInfo(noeud):
    '''
    Effet : Renvoie l'id d'un noeud
    Entrée : Une liste (un noeud)
    Sortie : Selon ce qui a été décidé dans le graphe (Entier, chaine de caractère...)
    '''
    return(noeud[0]) 

def ajoutArete(graphe,dep,arr,info=1,bijec=False,etat='I'):
    '''
    Effet : Création d'une arête entre 2 noeuds et ajout au graphe passé en paramètre
    Entrée : Une liste (le graphe), une valeur l'ID du noeud de départ, une valeur l'ID du noeud d'arrivée, 
    une valeur qui caractérise l'arête, un booléen pour indiquer si le graphe est orienté (bijec=False) ou non (bijec=True),
    un état (de base 'I' pour inconnu)
    Sortie : aucune 
    '''
    for noeud in graphe :
        if accesInfo(noeud)==dep:
            noeud[2].append([arr,info,etat])
    if bijec==True:
        for noeud in graphe :
            if accesInfo(noeud)==arr:
                noeud[2].append([dep,info,etat])
        

#Création du graphe (une liste vide)
graphe=[]
graphe2=[]

#Ajout d'un graphe perso
ajoutNoeud(graphe2,'A')
ajoutNoeud(graphe2,'B')
ajoutNoeud(graphe2,'C')
ajoutNoeud(graphe2,'D')
ajoutArete(graphe2,'A','B',1,True)
ajoutArete(graphe2,'B','C',1,True)
ajoutArete(graphe2,'C','A',1,True)
ajoutArete(graphe2,'A','D',1,True)




#Ajout des noeuds (page 81 graphe de gauche)
ajoutNoeud(graphe,'A')
ajoutNoeud(graphe,'B')
ajoutNoeud(graphe,'C')
ajoutNoeud(graphe,'D')
ajoutNoeud(graphe,'E')

#Ajout des arêtes (page 81 graphe de gauche)
ajoutArete(graphe,'A','B',3,True)
ajoutArete(graphe,'A','E',1,True)
ajoutArete(graphe,'A','D',1,True)
ajoutArete(graphe,'B','E',1,True)
ajoutArete(graphe,'B','C',1,True)
ajoutArete(graphe,'C','E',7,True)
ajoutArete(graphe,'C','D',3,True)
ajoutArete(graphe,'D','E',2,True)

#Fonctions annexes :

def valNoeud(noeud):
    return(noeud[0])

def areteNoeud(noeud):
    return(noeud[2])

def valArete(arete):
    return(arete[0])

def etatNoeud(noeud):
    return(noeud[1])

def etatArete(arete):
    return(arete[2])


def etatVisite(graphe,dep,ar):
    '''
    Effet passe une arête en état visitée
    Entrée : un graphe, Id de départ et d'arrivée (de noeuds)
    Sortie : aucune
    '''
    for noeud in graphe :
        if valNoeud(noeud)==dep or valNoeud(noeud)==ar:
            for arete in areteNoeud(noeud):
                if valArete(arete)==dep or valArete(arete)==ar:
                    arete[2]='V'

def etatRetour(graphe,dep,ar):
    '''
    Effet passe une arête en état retour
    Entrée : un graphe, Id de départ et d'arrivée (de noeuds)
    Sortie : aucune
    '''
    for noeud in graphe :
        if valNoeud(noeud)==dep or valNoeud(noeud)==ar:
            for arete in areteNoeud(noeud):
                if valArete(arete)==dep or valArete(arete)==ar:
                    arete[2]='R'
                    
def etatDecouvert(graphe,val):
    '''
    Effet passe un noeud en Découvert
    Entrée : un graphe, Id de noeud
    Sortie : aucune
    '''
    for noeud in graphe :
        if valNoeud(noeud)==val:
            noeud[1]='D'


#Parcours en profondeur
'''Remarque : Mon id est une lettre donc le choix des chemins est aleatoire
On peut ajouter des contraintes sur le poids des chemins.
'''

def parcoursProfondeur(graphe,Id):
    '''
    Effet :parcours en profondeur du graphe avec changement d'état.
    Entrée :
    Sortie :
    '''
    etatDecouvert(graphe,Id)
    for noeud in graphe :
        if valNoeud(noeud)==Id :
            for arete in areteNoeud(noeud) :
                if etatArete(arete)=='I' :
                    for arrive in graphe :
                        if valNoeud(arrive)==valArete(arete) :
                            if etatNoeud(arrive) == 'I' :
                                etatVisite(graphe,valNoeud(Id),valNoeud(arrive))
                                parcoursProfondeur(graphe,valNoeud(arrive))
                            else :
                                etatRetour(graphe,valNoeud(Id),valNoeud(arrive))
    
def parcoursProfondeur2(graphe,Id,liste=[]):
    '''
    Effet : parcours en profondeur du graphe.
    Entrée :
    Sortie :La liste dans l'ordre des noeuds visités.
    '''
    etatDecouvert(graphe,Id)
    liste.append(Id)
    for noeud in graphe :
        if valNoeud(noeud)==Id :
            for arete in areteNoeud(noeud) :
                if etatArete(arete)=='I' :
                    for arrive in graphe :
                        if valNoeud(arrive)==valArete(arete) :
                            if etatNoeud(arrive) == 'I' :
                                etatVisite(graphe,valNoeud(Id),valNoeud(arrive))
                                parcoursProfondeur2(graphe,valNoeud(arrive),liste)
                            else :
                                etatRetour(graphe,valNoeud(Id),valNoeud(arrive))
    return(liste)

                                
                                


print(parcoursProfondeur2(graphe,'A'))

print(graphe)
    
    



