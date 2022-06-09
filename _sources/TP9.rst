******************************************************
TP9 : Plus courts chemins
******************************************************


.. note:: **Les objectifs du TP :**

    * Implémenter Dijkstra avec un ensemble et une file de priorité.
    * Utiliser Dikstra.
    * Découvrir A*.
   

.. note:: Pour représenter un egraphe pondéré on utilisera une structure de dictionnaire de dictionnaires.
    
    Par exemple :

        .. code-block:: python

            G = {
                0: {1: 1},
                1: {3: 2},
                2: {1: 3},
                3: {0: 1, 4: 1},
                4: {0: 3, 1: 2, 2: 2, 5: 2},
                5: {2: 4, 7: 0},
                6: {0: 3, 3: 0, 5: 2},
                7: {2: 3}
                }
 
    représente le graphe :

        .. figure:: Dijkstra.png
            :align: center
            :scale: 75%
            
    De sorte que :code:`G[3]` est un dictionaire dont les clefs sont les successeurs du sommet :code:`3`, et tel que :code:`G[3][4]` est le poids de l'arrête :math:`(3, 4)`.
    

        
Variations autour de Dijkstra
=============================

.. note:: Pour rappel :

    .. figure:: algo_dijkstra.png
        :align: center
        

**Exercice :** Ecrire une fonction de signature :code:`dijkstra_set(G: dict, src: int)->tuple[list[int],list[int]]`, qui prend comme argument un graphe :code:`G` pondéré sous forme de dictionnaire de dictionnaires, et un sommet :code:`src`, et qui retourne les listes :code:`dict` et :code:`pred`, respectivement des distances à :code:`src` et des prédecesseurs dans le plus court chemin de :code:`src`à un sommet :code:`s` . L'algorithme utilisera une ensemble comme décrit dans le cours.

.. admonition:: Solution
   :class: dropdown; tip
   
    .. code-block:: python
    
            inf = float('inf')

            def min_dist(dist,M):
                s = None
                mini = inf
                for i in range(len(dist)):
                    if i in M and dist[i] < mini:
                        s = i
                        mini = dist[i]
                return s

            def dijkstra_set(G: dict, src: int)->tuple[list[int],list[int]]:

                n = len(G)

                dist = [inf] * n
                pred = [None] * n

                pred[src] = -1
                dist[src] = 0

                M = set(range(n))

                s = src

                while s != None and len(M) > 0:
                    M.discard(s)
                    for v in G[s]:
                        if dist[s] + G[s][v] < dist[v]:
                            dist[v] = dist[s] + G[s][v]
                            pred[v] = s
                    s = min_dist(dist, M)

                return dist, pred




**Exercice :** Ecrire une seconde fonction de signature :code:`dijkstra_heap(G: dict, src: int)->tuple[dict,dict]`, qui prend comme argument un graphe :code:`G` sous forme de dictionnaire de dictionnaires, et un sommet :code:`src`, et qui retourne les dictionnaires :code:`dist` et :code:`pred`, respectivement des distances à :code:`src` et des prédecesseurs dans le plus court chemin de :code:`src` à un sommet :code:`s`. L'algorithme utilisera un file de priorité comme décrit dans le cours. Vous utiliserez le module :code:`heap` fournit avec le TP.


.. admonition:: Solution
   :class: dropdown; tip
   
    .. code-block:: python

        from heap import *

        def dijkstra_heap(G: dict, src: int):
            
            n = len(G)
            dist, pred = {}, {}
            for node in G.keys():
                dist[node] = inf
                pred[node] = None

            pred[src] = -1
            dist[src] = 0

            M = Heap([])

            M.push((dist[src],src))

            while len(M)>0:

                _, s = M.pop()

                for v in G[s]:
                    d = dist[v]
                    if dist[s] + G[s][v] < dist[v]:
                        dist[v] = dist[s] + G[s][v]
                        pred[v] = s
                        M.update((d, v), (dist[v], v))


            return pred, dist





**Exercice :** Utiliser la fonction :code:`alea_directed_graphe`, qui se trouve dans le module :code:`TP9` pour générer des graphes orientés et pondérés de tailles :math:`100*2^k` pour :math:`1\leq k\leq 7`, et comparer les temps d'exécution des deux fontions :code:`dijkstra_set` et :code:`dijkstra_heap`. Que constatez-vous ?

**Exercice :** Ecrire une fonction de signature :code:`build_path(pred: dict, src, dst):->list` qui retourne la liste des sommets qui constituent le plus court chemin de :code:`src` à :code:`dst`.

.. admonition:: Solution
   :class: dropdown; tip
   
    .. code-block:: python

        def build_path(pred: dict, src , dst):
            path = []
            node = dst

            while pred[node] != -1:
                path = [node] + path
                node = pred[node]
            path = [src] + path
            return path

**Exercice :** Modifier le code la fonction :code:`dijkstra_heap`, pour écrire une nouvelle fonction de signature :code:`dijkstra(G: dict, src: int, dst: int)->float, list[int]`, qui retourne le plus court chemin de :code:`src` à :code:`dst` dans le graphe :code:`G`, s'il existe, ainsi que sa longueur, et :code:`None` sinon. Vous veuillerez à arrêter l'agorithme dès que la destination :code:`dst` est atteinte.

**Exercice (bonus) :** Ecrice une fonction :code:`round_trip(G: dict, src: int, dst: int)->list[int]` qui retourne, s'il existe, le plus court chemin aller-retour de :code:`src` à :code:`dst` qui au retour ne passe pas par les mêmes sommets qu'à l'aller.



L'algorithme A*
===============

.. note:: L'algorithme A* est un algorithme de recherche de chemin dans un graphe entre un noeud initial :code:`src` et un noeud final :code:`dst`. Il utilise une évaluation heuristique sur chaque noeud pour estimer le meilleur chemin y passant, et visite ensuite les noeuds par ordre de cette évaluation heuristique. Vous trouverez de nombreuses informations `ici <https://fr.wikipedia.org/wiki/Algorithme_A*>`_.

    Imaginons que le graphe que l'on va parcourir représente les cases d'un plateau sur lequel on souhaite se déplacer.
    
    .. figure:: grille.png
        :align: center
        
    Si nous souhaitons trouver le chemin le plus court du sommet :code:`(0, 0)` au sommet :code:`(2, 2)`. L'application de l'algorithme de Dijkstra, va visiter les neuf points du sommets du graphe, en procédant à un parcours largeur. Notre intuition est que des trois sommets :code:`(1, 0)`, :code:`(1, 1)` et :code:`(0, 1)`, nous devrions dès le début privilégier celui qui nous rapproche le plus de la destination, soit le :code:`(1, 1)`. 
    
    .. figure:: grille3.png
        :align: center


    Pour déterminer quelle est la bonne direction on peut utiliser comme heuristique :code:`h` la distance entre le noeud étudié et la déstination, quelque soit cette distance (distance euclidienne, distance de Manhattan, etc...). Dans ce cas, la priorité avec laquelle on doit traiter un sommet est donnée par la minimisation de la quantité :code:`dist[s]+h(s,dst)`, où :code:`dist[s]` est la distance de :code:`src` à :code:`s`, et :code:`h(s, dst)` est la distance de :code:`s` à la destination :code:`dst`.
    
    Si l'heuristique est la fonction identiquement nulle, on retombe sur Dijkstra.
    
    
**Exercice :** Implémenter une fonction de signature :code:`A_star(G: dict, h: callable, src: tuple[int,int], dst:tuple[int,int])->list[int],int, int`, qui prend comme argument un graphe, une heuristique, un sommet source et un sommet destination et qui retourne le dictionnaire :code:`pred` des prédecesseurs dans le plus court chemin trouvé entre :code:`src` et :code:`dst`, s'il existe. Ainsi que le nombre de sommets visités lors de la recherche du chamin, et le nombre d'itération de la boucle principale effectuées pour déterminer le chemin.

.. admonition:: Solution
   :class: dropdown; tip
   
   .. code-block:: python
   


.. note:: Dans le module :code:`TP9`, vous trouverez les graphes qui représentent les plateaux suivants :

    .. figure:: plateau_L.png
        :align: center
        :scale: 20%
        
        Graphe G1
        
    .. figure:: plateau_B.png
        :align: center
        :scale: 20%
        
        Graphe G2
        
    .. figure:: plateau_2B.png
        :align: center
        :scale: 20%
        
        Graphe G3
        
    .. figure:: plateau_Lab.png
        :align: center
        :scale: 20%
        
        Graphe G4
        
    .. figure:: plateau_Lab2.png
        :align: center
        :scale: 20%
        
        Graphe G5
    
    Le but de cette partie et de voir quelles solutions sont proposées par Dijkstra et par A* pour aller de la case en bas à gauche à la case en haut à droite. 
        
    Vous avez à votre disposition les fonctions du module :code:`TP9` pour afficher les plateaux ainsi que les chemins trouvés.
        
    Voici différentes propositions d'heuristiques très classqiues et moins classiques :
    
    .. code-block:: python
    

        def h(node, dst):
            return abs(node[1]-dst[1])+abs(node[0]-dst[0])

        def h1(node, dst):
            return (node[1]-dst[1])**2+(node[0]-dst[0])**2

        def h2(node , dst):
            return max(abs(node[1]-dst[1]),abs(node[0]-dst[0]))

        def h3(node , dst):
            return abs(node[1]-dst[1])*abs(node[0]-dst[0])

        def h4(node , dst):
            return 1/(1+(abs(node[1])))

        def h5(node, dst):
            return 1/(1+(abs(node[1])+abs(node[0])))



**Exercice :** Pour chaqu'un des graphes de 1 à 4, tracer les chemins obtenus avec Dijkstra et A*, avec chacune des heuristiques.

**Exercice :** Pour chaque graphe, noter le nombres d'itérations, le nombre de sommets visités ainsi que la longueur des chemins trouvés, par Dijkstra et A* pour chacune des heuristiques. 

    * Quelle semble être la meilleure heuristique pour chacun des graphes ?
    * Une des heuristiques est-elle meilleure que toutes les autres ?
   
.. note:: D'après Wikipédia :

    Un algorithme de recherche qui garantit de toujours trouver le chemin le plus court à un but s'appelle « algorithme admissible ». Si A* utilise une heuristique qui ne surestime jamais la distance (ou plus généralement le coût) du but, A* peut être avéré admissible. Une heuristique qui rend A* admissible est elle-même appelée « heuristique admissible ».

    On peut démontrer que A* ne considère pas plus de nœuds que tous les autres algorithmes admissibles de recherche, à condition que l'algorithme alternatif n'ait pas une évaluation heuristique plus précise. Dans ce cas, A* est l'algorithme informatique le plus efficace garantissant de trouver le chemin le plus court.
    
    Le prochain exercice, va nous permettre d'observer ce qu'il se passe si l'on passe d'une heuristique admissible à une heuristique qui surestime systématiquement le coût pour atteindre la destination.

**Exercice :** Ecrire une fonction de signature :code:`Aw_star(G: dict, h: callable, src: int, dst: int, w: float)->list[int],int, int`, telle que :

    :code:`Aw_star(G, h, src, dst, w) = A_star(G, w * h, src, dst)` 

L'argument :code:`w` agit ici comme un poids pour l'heuristique.

En prenant différentes valeurs pour :code:`w` (prendre par exemple :math:`1`, :math:`10^4` et :math:`10^5`) observez les différents résultats obtenus avec le graphe G5 et toutes les heuristiques.

Comparez la longueur des chemins trouvés, observez qu'ils ne sont pas toujours optimaux mais que dans certaines situations ils ont nécessité beaucoup moins de traitement.

On pourra par exemple enregistrer les résultats dans un fichier csv, dont les colones seraient : ['Fonctions','Poids w','Longueur','Sommets traités','Itérations'], puis ajouter une colone pour calculer le pourcentage que représente l'augmentation de la longueur du chemin par rapport à la longueur optimale, puis trier les données seulon le nombre de sommet traités.




