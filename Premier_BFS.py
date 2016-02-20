# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:44:20 2016

@author: jeanbache
"""

# Un premier BFS (Breadth First Search)
# Voir autre implémentation avec une File (FIFO) 


def BFS_1(graph, source = 0):
    """ Parcours en largeur d'un graphe non orienté, non pondéré
        :Args: graph : liste d'adjacence ou dictionnaire d'adjacence
                     : les sommets : de 0 à n-1
                     : pour k entre 0 et n-1
                     : graph[k] est la liste des sommets adjacents à k 
              source : l'un des sommets, par défaut 0
        Retourne: 
        deux dictionnaires: 
        dictionnaire level: level[v] est la distance de la source à v
        dictionnaire parent: parent[v] est le prédécesseur de v dans
                             le parcours BFS
        Complexité temporelle: O(V+E) (V nombre de sommets, E nombre d'aretes)
        A justifier
    """
    level = {source: 0}
    parent = {source: None}
    i = 1
    frontiere = [source]   # niveau precedent i-1
    while frontiere:
        next = []          # la frontiere suivante, prochain niveau : i
        for u in frontiere:
            for voisin in graph[u]:
                if voisin not in parent: # voisin pas encore vu (test en O(1) (dictionnaire))
                    parent[voisin] = u
                    level[voisin] = i   # level[u] + 1
                    next.append(voisin)
        frontiere = next
        i +=1      
    return level, parent
    
# Pour obtenir un chemin de la source à un sommet v:
# parent[v], parent[parent[v]], etc ... et inverser
                