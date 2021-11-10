

****************************************************
TP2 : Des modules, des tests et un peu de complexité
****************************************************

.. note :: **Les objectifs du TP :**

    * Importer correctement des modules.
    * Ecrire des tests pour vérifier la correction de ses fonctions.
    * Avoir des notions de la complexité de ses algorithmes.


.. rst-class:: html-toggle

Utiliser des modules
========================

Généralités
-------------

.. note:: Lorsque vous fermez et réouvrez un IDLE tout ce que vous avez déclaré lors de votre précédente session est perdu. C'est pourquoi pour rédiger des programmes plus longs, vous utilisez des *script*, c'est-à-dire des fichiers ayant pour extension :code:`.py`. 

    Plus votre programme grandit plus vous serez amené à le découper en plusieurs fichiers, ce qui d'ailleurs vous permettra de réutiliser des fonctions écrites pour un programme dans un autre sans avoir à les recopier.

    Un tel fichier est appelé un *module*. Un module peut contenir des définitions.
    
**Exercice :** Dans votre répertoire créez un dossier :code:`intro_module`, puis dans l'IDLE créez un premier fichier :code:`functions.py` contenant :

    .. code-block:: python
    
        def square(n):
            return n*n
            
        def cube(n):
            return n*square(n)
            
    Dans un second fichier :code:`main.py` copiez :
    
    .. code-block:: python
    
        import functions
        
        x = functions.square(5)
        print(x)
        
    Maintenant interprétez :code:`main.py`. Vous pouvez remarquer que vous avez eu accès à la fonction :code:`square` contenue dans le fichier :code:`functions.py`. Pour faire appel à cette fonction nous avons préfixé son nom par le nom du module qui la contient : :code:`functions.square`.
    

.. note:: Les importations de modules doivent se faire au début de votre fichier principal, à raison d'une importation par ligne.

    Le nom de certains modules étant très long on peut les importer avec un nom plus petit en utilisant :code:`as`:
    
    .. code-block:: python
    
        import module_au_nom_trop_long as mnl
        
    Dans ca cas on préfixera le nom des fonctions par :code:`mnl`.
    
    Comme un module peut comporter un nombre très important de fonctions, et qu'il peut arriver que vous n'ayez besoin que de l'une ou l'autre, il est possible de n'importe que celles dont vous avez besoin :
    
    .. code-block:: python
    
        from functions import cube
        
    Dans ca cas, il ne sera pas besoin de préfixer leurs noms pour les appeler.
    
    Enfin, il reste un possibilité d'importer toutes les fonctions d'un module, sans avoir à préfixer leur nom lors de l'appel :
    
    .. code-block:: python
    
        from functions import *
        
    Mais, ça rend votre code moins lisible et risque de provoquer des problèmes si vous importez deux modules qui contiennent des fonctions ayant le même nom.
    
    Pour tout savoir sur les modules c'est par `ici <https://docs.python.org/fr/3/tutorial/modules.html>`_


.. image:: antigravity.png
   :height: 588px
   :width: 518px
   :scale: 80 %
   :align: center

Vous pouvez essayer d'importer le même module pour voir ce qui se passe.


Des exemples de modules
-----------------------

**Le module :** :code:`random`

.. note:: Dans ce module vous trouverez de nombreuses fonctions qui permettent de simuler des phénomènes aléatoires. Pour voir l'ensemble des fonctions contenues dans un module on peut utiliser la fonction :code:`help`.

**Exercice :** Dans une console, importez le module :code:`random` et utilisez la commande :code:`help` pour obtenir la liste des fonctions qu'il contient.
    
    Que font les fonctions :code:`randint`, :code:`choice`, :code:`random` et :code:`shuffle` ?
    
    Quelle est la différence en la fonction :code:`choices` et la fonction :code:`sample` ?

.. admonition:: Solution
   :class: dropdown; tip
   
   La première simule un tirage avec répétition (on remet l'objet tiré avant de retirer) alors que la seconde simule un tirage sans répétition (comme si on tirer les éléments en même temps).

**Exercice :** Ecrire une fonction :code:`chifoumi()` qui retourne un élément au hasard de la liste :code:`liste = [ "Papier", "Caillou", "Ciseaux"]`. 


.. admonition:: Solution
   :class: dropdown; tip
   
        .. ipython:: python
            
            from random import choice
            
            def chifoumi()->str:
                liste = [ "Pierre", "Caillou", "Ciseaux"]
                return choice(liste)
                
            chifoumi()
                
**Exercice :** Ecrire une fonction :code:`pwd_generator(Alpha, alpha, digit, spe)` qui prend comme arguments les cinq entiers :code:`Alpha`, :code:`alpha`, :code:`digit` et :code:`spe` et qui retourne un mot de passe sous forme d'une chaîne de caractères comportant :

        • :code:`Alpha` lettres majuscules
        • :code:`alpha` lettres minuscules
        • :code:`digit` chiffres
        • :code:`spe` caractères parmi #@$%?_
        
        

.. admonition:: Solution
   :class: dropdown; tip
   
        .. code-block:: python
            
            from random import choices, shuffle
            
            def pwd_generator(Alpha:int, alpha:int, digit:int, spe:int)->str:
                lettres = "abcdefghijklmnopqrstuvwxyz"
                Lettres = lettres.upper()
                chiffres = "0123456789"
                speciaux = "#@$%?_"
                
                pwd = choices(Lettres, k=Alpha)
                pwd += choices(lettres, k=alpha)
                pwd += choices(chiffres, k=digit)
                pwd += choices(speciaux, k=spe)
                shuffle(pwd)
                return "".join(pwd)  
            
            
**Le module :** :code:`time`

.. note:: Ce module contient de nombreuses fonctions relatives au temps comme son nom l'indique.

**Exercice :** Que font les fonctions :code:`time`, :code:`time_ns`, :code:`ctime`,  :code:`perf_counter` et :code:`perf_counter_ns` ?

**Exercice :** Combien de temps Python met-il pour créer une liste de :math:`10^6` entiers pseudo-aléatoires compris entre :math:`10^3` et :math:`10^5`? Même question pour des listes de tailles :math:`10^7` et :math:`10^8`. Ecrivez une fonction.



.. admonition:: Solution
   :class: dropdown; tip
   
    .. ipython:: python
    
        from time import perf_counter
        from random import randint
        
        def time_it(n:int)->float:
            t1 = perf_counter()
            [randint(10**3,10**5) for __ in range(n)]
            t2 = perf_counter()
            return t2-t1
            
        time_it(10**6)
        
        time_it(10**7)
        
        time_it(10**5)
        
**Le module :** :code:`matplotlib` 

.. note:: Ce module offre de nombreux moyens de représenter graphiquement des données. Vous trouverez toute sa documentation `ici <https://matplotlib.org>`_. 

    Nous allons nous contenter d'un minuscule aperçu des fonctions proposées par ce module.

**Exercice :** Copier-coller le code suivant, et essayez de comprendre chaque ligne de commande.

    .. code-block:: python
        
        import matplotlib.pyplot as plt
        
        x = [1,2,3,4,5]
        y = [2,4,6,2,1]
        z = [5,3,9,3,2]
        
        plt.plot(x,y,'r')
        plt.plot(x,z,'g')
        plt.title("Un exemple")
        plt.legend(['Les y', 'Les z'], loc='upper left')
        plt.show()
        
**Exercice :** Tracer le temps mis par Python pour créer une liste de :code:`n` entiers pseudo-aléatoires compris entre :math:`10^3` et :math:`10^5` en fonction de :code:`n`, pour :code:`n` allant de :math:`10^5` à :math:`10^6` par pas de :math:`10^5`.


.. admonition:: Solution
   :class: dropdown; tip
   
   .. code-block:: python 
   
      from time import perf_counter
      from random import randint
      import matplotlib.pyplot as plt

      def time_it(n:int)->float:
          t1 = perf_counter()
          [randint(10**3,10**5) for __ in range(n)]
          t2 = perf_counter()
          return t2-t1

      # Création des tableaux de valeurs
      x = [n for n in range(10**5,10**6+1,10**5)]
      y = [time_it(n) for n in x]

      # Préparation du graphique
      plt.plot(x,y)
      plt.title("Temps de création d'une liste aléatoire en fonction de sa longueur")

      # Affichage
      plt.show()


Des tests
=========

.. note:: Lorsque l'on a écrit une fonction on souhaite souvent la tester pour voir si elle fonctionne bien comme c'était prévu.

    Dans la vraie vie, un developpeur est obligé de fournir des tests qui prouvent que ce qu'il a programmé fonctionne bien et s'intègre bien au projet sur lequel il travaille.
    
    Il faut donc automatiser les tests, pour ça on recourt aux *tests unitaires*, c'est ce que j'utilise pour corriger vos DM. Python offre de nombreux modules pour écrire des test unitaires. Nous allons en utiliser un qui est très pratique, facile à mettre en oeuvre et qui ne demande pas de connaissance particulière. Il s'agit de :code:`doctests`, dont vous trouverez toute la documentation `ici <https://docs.python.org/3/library/doctest.html>_`.
    
    Avec :code:`doctest` on peut écrire des tests dans la docstring de la fonction.
    
    Imaginons que j'ai écrit la fonction suivante :
    
        .. code-block:: python

           def add(a, b):
               """
               calculate the sum of a and b

               Args:
                   a, b : two objects of the same class which are summable.

               Returns:
                   the sum of a and b
               """
               return a + b
           
    
           
    Si j'utilise ma fonction dans la console de l'IDLE, je m'attends à obtenir les résultats suivants :
    
        .. code-block:: pycon
        
           >>> add(5,3)
           8
           >>> add(5.,3.)
           8.0
           >>> add('Hello',' World!')
           'Hello World!'
    
    Pour tester si ma fonction retourne bien ce que je veux il me suffit d'ajouter ces résulats à la docstring de ma fonction et d'importer le module :code:`doctests`, puis d'ajouter à la fin de mon script les lignes suivantes :
     
        .. code-block:: python
           
           def add(a, b):
               """
               calculate the sum of a and b

               Args:
                   a, b : two objects of the same class which are summable.

               Returns:
                   the sum of a and b
                   
               Examples:
                      
               >>> add(5,3)
               8
               
               >>> add(5.,3.)
               8.0
               
               >>> add('Hello',' World!')
               'Hello World!'
               """
               return a + b
               
           if __name__ == '__main__':
               import doctest
               doctest.testmod()
               
               
   
    Copier-coller ce code dans un fichier puis intérprétez le. Que se passe-t-il ?
    
    Maintenant modifier les lignes :
    
        .. code-block:: python
        
            >>> add(5, 3)
            8
            
    en 
    
        .. code-block:: python
        
            >>> add(5, 3)
            10
            
    Puis intérprétez à nouveau votre script. Qu'obtenez-vous ?
    
    La liste des tests que vous souhaitez faire passer à votre fonction peut être longue. Dans ce cas il est plus judicieux de les placer dans un fichier texte (extension :code:`.txt`) et de faire appel à :code:`doctest.testfile()` à la place de :code:`doctest.testmod()`.
    
    Imaginons que mon script se nomme :code:`add_function.py` et contienne :
    
      
        .. code-block:: python
           
           def add(a, b):
               """
               calculate the sum of a and b

               Args:
                   a, b : two objects of the same class which are summable.

               Returns:
                   the sum of a and b
               """
               return a + b
               
           if __name__ == '__main__':
               import doctest
               doctest.testfile("add_examples.txt")
               
    Alors mon fichier texte :code:`add_examples.txt` pourrait être :
    
        .. code-block:: python
        
            >>> from essai_mod import add

            >>> add(5,3)
            8

            >>> add(5.,3.)
            8.0

            >>> add('Hello',' World!')
            'Hello World!'

            >>> type(add(2,3))
            <class 'int'>

            >>> type(add(2.,3.))
            <class 'float'>
            
            >>> type(add('Hello', ' World!')) == str
            True
   
    
    
    Faites un copier-coller du script et du fichier texte, puis essayez le script.


**Exercice :** Ecrire un jeu de tests pour la fonction :code:`fibo` que vous avez programmée dans le TP1.

**Exercice :** Ecrire un jeu de tests pour la fonction :code:`is_palindrome` que vous avez programmée dans le TP1.

**Exercice :** Ecrire un jeu de tests pour la fonction :code:`largest_growing_sub_list` que vous avez programmée dans le TP1.

**Exercice :** Ecrire un jeu de tests pour la fonction :code:`creat_dict_pos` que vous avez programmée dans le TP1.


Un peu de complexité
====================

.. note:: Plusieurs algorithmes peuvent répondre à un même problème. Il est naturel de chercher lequel est le plus efficace. Il y a deux notions d'efficacité qui nous intéressent : la rapidité et le besoin de ressource en mémoire. On parle de *complexité temporelle* et de *complexité spatiale*.

    On va commencer par observer des complexité temporelles différentes pour réoudre un même problème.
    
    Pour ça, nous allons utiliser les fonctions suivantes :
    
        .. code-block:: python
            
            from time import perf_counter
            from typing import Callable
            
            # Cette fonction, un peu particulière, permet de mesurer 
            # le temps d'éxécution d'une fonction :code:`f`.
            
            
            def timing(f:Callable[[Any],Any])->float:
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
                
            # Des fonctions statistiques pour traiter les données
            # avant de les afficher.
            
            def mean(l:list[float])->float:
                """
                Calculate the mean value of the list of float l.
                
                Args:
                    l : a list of float
                Returns:
                    a float that the mean value of l.
                """
                return sum(l)/len(l)

            def std_deviation(l:list[float])->float:
                """
                Calculate the standard deviation of l.
                
                Args:
                    l : a list of float
                Returns:
                    a float that is the standard deviation of l.
                """
                return (mean([k**2 for k in l])-(mean(l))**2)**(1/2)

            def traitement(l):
                """
                ???
                """
                m = mean(l)
                e = std_deviation(l)
                return mean([k for k in l if m-e <= k <= m+e])

    La première fonction :code:`timing()` est un peu particulière, c'est ce que l'on appelle un *décorateur* et vous n'avez pas à savoir en écrire ni même comprendre comme ça fonctionne, mais voilà comment on l'utilise pour mesurer le temps d'exécution d'une fonction :
    
        .. code-block:: python
        
            @timing
            def ma_fonction_a_mesurer(n:int)->int:
                return 10**(2*n)
                
    On a dit qu'on a décoré notre fonction, et maintenant quand nous appelerons :code:`ma_fonction_a_mesurer(n)` ce qui sera retourner sera le temps d'exécution en seconde :
    
        .. code-block:: python

            >>> ma_fonction_a_mesurer(10)
            3.334018401801586e-06
            >>> ma_fonction_a_mesurer(100)
            4.417030140757561e-06
            >>> ma_fonction_a_mesurer(1000)
            3.5499921068549156e-05
            >>> ma_fonction_a_mesurer(10**6)
            0.7475648750551045
            >>> ma_fonction_a_mesurer(10**7)            
            30.249255042057484

    Donc il faut environ 30 secondes pour calculer :code:`ma_fonction_a_mesurer(10**7)`.
    
    
Un premier exemple
------------------


**Exercice :** Voici deux fonctions qui calculent la même chose : 

        .. code-block:: python

            def power(x:int, n:int)->int:
                r = 1
                for __ in range(n):
                    r *= x
                return r

            def quick_power(x:int,n:int)->int:
                r = 1
                y = x
                k = n
                while k != 0:
                    if k % 2 == 1:
                        r *= y
                    k //= 2
                    y = y**2
                return r
                
                
    **Q1 :** Que calculent-elles ? Si c'est évident pour la première, ca l'est moins pour la seconde mais essayez les pour vous convaincre.
    
    **Q2 :** Utilisez les fonctions données plus haut pour tracer sur un même graphique les temps d'exécution de ses deux fonctions, en fonction de :code:`n`, pour calculer :code:`power(2,n)` et :code:`quick_power(2,n)` pour :code:`n` allant de :math:`1` et :math:`500` par pas de :math:`20`. 
    
    Pour améliorer le rendu, pour chaque valeur de :code:`n` vous procèderez à :math:`30` mesures puis vous appliquerez la fonction :code:`traitement` à la liste :code:`l` de ces dix mesures et placerez le point de coordonnées :math:`(n,\text{traitement}(l))`.

    .. admonition:: Solution
       :class: dropdown; tip   

       .. code-block:: python

            # Décoration des fonctions
            @timing
            def quick_power(x,n):
                r = 1
                y = x
                k = n
                while k != 0:
                    if k % 2 == 1:
                        r *= y
                    k //= 2
                    y = y**2
                return r


            @timing
            def power(x, n):
                rep = 1
                for __ in range(n):
                    rep *= x
                return rep


            # Création des listes 
            x = list(range(1,500,10))
            y = [traitement([power(2,n) for __ in range(30)]) for n in x]
            z = [traitement([quick_power(2,n) for __ in range(30)]) for n in x]

            # Préparation des graphes
            plt.plot(x,y)
            plt.plot(x,z)
            plt.legend(['power', 'quick_power'], loc='upper left')
            # Affichage
            plt.show()



       .. image:: expo_quick_expo.png
          :height: 480px
          :width: 640px
          :scale: 80 %
          :align: center
          
          
    **Q3 :** Si on note :math:`T_{\text{expo}}(n)` et :math:`T_{\text{q_expo}}(n)` les fonctions qui donnent les temps d'exécution des fonctions :code:`expo(2,n)` et :code:`quick_expo(2,n)` en fonction de :math:`n`. Comment qualiferiez-vous leurs courbes représentatives ? 
    
    Conclusion ? Quelle est la fonction la plus efficace en terme de temps ?
    
    

  


    .. admonition:: Solution
       :class: dropdown; tip   

        Il semble que :math:`T_{\textrm{expo}}(n)` soit une fonction linéaire et que :math:`T_{\textrm{q_expo}}(n)` soit une fonction logarithme au vu de leurs courbes.
        
        Donc :code:`quick_expo` est bien plus rapide.


Un second exemple
-----------------

**Exercice :** On considère la fonction suivante :

    .. code-block:: python
    
        def minmax(t:list[int])->tuple(int,int):
            n = len(t)
            m, M = t[0], t[0]
            for i in range(n):
                if t[i] > M: M = t[i]
                if t[i] < m: m = t[i]
            return m, M


    **Q1 :** Que détermine cette fonction ?
    
    **Q2 :** Nous souhaitons déterminer son efficacité temporelle. Quel va être le paramètre en fonction duquel nous allons exprimer son temps d'exécution :math:`T`?
  

    .. admonition:: Solution
       :class: dropdown; tip   
       
        La taille de la liste :code:`t` est le bon paramètre.
    
    **Q3 :** Créer une liste :code:`tests` qui contient des listes :code:`l_n` de :math:`20` listes de :math:`n` entiers pseudo-aléatoires compris entre :math:`0` et :math:`10^5`, pour :math:`n` allant de :math:`10` à :math:`10000` par pas de :math:`50`.
    
  
    .. admonition:: Solution
       :class: dropdown; tip   

            .. code-block:: python

                from random import randint

                tests = []
                r = range(10,10**4,50)
                for n in r:
                    tmp = []
                    for __ in range(20):
                        t = [randint(0,100000) for __ in range(n+1)]
                        tmp.append(t)
                    tests.append(tmp)
    
    
    **Q4 :** Tracer sur un graphique le temps d'exécution de la fonction :code:`minmax(t)` en fonction de la longueur de :code:`t`. Pour améliorer le rendu vous utiliserez la fonction :code:`traitement`.
    
   
    .. admonition:: Solution
       :class: dropdown; tip   

            .. code-block:: python

                # On décore la fonction
                @timing()
                def minmax(t:list[int])->tuple(int,int):
                    n = len(t)
                    m, M = t[0], t[0]
                    for i in range(n):
                        if t[i] > M: M = t[i]
                        if t[i] < m: m = t[i]
                    return m, M

                x = list(r)
                y = [traitement([minmax(t) for t in l]) for l in tests]

                plt.title("Tps d'exécution de minmax(t)")
                plt.plot(x,y)
                plt.show()  

        
       .. image:: temps_minimax.png
          :height: 480px
          :width: 640px
          :scale: 80 %
          :align: center
    

    **Q5 :** D'après son graphe, comment varie :math:`T(n)` en fonction de :math:`n` ?
    
    .. admonition:: Solution
        :class: dropdown; tip   

          :math:`T(n)` semble être linéaire.
          
            
    
Un troisième exemple
--------------------

**Exercice :** On considère la fonction suivante qui trie un tableau de nombres entiers :

    .. code-block:: python
    
            def tri_pi(t):
                n = len(t)
                rep = False
                while not rep:
                    rep = True
                    for i in range(0,n-1,2):
                        if t[i] > t[i+1]:
                            t[i], t[i+1] = t[i+1], t[i]
                            rep = False
                    for i in range(1,n-1,2):
                         if t[i] > t[i+1]:
                            t[i], t[i+1] = t[i+1], t[i]
                            rep = False
                

    **Q1 :** Essayer cette fonction pour vous convaincre qu'elle trie bien un tableau.
    
    **Q2 :** Nous souhaitons déterminer son efficacité temporelle. Quel va être le paramètre en fonction duquel nous allons exprimer son temps d'exécution :math:`T`?
    
    **Q3 :** Créer une liste :code:`tests` qui contient des listes :code:`l_n` de :math:`20` listes de :math:`n` entiers pseudo-aléatoires compris entre :math:`0` et :math:`100`, pour :math:`n` allant de :math:`10` à :math:`2000` par pas de :math:`100`. 
    
       
    .. admonition:: Solution
       :class: dropdown; tip   

       .. code-block:: python

            tests = []   
            r = range(10,2*10**3,100)
            for n in r:
                tmp = []
                for __ in range(10):
                    t = [randint(0,100) for __ in range(n+1)]
                    tmp.append(t)
                tests.append(tmp) 
                
    **Q4 :** Tracer sur un graphique le temps d'exécution de la fonction :code:`tri_pi(t)` en fonction de la longueur de :code:`t`. Pour améliorer le rendu vous utiliserez la fonction :code:`traitement`.

       
    .. admonition:: Solution
       :class: dropdown; tip   

       .. code-block:: python
       
            # On décore la fonction 

            @timing
            def tri_pi(l):
                rep = False
                while not rep:
                    rep = True
                    for i in range(0,len(l)-1,2):
                        if l[i] > l[i+1]:
                            l[i], l[i+1] = l[i+1], l[i]
                            rep = False
                    for i in range(1,len(l)-1,2):
                         if l[i] > l[i+1]:
                            l[i], l[i+1] = l[i+1], l[i]
                            rep = False

            # On prépare et on affiche le graphe
            x = list(r)
            y = [traitement([tri_pi(t) for t in l]) for l in tests]
            plt.plot(x,y)

        
       .. image:: temps_tri_pi.png
          :height: 480px
          :width: 640px
          :scale: 80 %
          :align: center

    **Q5 :** D'après son graphe, comment varie :math:`T(n)` en fonction de :math:`n` ?
    
         
    .. admonition:: Solution
       :class: dropdown; tip   

        :math:`T(n)`semble être quadratique en :math:`n`, c'est-à-dire être une fonction polynomiale de degré 2.
        
    **Q6 :** Le module :code:`numpy` offre une fonction qui permet de trouver le polynôme de degré 2 qui s'approche le plus de :math:`T`. Voilà comment l'utiliser :
    
    .. code-block:: python

        z = np.polyfit([x[i] for i in [0,len(x)//2,len(x)-1]],[y[i] for i in [0,len(x)//2,len(x)-1]],2)
        p = np.poly1d(z)

    :code:`z` est un tableau qui contient les trois coefficients du polynôme que l'on cherche, et :code:`p` représente cette fonction. Les coefficients que l'on trouve dépendent de l'ordinateur sur lequel on fait trouner notre script. 

    Modifier le code précédent pour tracer sur un même graphique la fonction :math:`T` et la fonction :code:`p`.
         
    .. admonition:: Solution
       :class: dropdown; tip   


        .. image:: tri_pi2.png
              :height: 480px
              :width: 640px
              :scale: 80 %
              :align: center


        Comme on ne voit presque aucune différence j'ai décalé les graphes pour obtenir :


        .. image:: tri_pi3.png
              :height: 480px
              :width: 640px
              :scale: 80 %
              :align: center
              
    **Q7 :** Utiliser la fonction :code:`p` pour estimer le temps nécessaire pour trier des tableaux de taille :math:`10^5`, :math:`10^6` et :math:`10^8`.
    
     
    .. admonition:: Solution
       :class: dropdown; tip   
       
       .. code-block:: python

            >>> from datetime import timedelta
            >>> print(timedelta(seconds=p(10**5)))                 
            0:06:42.663611
            >>> print(timedelta(seconds=p(10**6)))                 
            11:11:14.948871
            >>> print(timedelta(seconds=p(10**8)))                 
            4661 days, 13:28:56.312128
            >>> 4661 /365                     
            12.76986301369863
        
      
       Autrement dit, il faudrait 12 ans pour trier un tableau de taille :math:`10^8` sur mon ordinateur.
    
    