******************************************************
TP4 : Récursivité
******************************************************


.. note:: **Les objectifs du TP :**

* Écrire des algorithmes récursifs  
* Mettre en oeuvre la mémoïsation 
       

.. rst-class:: html-toggle

Ceux qu'il faut avoir programmés une fois
======================================


**Question 1 :** Écrire une fonction :code:`exp1(a,n)` qui prend comme arguments un nombre flottant :code:`a` et un entier :code:`n` et qui retourne :math:`a^n`, en utilisant l'opérateur puissance de Python. Écrire une deuxième fonction récursive :code:`exp2(a,n)`, qui retourne encore :math:`a^n`, et qui exploite la relation :math:`a^n = a\times a^{n-1}`.

    Écrire une troisième fonction :code:`exp3(a,n)`, qui retourne toujours :math:`a^n`, en exploitant la relation :

    .. math:: a^n = a^{\lfloor n/2\rfloor}\times a^{n-\lfloor n/2\rfloor}  
 
    Écrire une quatrième fonction :code:`exp4(a,n)`,qui retourne toujours :math:`a^n` , en exploitant la même relation, mais en exploitant en plus que :

    .. math:: n-\lfloor n/2\rfloor = \left\{\begin{array}{lr} \lfloor n/2\rfloor&\text{ si $n$ est pair.}\\ \lfloor n/2\rfloor + 1&\text{ sinon.}\end{array}\right.

    Modifier vos codes pour compter le nombre d'appels récursifs des fonctions. 

    Utiliser la fonction :code:`perf_counter()` du module :code:`time` pour mesurer le temps d'exécution de ces quatre fonctions par calculer :math:`2^{900}`. Qu'observez-vous ?

    Comparer le nombre d'appels récursifs des trois fonctions :code:`exp2(a,n)`, :code:`exp3(a,n)` et :code:`exp4(a,n)`, pour :math:`a=2` et :math:`n=100,\,200,\,400,\,800`.

    Évaluez le nombre de multiplication effectuées par :code:`exp3(a,n)` et :code:`exp4(a,n)`.



**Question 2 :** Écrire une fonction récursive :code:`sum_digits(n)` qui prend comme argument un entier :math:`n` et qui retourne la somme de ses chiffres.



**Question 3 :** Soient :math:`a` et :math:`b` deux flottants, on définit les suites :math:`(u_n)`et :math:`(v_n)` par :math:`u_0= a` et :math:`v_0=b` et pour :math:`n\geq 0` :

    .. math:: u_{n+1} = \sqrt{u_n v_n} \text{ et }v_{n+1}=\dfrac{1}{2}\left(u_n+v_n\right).

    Écrire deux fonctions récursives :code:`seq_u(n)` et :code:`seq_v(n)` qui retourne respectivement les valeurs de :math:`u_n` et :math:`v_n`.    


**Question 4 :** Pour dénombrer :math:`\mathbb{N}\times\mathbb{N}`, on peut utiliser la fonction de Cantor pour numéroter les éléments de :math:`\mathbb{N}\times\mathbb{N}` de la manière illustrée sur la figure suivante :

    .. image:: Pairing_Function.png
       :height: 440 px
       :width: 440 px
       :scale: 60 %
       :alt: pairing_function
       :align: center

   

    Écrire une fonction récursive :code:`pairing_function(x,y)` qui prend comme argument un élément :math:`(x,y)\in \mathbb{N}\times\mathbb{N}` et qui retourne son numéro.

    Écrire, de manière récursive, la fonction réciproque :code:`inv_pairing_function(n)` qui prend comme argument un entier :math:`n` et qui retourne le couple :math:`(x,y)` dont il est le numéro.   


**Question 5 :** Écrire une fonction récursive :code:`binary_digits(n)` qui retourne la liste des chiffres de l'écriture binaire de l'entier :code:`n` passé en argument.

**Question 6 :** Dans cet exercice on représente les ensembles d'entiers par des listes d'entiers deux à deux distincts. Écrire une fonction récursive :code:`list_of_subset(E)` qui prend comme argument un ensemble et qui retourne l'ensemble de ses sous-ensembles. On pourra remarquer que si :math:`E` est un ensemble et si :math:`a\in E`, alors les sous-ensembles de :math:`E` sont ceux de :math:`E\setminus\{a\}`, et ceux de :math:`E\setminus\{a\}` auxquels on ajoute :math:`a`.



.. _toggle-test-link:

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

                def triangle([[x1,y1],[x2,y2],[x3,y3]]):
                    liste = [[x1,y1],[x2,y2],[x3,y3]]
                    ax.add_patch(Polygon(liste, closed=True,fill=True, color='red'))


**Question 1 :** Écrire une fonction récursive :code:`bubble1(n)` qui prend comme argument un entier :math:`n`, et qui permet d'obtenir la figure suivante pour :math:`n=5` :

	.. image:: Bubble_1.png
       	   :height: 480 px
           :width: 640 px
           :scale: 60 %
           :alt: bubble1(5)
           :align: center


**Question 2 :** Écrire une fonction récursive :code:`bubble2(n)` qui prend comme argument un entier :math:`n`, et qui permet d'obtenir la figure suivante pour :math:`n=5` :

	.. image:: Bubble_2.png
       	   :height: 480 px
           :width: 640 px
           :scale: 60 %
           :alt: bubble1(5)
           :align: center


 

**Question 3 :** Écrire une fonction récursive :code:`sierpinski(n)` qui prend comme argument un entier :math:`n`, et qui permet d'obtenir les figures suivantes pour :math:`n=1,2,3` et :math:`4` :
 
         .. image:: sierpinski_1.png
       	   :height: 480 px
           :width: 640 px
           :scale: 60 %
           :alt: Sierpinski
           :align: left

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
           :align: left

	 .. image:: sierpinski_4.png
       	   :height: 480 px
           :width: 640 px
           :scale: 60 %
           :alt: Sierpinski
           :align: center


     Tous les triangles sont équilatéraux.

.. _toggle-test-link:


Mémoïsation
================================================================


.. note:: Nous pouvons diminuer les coûts temporels et spatiaux d'une fonction aux appels récursifs multiples en enregistrant les calculs déjà effectués dans une mémoire cache. Nous allons appliquer ce principe au calcul récursif du :math:`n`-ième terme de la suite de Fibonacci.



   
**Question 1 :** Écrire une fonction itérative :code:`fibo_it(n)` qui prend comme argument un entier :math:`n` et qui retourne le :math:`n`-ième terme de la suite de Fibonacci.

**Question 2 :** Écrire une fonction récursive :code:`fibo_rec(n)` qui prend comme argument un entier :math:`n` et qui retourne le :math:`n`-ième terme de la suite de Fibonacci.

**Question 3 :** Écrire une fonction récursive :code:`fibo_m(n)` qui tire profit de la mémoïsation. Pour cela vous allez utiliser une liste comme :code:`cache` pour stocker les résultats des calculs intermédiaires. Au départ vous initialiserez le cache avec les deux premiers termes de la suite : :code:`cache = [0,1]`. Ensuite avant de faire un appel récursif vous vérifierez si le terme que vous souhaitez calculer n'est pas déjà en cache.

**Question 4 :** Écrire une fonction récursive avec mémoïsation :code:`fact_m(n)` qui prend comme argument un entier :math:`n` et qui retourne :math:`n!`.
