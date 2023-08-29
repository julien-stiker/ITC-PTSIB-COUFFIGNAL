#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 15:56:00 2022

@author: julien stiker
"""

### Graphe aléatoire
from random import randint, choices
   
def alea_directed_graphe(n: int)-> dict:
    G = {}
    S = list(range(n))
    for i in range(n):
        adj = {}
        nb_v = randint(0,n-1)
        voisins = choices(S, k = nb_v)
        for v in sorted(voisins):
            adj[v] = randint(0,100)
        G[i] = adj
    return G


### Construction du graphe général de taille n x m

import math    
    
def grid(n, m):
    vertex = [(x,y) for x in range(n) for y in range(m)]
    G = {}
    for v in vertex:
        x, y = v
        voisins = {}
        if x == 0:
            if y == 0:
                voisins[(1,0)] = 1
                voisins[(0,1)] = 1
                voisins[(1,1)] = math.sqrt(2)
            elif y < m-1:
                voisins[(0,y-1)] = 1
                voisins[(0,y+1)] = 1
                voisins[(1,y)] = 1
                voisins[(1,y+1)] = math.sqrt(2)
                voisins[(1,y-1)] = math.sqrt(2)
            elif y == m-1:
                voisins[(1,m-1)] = 1
                voisins[(0,m-2)] = 1
                voisins[(1,m-2)] = math.sqrt(2)
        if x == n-1:
            if y == 0:
                voisins[(n-2,0)] = 1
                voisins[(n-1,1)] = 1
                voisins[(n-2,1)] = math.sqrt(2)
            elif y < m-1:
                voisins[(n-1,y+1)] = 1
                voisins[(n-1,y+1)] = 1
                voisins[(n-2,y)] = 1
                voisins[(n-2,y+1)] = math.sqrt(2)
                voisins[(n-2,y-1)] = math.sqrt(2)
            elif y == m-1:
                voisins[(n-1,m-1)] = 1
                voisins[(n-1,m-2)] = 1
                voisins[(n-1,m-2)] = math.sqrt(2)
        if 1 <= x <= n-2 and y == 0:
            voisins[(x-1, 0)] = 1
            voisins[(x+1, 0)] = 1
            voisins[(x, y+1)] = 1
            voisins[(x-1,y+1)] = math.sqrt(2)
            voisins[(x+1,y+1)] = math.sqrt(2)
        if 1 <= x <= n-2 and y == m-1:
            voisins[(x-1, m-1)] = 1
            voisins[(x+1, m-1)] = 1
            voisins[(x, y-1)] = 1
            voisins[(x-1,y-1)] = math.sqrt(2)
            voisins[(x+1,y-1)] = math.sqrt(2)
        if 1 <= x <= n-2 and 1 <= y <= m-2:
            voisins[(x+1,y)], voisins[(x-1,y)] = 1, 1
            voisins[(x,y+1)], voisins[(x,y-1)] = 1, 1
            voisins[(x+1,y+1)], voisins[(x-1,y+1)] = math.sqrt(2), math.sqrt(2)
            voisins[(x+1,y-1)], voisins[(x-1,y-1)] = math.sqrt(2), math.sqrt(2)
        G[v] = voisins
        
    return G
            

#### Les graphes :


G1 = grid(25, 25)
for x in range(15,20):
    for y in range(5,20):
        G1[(x,y)]={}
for x in range(5,20):
    for y in range(15,20):
        G1[(x,y)]={}


        
 
G2 = grid(25, 25)
for x in range(3,25):
    for y in range(19,22):
        G2[(x,y)]={}

        

G3 = grid(25, 25)
for x in range(3,25):
    for y in range(19,22):
        G3[(x,y)]={}
for x in range(0,22):
    for y in range(5,8):
        G3[(x,y)]={}



G4 = grid(25, 25)
for x in range(3,25):
    for y in range(19,22):
        G4[(x,y)]={}
for x in range(0,22):
    for y in range(5,8):
        G4[(x,y)]={}
for x in range(3,6):
    for y in range(11,19):
        G4[(x,y)] = {}
for x in range(19,22):
    for y in range(8,17):
        G4[(x,y)]={}    
        
G5 = grid(50,50)
for x in range(3,50):
    for y in range(19,22):
        G5[(x,y)]={}
for x in range(0,22):
    for y in range(5,8):
        G5[(x,y)]={}
for x in range(3,6):
    for y in range(11,19):
        G5[(x,y)] = {}
for x in range(19,22):
    for y in range(8,17):
        G5[(x,y)]={}
for x in range(20,23):
    for y in range(21,33):
        G5[(x,y)] = {}
for x in range(0,12):
    for y in range(30,33):
        G5[(x,y)]={}    

for x in range(15,21):
    for y in range(27,30):
        G5[(x,y)]={}  
        
for x in range(3,40):
    for y in range(40,43):
        G5[(x,y)]={}  
        
for x in range(37,40):
    for y in range(26,40):
        G5[(x,y)]={}  
        
for x in range(21,40):
    for y in range(10,13):
        G5[(x,y)]={} 
for x in range(44,49):
    for y in range(35,38):
        G5[(x,y)]={}

### Affichage
import matplotlib.pyplot as plt
        
def __quadrillage(n,m):
    for x in range(n+1):
        plt.plot([x-0.5,x-0.5],[-0.5,m-.5], color='#318ce7')
    for y in range(m+1):
        plt.plot([-0.5,n-.5],[y-0.5,y-0.5], color='#318ce7')
        
def __affiche_graph(G):
    for s in G.keys():
        x, y = s
        if G[s] == {}:
            plt.plot(x,y,marker="X", color='blue')
            
def __affiche_chemin(path, visited):
    for x,y in visited:
        plt.plot(x,y,marker="+", color="orange")
    for x,y in path:
        plt.plot(x,y,marker="o", color="magenta")    
        
def affichage(G, n, m, path, visited):
    fig = plt.figure(dpi=300,figsize=(10, 10)) 
    plt.axis("equal")
    __quadrillage(n, m)
    __affiche_graph(G)
    __affiche_chemin(path, visited)
    plt.show
    


    
