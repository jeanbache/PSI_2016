# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:39:11 2016

@author: jeanbache
"""

# TRIS (par comparaison). Voir aussi Counting Sort, Radix Sort 

# Ce qu'on a fait sur les tris en 2015_16
# Il faut que je rajoute le fichier tests
# Et scinder ce fichier en plusieurs :)

import copy
import random

#I Fusion et Tri fusion (Mergesort)

# Deux strategies : aucune en place
# A: une premiere en copiant toute la liste une fois
#                 on s'en sert de liste auxiliaire pour aller-retours

# B: une deuxieme en ne creant de liste auxiliaire que dans la fonction de fusion
# Question : laquelle preferer ? 

# A Strategie 1
def merge_1(g, m, d, a, aux):
    """fusionne les sous-listes triées (en entree) a[g:m] et a[m:d]
       :param: a   : liste d'entiers que l'on veut trier par tri_fusion
       :param: aux : initialement copie de a, 
                     definie dans la fonction principale du tri_fusion
                    (fonction un_merge_sort(a))
       :param: g, m, d (gauche, milieu, droite(exclu))
       
       retour: aucun (None)
       
       en sortie, la tranche a[g:d] est triee
       
       Complexite: O(N) si N = (d-g)
    """
    
    for k in range(g, d):          # copie de la tranche à fusionner
        aux[k] = a[k]              
        
    i, j = g, m                    # un indice pour chaque sous tranche
    
    for k in range(g, d):          # boucle realisant la fusion dans a[g:d]
                                   # NB: on peut "condenser" les conditions booleennes
        if i >= m :                # si la premiere sous liste est epuisee
            a[k] = aux[j] ; j += 1
        elif j >= d:               # si la seconde sous liste est epuisee
            a[k] = aux[i] ; i += 1
        elif aux[j] < aux[i]:      # permet d'avoir un tri stable
            a[k] = aux[j] ; j += 1
        else:
            a[k] = aux[i] ; i += 1
        
# Le même, sans commentaire, avec un while

def merge_1_bis(g, m, d, a, aux):
    """Voir commentaires merge_1"""
    for k in range(g, d):          
        aux[k] = a[k]
        
    i, j, k = g, m, g
    
    while i < m and j < d:
        if aux[j] < aux[i]:
            a[k] = aux[j]
            k += 1; j+= 1
        else:
            a[k] = aux[i]
            k += 1; i+= 1
            
    while i < m:
        a[k] = aux[i]
        k += 1; i+= 1
        
    while j < d:
        a[k] = aux[j]
        k += 1; j+= 1

# Fonction de tri fusion numero 1
def un_merge_sort(a):
    """ code principal du tri fusion avec merge_1, ou merge_1_bis
        :param: a liste d'entiers a trier par ordre croissant
        tri en place: NON (liste auxiliaire aux)
        tri stable: OUI
        Complexite temporelle: O(nln(n)) si n est la longueur de a
        retour: None
        """
    aux = copy.copy(a) # on ne cree de nouvelle liste qu'a cet endroit
                       # cette liste aux permet les aller-retour entre a et aux
    def rec_sort(a, g, d):
        """Fonction recursive
           param: a 
           param: g indice gauche de la tranche (inclus)
           param: d indice droit de la tranche (exclu)
           """
        if g < d - 1: # seulement s'i y a deux éléments au moins dans a[g:d]
            m = g + (d-g) // 2
            rec_sort(a, g, m) # appel recursif gauche
            rec_sort(a, m, d) #appel recursif droit
            if a[m - 1] > a[m]: # s'il faut retrier !
                merge_1(g, m, d, a, aux) # fusion 
                
    rec_sort(a, 0, len(a)) #appel de la fonction recursive sur toute la liste
    
        
# Strategie 2 

def merge_2(one, two):
    """ Fonction de fusion de deux listes 
        :param: one, two listes par ex d'entiers deja triees(ordre croissant)
        retourne: liste fusion de one et two
        Complexite : O(len(one)+len(two)) 
    """
    len_1 , len_2 = len(one), len(two)
    three = [_ for _ in range(len_1+len_2)] # Utile (?) ou preferer append ? 
    i, j, k = 0, 0, 0
    while i < len_1 and j < len_2:
        if two[j] < one[i]:
            three[k] = two[j]
            k += 1; j += 1
        else:
            three[k] = one[i]
            k += 1; i += 1
            
    while i < len_1:
        three[k] = one[i]
        k += 1; i += 1
        
    while j < len_2:
        three[k] = two[j]
        k += 1; j += 1
        
    return three
        
        
def un_autre_merge_sort(a):
    """ code principal du tri fusion avec merge_2
        :param: a liste d'entiers a trier par ordre croissant
        tri en place: NON (listes auxiliaires dans la fusion)
        tri stable: OUI
        Complexite temporelle: O(nln(n)) si n est la longueur de a
        retour: None
        """
    aux = copy.copy(a) # on ne cree de nouvelle liste qu'a cet endroit
                       # cette liste aux permet les aller-retour entre a et aux
    def rec_sort_bis(a, g, d):
        """Fonction recursive
           param: a 
           param: g indice gauche de la tranche (inclus)
           param: d indice droit de la tranche (exclu)
           """
        if g < d - 1: # seulement s'i y a deux éléments au moins dans a[g:d]
            m = g + (d-g) // 2
            rec_sort_bis(a, g, m) # appel recursif gauche
            rec_sort_bis(a, m, d) #appel recursif droit
            if a[m - 1] > a[m]: # s'il faut retrier !
                a[g:d] = merge_2(a[g:m],a[m:d])
                
    rec_sort_bis(a, 0, len(a)) #appel de la fonction recursive sur toute la liste
                            
#II Tri insertion puis Shellsort
#II A: tri insertion
def swap(a, i, j):
    a[i], a[j] = a[j], a[i]
    
def insertion(a,i):
    """ a liste d'entiers par exemple, i indice valide pour a
        Hypothese: a[:i] deja triee par ordre croissant
        Insere a[i] a sa place dans a[:i+1]
        Complexité : O(i)
    """
    j = i
    while (j > 0) and (a[j] < a[j-1]): # le "and" est paresseux
        swap(a, j - 1, j)              # NB: autre version avec moins d'echanges
        j -= 1                         #     memoriser a[i], chercher sa place en
                                       #     decalant

def insertion_sort(a):
    """ Trie la liste a par ordre croissant
        Tri en place: OUI, stable : OUI. Complexité: quadratique (lineaire si deja triee)
    """
    n = len(a)
    for i in range(1,n):
        insertion(a, i)
        
#II B: Shellsort    

def h_insertion(a, i, h): 
    """insertion modulo h de a[i] 
       dans la sous liste supposee triee modulo h a[:i]
    """
    j = i
    while (j >= h) and (a[j] < a[j-h]): # le "and" est paresseux
        swap(a, j, j - h)
        j = j - h
        
def h_insertion_sort(a, h):
    n = len(a)
    for i in range(1,n):
        h_insertion(a, i, h)        
                
def shell_sort(a):
    """Trie la liste a par ordre croissant
       En realisant un tri insertion par pas de h pour h dans la suite h(0)=1 h(k+1)= 3*h(k)+1
       Complexite ???
       """
    n = len(a)
    h = 1
    while (3*h + 1) < n:
        h = 3*h + 1
    while h >= 1:
        h_insertion_sort(a, h)
        h = h // 3
    
                
#III Tri rapide: premiere version sans precaution
#III.A Partition basique, hypothese clefs distinctes ou a peu pres (?)
#III.B Traduction en Python d'un code Java de Sedgewick
#III.C Cas où les clefs en double sont nombreuses: Partition en 3

def partition(a, g, d):# d INCLUS (tranche a[g: d+ 1])
    pivot = a[g]
    indice = g
    for i in range(g + 1, d + 1):
        if a[i] < pivot:
            indice += 1
            swap(a, indice, i)
    swap(a, g, indice)
    return indice

def quick_sort_rec(a, g, d):
    """ Tri rapide recursif tranche a[g:d+1]"""
    if g < d:
        m = partition(a, g, d)
        quick_sort_rec(a, g, m - 1)
        quick_sort_rec(a, m + 1, d)
    
def quick_sort(a):
    """ Tri rapide d'une liste a (d'entiers par exemple) (ordre croissant)
        En place : OUI
        Stable: NON
        Optionnel:  melanger la liste avant pour eviter le cas O(n^2)
        Complexite: en moyenne O(nln(n)), 
                    au pire O(n^2) (liste presque triee, nombreuses clefs en double)
                    Voir 3_way_quicksort ci dessous en cas de nombreuses clefs identiques
    """
    n = len(a)
    for i in range(1,n):        # shuffle de la liste (optionnel)
        r = random.randint(0,i)
        swap(a, i, r)
        
    quick_sort_rec(a, 0, n-1) # appel de la fonction recursive sur toute la liste

  

#III.B Adaptation d'un code Java de Sedgewick pour le tri rapide

def partition_sedge(a, g, d):
    i = g
    j = d + 1
    while True:
        i += 1
        while a[i] < a[g]:
            if i == d:
                break
            i += 1
        j = j - 1
        while a[g] < a[j]:
            if j == g:
                break
            j = j - 1
            
        if i >= j:
            break
        swap(a, i, j)
    swap(a, g, j)
    return j
    
def sedgesort_rec(a, g, d):
    if g < d:
        j = partition_sedge(a, g, d)
        sedgesort_rec(a, g, j - 1)
        sedgesort_rec(a, j + 1, d)
        
def sedgewick(a):                  # ajouter le shuffle 
    sedgesort_rec(a, 0, len(a) - 1)
    
  
    
#III.C 3-way Qsort en cas de clefs dupliquees nombreuses

    
def three_way_qsort(a, g, d):
    """Tri recursif d'une liste d'entiers a
       :param: a liste d'entiers(par exemple)
       :param: g indice valide pour a, extremite gauche de la tranche
       :param: d indice valide pour a, extremite droite de la tranche
       Partitionne la tranche a[g:d+1] en 3:
       < pivot | = pivot | > pivot
       Deux appels récursifs sur les tranches aux extremités
    """
    if g < d:
        lt = g            # Faire un schéma pour vérifier l'invariant de boucle
        gt = d
        v = a[g] # le pivot
        i = g
        while i <= gt:              
            if a[i] < v:
                swap(a, lt, i)
                i += 1
                lt += 1
            elif a[i] > v:
                swap(a, i, gt)
                gt = gt - 1
            else:
                i += 1
        three_way_qsort(a, g, lt - 1)
        three_way_qsort(a, gt + 1, d)

def three_way_sort(a):
    three_way_qsort(a, 0, len(a) - 1)


# rajouter tests



    
    