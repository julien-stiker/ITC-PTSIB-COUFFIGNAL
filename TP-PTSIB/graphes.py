import Queue
import heapq

class GraphMat:
      
      def __init__(self, order, directed=False):
            """ Args :
                  order ( int ) : Number of vertices .
                  directed (bool): True if the graph is directed. False otherwise. """
            self.order = order
            self.directed = directed
            self.adj = [[0 for j in range(order)] for i in range(order)]

    

class Graph:
    """ Simple class for graph: adjacency lists

    Attributes:
        order (int): Number of nodes.
        directed (bool): True if the graph is directed. False otherwise.
        adjlists (List[List[int]]): Lists of connected vertices for each vertex.
        labels (list[str]): optionnal vector of vertex labels
        costs (dict): [optionnal] edge (src, dst) -> cost (float)
        infos (dict)! optionnal dictionary for informations (purpose, dimensions, ...)
    """

    def __init__(self, order, directed=False, costs=False, labels=None):
        """Init graph, allocate adjacency lists

        Args:
            order (int): Number of nodes.
            directed (bool): True if the graph is directed. False otherwise.
            labels (list[str]): optionnal vector of vertex labels
            costs (bool): True if the graph is weighted. False otherwise. 

        """

        self.order = order
        self.directed = directed
        if costs:
            self.costs = {}
        else:
            self.costs = None
        self.adjlists = []
        for _ in range(order):
            self.adjlists.append([])
        self.labels = labels


    def addedge(self, src, dst, cost=None):
        """Add egde to graph.
    
        Args:
            src (int): Source vertex.
            dst (int): Destination vertex.
            cost: if not None, the cost of edge (src, dst)
    
        Raises:
            IndexError: If any vertex index is invalid.
            Exception: If graph is None.
    
        """
    
        # Check graph and vertex indices.
        if self is None:
            raise Exception('Empty graph')
        if src >= self.order or src < 0:
            raise IndexError("Invalid src index")
        if dst >= self.order or dst < 0:
            raise IndexError("Invalid dst index")
        # Add edge if multi or not already existing, and reverse-edge if undirected.
        if src != dst and dst not in self.adjlists[src]:
            self.adjlists[src].append(dst)
            if not self.directed and dst != src:
                self.adjlists[dst].append(src)
        if self.costs != None:
            self.costs[(src, dst)] = cost
            if not self.directed:
                self.costs[(dst, src)] = cost


    def addvertex(self, number=1, labels=None):
        """Add number vertices to graph.
    
        Args:
            number (int): Number of vertices to add.
            labels (str list) optionnal list of new vertex labels
        Raises:
            Exception: If graph is None.
                
        """
        # Check graph
        if self is None:
            raise Exception('Empty graph')    
        # Increment order and extend adjacency list
        self.order += number
        for _ in range(number):
            self.adjlists.append([])
        if labels:
            self.labels += labels

    def removeedge(self, src, dst):
        """Remove egde from the graph.
    
        Args:
            src (int): Source vertex.
            dst (int): Destination vertex.
    
        Raises:
            IndexError: If any vertex index is invalid.
            Exception: If graph is None.
    
        """
    
        # Check graph and vertex indices.
        if self is None:
            raise Exception('Empty graph')
        if src >= self.order or src < 0:
            raise IndexError("Invalid src index")
        if dst >= self.order or dst < 0:
            raise IndexError("Invalid dst index")
        # Add edge if multi or not already existing, and reverse-edge if undirected.
        if dst in self.adjlists[src]:
            self.adjlists[src].remove(dst)
            if self.costs:
                self.costs.pop((src, dst))
            if not self.directed and dst != src:
                self.adjlists[dst].remove(src)
                if self.costs:
                    self.costs.pop((dst, src))
                
        
def dot(ref):
    """Write down dot format of graph.

    Args:
        ref (Graph).

    Returns:
        str: String storing dot format of graph.

    """

    # Check if empty graph.
    if ref is None:
        return "graph G { }"
    # Build dot for non-empty graph.
    (s, link) = ("digraph ", " -> ") if ref.directed else ("graph ", " -- ")
    s += " G {\n"
    if not ref.labels:   
        s += "node [shape = circle]\n"
    for src in range(ref.order):
        if ref.labels:
            s += "  " + str(src) + '[label = "' + ref.labels[src] + '", xlabel = "' + str(src) + '"]\n'
        else:
            s += "  " + str(src) + '\n'        
        for dst in ref.adjlists[src]:
            cost = ' [label=' + str(ref.costs[(src, dst)]) + '] ' if ref.costs else ""
            if ref.directed or src >= dst:
                s += "  " + str(src) + link + str(dst) + cost + '\n'
    s += '}'
    return s

def toDotHighlightEdges(G, edges):
    (dot, link) = ("digraph ", " -> ") if G.directed else ("graph ", " -- ")
    dot += "G {\n"
    if not G.labels:
        dot += "node [shape = circle]\n"
        
    #vertex traversal
    for s in range(G.order):
        if G.labels:
            dot += "  " + str(s) + '[caption = "' + G.labels[s] + '"]\n'
        else:
            dot += "  " + str(s) + '\n'        
        # adjacent list traversal
        for adj in G.adjlists[s]:   
            if G.directed or s >= adj:
                if (s, adj) in edges or (adj, s) in edges:
                    highLight = ', color="red", style="bold"'
                else:
                    highLight = ''
                cost = 'label=' + str(G.costs[(s, adj)]) if G.costs else ''
                if highLight or cost:
                    cost = ' [' + cost + highLight + ']'
                dot += "  " + str(s) + link + str(adj) + cost + '\n'
    dot += '}'
    return dot
    



def display(ref, eng=None, highlightedges=None):
    """
    *Warning:* Made for use within IPython/Jupyter only.
    eng: graphivz.Source "engine" optional argument (try "neato", "fdp", "sfdp", "circo")
    """
    try:
        from graphviz import Source
        from IPython.display import display
    except:
        raise Exception("Missing module: graphviz and/or IPython.")
    if highlightedges:
        dotstr = toDotHighlightEdges(ref, highlightedges)
    else:
        dotstr = dot(ref)
    display(Source(dotstr, engine = eng))

    
# load / save gra(wgra) format    

def load(filename):
    """Build a new graph from a GRA file.

    Args:
        filename (str): File to load.

    Returns:
        Graph: New graph.

    Raises:
        FileNotFoundError: If file does not exist. ????

    """

    f = open(filename)
    lines = f.readlines()
    infos = {}
    i = 0
    while '#' in lines[i]: # lines[i][0] == '#'
        (key, val) = lines[i][1:].strip().split(": ")
        infos[key] = val
        i += 1
    
    directed = bool(int(lines[i]))
    order = int(lines[i+1])
    g = Graph(order, directed)
    g.infos = infos
    if g.infos and "labels" in g.infos:
        g.labels = g.infos["labels"].split(',')
    for line in lines[i+2:]:
        edge = line.strip().split(' ')
        (src, dst) = (int(edge[0]), int(edge[1]))
        g.addedge(src, dst)
    f.close()
    return g



def load_weightedgraph(filename, costType=float):
    """Build a new weighted graph from a WGRA file.

    Args:
        filename (str): File to load.

    Returns:
        Graph: New graph.
    """
    f = open(filename)
    lines = f.readlines()
    infos = {}
    i = 0
    while '#' in lines[i]:
        (key, val) = lines[i][1:].strip().split(": ")
        infos[key] = val
        i += 1
    directed = bool(int(lines[i]))
    order = int(lines[i+1])
    G = Graph(order, directed, costs=True)
    G.infos = infos
    if G.infos and "labels" in G.infos:
        G.labels = G.infos["labels"].split(',')    
    for line in lines[i+2:]:
        edge = line.strip().split(' ')
        (x, y, cost) = (int(edge[0]), int(edge[1]), costType(edge[2]))
        G.addedge(x, y, cost)
    f.close()

    return G
    
def save(G, fileOut):
    gra = ""
    if G.labels:
        lab = "#labels: "
        for i in range(G.order - 1):
            lab += G.labels[i] + ','
        lab += G.labels[-1]
        gra += lab + '\n'
    gra += str(int(G.directed)) + '\n'
    gra += str(G.order) + '\n'
    for s in range(G.order):
        for adj in G.adjlists[s]:
            if G.directed or s >= adj:
                cost = ' ' + str(G.costs[(s, adj)]) if G.costs else ""
                gra += str(s) + " " + str(adj) + cost + '\n'
    fout = open(fileOut, mode='w')
    fout.write(gra)
    fout.close()


# add-on: sorts adjacency lists -> to have same results as those asked in tutorials/exams

def sort(G):
    """
    sort adjacency lists -> to have same results as those asked in tutorials/exams
    """
    for i in range(G.order):
        G.adjlists[i].sort()

#
def fromlist(order, directed, edges):
    """Build a new graph from an int tuple list.

    Args:
        order (int): Order of graph.
        directed (bool): True if the graph is directed. False otherwise.
        edges (List[(int, int)]): Source/Destination tuple list.

    Returns:
        Graph: New graph.

    Raises:
        IndexError: If either order or edge extremity is invalid.

    """

    # Check order:
    if order <= 0:
        raise IndexError('Invalid order')
    # Build graph
    g = Graph(order, directed)
    for (src, dst) in edges:
        g.addedge(src, dst)
    return g

# Another way to display graphs

def displaySVG(ref, filename='temp'):
    """Render a graph to SVG format.

    *Warning:* Made for use within IPython/Jupyter only.

    Args:
        ref (Graph).
        filename (str): Temporary filename to store SVG output.

    Returns:
        SVG: IPython SVG wrapper object for graph.

    """

    # Ensure all modules are available
    try:
        from graphviz import Graph as gvGraph, Digraph as gvDigraph
        from IPython.display import SVG
    except:
        raise Exception("Missing module: graphviz and/or IPython.")
    # Traverse graph and generate temporary Digraph/Graph object
    output_format = 'svg'
    if ref.directed:
        graph = gvDigraph(filename, format=output_format)
    else:
        graph = gvGraph(filename, format=output_format)
    if ref is not None:
        for src in range(ref.order):
            src_id = 'node_' + str(src)
            graph.node(src_id, label=str(src))
            for dst in ref.adjlists[src]:
                if ref.directed or src >= dst:
                    graph.edge(src_id, 'node_' + str(dst))
    # Render to temporary file and SVG object
    graph.render(filename=filename, cleanup=True)
    return SVG(filename + '.' + output_format)


def affiche_matrix(M):
      for ligne in M:
            print(ligne, end="\n")
            
G1 = Graph(9, directed=True)

G1.adjlists = [[1, 1, 1, 6, 2],
[3, 3], [6, 8], [6] ,
[3] ,
[2, 6], [3, 4], [6, 5, 8], [8]]

G2 = Graph(9, directed=False)

G2.adjlists = [[2, 1, 1, 1],
[0, 0, 0, 3, 3], [0] ,
[1, 1],
[5, 6, 7],
[4, 7, 8],
[4, 7],
[4, 6, 5, 8, 7], [7, 5]]

def in_ou_degrees(G):
    d_in = [0] * G.order
    d_out = [0] * G.order
    for x in range(G.order):
          d_out[x] = len(G.adjlists[x])
          for y in G.adjlists[x]:
                d_in[y] += 1
    return d_in, d_out


#G3 = adj2mat(G1)

"""
Breadth-first search (BFS)
"""

# simple BFS, vertices are marked with booleans, with adjacency matrix
# display vertices, on line per tree

def __BFS(Gmat, s, M):
    q = Queue.Queue()
    q.enqueue(s)
    M[s] = True
    while not q.isempty():
        x = q.dequeue()
        print(x)
        for y in range(Gmat.order):
            if Gmat.adj[x][y]:    # x is adjacent to y
                if not M[y]:  # y is not marked
                    M[y] = True
                    q.enqueue(y)
                

def BFS(Gmat):
    M = [False] * Gmat.order
    for s in range(Gmat.order):
        if not M[s]:    #s is not marked
            __BFS(Gmat, s, M)
        print()


def __BFS_forest(G, s, p):
    q = Queue.Queue()
    q.enqueue(s)
    p[s] = -1   # root
    while not q.isempty():
        x = q.dequeue()
        for y in G.adjlists[x]:
            if p[y] == None:
                q.enqueue(y)
                p[y] = x

def BFS_forest(G):
    p = [None] * G.order
    for s in range(G.order):
        if p[s] is None:
            __BFS_forest(G, s, p)
    return p    # represents the spanning forest
    
# graph depth-first traversal with back edge detection
def __dfsForest(G, s, p, edges):
    for adj in G.adjlists[s]:
        if p[adj] == None:  # tree edge
            p[adj] = s      # vertices has to be marked here
            print(s, "->", adj)
            edges.append((s, adj, "tree"))
            __dfsForest(G, adj, p, edges)
        else:
            if adj != p[s]:   
                if (adj, s, "back") not in edges:   # not for students!
                    edges.append((s, adj, "back"))
                
def dfs_graph_for_dot(G, src=None):
    (edges, roots) = ([], [])
    p = [None] * G.order
    if src != None:
        p[src] = -1
        roots.append(src)
        __dfsForest(G, src, p, edges)
    for s in range(G.order):
        if p[s] == None:
            p[s] = -1
            roots.append(s)
            __dfsForest(G, s, p, edges)
    return (p, roots, edges)   


def dfs(G):
    
    pref = [0]* G.order
    suff = [0]* G.order
    cpt = 0
    cpts = 0
    for s in range(G.order):
        if pref[s] == 0:
            
            cpt, cpts = __dfs(G,s,pref,suff,cpt, cpts)
        
    return pref, suff
            
def __dfs(G,s,pref,suff,cpt,cpts):
    cpt += 1
    
    pref[s] = cpt 
    for v in G.adjlists[s]:
        if pref[v] == 0:
            print("{} -> {} arc couvrant".format(s,v))
            cpt, cpts = __dfs(G,v,pref,suff,cpt, cpts)
        elif pref[s] < pref[v]:
            print("{} -> {} arc en avant".format(s,v))
        elif suff[v] == 0:
            print("{} -> {} arc retour".format(s,v))
        else:
            print("{} -> {} arc croisé".format(s,v))
    cpts += 1
    suff[s] = cpts
    return cpt, cpts
            
            
def dfs_dico(G):
    n = len(G)
    pref = [0]* n
    suff = [0]* n
    cpt = 0
    cpts = 0
    for s in range(n):
        if pref[s] == 0:
            cpt, cpts = __dfs_dico(G,s,pref,suff,cpt, cpts)
        
    return pref, suff
            
def __dfs_dico(G,s,pref,suff,cpt,cpts):
    cpt += 1
    
    pref[s] = cpt 
    for v in G[s]:
        if pref[v] == 0:
            print("{} -> {} arc couvrant".format(s,v))
            cpt, cpts = __dfs_dico(G,v,pref,suff,cpt, cpts)
        elif pref[s] < pref[v]:
            print("{} -> {} arc en avant".format(s,v))
        elif suff[v] == 0:
            print("{} -> {} arc retour".format(s,v))
        else:
            print("{} -> {} arc croisé".format(s,v))
    cpts += 1
    suff[s] = cpts
    return cpt, cpts    
    
    
def load(filename):
    """Build a new graph from a GRA file.

    Args:
        filename (str): File to load.

    Returns:
        Graph: New graph.

    Raises:
        FileNotFoundError: If file does not exist. ????

    """

    f = open(filename)
    lines = f.readlines()
    infos = {}
    i = 0
    while '#' in lines[i]: # lines[i][0] == '#'
        (key, val) = lines[i][1:].strip().split(": ")
        infos[key] = val
        i += 1
    
    directed = bool(int(lines[i]))
    order = int(lines[i+1])
    g = Graph(order, directed)
    g.infos = infos
    if g.infos and "labels" in g.infos:
        g.labels = g.infos["labels"].split(',')
    for line in lines[i+2:]:
        edge = line.strip().split(' ')
        (src, dst) = (int(edge[0]), int(edge[1]))
        g.addedge(src, dst)
    f.close()
    return g



def load_weightedgraph(filename, costType=float):
    """Build a new weighted graph from a WGRA file.

    Args:
        filename (str): File to load.

    Returns:
        Graph: New graph.
    """
    f = open(filename)
    lines = f.readlines()
    infos = {}
    i = 0
    while '#' in lines[i]:
        (key, val) = lines[i][1:].strip().split(": ")
        infos[key] = val
        i += 1
    directed = bool(int(lines[i]))
    order = int(lines[i+1])
    G = Graph(order, directed, costs=True)
    G.infos = infos
    if G.infos and "labels" in G.infos:
        G.labels = G.infos["labels"].split(',')    
    for line in lines[i+2:]:
        edge = line.strip().split(' ')
        (x, y, cost) = (int(edge[0]), int(edge[1]), costType(edge[2]))
        G.addedge(x, y, cost)
    f.close()

    return G
    

import queue
   
def dfs_suff(G, x, M, st):
    M[x] = True
    for y in G.adjlists[x]:
        if not M[y]:
            dfs_suff(G, y, M, st)
    st.put(x)

def topological_order(G, src):
    '''
    topological order (stack) of subgraph from vertices reachable from src
    '''
    M = [False] * G.order
    order = queue.LifoQueue() 
    dfs_suff(G, src, M, order)
    return order

    
G4 = Graph(7, directed=True)

G4.adjlists= [
    [1,2,4],
    [],
    [1,4],
    [0,4,6],
    [1],
    [1,3,6],
    [5]
    ]   
    
    
order = topological_order(G4,3)
while not order.empty():
    x = order.get()
    print(x)

Gb = Graph(8,directed=True,costs=True)
Gb.adjlists = [
        [1],
        [3],
        [1],
        [0,4],
        [0,1,2,5],
        [2,7],
        [0,3,5],
        [2]
        ]
Gb.costs = {
        (0,1):1,
        (1,3):2,
        (2,1):3,
        (3,0):1,
        (3,4):1,
        (4,0):3,
        (4,1):2,
        (4,2):2,
        (4,5):2,
        (5,2):4,
        (5,7):0,
        (6,0):3,
        (6,3):0,
        (6,5):2,
        (7,2):3
        }

def Bellman1(G, src, dst=None):
    dist = [inf] * G.order
    dist[src] = 0
    p = [None] * G.order
    p[src] = -1
    order = topological_order(G, src)
    x = order.pop()
    while not order.isempty() and (x != dst):
        print(x)
        for y in G.adjlists[x]:
            if dist[x] + G.costs[(x, y)] < dist[y]:
                dist[y] = dist[x] + G.costs[(x, y)]
                p[y] = x
        x = order.pop()
    return (dist, p)

inf = float('inf')
def min_dist(dist,M):
    s = None
    mini = inf
    for i in range(len(dist)):
        if i in M and dist[i] < mini:
            s = i
            mini = dist[i]
    return s

    

from time import perf_counter
from typing import Callable

# Cette fonction, un peu particulière, permet de mesurer
# le temps d'éxécution d'une fonction :code:`f`.


def timing(f)->float:
    """
    Measure execution time in s

    Args:
        f : a function
    Returns:
        a float that is the time in s to perform f
    """
    def wrap(*args):
        time1 = perf_counter()
        ret = f(*args)
        time2 = perf_counter()
        return (time2-time1)
    return wrap


    
    
      
    
@timing   
def dijkstra(G: dict, src:int):
    n = len(G)
    
    dist = [inf]*n
    pred = [None]*n
    
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


from fibheap import *


@timing  
def dijkstra2(G: dict, src):
    n = len(G)
    dist, pred = {}, {}
    for node in G.keys():
        dist[node] = inf
        pred[node] = None
    
    pred[src] = -1
    dist[src] = 0
    
    M = []
    
    heapq.heappush(M,(dist[src],src))

    while len(M) > 0:
        
        _, s = heapq.heappop(M)
           
        for v in G[s]:
            if dist[s] + G[s][v] < dist[v]:
                dist[v] = dist[s] + G[s][v]
                pred[v] = s
                heapq.heappush(M, (dist[v], v))
    return pred, dist
          
@timing
def dijkstra_fib(G: dict, src):
    n = len(G)
    dist, pred = {}, {}
    for node in G.keys():
        dist[node] = inf
        pred[node] = None
    
    pred[src] = -1
    dist[src] = 0
    
    M = makefheap()
    
    fheappush(M,(dist[src],src))

    while not M.is_empty():
        
        _, s = fheappop(M)
           
        for v in G[s]:
            if dist[s] + G[s][v] < dist[v]:
                dist[v] = dist[s] + G[s][v]
                pred[v] = s
                fheappush(M, (dist[v], v))
                
                
    return pred, dist

from heap import *
@timing
def dijkstra_heap(G: dict, src):
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

def show_path(pred, src, dst):
    path = []
    node = dst
    
    while pred[node] != -1:
        path = [node] + path
        node = pred[node]
    path = [src] + path
    return path
        

def build_path(pred, src, dst):
    path = []
    node = dst
    
    while pred[node] != -1:
        path = [node] + path
        node = pred[node]
    path = [src] + path
    return path
        
def graph_to_dic(G):
    Gd = {}
    for s in range(G.order):
        w = {}
        for v in G.adjlists[s]:
            w[v] = G.costs[(s,v)]
        Gd[s] = w
        
    return Gd
        
 
G14 = graph_to_dic(Gb)    
    
    
    



    


    
    
    
from random import randint, choices
   
def alea_directed_graphe(n):
    G = {}
    S = list(range(n))
    for i in range(n):
        adj = {}
        nb_v = randint(0,n-1)
        voisins = choices(S,k=nb_v)
        for v in sorted(voisins):
            adj[v] = randint(0,100)
        G[i] = adj
    return G

# tests = []
# tailles = [2**k *100 for k in range(7)]
# for n in tailles:
#     tests.append(alea_directed_graphe(n))
# print('ici')   
# for G in tests:
#     print('2->',dijkstra_heap(G, 0))
#     print('1->',dijkstra(G,0))

        
        
    
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
            
                
             
                
        
        
        
import numpy as np
import matplotlib.pyplot as plt



  
def dijkstra3_grid(G: dict, src, dst):
    n = len(G)
    dist, pred = {}, {}
    for node in G.keys():
        dist[node] = inf
        pred[node] = None
    
    pred[src] = -1
    dist[src] = 0
    
    M = []
    
    heapq.heappush(M,(dist[src],src))
    visited = [src]
    
    
    cpt = 0
    while len(M) > 0:
        cpt += 1
        _, s = heapq.heappop(M)
        visited.append(s)
        if s == dst:
            return cpt, visited, show_path(pred, src, dst)
            
        for v in G[s]:
            if dist[s] + G[s][v] < dist[v]:
                dist[v] = dist[s] + G[s][v]
                pred[v] = s
                heapq.heappush(M,(dist[v],v))
    return cpt, visited, show_path(pred,src,dst)



@timing 
def dijkstra4_grid(G: dict, src, dst):
    n = len(G)
    dist, pred = {}, {}
    for node in G.keys():
        dist[node] = inf
        pred[node] = None
    
    pred[src] = -1
    dist[src] = 0
    
    M = Heap([])
    M.push((0,src))
    
    
    visited = [src]
    
    
    cpt = 0
    while len(M) > 0:
        cpt += 1
        _, s = M.pop()
        visited.append(s)
        if s == dst:
            print(cpt)
            print(len(visited))
            
            return cpt, visited, show_path(pred, src, dst)
            
        for v in G[s]:
            d = dist[v]
            if dist[s] + G[s][v] < dist[v]:
                dist[v] = dist[s] + G[s][v]
                pred[v] = s
                M.update((d,v),(dist[v],v))
                visited.append(v)
                
    return cpt, visited, show_path(pred,src,dst)
    
    

def h(node, dst):
    return abs(node[1]-dst[1])+abs(node[0]-dst[0])

def h1(node, dst):
    return (node[1]-dst[1])**2 + (node[0]-dst[0])**2

def h2(node , dst):
    return max(abs(node[1]-dst[1]),abs(node[0]-dst[0]))

def h3(node , dst):
    return abs(node[1]-dst[1])*abs(node[0]-dst[0])

def h4(node , dst):
    return 1/(1+(abs(node[1])))

def h5(node, dst):
    return 1/(1+(abs(node[1])+abs(node[0])))

def h0(node, dst):
    return math.sqrt( (node[1]-dst[1])**2 + (node[0]-dst[0])**2) 

def h6(node , dst):
    return 1/(1+(abs(node[0])))

def A_grid_1(G: dict, src, dst, h, w):
    n = len(G)
    dist, pred = {}, {}
    for node in G.keys():
        dist[node] = inf
        pred[node] = None
    
    
    
    pred[src] = -1
    dist[src] = 0
    
    M = Heap([])
    
    M.push((dist[src]+ w*h(src,dst),src))
    visited = [src]
    
   
    cpt = 0
    while len(M) > 0:
        cpt += 1
        _, s = M.pop()
        visited.append(s)
        if s == dst:
            return cpt, visited, dist, show_path(pred, src, dst)
            
        for v in G[s]:
            if v not in visited:
                H = w * h(v, dst)
                d = dist[v]
                p = d + H
                if dist[s] + G[s][v] < dist[v]:
                    dist[v] = dist[s] + G[s][v]
                    pred[v] = s
                    priority = dist[v] + H
                    M.update((p, v), (priority, v))
                    #visited.append(v)
    return cpt, visited, dist, show_path(pred,src,dst)




def affiche(n: int, m:int, path = False):
    fig = plt.figure(dpi=300,figsize=(10, 10)) 
    
    G = grid(n, m)
    plt.axis("equal")
    for x in range(15,20):
        for y in range(5,20):
            G[(x,y)]={}
            plt.plot(x,y,marker="X", color='blue')
    
        
    for x in range(5,20):
        for y in range(15,20):
            G[(x,y)]={}
            plt.plot(x,y,marker="X", color='blue')
        
    cpt, visited, path = A_grid_1(G, (0, 0), (n-1, m-1), h, 1)
    
    print('Longueur du chemin : ',len(path))
    print('Itérations :', cpt)
    print('Sommets traités :',len(visited))
    
    for x in range(n+1):
        plt.plot([x-0.5,x-0.5],[-0.5,m-.5], color='#318ce7')
    for y in range(m+1):
        plt.plot([-0.5,n-.5],[y-0.5,y-0.5], color='#318ce7')
    
    # for x,y in visited:
    #     plt.plot(x,y,marker="+", color="orange")
    # for x,y in path:
    #     plt.plot(x,y,marker="o", color="magenta")
    plt.show()        
        
        
        
def quadrillage(n,m):
    for x in range(n+1):
        plt.plot([x-0.5,x-0.5],[-0.5,m-.5], color='#318ce7')
    for y in range(m+1):
        plt.plot([-0.5,n-.5],[y-0.5,y-0.5], color='#318ce7')
        
def affiche_graph(G):
    for s in G.keys():
        x, y = s
        if G[s] == {}:
            plt.plot(x,y,marker="X", color='blue')
            
def plateau(G, n, m):
    fig = plt.figure(dpi=300,figsize=(10, 10)) 
    plt.axis("equal")
    quadrillage(n, m)
    affiche_graph(G)
    #plt.show()         
    
#Obstacle en L
G1 = grid(25, 25)
for x in range(15,20):
    for y in range(5,20):
        G1[(x,y)]={}
for x in range(5,20):
    for y in range(15,20):
        G1[(x,y)]={}

#plateau(G1, 25, 25)
        
 
G2 = grid(25, 25)
for x in range(3,25):
    for y in range(19,22):
        G2[(x,y)]={}
#plateau(G2, 25, 25)
        

G3 = grid(25, 25)
for x in range(3,25):
    for y in range(19,22):
        G3[(x,y)]={}
for x in range(0,22):
    for y in range(5,8):
        G3[(x,y)]={}
#plateau(G3, 25, 25)



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
#plateau(G1, 25, 25)
# plateau(G1, 25, 25)      
# cpt, visited, path = A_grid_1(G1, (0, 0), (24, 24), h1, 1) 
# print(len(visited))
# print(len(path))
# print(cpt)      
# for x,y in visited:
#     plt.plot(x,y,marker="+", color="orange")
# for x,y in path:
#     plt.plot(x,y,marker="o", color="magenta")    
    
# plt.show()    


# print("Pour G1")

# H = [h1, h2, h3, h4, h5]
# i = 0
# for w in [0.5,1,1000]:
#     print('w = ', w)
#     for h in H:

#         cpt, visited, path = A_grid_1(G4, (0, 0), (24, 24), h, w) 
#         print('Pour {}'.format(h.__name__))
#         print('    Itérations : ' , cpt)
#         print('    Longueur : ', len(path))
#         print('   Nbre sommets : ',len(visited))
        


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


def lenght_path(G, pred, dist, src, dst):
    pass


i = 0
res = [['Fonctions','Poids w','Longueur','Sommets traités','Itérations']]

for f in [h0,h,h1,h2,h3,h4,h5, h6]:
    for w in [1,10**4,10**5,10**6]:      
        cpt, visited, dist, path = A_grid_1(G5, (0, 0), (49, 49), f, w)    
        
        plateau(G5,50,50)
        for x,y in visited:
            plt.plot(x,y,marker="+", color="orange")
        for x,y in path:
            plt.plot(x,y,marker="o", color="magenta") 
        i += 1
        print(i)
        plt.title('Pour {} et w = {}. L = {}, Nb sommets = {} en {} itérations'.format(f.__name__,w,dist[(49,49)],len(visited),cpt))  
        res.append([f.__name__,str(w),"{:.2f}".format(dist[(25,45)]),str(len(visited)),str(cpt)])
        plt.savefig("3_Pour {} et w = {} et dst = (49,49)".format(f.__name__,w))
        
import csv
with open('resultats.csv', 'w') as fichier: 
         ecrire = csv.writer(fichier)
         for ligne in res:
             ecrire.writerow(ligne)        
        
# cpt, visited, path = A_grid_1(G5, (0, 0), (49, 49), f, 1)    

# plateau(G5,50,50)
# for x,y in visited:
#     plt.plot(x,y,marker="+", color="orange")
# for x,y in path:
#     plt.plot(x,y,marker="o", color="magenta") 
# i += 1
# print(i)
# plt.title('Pour {} et w = {}. L = {}, Nb sommets = {} en {} itérations'.format(f.__name__,w,len(path),len(visited),cpt))  
# plt.show() 
        
    
