# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 16:22:48 2016

@author: jeanbache
"""

# Une classe Pile, une classe File
# Remarque d'un collegue : pas de majuscule dans les noms de méthodes

class Pile:
    
    def __init__(self):
        self.lst = []
        
    def is_empty(self):
        return len(self.lst) == 0
        
    def push(self, v):
        """ Empile v"""
        self.lst.append(v)
        
    def pop(self):
        """ Depile et renvoie le sommet
            Precaution: tester avant que la pile ne soit pas vide
        """
        return self.lst.pop()
        
    # Toutes operations en temps constant (ou constant amorti)
        
class File:
    
    def __init__(self):
        self.sortie = Pile()
        self.entree = Pile()
        
    def is_empty(self):
        return self.entree.is_empty() and self.sortie.is_empty()
        
    def push(self, v):
        self.entree.push(v)
        
    def pop(self):
        """ Precaution: s'assurer que la file n'est pas vide avant"""
        if self.sortie:
            self.sortie.pop()
        else:
            while self.entree:
                self.sortie.push(self.entree.pop())
            self.sortie.pop()
            
        