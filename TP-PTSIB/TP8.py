
import queue

def bfs_path(G: dict, src: int, dst: int)->list:
    n = len(G)
    peres = [None] * n
    path = []
    if __bfs_path(G,src, dst, peres):
        while dst != -1:
            path = [dst] + path
            dst = peres[dst]
    return path

def __bfs_path(G: dict, src: int, dst: int, peres: list)->bool:
    f = queue.Queue()
    f.put(src)
    peres[src] = -1
    while not f.empty():
        s = f.get()
        for v in G[s]:
            if peres[v] == None:
                peres[v] = s
                if v == dst:
                    return True
                f.put(v)
    return False

def dfs_path(G: dict, src:int, dst: int)-> list:
    n = len(G)
    peres = [None] * n
    path = []
    if __dfs_path(G, src, dst, peres):
        while dst != -1:
            path = [dst] + path
            dst = peres[dst]
    return path
      
def __dfs_path(G: dict, src: int, dst: int, peres: list)->bool:
    peres[src] = -1
    p = queue.LifoQueue()
    p.put(src)
    while not p.empty():
        s = p.get()
        for v in G[s]:
            if peres[v] == None:
                peres[v] = s
                if v == dst:
                    return True
                p.put(v)
    return False


def same_component(G: dict, x: int, y: int)->bool:
    n = len(G)
    M = [False] * n
    if __same_component(G, x, y, M):
        return True
    return False

def __same_component(G: dict, x: int, y: int, M: list)->bool:
    M[x] = True
    for v in G[x]:
        if not M[v]:
            if v == y or __same_component(G, v, y, M):
                return True
    return False

def connexity_number(G: dict)->int:
    n = len(G)
    M = [False] * n
    cp = 0
    for s in range(n):
        if not M[s]:
            __connexity_number(G, s, M)
            cp += 1
    return cp

def __connexity_number(G, s, M):
    M[s] = True
    for v in G[s]:
        if not M[v]:
            M[v] = True
            __connexity_number(G, v, M)
    
def component(G):
    n = len(G)
    M = [False] * n
    cc = []
    for s in range(n):
        if not M[s]:
            new_cc = __component(G, s, M, cc = [s])
            cc.append(new_cc)
            
    return cc

def __component(G, s, M, cc):
    M[s] = True   
    for v in G[s]:
        if not M[v]:
            M[v] = True
            cc.append(v)           
            __component(G, v, M, cc)
    return cc


def dfs_forest(G):
    n = len(G)
    pref = [0] * n
    suff = [0] * n
    pere = [None] * n
    cpt = 0
    cpts = 0
    for s in range(n):
        if pref[s] == 0:
            pere[s] = -1
            cpt, cpts = __dfs_forest(G,s,pref,suff, pere,cpt, cpts)
        
    return pere, pref, suff
            
def __dfs_forest(G,s,pref,suff,pere,cpt,cpts):
    cpt += 1
    
    pref[s] = cpt 
    for v in G[s]:
        if pref[v] == 0:
            pere[v] = s
            print("{} -> {} arc couvrant".format(s,v))
            cpt, cpts = __dfs_forest(G,v,pref,suff,pere,cpt, cpts)
        elif pref[s] < pref[v]:
            print("{} -> {} arc en avant".format(s,v))
        elif suff[v] == 0:
            print("{} -> {} arc retour".format(s,v))
        else:
            print("{} -> {} arc croisé".format(s,v))
    cpts += 1
    suff[s] = cpts
    return cpt, cpts    
    

def essai(g: dict)->tuple[list[int],list[int]]

def __bfs(G, s, p, edges):
    q = queue.Queue()
    q.put(s)
    p[s] = -1   
    while not q.empty():
        s = q.get()
        print(s, end = ' ')
        for adj in G[s]:
            if p[adj] == None:      
                p[adj] = s
                q.put(adj)
                edges.append((s, adj, "tree"))

def bfs_for_dot(G):
    """
    full BFS of G (Graph) for spanning forest
    src: optionnal parameter = first vertex
    return (p, roots, edges):
    - p: the parent vector (-1 for roots)    
    - roots: the root vector    
    - edges: list of tree edges ((x, y, "tree") for each edge x -> y) 
    """
    n = len(G)
    edges, roots = [], []
    p = [None] * n   
    
    for s in range(n):
        if p[s] == None:       
            roots.append(s)
            __bfs(G, s, p, edges)

    return(p, roots, edges)




   

G1 = {
    0:[1, 4,5 ],
    1:[2, 3,4 ],
    2:[4],
    3:[6, 9],
    4:[],
    5:[7, 10],
    6:[9],
    7:[0, 8, 10, 12],
    8:[12],
    9:[],
    10:[8],
    11:[9],
    12:[0, 3]
    }


G2 = {
    0:[1],
    1:[0,2,4],
    2:[1,4],
    3:[5,7],
    4:[1,2],
    5:[3,7,8],
    6:[9],
    7:[3,5],
    8:[5,7],
    9:[6]}

G3 = {
    0 : [2],
    1 : [2, 5],
    2 : [3, 8],
    3 : [0, 1, 4],
    4 : [3, 10],
    5 : [6],
    6 : [5, 7],
    7 : [9],
    8 : [7, 10],
    9 : [8, 10],
    10 : []
    }

G4 = {
    0 : [1, 4, 7],
    1 : [2, 7],
    2 : [5],
    3 : [2, 4],
    4 : [5],
    5 : [6],
    6 : [],
    7 : [6],
    8 : [7],
    }
