******************************************************
TP4 : Récursivité
******************************************************


.. note:: **Les objectifs du TP :**

    * Écrire des algorithmes récursifs  
    * Mettre en oeuvre la mémoïsation 
       

.. note:: Si l'on souhaite écrire une fonction qui calcule :math:`n!` , au lieu de calculer tous les produits on peut écrire, pour :math:`n>1`, que :math:`n!=n\times (n-1)!` et :math:`1!=1`. Autrement dit, si :math:`f` est cette fonction alors elle vérifie :
        :math:`f(n)=n\times f(n-1)` si :math:`n>1` et :math:`f(1)=1` .

	On pourrait donc l'écrire :

	.. code-block :: python

            def factorielle(n):
                if n == 1: 
                    return 1
                else:
                    return n*factorielle(n-1)

    Calculer de cette manière s'appelle la *récursivité*, la fonction s'appelle elle-même.

    Une fonction récursive commence toujours par traiter ce qu'on appelle les *conditions d'ârret*, dans notre exemple il n'y en a qu'une, mais il peut y en avoir plusieurs.

    En utilisant le décorateur suivant, vous pourrez observer les appels successifs d'une fonction récursive :
    
 	.. code-block :: python

            def trace(func):
                def wrapper(*args):
                    print(' ' * wrapper.space, end='')
                    print('{} <− {}'.format(func.__name__, str(args))) 
                    wrapper.space += 1
                    val = func(*args)
                    wrapper.space -= 1
                    print(' ' * wrapper.space, end='')
                    print('{} −> {}'.format(func.__name__, str(val))) 
                    return val
                wrapper.space = 0 
                return wrapper   

    Prenons un exemple. Considérons la fonction suivante :
        
 	.. code-block :: python
            
            @trace
            def s(a:int, b:int):
                if a == 0:
                    return b
                else:
                    return s(a-1,b+1)

    Que calcule cette fonction ?
    Avec le décorateur on obtient :
    
    .. code-block :: python
    
        >>> s(4,3)
        s <− (4, 3)
         s <− (3, 4)
          s <− (2, 5)
           s <− (1, 6)
            s <− (0, 7)
            s −> 7
           s −> 7
          s −> 7
         s −> 7
        s −> 7
    

    Vous pouvez voir que la fonction a été appelée cinq fois, avant de retourner cinq fois... On dit qu'on a *empilé* les appels. Le nombres d'appels peut-être très important, ce qui est un problème. C'est ce qui nous intéressera à la fin du TP.
    
    

.. rst-class:: html-toggle

Ceux qu'il faut avoir programmés une fois
============================================


**Exercice :**

 * Écrire une fonction :code:`exp1(a,n)` qui prend comme arguments un nombre flottant :code:`a` et un entier :code:`n` et qui retourne   :math:`a^n`, en utilisant l'opérateur puissance de Python. 
 
 * Écrire une deuxième fonction récursive :code:`exp2(a,n)`, qui retourne encore       :math:`a^n`, et qui exploite la relation :math:`a^n = a\times a^{n-1}`.

 * Écrire une troisième fonction :code:`exp3(a,n)`, qui retourne toujours :math:`a^n`, en exploitant la relation :

    .. math:: a^n = a^{\lfloor n/2\rfloor}\times a^{n-\lfloor n/2\rfloor}  
 
 * Écrire une quatrième fonction :code:`exp4(a,n)`,qui retourne toujours :math:`a^n` , en exploitant la même relation, mais en exploitant en plus que :

    .. math:: n-\lfloor n/2\rfloor = \left\{\begin{array}{lr} \lfloor n/2\rfloor&\text{ si $n$ est pair.}\\ \lfloor n/2\rfloor + 1&\text{ sinon.}\end{array}\right.

 * Modifier vos codes pour compter le nombre d'appels récursifs des fonctions. 

 * Utiliser la fonction :code:`perf_counter()` du module :code:`time` pour mesurer le temps d'exécution de ces quatre fonctions par calculer :math:`2^{900}`. Qu'observez-vous ?

 *  Comparer le nombre d'appels récursifs des trois fonctions :code:`exp2(a,n)`, :code:`exp3(a,n)` et :code:`exp4(a,n)`, pour :math:`a=2` et :math:`n=100,\,200,\,400,\,800`.

 * Évaluez le nombre de multiplication effectuées par :code:`exp3(a,n)` et :code:`exp4(a,n)`.

.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python

            def exp1(a,n):
                  return a**n


            def exp2(a,n):
                  if n == 0:
                        rep = 1
                  else:
                        rep = a*exp2(a,n-1)
                  return rep

            def exp3(a,n):
                  if n == 0:
                        rep = 1
                  elif n == 1:
                        rep = a
                  else:
                        p = n // 2
                        rep = exp3(a,p)*exp3(a,n-p)
                  return rep


            def exp4(a,n):
                  if n == 0:
                        rep = 1
                  elif n == 1:
                        rep = a
                  elif n % 2 == 0:
                        rep = exp4(a*a, n//2)
                  else:
                        rep = a*exp4(a*a, n//2)
                  return rep

    

**Exercice :** Écrire une fonction récursive :code:`sum_digits(n)` qui prend comme argument un entier :math:`n` et qui retourne la somme de ses chiffres.


.. admonition:: Solution
   :class: dropdown; tip
   
        .. code-block :: python
        
                def sum_digits(n):
                    if n < 10:
                        rep = n
                    else:
                        rep = (n%10)+ sum_digits(n//10)
                    return rep
                    

**Exercice :** Soient :math:`a` et :math:`b` deux flottants, on définit les suites :math:`(u_n)`et :math:`(v_n)` par :math:`u_0= a` et :math:`v_0=b` et pour :math:`n\geq 0` :

    .. math:: u_{n+1} = \sqrt{u_n v_n} \text{ et }v_{n+1}=\dfrac{1}{2}\left(u_n+v_n\right).

    Écrire deux fonctions récursives :code:`seq_u(n,a,b)` et :code:`seq_v(n,a,b)` qui retourne respectivement les valeurs de :math:`u_n` et :math:`v_n`.    


**Exercice :** Pour dénombrer :math:`\mathbb{N}\times\mathbb{N}`, on peut utiliser la fonction de Cantor pour numéroter les éléments de :math:`\mathbb{N}\times\mathbb{N}` de la manière illustrée sur la figure suivante :

    .. image:: Pairing_Function.png
       :height: 440 px
       :width: 440 px
       :scale: 60 %
       :alt: pairing_function
       :align: center

   

    Écrire une fonction récursive :code:`pairing_function(x,y)` qui prend comme argument un élément :math:`(x,y)\in \mathbb{N}\times\mathbb{N}` et qui retourne son numéro.


.. admonition:: Solution
   :class: dropdown; tip
   
        .. code-block :: python
        
            def pairing_function(x,y):
                if x == 0 and y == 0:
                    return 0
                if y > 0:
                    return 1 + pairing_function(x+1, y-1)
                return 1 + pairing_function(0, x-1)
                  




Écrire, de manière récursive, la fonction réciproque :code:`inv_pairing_function(n)` qui prend comme argument un entier :math:`n` et qui retourne le couple :math:`(x,y)` dont il est le numéro.   


.. admonition:: Solution
   :class: dropdown; tip
   
        .. code-block :: python

            def inv_pairing_function(n):
                if n == 0:
                    return (0,0)
                (x,y) = inv_pairing_function(n-1)
                if x > 0:
                    return (x-1,y+1)
                return (y+1,0)
                


**Exercice *Difficile* :** Dans cet exercice on représente les ensembles d'entiers par des listes d'entiers deux à deux distincts. Écrire une fonction récursive :code:`list_of_subset(E)` qui prend comme argument un ensemble et qui retourne l'ensemble de ses sous-ensembles. On pourra remarquer que si :math:`E` est un ensemble et si :math:`a\in E`, alors les sous-ensembles de :math:`E` sont ceux de :math:`E\setminus\{a\}`, et ceux de :math:`E\setminus\{a\}` auxquels on ajoute :math:`a`.

.. admonition:: Solution
   :class: dropdown; tip
   
        .. code-block :: python

            def subset(E):
                if E == []:
                    rep = [[]]
                else:
                    E1 = subset(E[1:])
                    E2 = [[E[0]] + s for s in E1]
                    rep = E1 + E2
                return rep




De beaux dessins
================================================================

.. note::  Voici le code d'une fonction qui permet de tracer un cercle de centre :math:`(x,y)` et de rayon :math:`r>0` :

   	.. code-block:: python

      		import matplotlib.pyplot as plt
      		fig, ax = plt.subplots()
      		ax.set_aspect(1)
      		plt.axis("equal")
  
      		def circle(x,y,r):
          	    ax.add_artist(plt.Circle((x,y),r,color ='r', fill = False))         
    
        Et voici celui d'une fonction qui trace un triangle plein dont les sommets sont :math:`(x_1,y_1)`, :math:`(x_2,y_2)` et :math:`(x_3,y_3)` :

        .. code-block:: python

                from matplotlib.patches import Polygon

                def triangle(x1,y1,x2,y2,x3,y3):
                    liste = [[x1,y1],[x2,y2],[x3,y3]]
                    ax.add_patch(Polygon(liste, closed=True,fill=True, color='red'))


**Exercice :** Écrire une fonction récursive :code:`bubble1(n)` qui prend comme argument un entier :math:`n`, et qui permet d'obtenir la figure suivante pour :math:`n=5` :

	.. image:: Bubble_1.png
       	   :height: 480 px
           :width: 640 px
           :scale: 60 %
           :alt: bubble1(5)
           :align: center
             
    
**Exercice :** Écrire une fonction récursive :code:`bubble2(n)` qui prend comme argument un entier :math:`n`, et qui permet d'obtenir la figure suivante pour :math:`n=5` :

	.. image:: Bubble_2.png
       	   :height: 480 px
           :width: 640 px
           :scale: 60 %
           :alt: bubble1(5)
           :align: center


 

**Exercice :** Écrire une fonction récursive :code:`sierpinski(n)` qui prend comme argument un entier :math:`n`, et qui permet d'obtenir les figures suivantes pour :math:`n=1,2,3` et :math:`4` :
 
         .. image:: sierpinski_1.png
       	   :height: 480 px
           :width: 640 px
           :scale: 60 %
           :alt: Sierpinski
           :align: center

         .. image:: sierpinski_2.png
       	   :height: 480 px
           :width: 640 px
           :scale: 60 %
           :alt: Sierpinski
           :align: center

         .. image:: sierpinski_3.png
       	   :height: 480 px
           :width: 640 px
           :scale: 60 %
           :alt: Sierpinski
           :align: center

	 .. image:: sierpinski_4.png
       	   :height: 480 px
           :width: 640 px
           :scale: 60 %
           :alt: Sierpinski
           :align: center


     Tous les triangles sont équilatéraux.



Optimisations
*************

Mémoïsation
================================================================


.. note:: Nous pouvons diminuer les coûts temporels et spatiaux d'une fonction aux appels récursifs multiples en enregistrant les calculs déjà effectués dans une mémoire cache. Nous allons appliquer ce principe au calcul récursif du :math:`n`-ième terme de la suite de Fibonacci.



   
**Exercice :** Écrire une fonction itérative :code:`fibo_it(n)` qui prend comme argument un entier :math:`n` et qui retourne le :math:`n`-ième terme de la suite de Fibonacci.

**Exercice :** Écrire une fonction récursive :code:`fibo_rec(n)` qui prend comme argument un entier :math:`n` et qui retourne le :math:`n`-ième terme de la suite de Fibonacci.

**Exercice :** Écrire une fonction récursive :code:`fibo_m(n)` qui tire profit de la mémoïsation. Pour cela vous allez utiliser une liste comme :code:`cache` pour stocker les résultats des calculs intermédiaires. Au départ vous initialiserez le cache avec les deux premiers termes de la suite : :code:`cache = {0 : 0, 1 : 1]`. Ensuite avant de faire un appel récursif vous vérifierez si le terme que vous souhaitez calculer n'est pas déjà en cache.

.. admonition:: Solution
   :class: dropdown; tip
   
        .. code-block :: python
        
                cache = {0:0, 1:1}
                def fibo_m(n):
                    if n in cache:
                        res = cache[n]
                    else:
                        cache[n] = fibo_m(n-1)+cache[n-2]
                        res =  cache[n]
                    return res

**Question 4 :** Écrire une fonction récursive avec mémoïsation :code:`fact_m(n)` qui prend comme argument un entier :math:`n` et qui retourne :math:`n!`.


Récursivité terminale et Tail Call Elimination
==============================================

.. note:: La *Tail Call Elimination (TCE)*, également connue sous le nom d'optimisation de la récursivité terminale, est une technique d'optimisation couramment utilisée pour les langages de programmation fonctionnels tels que Scheme, mais elle peut également être appliquée à Python.

La TCE consiste à remplacer une récursivité terminale par une boucle, de sorte que la pile d'appels ne soit plus nécessaire pour exécuter la fonction, ce qui peut améliorer les performances et éviter un éventuel débordement de la pile d'appels.

Pour le faire il suffit de remarquer qu'un appel récursif terminal revient à effectuer un **GOTO** avec une mise à jour des différents paramètres. Prenons l'exemple de l'algorithme d'Euclide du calcul du pgcd : (on suppose :math:`a>b`):

    .. code-block:: python
    
        def pgcd_rec(a : int, b : int)->int:
            if b == 0:
                pgcd = a
            else:
                pgcd = pgcd_rec(b, a % b)
            return pgcd

L'appel récursif est bien terminal. Si l'on se sert de la condition d'arrêt comme condition d'une boucle :code:`while` et que l'on mets les différentes variables à jour on obtient l'algoritme itératif suivant :


    .. code-block:: python
    
        def pgcd(a : int,b : int)->int:
            while b > 0:
                a, b = b, a % b
            return b


**Exercice :** Effectuer une TCE sur la fonction suivante :

    .. code-block:: python 
    
        def s(a : int, b : int)->int
            if a == 0:
                return b
            else:
                return s(a-1,b+1)


.. admonition:: Solution
   :class: dropdown; tip

        def s(a : int, b : int)->int
            while a > 0:
                a -= 1
                b += 1
            return b

**Exercice :** Effectuer une TCE sur la fonction suivante :

    .. code-block:: python 
    
        def palindrome(mot : str)->bool:
            if len(mot) < 2:
                return True
            elif mot[0] != mot[-1]:
                return False
            else:
                return palindrome(mot[1:-1])




.. admonition:: Solution
   :class: dropdown; tip

    .. code-block :: python 
    
        def palindrome(mot : str)->bool:
            rep = True
            while len(mot) > 1 and rep:
                print(mot)
                if mot[0] != mot[-1]:
                    rep = False
                mot = mot[1:-1]
            return rep

.. note:: La TCE n'est possible que si la récursion est terminale. Dans certains cas il est possible de transformer une récursion quelconque en une récursion terminale. Pour cela on a recourt à des **accumulateurs** pour stocker les résultats intermédiaires et les passer comme argument lors de chaque appel récursif. Par exemple la fonction récursive suivante n'est pas terminale :


    .. code-block :: python
    
        def somme(n : int)->int:
            if n == 0:
                return 0
            else:
                return n + somme(n-1)

    Pour transformer cette fonction en une fonction récursive terminale, on peut utiliser un accumulateur pour stocker la somme partielle et le passer comme argument lors de chaque appel récursif :
    


    .. code-block :: python
    
        def somme(n : int, acc = 0)->int:
            if n == 0:
                return acc
            else:
                return somme(n-1, acc+n)


    Dans cette fonction, :code:`acc` est l'accumulateur qui stocke la somme partielle. L'appel initial de la fonction utilise une valeur par défaut de 0 pour l'accumulateur. Lors de chaque appel récursif, la fonction passe :code:`acc+n` comme nouvel accumulateur.
    

**Exercice :** Utiliser un accumulateur pour transformer la fonction récursive suivante :

    .. code-block:: python
    
        def puissance(base : int, exposant : int):
            if exposant == 0:
                return 1
            else:
                return base * puissance(base, exposant - 1)

.. admonition:: Solution
   :class: dropdown; tip

    .. code-block:: python
    
        def puissance(base, exposant, accumulateur=1):
            if exposant == 0:
                return accumulateur
            else:
                return puissance(base, exposant - 1, accumulateur * base)
                
**Exercice :** Utiliser un accumulateur pour transformer la fonction récursive suivante :

    .. code-block:: python
    
        def somme_carres(n : int)->int:
            if n == 0:
                return 0
            else:
                return n**2 + somme_carres(n-1)

.. admonition:: Solution
   :class: dropdown; tip

    .. code-block:: python
    
        def somme_carres(n : int, acc=0)->int:
            if n == 0:
                return acc
            else:
                return somme_carres(n-1, acc+n*n)
                
                
                
**Exercice :** Utiliser deux accumulateurs pour transformer la fonction récursive suivante :

    .. code-block :: python
    
        def fibonacci(n : int)->int:
            if n in [0,1]:
                return n
            else:
                return fibonacci(n-1) + fibonacci(n-2)
                

.. admonition:: Solution
   :class: dropdown; tip

    .. code-block:: python
    
        def fibonacci(n, next=0, acc=1):
            if n == 0:
                return a
            elif n == 1:
                return b
            else:
                return fibonacci(n-1, next , acc + next)

**Exercice :** Utiliser un accumulateur (attention ce n'est pas un nombre) pour transformer la fonction récursive suivante :

   .. code-block :: python

        def concat_strings(lst : list[str])->str:
            if len(lst)==0:
                return ''
            else:
                return lst[0] + concat_strings(lst[1:])
                

.. admonition:: Solution
   :class: dropdown; tip

    .. code-block:: python

        def concat_strings(lst, acc=""):
            if not lst:
                return acc
            else:
                return concat_strings(lst[1:], acc + lst[0])
                
                
*Exercice :** Ecrire des versions itératives de toutes les dernières fonctions.

