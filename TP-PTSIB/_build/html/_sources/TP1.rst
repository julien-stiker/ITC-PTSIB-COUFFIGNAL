
******************************************
TP1 : La reprise
******************************************

.. note :: **Les objectifs du TP :**

	* Préparer votre environnement de travail et organiser votre dossier utilisateur.
	* Réviser les bases de Python : Syntaxe, type, variables, branchements conditionnels, boucles et fonctions.


.. rst-class:: html-toggle

Environnement de travail
========================


Dans Windows
------------

Dans l'ordre :
	
	1. Ouvrez votre session.
	2. Dans votre répertoire créer un dossier nommé TP qui contiendra tous les TP de cette année.
	3. Dans ce dossier, créer un dossier TP1 qui contiendra les fichiers de ce TP.


Dans l'IDLE
-----------

Lancez l'IDLE, Python 3. La fenêtre qui s'ouvre s'appelle **"Python Shell"** et ressemble peu ou prou à ça :

.. image:: PythonShell.png
   :height: 980px
   :width: 1540px
   :scale: 60 %
   :align: center

.. note:: Le symbole
		:code:`>>>`
		s'appelle le **"prompt"** ou **l"invite de commande"**. Il signifie que l'interpréteur est disponible à prendre vos commandes.

.. note:: **La syntaxe de base en Python :**

	* Les commentaires, que vous utiliserez (plus tard) pour annoter votre code afin de le rendre 	compréhensible et de vous souvenir de ce qu'il fait s'obtiennent avec un **#**.

	    .. code-block:: python

	        # Tout ce qui suit un dièse sur une ligne est ignoré
	* De manière générale vous taperez une instruction par ligne, sans marqueur à la fin.
	* Si vous souhaitez taper plusieurs instructions par ligne, il faudra les séparer par **;**
	* L'indentation est syntaxique et non décorative. Un bloc **doit être indenté** et doit toujours être précédé d'une ligne se terminant par  un **":"**

	    .. code-block:: python

        	if montant > 50:
        	    print("Frais de port offerts")
        	else:
        	    print("Frais de port : 5 euros")
        	    montant += 5
        
Pyhton sait compter et il nous le prouve.

**Exercice :** Taper les différentes opérations suivantes (chacune sur une ligne) :
		
		.. code-block:: python
		
			2 + 3; 3 - 5; -2 * 7; 9 ** 2; 3.11 / 2.7; 2.2 / 3.5; 15.0 / 2.0; 15 // 2; 16 % 3  
            
.. warning::
	On utilise la notation anglo-saxonne le point remplace la virgule. 

Vous devriez obtenir quelque chose comme ça :

		.. code-block:: python
			
			>>> 2 + 3
			5			
			...



* Observez le format des différents résultats.
* Quittez l'IDLE et le relancer. Qu'observez-vous ?

.. note:: 
    
            .. table::
               :align: center

               ==================  ======================================  
               Opération           Résultat                   
               ==================  ======================================
               :code:`+`           Addition       
               :code:`-`           Soustraction
               :code:`*`           Multiplication
               :code:`**`          Puissance
               :code:`/`           Division
               :code:`//`          Quotient dans la division euclidienne
               :code:`%`           Reste dans la division euclidienne      	
               ==================  ======================================   


.. warning:: A la fermeture de l'IDLE tout ce qui est tapé dans le shell est perdu...


.. note::
	Pour ouvrir/sauver un nouveau fichier vous pouvez utiliser le menu *Edit* ou *Edition*. Ou alors utiliser les raccourcis clavier : *CTRL - N* et *CTRL - S*.

	De même pour l'exécuter vous pouvez utiliser le raccourci *F5*.


**Exercice :** Ouvrez une nouvelle fenêtre et sauvez le fichier dans votre dossier TP1 sous le nom : :code:`TP1.py`. Dans ce fichier inscrivez les commandes suivantes :

.. code-block:: python

	1 + 1
	print("2")
	2 + 3
	print(2 * 3)
	2 * 3  

Enregistrez et exécutez votre fichier. Qu'observez-vous ? Que fait Python exactement ?


.. warning:: Contrairement à ce qui se passe dans le shell, lorsqu'on exécute le code contenu dans un fichier Python effectue les calculs mais ne les affiche pas. Pour les afficher il faut le demander à l'aide de la commande :code:`print`. 



**Exercice :** Modifiez le code contenu dans le fichier :code:`TP1.py` pour qu'à l'exécution il affiche la table de 7 après avoir fait les calculs.

.. admonition:: Solution
   :class: dropdown; tip

    .. code-block:: python
    
        print(1*7)
        print(2*7)
        print(3*7)
        print(4*7)
        print(5*7)
        print(7*7)
        print(8*7)
        print(9*7)
        print(10*7)


**Exercice :** Remplacez le code du fichier :code:`TP1.py` par :

.. code:: python
	
	for i in range(1,11):
    		print(i,"* 7 = ", i*7)

Enregistrez et exécutez le avec Python 3. Magique non ? Que signifie ce code d'après vous ?

.. rst-class:: html-toggle



Dans Spyder
-----------

Lancez Spyder. La fenêtre qui s'ouvre ressemble à ça :



.. image:: Spyder.jpg
   :height: 1904 px
   :width: 3104 px
   :scale: 30 %
   :align: center

Il y a trois panneaux qui constituent la fenêtre :

	1. Une console IPython en bas à droite, prête à interpréter des commandes Python. Ici le prompt n'est pas le même    car c'est une console IPython. Il prend la forme :code:`In [1]:` avec un numéro d'entrée.    
	2. Un panneau d'information en haut à droite, qui comporte quatre onglets :
    
            * Un explorateur de variables.
            * Un explorateur de fichiers.
            * Une rubrique d'aide.
            * Un visualisateur de graphe.
        
        
	3. Un éditeur à gauche dans lequel vous écrirez vos programmes.

.. warning:: Ne déplacez pas les différents panneaux !! Ne les redimensionnez pas non plus !! 

**Exercice :** Vérifiez que la console réagit exactement comme le shell de l'IDLE, en exécutant quelques commandes.

**Exercice :** Ouvrez le fichier :code:`TP1.py` et exécutez le.

.. note:: Dans Spyder aussi on peut utiliser des raccourcis clavier :

	* *CTRL-O* : Ouvrir un fichier.
	* *CTRL-S* : Sauvegarder.
	* *CTRL-N* : Nouveau fichier.
	* *F5* : Exécuter.

.. rst-class:: html-toggle

.. _toggle-test-link:

Variables et Affectations
==================================

Littéraux
---------

.. note:: Un **littéral** est une valeur écrite dans le programme.

Exemples :

* Un entier : ``2``
* Un nombre à virgule flottante : ``3.14``
* Un nombre complexe : ``4j``
* Une chaine de caractères : ``"PTSI-B"``
* Une liste d'entiers : ``[3, 2, 1]``

Lorsque vous tapez un littéral dans la console Python crée, disons, un nouvel "*objet*".


.. code-block:: python

   >>> (2022, id(2022), type(2022))
   (2020, 4342639664, <class 'int'>)
   
En plus de sa valeur, Python assigne à l'objet un **identifiant**, ici 4342639664, qui indique où l'objet est gardé en mémoire et un **type**, ici :code:`int` pour entier.

Nous verrons plus en détail les types un peu plus loin, parmi les principaux on trouve :

    * Les entiers :code:`int`
    * Les flottants :code:`float`
    * Les chaines de caractères :code:`str`
    * Les listes :code:`list`
    * Les booléens :code:`bool`
    * Les dictionnaires :code:`dict`




Variables et affectations
-------------------------

L'identifiant d'un objet est assez contraignant à utiliser. On a alors recourt aux variables.

.. note:: Une **variable** permet de stocker en mémoire une donnée pour la réutiliser à plusieurs reprises en la désignant par un nom.
	
	Pour donner une valeur à une variable en Python on utilise le symbole :code:`=` , cette opération s'appelle une **affectation de valeur** à une variable, ou plus simplement une **affectation de variable**.
	
	Une affectation crée une **liaison** entre un nom et une donnée stockée en mémoire.

.. warning:: Les noms de variable (et aussi : de fonction, de classe...) doivent respecter certaines règles syntaxiques :
	
	* Ils ne peuvent contenir que des lettres, des chiffres, des *underscores* ( _ ), et doivent commencer par une lettre.
	* La **casse** est importante, autrement Python fait la différence entre majuscule et minuscule (ma_variable ≠ Ma_VaRiAbLE).
	* D'après la **PEP8**, les noms de variables doivent être écrits en minuscules, avec des underscores si nécessaire : :code:`ma_variable`.
	* Les noms des constantes doivent être écrits tout en majuscules, avec des underscores si nécessaire :  :code:`UNE_CONSTANTE`.
	* Certains noms sont **réservés** par le langage et ne peuvent être utilisés comme nom de variable. Voici la liste pour Python 3 :
    
       
    
            ============== =============== ============= =============== ================
            :code:`and`    :code:`assert`  :code:`break` :code:`class`   :code:`continue`
            :code:`def`    :code:`del`     :code:`elif`  :code:`else`    :code:`except`
            :code:`exec`   :code:`finally` :code:`for`   :code:`from`    :code:`global`
            :code:`if`     :code:`import`  :code:`in`    :code:`is`      :code:`lambda`
            :code:`not`    :code:`or`      :code:`pass`  :code:`print`   :code:`raise`
            :code:`return` :code:`try`     :code:`while` :code:`yield`   :code:`as`
            :code:`with`                                                     
            ============== =============== ============= =============== ================

	Dans un programme complexe, il faut impérativement donner des noms significatifs aux variables, de sorte d'en faciciliter la lecture et la compréhension.


.. warning:: Le symbole :code:`=` utilisé pour l'affectation ne représente pas une égalité. En particulier il n'est pas symétrique.

    .. ipython::
        :okexcept:
        
        In [1]: a = 2
        
        In [2]: a
        
        
        In [3]: 2 = a
        
   
	
.. note:: Il est d'usage de laisser une espace avant et une autre après le signe :code:`=`.

**Exercice :** Dans la console créez une variable :code:`mon_annee` et affectez lui votre année de naissance. Demandez à Python son identifiant et son type à l'aide des commandes :code:`id()` et :code:`type()`. Taper ensuite les différentes commandes suivantes :

	.. code-block:: python
	   
	   mon_annee + 1 ; 3*mon_annee ; mon_annee + mon_annee ; 

**Exercice :** Dans la console tapez les lignes suivantes.


    .. ipython:: python

        a = 3
        a = a + 2
  
Que vaut :code:`a` à votre avis ? Vérifiez en affichant la valeur de :code:`a`.

    .. ipython:: python

        a += 2
        a

Qu'a fait Python ? Essayez avec d'autres valeurs que 2 et avec d'autres opérateurs que :code:`+`.


.. admonition:: Solution
   :class: dropdown; tip

   Il est équivalent de taper :code:`a += 2` ou de taper :code:`a = a + 2`.

.. note:: On peut abréger certaines affectations.
	
	.. code-block:: python

		a -= k   
		a /= k   
		a //= k  
		a %= k
		a *= k
		a **= k 

**Exercice :**  Dans la console, tapez les commandes suivantes.

    .. ipython:: python

        a = 10
        b = 20
        a = b
        b = a


Que valent :code:`a` et :code:`b` maintenant ? Vérifiez.

.. admonition:: Solution
   :class: dropdown; tip
   
   :code:`a = 20` et :code:`b = 20`.

Essayez les commandes suivantes :

    .. ipython:: python

        a = 10
        b = 20
        c = a
        a = b
        b = c
        
Que valent :code:`a` et :code:`b` maintenant ? Vérifiez. 

.. admonition:: Solution
   :class: dropdown; tip
   
   :code:`a = 20` et :code:`b = 10`. On a échangé les valeurs de :code:`a` et de :code:`b`.


Observez ce qu'il se passe s'il on fait :

    .. ipython:: python

        a = 10
        b = 20
        print("a = ", a, "b = ", b)
        (a,b) = (b,a)
        print("a = ", a, "b = ", b)

Que s'est-il passé ?

.. note:: On parle d'**affectations multiples** lorsqu'on affecte plusieurs variables en même temps. Par exemple :

	.. ipython:: python

 		(a, b) = (4, 5) ; (a, b)
   		(a, b) = (b, a) ; (a, b)
   		
	C'est très pratique pour échanger les valeurs de deux variables.

**Exercice :** Copiez-collez les instructions suivantes dans le fichier :code:`TP1.py` et sauvez.

.. code-block :: python

    a = 10
    b = 20
    c = 30
    a *= 2
    c = b-a
    print((a+b)*c+1)
       
Quel résultat va s'afficher à l'exécution ? Vérifiez.

.. admonition:: Solution
   :class: dropdown; tip
   
   :code:`1`

 	




.. rst-class:: html-toggle

.. _toggle-test-link:

Types de données simples
========================

.. note:: En Python le typage des données est *dynamique* : les variables n'ont pas à proprement parler de type, c'est leurs valeurs qui en ont un. Donc au cours de l'exécution une même variable peut contenir des valeurs de types différents.

        .. ipython :: python

            a = 4
            type(a)
            a = (3, 8)
            type(a)

    Dans Spyder vous pouvez utilisez l'**explorateur de variables** pour connaître la valeur et le type d'une variable, et l'espace mémoire qui lui est alloué.


        .. ipython :: python

            a = 2
            b = 'PTSI-B'
            c = True
            d = 10.
            e = [1, 2, 3]
            f = {'cat': 1, 'dog': 2}


    
    Ce qui donnera :

        .. image:: ExplorateurDeVariables.png
            :scale: 50 %
            :align: center

Les nombres
-----------

En Python il y a essentiellement quatre types de nombres :

	* Les entiers de type :code:`int`
	* Les flottants de type :code:`float`
	* Les complexes de type :code:`complex`
	* Les fractions de type :code:`fraction` 


 
**Exercice :** Qu'observez-vous quant aux types dans les résultats suivants ?

    .. ipython :: python

        a = 1 ; type(a)
        b = 1. ; type(b)
        import cmath
        c = 1j ; type( c )
        import fractions
        d = fractions.Fraction(3,8) ; f = fractions.Fraction(6,4)
        print(d+f); type(d)
        a+2 ; type(a+2)
        2*a ;type(2*a)
        a+2. ; type(a+2.)
        2.*a ; type(2.*a)
        b+2 ; type(b+2)
        b+2. ; type(b+2.)
        2 + c ; type(2+c)



.. note:: Python applique lui-même des **conversions de types**, on dit que ces conversions sont *implicites*.
	Le conversions de type numérique :code:`int` → :code:`float` → :code:`complex` sont les seules conversions implicites de type qui sont autorisées, toutes les autres sont formellement interdites et aboutissent à un message d'erreur. C'est pourquoi on dit que le **typage est fort**.



   `Lien vers la documentation du module de math <http://docs.python.org/3/library/math.html>`_

**Exercice :** Que pouvez-vous déduire des résultats suivants ?

    .. ipython :: python
    
        2 ** 100
        2. ** 100
        
.. admonition:: Solution
   :class: dropdown; tip
   
   On peut en déduire que le type :code:`int` est plus précis que le type :code:`float`.

.. note ::

    Lorsque l’on veut modeliser un problème il faut choisir entre les types :code:`int` et :code:`float` pour représenter une donnee numerique.

    * Si la valeur exacte des calculs est importante les entiers sont plus appropries, de même si les calculs portent sur des donnees d’ordres de grandeur très differents.
    
    * Les flottants sont utiles pour repr ́esenter des grandeurs physiques par exemple comme la vitesse, la temperature, le temps, etc. . ., dont seuls les premiers chiffres sont significatifs.
   


Chaînes de caractères
---------------------

.. note:: Une **chaine de caractères**, comme son nom l'indique est une série de lettres.
	On peut écrire une chaine de caractère de plusieurs façons :
		* entre guillemets
		* entre apostrophes
		* entre triples guillemets
	Le type d'une chaine est :code:`str`.

    .. ipython :: python

        s1 = "Bonjour "
        s2 = ' à '
        s3 = """ tous."""
        type(s1)
		
    On peut **concaténer** des chaines de caractère à l'aide de l'opérateur :code:`+` et les répéter à l'aide de :code:`*`.

    .. ipython :: python

        print(s1+s2+s3)
        print(2*s1)

    On peut accéder aux différentes lettres d'une chaine de caractère en utilisant des crochets :code:`[]`.

**Exercice :** Observez les résultats ci-dessous, et en déduire le sens de :code:`s[p:q:r]`.

    .. ipython :: python

        s = "Hello World!"
        print(s)
        s[0]
        s[11]
        s[3:5]
        s[:5]
        s[6:]
        s[:]
        s[-3]
        s[-3:]
        s[0:8:2]
        s[::3]

.. admonition:: Solution
   :class: dropdown; tip
   
   :code:`s[p:q:r]` retourne la chaine de caractères formée par les caractères de la chaine :code:`s` d'indice :math:`i` tels que :math:`p\leq i< q` avec un pas de :math:`r`. Si l'on omet le premier ou le dernier indice on considère que respectivement l'on commence à :math:`0`, ou que l'on va jusqu'au bout de la chaine. A noter que le pas est optionnel.

**Exercice :** Définissez la chaine de caractère :code:`s = "0123456789"` et écrivez les instructions qui afficheront les résultats suivants :

	.. code-block:: python

		'0123456789'
		'5'
		'345'
		'789'
		'02468'
		'13579'
		'036'

.. admonition:: Solution
   :class: dropdown; tip
   
   .. ipython :: python
   
        s = '0123456789'
        s
        s[5]
        s[3:6]
        s[7:]
        s[::2]
        s[1::2]
        s[:7:3]
        

.. note:: Une liste de commande pour obtenir certains caractères ou pour formater du texte.

   .. table::
   =======================	===========
   Utilité  	  		Caractère
   =======================	===========
   Aller à la ligne 		\\n
   Tabulation			\\t
   Afficher un anti-slash 	\\
   Afficher une apostrophe 	\\'
   Afficher un guillemet 	\\"
   Saut de page			\\f
   Retour en arrière 		\\b
   Retour chariot 		\\r

   =======================	===========


				
**Exercice :** Dans la console tapez les instructions qui affichent (en respectant la mise en forme exacte) :

	.. code-block:: python
	
		"J'aime beaucoup Python.
 	 		Même si je ne comprends pas tout."

 
.. admonition :: Solution
   :class: dropdown; tip
   
   .. ipython :: python
   
        s = "\"J\'aime beaucoup Python.\n \t Même si je ne comprends pas tout.\""

.. note :: Les chaines de caractères sont non-mutables !

    .. ipython :: python
        :okexcept:
        
        s = 'abcdef'
        s[1] = a
        

Les booléens
------------

.. note:: 
	En Python les booléens vrai et faux se notent :code:`True`, :code:`False`.
	
	Ils sont manipulables avec les opérations standards :code:`+, -, *, \, or, and, not` et avec les opérateurs de comparaison.
	
	Les opérateurs de comparaison sont :

		* L'égalité :code:`==`
		* L'inégalité :code:`!=`
		* Les comparateurs d'ordre : :code:`< <= > >=`
		* L'identité :code:`is` qui compare les :code:`id()` .

	Ils retournent un booléen.

	L'évaluation d'une expression booléenne s'arrête dès que le résultat est connu (opérateurs **paresseux** ou **en court-circuit**)

    .. ipython :: python

        True and False
        # Les expressions a et b ne sont pas évaluées
        a = True; b = False; True and (a or b)
        not False
 	  


**Exercice :** Tapez dans la console et évaluez les instructions suivantes.

	.. code-block:: python

	  True + True ; True + False ; True * False ; False + False ; False * False
 	  2 < 3
	  2 != 3
	  s1 = "trois" ; s2 = "sept"
	  s1 > s2
	  2 + 3 == 5
	  a = 2 ; b = 2.
	  a == b
	  a is b
	  a = 2 ; b = 2
	  a == b
	  a is b
	  1 < 2 and 3 <= 5
	  not(3 > 4)
	  'a'+'b' == 'ab' or 7 < 3

.. admonition:: Solution
   :class: dropdown; tip
   
    .. ipython :: python

        True + True
        True + False
        True * False
        False + False
        False * False
        2 < 3
        2 != 3
        s1 = "trois" ; s2 = "sept"
        # Ici c'est l'ordre lexicographique 
        s1 > s2
        2 + 3 == 5
        a = 2 ; b = 2.
        a == b
        a is b
        a = 2 ; b = 2
        a == b
        a is b
        1 < 2 and 3 <= 5
        not(3 > 4)
        'a'+'b' == 'ab' or 7 < 3


Conversion de types
-------------------

.. note:: En Python on peut faire certaines conversions de type, pour transformer un nombre en chaine de caractère ou l'inverse par exemple.

.. ipython:: python

    s = str(123) ; print(s) ; type(s)
    s = int(s) ; print(s) ; type(s)

**Exercice :** Dans la console essayez les conversions suivantes :

	.. code-block:: python
	
		float(123) ; bool(0) ; str(True) ; float(’1.22’) ; int(1.23) 
		bool(1) ; bool(’abc’) ; float(’123’) ; int(True) ; str(123) ; bool(’’)
		float(True) ; int(False) ; str(1.23) ; bool(1.23) ; float(False)


.. rst-class:: html-toggle

Entrées-sorties
===============

.. note:: Pour afficher un résultat dans la console on utilise la commande :code:`print`

    .. ipython :: python

        a = 3 
        b = 2
        print("La somme de {} et {} est {}".format(a,b,a+b))

    La méthode de chaine de caractères :code:`format` permet de formater une chaine avec des expressions. On peut aussi utiliser les :code:`f-string` pour faire la même chose. Une :code:`f-string` est une chaine de caractères préfixée par :code:`f` ou :code:`F` :
    
    .. ipython :: python
        
        a = 3
        b = 2
        print(f"Le produit de {a} et {b} est {a*b}")
    
    La fonction :code:`print` est très pratique pour afficher des résultats intermédiaires lorsque l'on cherche à déboguer un programme. Bien entendu Python offre mieux pour le `logging <https://docs.python.org/fr/3/howto/logging.html>`_.
    
    Pour lire une entrée au clavier on utilise la commande :code:`input` en Python 3 le résultat est un chaine de caractère.

	.. code-block:: python
		
		n = int(input("Entrez un nombre : ")) ; print(n/2)
        
    Pour en savoir plus sur les entrées-sorties c'est par `ici <https://docs.python.org/fr/3/tutorial/inputoutput.html#>`_.

**Exercice :** Ecrire dans un fichier :code:`TP1-exercice17.py` un programme qui demande à l'utilisateur son nom, son prénom et son année de naissance et qui retourne le résultat suivant sous la forme :

	.. code-block:: python
	
		Nom : Leponge
		Prénom : Bob 
		Année de naissance : 1900
	

.. admonition:: Solution
   :class: dropdown; tip
 
    .. code-block :: python
    
        nom = input("Entrez votre nom : ")
        prenom = input("Entrez votre prénom : ")
        annee = input("Entrez votre année de naissance : ")
        print("Nom : {}\rPrénom : {} \rAnnée de naissance : {}".format(nom,prenom,annee))



**Exercice :** Ecrire dans un fichier :code:`TP1-exercice18.py` un programme qui demande à l'utilisateur le rayon d'une sphère et qui retourne le résultat suivant sous la forme :

	.. code-block:: python

		Entrez le rayon en cm : 5
		Une sphere de rayon 5.0 cm a pour surface : 314.159265359 cm2
		Une boule de rayon 5.0 cm a pour volume : 523.5987755982989 cm3


.. admonition:: Solution
   :class: dropdown; tip
   
   .. code-block:: python

        from math import pi
        rayon = float(input("Entrez le rayon en cm : "))
        s = 4*pi*rayon**2
        v = 4/3*pi*rayon**3
        print(f"Une sphere de rayon {rayon} cm a pour surface : {s} cm2.")
        print(f"Une boule de rayon {rayon} cm a pour volume : {v} cm3.")


**Exercice :** Ecrire dans un fichier :code:`TP1-exercice19.py` un programme qui demande à l'utilisateur son nom et son prénom et qui retourne ses initiales.


.. admonition:: Solution
    :class: dropdown; tip
    
    .. code-block:: python
    
        nom = input("Entrez votre nom : ")
        prenom = input("Entrez votre prenom : ")
        print("Vos initiales sont  : {}.{}.".format(nom[0],prenom[0]))




Structures de contrôle
======================


Instruction conditionnelle
--------------------------

.. note:: Les instructions conditionnelles sont essentielles en informatique. Elles permettent d'exécuter des instructions sous réserve que certaines soient vérifiées.

	Un exemple très simple, dans le quel on test si la valeur d'une variable est plus petite que 3, et si c'est le cas on affiche qu'elle l'est.

	.. code-block:: python

		>>> if a < 3 :
		...     print("a est plus petit que 3")
	
	Cette structure de condition est dite **minimale**. Il en existe des plus complexes.

.. warning:: L'indentation est essentielle ! L'indentation c'est le décalage marqué sur la seconde ligne. Il est égal à 4 espaces (c'est mieux) ou une tabulation. 
	On ne mélange pas les espaces et les tabulations !	



.. note:: Une structure conditionnelle complète suit le schéma suivant :

		.. code-block:: python

   			 if condition_1:
       				 instructions_1

    			 elif condition_2:
        			 instructions_2

    			 elif condition_3:
        			 instructions_3
    			 ...

    			 else:
        			instructions_else

	Les instructions de la première condition évaluée à :code:`True` sont exécutées, si aucune ne l'est on exécute :code:`instructions_else` .





**Exercice :** Si :code:`x`, :code:`y` et :code:`z` sont des nombres, quelle est la valeur de  :code:`m` à la fin de cet algorithme ?:

	.. code-block:: python

            m   =   0
            if x > y:
                if x > z:
                    m   =   x
                else:
                    m   =   z
            else:
                if y > z:
                    m   =   y 
                else:
                    m   =   z


        
Vérifiez le.


**Exercice :** Ecrire un programme qui prend comme entrée un entier :code:`n` et qui affiche le double s'il est impair, le triple s'il est pair mais pas divisible par 4 et sa moitié sinon.


.. admonition:: Solution
   :class: dropdown; tip
 
    .. code-block :: python
    
        if n % 2 == 1:
            print(2*n)
        elif n % 4 ==0:
            print(n//2)
        else:
            print(3*n)


**Exercice :** Ecrire un programme qui demande les trois coefficients réels d'un trinôme :math:`ax^2+bx+c` à l'utilisateur et qui retourne une phrase indiquant le nombre de racines réelles distinctes de ce trinôme, après avoir vérifié qu'il s'agissait bien d'un polynôme du second degré.


.. admonition:: Solution
   :class: dropdown; tip
 
    .. code-block :: python
    
        a = float(input("Entrez le coefficient a : "))
        b = float(input("Entrez le coefficient b : "))
        c = float(input("Entrez le coefficient c : "))
        if a == 0:
            print("Ce n'est pas un polynôme de degré deux !")
        else:
            delta = b**2 - 4*a*c
            if delta > 0:
                print("Le trinôme {}*x^2+{}*x+{} possède deux racines réelles distinctes.".format(a,b,c))
            elif delta == 0:
                print("Le trinôme {}*x^2+{}*x+{} possède une racine réelle.".format(a,b,c))
            else:
                print("Le trinôme {}*x^2+{}*x+{} ne possède pas de racines réelles.".format(a,b,c))



**Exercice :** Ecrire un programme qui demande une année à l'utilisateur et qui indique si elle est bissextile ou non. Une année est bissextile par définition si sa valeur vérifie l'une des conditions :

	* être multiple de 4 mais pas de 100 ;
	* être multiple de 400.


.. admonition:: Solution
   :class: dropdown; tip
 
    .. code-block :: python
    
        annee = int(input("Entrez une année : "))
        if annee % 4 != 0:
            print("L'année {} n'est pas bissextile".format(annee)})
        elif annee % 100 != 0:
            print("L'année {} est bissextile".format(annee)})
        elif annee % 400 != 0:
            print("L'année {} n'est pas bissextile".format(annee)})
        else:
            print("L'année {} est bissextile".format(annee)})




.. admonition:: Solution 2 : avec les mots or et and
   :class: dropdown; tip
 
    .. code-block :: python

        annee = input("Saisissez une année : ") # L'utilisateur fournit une année à tester
        annee = int(annee) # Erreur si l'utilisateur n'a pas saisi un nombre

        if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
            print("L'année saisie est bissextile.")
        else:
            print("L'année saisie n'est pas bissextile.")

    

**Petit problème :** Ecrire un programme qui retourne le plus grand nombre parmi les quatre nombres :code:`w, x, y` et :code:`z`.


.. admonition:: Solution 2 : avec les mots or et and
   :class: dropdown; tip
 
    .. code-block :: python

          maximum = w
          if x > w:
                maximum = x
                if y > x or y > z:
                      maximum = y
                elif z > x:
                      maximum = z
          else:
                if y > w or y > z:
                      maximum = y
                elif z > w:
                      maximum = z
          return maximum

Boucle :code:`while`
--------------------

.. note:: Les boucles permettent de répéter certaines opérations autant de fois que nécessaire. Nous en verrons de deux sortes.

	Une boucle :code:`while` permet de répéter un bloc d'instructions tant qu'une condition est vérifiée.
	La structure d'une boucle :code:`while` (*tant que* en anglais) est la suivante :

		.. code-block:: python

			while condition: # Tant que la condition est remplie effectuer les instructions
				instructions
	Un exemple : La table de 7.

		.. code-block:: python

			i = 0 # On initialise notre compteur
			while i < 10: # Tant que le compteur i est strictement plus petit que 10 faire :
				print("{} * 7 = {}".format(i+1,(i+1)*7)) # Afficher le résultat
				i += 1 # Incrémenter le compteur
 

.. warning:: 
	Si dans ce programme vous oubliez d'incrémenter le compteur il ne sera jamais supérieur ou égale à 10 et votre programme ne s'arrêtera jamais !!	On appelle ça une boucle infinie.
	Si vous avez lancé une boucle infinie vous pouvez l'arrêter avec *CTRL - C* si vous êtes dans un shell ou à l'aide du bouton triangulaire orange dans la console de Syder.


**Exercice :** Ecrire un programme qui calcule la somme des :math:`100` premiers entiers. 


.. admonition:: Solution
   :class: dropdown; tip
   
   .. code-block :: python
 
        somme = 0 #Initialisation de la somme
        i=0 #Initialisation du compteur
        while i <= 100: #Tant que i est plus petit que 20 faire
            somme += i #Ajouter i à somme
            i += 1 #Incrémenter i de 1


**Exercice :** Que vaut :code:`somme` à la fin ?
	.. code-block:: python
	
		somme = 0
		i=0
		while i <= 20:
			if i % 2 == 0:
				somme += i
			i += 1

	Réécrire ce code sans la structure conditionnelle.


.. admonition:: Solution
   :class: dropdown; tip
   
   :code:`somme` contient la somme des nombres pairs de :math:`0` à :math:`20`.
 
    .. code-block :: python

        somme = 0 #Initialisation de la somme
        i=0 #Initialisation du compteur
        while i <= 20: #Tant que i est plus petit que 20 faire
            somme += i #Ajouter i à somme
            i += 2 #Incrémenter i de 2
        

**Exercice :** (Racine carrée entière) Ecrire un programme qui demande à l'utilisateur un nombre entier :code:`n` , qui affiche l'entier dont le carré est l'entier, inférieur ou égal, le plus proche de :code:`n`. Par exemple il affichera :code:`2` si l'utilisateur rentre :code:`7`.


.. admonition:: Solution
   :class: dropdown; tip
   
   .. code-block :: python
        
       n = int(input("Entrez un entier : "))
       i = 0 # Initialisation du compteur
       while (i+1) ** 2 <= n: #Tant que le carré du compteur i est plus petit que n faire
          i += 1 # Incrémenter i
       print(" La racine carrée entière de {} est : {}".format(n, i)

**Exercice :** Ecrire un programme qui calcule la somme des multiples de 3 ou de 5 strictement inférieurs à 1000.



.. admonition:: Solution
   :class: dropdown; tip
   
   .. ipython :: python

        i=0
        somme = 0
        while i < 1000:
            if i % 3 == 0 or i % 5 == 0:
                somme += i
            i += 1
        somme


**Exercice :** (L'algorithme des différences successives) 
	Que calcule cet algorithhme ? 
	Le modifier pour obtenir la division euclidienne de :code:`a` par :code:`b`.

	.. image:: Diag-DiffSucc.jpg
	   :height: 320px
           :width: 345px
	   :scale: 100 %
	   :align: center
		

.. admonition:: Solution
   :class: dropdown; tip

    .. code-block :: python

        q = 0
        r = a
        while b < r:
            q += 1
            r -= b
       
        

**Petit problème 1 :** 
	On définit la suite de Fibonacci par :

	.. image:: Fibo.jpg
		:height: 151px
           	:width: 518px
   		:scale: 50%
   		:align: center


	Calculer la somme des termes pairs plus petit que quatre millions.


.. admonition:: Solution
   :class: dropdown; tip

    .. ipython :: python

        a = 1
        b = 2
        somme = b
        while b <= 4*10**6:
              a, b = b, a + b
              if b % 2 == 0:
                    somme += b
        somme



Boucle :code:`for`
------------------

.. note::  La structure d'une boucle :code:`for` (*pour* en anglais) est la suivante :

		.. code-block:: python

			for element in iterable: # Pour tous les éléments de l'itérable faire :
    				instructions

	La boucle :code:`for` permet d'effectuer un bloc d'instructions pendant que :code:`element` prend successivement toutes les valeurs dans :code:`itérable` .	

	Un exemple : Avec une chaine de caractères comme itérable.

		.. code-block:: python
			
			chaine = "Vive la PTSI-B!"
			for lettre in chaine: # Pour chaque lettre dans chaine faire :
				print(lettre) # Afficher la lettre

	Notez bien que c'est la commande :code:`for` qui a crée le variable :code:`lettre`.

**Exercice :** Dans la console écrire un programme qui affiche toutes les consonnes de la chaine "Vive les TP Python en PTSI-B" et qui affiche un underscore à la place des voyelles.


.. admonition:: Solution
   :class: dropdown; tip

    .. code-block :: python

        chaine = "Vive les TP Python en PTSI-B"
        for lettre in chaine:
            if lettre not in "AEIOUYaeiouy":
                print(lettre)
            else:
                print("_")


.. note:: La fonction :code:`range` est très utile, elle génère des itérables constitués par des suites de nombres, on l'utilise comme suit :

		.. code-block:: python
			
			range(m) # Ensemble des entiers de :math:`0` à :math:`m-1`
			range(n, m) # Ensemble des entiers de :math:`n` à :math:`m-1`
 			range(n, m, p) # Ensemble des entiers de :math:`n` à :math:`m-1` par pas de :math:`p`

**Exercice :** Dans la console écrire un programme qui affiche la somme des carrés des entiers de 10 à 38, puis la somme des cubes des entiers impaires de 10 à 38, qui utilise l'expression :code:`range()`.


.. admonition:: Solution
   :class: dropdown; tip

    .. ipython :: python
    
        somme = 0
        for i in range(10,39):
            somme += i**2
        somme

        somme2 = 0
        for i in range(11,15,2):
            somme2 += i**3
        somme2


**Exercice :** Dans la console écrire un programme qui calcule :math:`5^{245}` en effectuant toutes les multiplications. Comparer avec :code:`5**245`.

.. admonition:: Solution
   :class: dropdown; tip

    .. ipython :: python

        resultat = 5
        for _ in range(1, 20):
            resultat *= resultat
        resultat

**Exercice :** Dans la console écrire un programme qui calcule :math:`50!` en effectuant toutes les multiplications. Comparer le résultat avec la fonction :code:`factorial` du module :code:`math`. Calculer la somme des décimales de ce nombre.

.. admonition:: Solution
   :class: dropdown; tip

    .. ipython :: python

        resultat = 1
        for i in range(2,51):
            resultat *= i
        resultat 
        # Première méthode
        somme = 0
        n = resultat
        while n > 0:
            somme += (n % 10)
            n = n // 10
        print("La somme des décimales est : {}".format(somme))
        # Seconde méthode
        somme2 = 0 
        chaine = str(resultat)
        for chiffre in chaine: somme2 += int(chiffre)
        somme2
        
        


Les fonctions
=============

Définition et appels
--------------------

.. note:: Une fonction permet d'appeler un groupe d'instructions à plusieurs reprises, sans avoir à le réécrire. Vous connaissez déjà un certain nombre de fonctions comme :code:`print`, :code:`input` ou encore :code:`range`.

	En Python une fonction se déclare à l'aide du mot-clé :code:`def`.

	Par exemple :
	
	.. code-block:: python
	
		def ma_fonction(arg_1,...,arg_n):
		    instruction 1
		    ...           #Les instructions forment le **corps** de la fonction.
		    instruction p
		

    Observons ce qui se passe en tapant :

        .. ipython :: python

            def double(x):
                print(2*x)
            double(5)


	Dans cet exemple la fonction :code:`double` prend un **argument**, ici appelé :code:`x`. Cet argument n'a pas de :code:`type` à priori.
	On peut essayer avec différents :code:`type` de donnée pour :code:`x` . Comme par exemple :
	
        .. ipython:: python

            double(5)
            double(5.)
            double("x")
            	

	Taper les commandes suivantes dans la console.

	.. ipython :: python

		def double_bis(x):
		     return 2*x
		 
		double_bis(2)
		n = double_bis(2)
		n # On a affecté la valeur retournée par la fonction à n
		
		m = double(2)
		m
		print(m) # Il n'y a rien dans m
		
	
	Qu'elle est la différence ?
	
	La fonction :code:`double` **affiche** le résultat, la fonction :code:`double_bis` **retourne une valeur**.
	Pour renvoyez un résultat il faut utiliser le mot-clé :code:`return`.
    
    On peut noter que la console IPython fait bien la différence.

.. danger :: Ne confondez surtout pas **afficher** et **retourner**, ou :code:`return` et :code:`print`.

	Si vous oubliez le mot-clé :code:`return`, il ne se passera rien, ou plutôt votre fonction renverra :code:`None`. 

	.. code-block:: python

		>>> def double_ter(x):
		...     2*x
		... 
		>>> double_ter(2)
		>>> print(double_ter(2))
		None
		>>> 
	
	En informatique, une fonction qui ne retourne rien s'appelle une **procédure**.
	
	

.. note:: D'après la **PEP8**, les noms de fonctions doivent être écrits en minuscules, avec des underscores si nécessaire.

.. admonition:: De bonnes pratiques !
    :class: important

    Lorsque l'on définit une fonction, il est impératif de l'accompagner d'une :code:`docstring`, c'est-à-dire d'une description de ce que fait la fonction, des arguments qu'elle prend et de ce qu'elle retourne le cas échéant (on ajoute aussi les exceptions qu'elle peut soulever mais nous verrons ça plus tard). Une dernière chose : il est d'usage d'écrire cette docstring en anglais... La `PEP-257 <https://www.python.org/dev/peps/pep-0257/>`_ décrit la bonne manière d'écrire une docstring en python, mais je préfère suivre les conseils donnés dans le `guide Google <https://google.github.io/styleguide/pyguide.html#Comments>`_.
    Voici un exemple de docstring :
    
        .. code-block :: python

            def square_root(x):
                """
                Calculate the square root of a number.

                Args:
                    x : the positive positive number to get the square root of.
                Returns:
                    the square root of x.
                Raises:
                    TypeError: if x is not a number.
                    ValueError: if x is negative.
                """

    Vous devez écrire une docstring pour chaque fonction que vous définirez !
    
    Pour aller plus loin encore, on peut utiliser les **annotations** de fonctions, ou **typing**. Il s'agit de spécifier le type des arguments passés à la fonction et de spécifier le type de ce que la fonction retourne le cas échéant de la manière suivante :
    
    .. code-block:: python
	
		def ma_fonction(arg_1:type_1,...,arg_n:type_n)->type_sortie:
        
    Par exemple pour la fonction :code:`square_root` on aurait :
    
    .. code-block:: python
    
        def square_root(x:float)->float:
        
    Notez que ce ne sont que des indications, Python ne vérifie rien et ne dira rien si vous ne respectez pas vos propres définitions. Pour en savoir plus c'est par `ici <https://docs.python.org/fr/3.10/library/typing.html>`_.

**Exercice :** Ecrire une fonction :code:`somme_n_entiers` qui prend comme argument un entier :code:`n` et qui retourne la somme des :math:`n` premiers entiers.


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python

            def somme_n_entiers(n:int)->int:
                """
                Calculate the sum of the n firsts integers

                Args: 
                    n : the last integer of the sum.
                Returns:
                    1 + ... + n.
                """
                s = 0
                for i in range(n+1):
                    s += i
                return s
                
**Exercice :** Ecrire une fonction :code:`percentage` qui prend deux nombres comme arguments :code:`score` et :code:`total` et qui retourne le pourcentage de réussite que représente :code:`score`.


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python
        
            def percentage(total:float, score:float)->float:
                """
                calculate the percentage corresponding to a grade.

                Args: 
                    total : a postive number > 0
                    score : a number 0 <= score <= total
                    
                Returns:
                    the percentage corresponding to the score obtained.
                """
                return 100*score/total
            
.. note :: Lorsque l'on écrit une fonction, on peut vouloir vérifier que des conditions qui sont **censées être satisfaites le sont effectivement**, à l'aide du mécanisme d'assertion proposé par Python.

    Par exemple, voici comment utiliser la fonction :code:`assert` pour vérifier que les préconditions de la fonction :code:`percentage` sont bien vérifiées :
    
            .. code-block :: python
                
                def percentage(total:float, score:float)->float:
                    """
                    calculate the percentage corresponding to a grade.

                    Args: 
                        total : a postive number > 0
                        score : a number 0 <= score <= total

                    Returns:
                        the percentage corresponding to the score obtained.
                    """
                    assert type(score) == float, "score must be a float number."
                    assert type(total) == float, "total must be a float number."
                    assert total > 0, "total must be strictly positive"
                    assert score >= 0, "score must be positive."
                    assert total >= score, "score must be smaller than total."
                    return 100*score/total
    
    Copiez-collez ce code et essayez le avec des préconditions non respectées, vous verrez que l'exécution du code s'interrompt avec la levée d'une exceprion de type :code:`AssertionError`, et que le message d'erreur prévu s'affiche, ce que nous n'aurions pas obtenu en utilisant des :code:`if`.
    
    Dans la vraie vie, on n''utilise des assertions qu'en phase de développement jamais en production, à moins que la fonction soit interne à un module, donc votre code doit fonctionner même si on les supprime.
    
    
    
    
    
**Exercice :** Ecrire une fonction :code:`factorielle` qui prend comme argument un entier :code:`n` et qui retourne :math:`n!`, après avoir testé que :math:`n` est bien un entier positif.


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python

            def factorielle(n:int)->int:
                """
                Calculate the factorial of n

                Args: 
                    n : the positive integer to get the factorial
                Returns:
                    1 x ... x n.
                """
                assert type(n) == int, "n must be an integer."
                assert n >= 0, "n must be positive"
                f = 1
                for i in range(1, n+1):
                    f *= i
                return f
                




**Exercice :** Ecrire une fonction :code:`syracuse1` qui prend comme argument un entier :code:`N` positif et qui retourne :math:`u_{100}` où la suite :math:`(u_k)_{k\in\mathbb{N}}` est définie par :math:`u_0 = N` et pour tout :math:`k\in\mathbb{N}`, :math:`u_{k+1} = u_k / 2`      si :math:`u_k` est pair et sinon :math:`u_{k+1}=3 u_k + 1`. Vous testerez que :code:`N`est bien un entier positif.


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python

            def syracuse1(N:int)->int:
                """
                Calculate the hundredth term of the syracuse sequence of N

                Args: 
                    N : the integer u_0 > 0
                Returns:
                    u_100
                """
                assert type(N) == int, "N must be an integer."
                assert N >=0, "N must be positive."
                u = N
                for _ in range(100):
                    if u % 2 == 0:
                        u = u // 2
                    else:
                        u = 3*u+1
                return u
   




**Exercice :** Ecrire une fonction :code:`fibo` qui prend comme argument un entier :code:`n` et qui retourne le n-ième terme de la suite de Fibonacci. Après avoir testé que :code:`n`est bien un entier positif.

.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python

            def fibo(n:int)->int:
                """
                Calculate the n-th term of the Fibonacci sequence.

                Args: 
                    n : a positive integer
                Returns:
                    u_n
                """
                assert type(n) == int, "n must be an integer."
                assert n >= 0, "n must be positive."
                u = 1
                v = 2
                for _ in range(n):
                    u, v = v, u+v
                return u

**Exercice :** Ecrire une fonction :code:`is_positive` qui prend comme argument un réel :code:`x` est qui renvoie :code:`True` si :code:`x` est positif et :code:`False` sinon. Après avoir testé que :code:`x` est bien un nombre flottant.


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python

            def is_positive(x:float)->bool:
                """
                Test if x is positive

                Args: 
                    x : the number to determine is positive or not.
                Returns:
                    True if x is positive, and False otherwise.
                """
                assert type(x) == float, "x must be a float number."
                return x >= 0


**Exercice :** Ecrire une fonction :code:`somme_dec` qui prend comme argument un entier :code:`n` positif et qui retourne la somme de ses décimales. Après avoir testé un que :code:`n` est un entier.


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python

            def somme_dec(n:int)->int:
                """
                Calculate the sum of the digits of n.

                Args: 
                    n : the number of which we will calculate the sum of the digits.
                Returns:
                    The sum of the digits of n
                """
                assert type(n) == int, "n must be an integer."
                assert n >= 0, "n must be positive."
                s = 0
                while n > 0:
                    s += n % 10
                    n //= 10
                return s
                


**Exercice :** Ecrire une fonction :code:`is_palindrome` qui prend comme argument une chaine de caractères et qui retourne :code:`True` si cette chaine est un palindrome et :code:`False` sinon. Après avoir testé que :code:`chaine`est bien une chaine de caractères de longueur supérieure ou égale à deux.


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python

            def is_palindrome(chaine:str)->bool:
                """
                Test if a string is a palindrome.

                Args: 
                    chaine : a string to test.
                Returns:
                    True if chain is a palindrome, and False otherwise.
                """
                assert type(chaine) == str, "type(chaine) must be str."
                assert len(chaine) >= 2, "len(chaine) must be greater than 2."
                i = 0
                res = True
                while res and i < len(chaine)//2:
                    if chaine[i] != chaine[-(i+1)]:
                        res = False
                    i += 1
                return res
  
.. note:: Une fonction peut renvoyer des données de tout :code:`type`.


Arguments
---------

.. note:: 

    Une fonction peut ne pas prendre d'argument ou en prendre plusieurs.

	Un exemple de fonction sans argument :

        .. code-block :: python

            def table7():
                """
                Show the 7 times table 

                Args: 
                    None
                Returns:
                    None
                """
                for i in range(11):
                    print(f"{i} * 7 = {i*7}")
            

    
    
    Avec deux ou trois arguments :

            .. code-block :: python

                    def pythagore(a, b):
                        """
                        Calculate the hypothenuse of the right triangle of legs a and b

                        Args: 
                            a : positive float
                            b : positive float
                        Returns:
                            the square of the length of the hypotenuse of the right triangle of legs a and b.
                        """
                        assert type(a) == float and type(b) == float," a and b must be float numbers."
                        assert a >= 0 and b >= 0, "a and b must be positives."
                        return a**2+b**2

                    def is_pythagore(a, b, c):
                        """
                        Determines if the triangle (a , b, c) is right at (a, b)

                        Args: 
                            a : positive float
                            b : positive float
                        Returns:
                            The square of the length of the hypotenuse of sides a and b
                        """
                        assert type(a) == float and type(b) == float," a and b must be float numbers."
                        assert a >= 0 and b >= 0, "a and b must be positives."
                        rep = False
                        if c == pythagore(a, b): # Ici on fait appelle à la fonction définie avant
                            rep = True
                        return rep

                    

**Exercice :** Ecrire une fonction :code:`somme_cube` qui prend deux entiers :code:`p` et :code:`q` comme arguments et qui retourne :math:`\displaystyle\sum_{p}^q k^3` .


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python

            def somme_cube(p:int, q:int)->int:
                """
                Calculate the sum of k^3 from p to q

                Args: 
                    p : a positive integer
                    q : a positive integer p < q
                Returns:
                    The sum of k^3 from p to q
                """
                assert type(p) == int and type(q) == int, "p and q must be integer."
                assert p >= 0, "p must be positive."
                assert q >= p, "q must be greater than p"
                s = 0
                for k in range(p,q+1):
                    s += k**3
                return s
                

**Exercice :** Ecrire une fonction :code:`max2` qui prend deux nombres réels en argument et qui retourne le maximum des deux.


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python

            def max2(x:float, y:float)->float:
                """
                Determines which of x and y is greater.

                Args: 
                    x : a float number
                    y : a float number
                Returns:
                    max(x,y)
                """
                assert type(x) == float and type(y) == float, "x and y must be float numbers."
            
                if x <= y:
                    rep = y
                else:
                    rep = x
                return rep





**Exercice :** Ecrire une fonction :code:`max3` qui prend trois nombres réels en argument et qui retourne le maximum des trois.


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python

            def max3(x:float, y:float, z:float)->float:
                """
                Determines which of x, y and z is greater.

                Args: 
                    x : a float number
                    y : a float number
                    z : a float number
                Returns:
                    max(x,y,z)
                """
                assert type(x) == float and type(y) == float and type(z) == float, "x, y and z must be float numbers."
            
                return max2(x,max2(y,z))


**Exercice :** Ecrire une fonction :code:`is_prime` qui prend comme argument un entier :code:`n` et qui retourne un booléen indiquant si :code:`n` est premier ou non.

.. admonition:: Solution
   :class: dropdown; tip

        .. ipython :: 
            :okexcept:

            In [1]: def is_prime(n:int)->bool:
               ...:     """
               ...:     Test the primality of n
               ...:     Args: 
               ...:         n : a positive integer
               ...:     Returns:
               ...:     True if n is prime, False otherwise.
               ...:     """
               ...:     assert type(n) == int, "n must be an integer."
               ...:     assert n >= 0, "n must be positive."
               ...:     rep = True
               ...:     if n in [0,1] or (n > 2 and n % 2 == 0):
               ...:         rep = False
               ...:     k = 3
               ...:     while rep and k**2 <= n:
               ...:         if n % k == 0:
               ...:             rep = False
               ...:         k += 2
               ...:     return rep
               

**Exercice :** Ecrire une fonction :code:`decompo_base` qui prend deux entiers :code:`n` et :code:`b` et qui retourne sous forme de liste la décomposition de :code:`n` dans la base :code:`b`.


.. note :: Une fonction peut prendre comme argument… une autre fonction.

   Par exemple :

    .. ipython ::

        In [1]: def cube(n:int)->int:
           ...:     """
           ...:     Calculate n**3
           ...:     Args: 
           ...:         n : an integer
           ...:     Returns:
           ...:         n**3
           ...:     """
           ...:     assert type(n) == int, "n must be an integer."
           ...:     return n**3

    Et 

    .. ipython :: 
    
        In [1]: from typing import Callable
    
        In [2]: def somme_fk(f:Callable[[int],float], p:int, q:int)->float:
           ...:    """
           ...:    Calculate the sum of f(k) for k from p to q.
           ...:    Args: 
           ...:        f : a function define on integer
           ...:        p : an integer
           ...:        q : an integer greater than p
           ...:    Returns:
           ...:        The sum of f(k) for k from p to q
           ...:    """
           ...:    assert type(p) == int and type(q) == int, "p and q must be integers numbers."
           ...:    assert p <= q, "q must be greater than p."
           ...:    somme = 0
           ...:    for i in range(p,q+1):
           ...:       somme += f(i)
           ...:    return somme
        
        In [3]: print(somme_fk(cube, 0, 4))
		
		 
**Exercice :** Ecrire une fonction :code:`produit_fk` qui prend en argument une fonction :math:`f` et deux entiers :math:`p<q` et qui retourne le produit des nombres :math:`f(k)` pour :math:`p\leq k\leq q`. Vérifiez votre résultat sur la fonction :code:`cube` et la fonction :code:`factorielle` .


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python
            
            from typing import Callable

            def produit_fk(f:Callable[[int],float], p:int, q:int)->float:
                """
                Calculate the product of f(k) for k from p to q.

                Args: 
                    f : a real function define on integer
                    p : an integer
                    q : an integer greater than p
                Returns:
                    the product of f(k) for k from p to q
                """
                assert type(p) == int and type(q) == int, "p and q must be integers numbers."
                assert p <= q, "q must be greater than p."
                
                p = 1
                for k in range(p, q+1):
                    p *= f(k)
                return p

Les lambda
----------

.. note :: Une fonction lambda est une fonction d'une seule ligne déclarée de manière anonyme (d'où le leur nom : lambda), qui peut avoir un nombre quelconque d'arguments, mais elle ne peut avoir qu'une seule expression. Il arrive souvent qu'une fonction lambda soit passée en argument à une autre fonction.


    .. ipython :: python
        :okexcept:
        
        f = lambda x, y : x + y
        f(2,3)
        f("Hello ","World!")
        
        somme_fk(lambda x : x**3, 0, 4)
        








Types de données composées
==========================


Les listes
----------

.. note:: Vous avez déjà vu comment créer une liste :

	Par la description de ses éléments :

	.. ipython:: python
	
		liste1 = ['a',128,'Bob',3.14]
		liste1
		

	Par concaténation ou multiplication d'un ou plusieurs blocs :
	
	.. ipython:: python

		liste2 = liste1 + liste1
		liste2
		liste3 = liste1 * 3
		liste3
		

	On peut aussi les définir en **compréhension** : 

        .. ipython :: python
        
            liste4 = [i**2 for i in range(5)]
            liste4
            liste5 = [1 for i in range(5)]
            liste5
            liste6 = [2*i+1 for i in range(-3,6) if i % 4 != 0]        
            liste6
            liste7 = [k for k in range(30) if is_prime(k)]
            liste7
        

	Notez bien la puissance de cette manière de définir une liste.

**Exercice :** Créer une liste :code:`liste1` dont les éléments sont les cubes des entiers compris entre :math:`-10` et :math:`20` qui ne sont ni multiples de :math:`2` ni de  :math:`3` .


.. admonition:: Solution
   :class: dropdown; tip
   
    .. ipython :: python
    
        [k**3 for k in range(-10,21) if (k % 2 != 0 and k % 3 != 0)]
   

**Exercice :** En utilisant la fonction :code:`randint` du module :code:`random`, créer une liste de :math:`20` nombres entiers aléatoires compris entre :math:`-100` et :math:`100`.

.. admonition:: Solution
   :class: dropdown; tip
   
    .. ipython :: python
        
        from random import randint
        [randint(-100,100) for _ in range(20)]


.. note :: 
    Une liste est une collection ordonnées d’objets séparés par des virgules et encadrée par des crochets.
    
    Par exemple :
    
    .. ipython :: python
        
        l1 = ['a',1]
        l2 = [1,'a']
        l1 == l2
        

    Pour obtenir la longueur d'une liste on utilise la fonction :code:`len`.
    
    .. ipython :: python
        
        l3 = [1,'a',3.14]
        len(l3)
    
    Pour accéder aux éléments d'une liste on utilise son indice (attention on commence à :math:`0`) :
    
    .. ipython :: python
        
        l3[0]
        l3[1]
        l3[2]
        
    Les listes sont itérables, en particulier on peut les parcourir avec une boucle :code:`for`:
    
    .. ipython :: python
    
        for i in range(len(l3)):
            print(l3[i])
            
    On peut obtenir une tranche (un slice) d'une liste :
    
    .. ipython :: python
    
        l = list(range(21))
        l[2:7]
        l[::3]
        l[1:20:5]
        
    Les listes sont mutables (on peut les modifier) :
    
    .. ipython :: python
        :okexcept:
        
        l = [1,2]
        l[0] = 3
        l
        
    On peut tester l'appartenance d'un élément à une liste :code:`l` grâce à l'expression :code:`x in l`.
    
    .. ipython :: python
    
        l = [1,2,'coucou']
        1 in l
        'coucou' in l
        3 in l


**Exercice :** Essayer les méthodes :code:`append`, :code:`extend`, :code:`count`, :code:`insert`, :code:`remove`, :code:`reverse` et :code:`sort`, après avoir lu leur documentation grâce à :code:`help(list)`.


**Exercice :** Ecrire une fonction une fonction :code:`swap(l:list, i:int, j:int)` qui ne retourne rien, mais qui échange dans la liste :code:`l` les éléménts en position :code:`i` et :code`j` , après avoir vérifié que :code:`i`et :code:`j` sont des indices valables.



.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python

            def swap(l:list, i:int, j:int):
                """
                Swap l[i] and l[j] if it's possible.

                Args: 
                    l : a real function define on integer
                    i : an integer
                    j : an integer 
                Returns:
                    Nothing
                """
                assert type(i) == int and type(j) == int, "i and j must be integers"
                assert 0 <= i < len(l) and 0 <= j < len(l),"i and j must be in range 0, len(l)-1
                
                l[i], l[j] = l[j], l[i]
                
**Exercice :** Ecrire une fonction :code:`is_in(elt:Any, l:list)->bool` qui teste si :code:`elt` est ou non dans la liste :code:`list`. (Sans utiliser :code:`in`).


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python
            
            from typing import Any
            
            def is_in(elt:Any, l:list)->bool:
                """
                Test if elt is in l.

                Args: 
                    elt : an element
                    l   : a list 
                Returns:
                    True if elt in l, False otherwise.
                """
                
                rep = False
                i = 0
                while i < len(l) and not rep:
                    if l[i] == elt:
                        rep = True
                    i += 1
                return rep
            
                
**Exercice :** Ecrire une fonction :code:`positions(elt:Any, l:list)->list` qui retourne la liste, éventuellement vide des indices des occurences de :code:`elt` dans la liste :code:`l`.


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python
            
            from typing import Any
            
            def positions(elt:Any, l:list)->list:
                """
                Find positions of elt in l.

                Args: 
                    elt : an element
                    l   : a list 
                Returns:
                    The list of indices of the positions of elt in the list l.
                """
                
                rep = []
                i = 0
                while i < len(l):
                    if l[i] == elt:
                        rep.append(i)
                    i += 1
                return rep
                
**Exercice :** Ecrire une fonction :code:`maximum(l:list[float])->list` qui retourne la liste formé du maximum de la liste de nombres :code:`list` et de l'indice de la première position de ce maximum dans la liste.



.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python
            
            def maximum(l:list[float])->(float, int):
                """
                Find the maximum of the list l and his first position.

                Args: 
                    l   : a list of float.
                Returns:
                    the tuple (max, ind_max)
                """
                
                max_tmp = l[0]
                max_ind = 0
                i = 0
                while i < len(l):
                    if l[i] > max_tmp:
                        max_tmp = l[i]
                        max_ind = i
                    i += 1
                return (max_tmp, max_ind)



    

**Exercice :** Ecrire une fonction :code:`is_increasing(l:list[float])->bool` qui teste si une fonction est croissante ou non et retourne le booléen correspondant.


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python
            
            def is_increasing(l:list[float])->bool:
                """
                Test if a list of float is increasing

                Args: 
                    l   : a list of float.
                Returns:
                    True if l is increasing, False otherwise.
                """
                
                rep = True
                i = 0
                while rep and i < len(l)-1:
                    if l[i+1] < l[i]:
                        rep = False
                return rep

**Exercice :** Ecrire une fonction :code:`largest_growing_sub_list(l:list[int])->list[int]` qui retourne la plus longue sous-liste croissante, constituée de termes consécutifs, d'une liste passée en argument.



.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python

            def largest_growing_sub_list(l:list[int])->list[int]:
                """
                Find the largest increasing sublist in l.

                Args: 
                    l   : a list of int.
                Returns:
                    The largest increasing sublist in l.
                """
                rep1 = [l[0]]
                rep2 = []
                for i in range(1,len(l)):
                      if len(rep1) == 0 or rep1[-1] <= l[i]:
                            rep1.append(l[i])
                      elif len(rep2) < len(rep1):
                          rep2 = rep1
                          rep1 = []
                      else:
                          rep1 = []
                return rep1


**Exercice :** Ecrire une fonction qui teste si une liste :code:`liste1` se trouve dans une autre liste :code:`liste2` à la position :code:`n`. On n'utilisera pas de slicing mais un test de correspondance élément par élément.


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python

            def is_sublist(l1:list[Any], l2:list[Any], n:int)->bool:
                """
                Test if l2 is a sub_list of l1 at position n.

                Args: 
                    l1 : a list.
                    l2 : a list
                    n  : an int
                Returns:
                    True if l2 is a sublist of l1 at position n, False othewise.
                """
                if len(l2) + n > len(l1):
                    rep = False
                else:
                    rep = True
                    i = n
                    while rep and i < n + len(l2) - 1:
                        if l1[i] == l2[i-n]:
                            i += 1
                        else:
                           rep = False
                return rep 



**Exercice :** Ecrire une fonction :code:`positions_dans_liste` qui retourne la liste des positions d'une sous liste :code:`liste1` dans une liste :code:`liste2`.


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python

            def positions_sublist(l1:list[Any], l2:list[Any])->list[int]:
                """
                Determine the list of positions of l2 as a sublist of l1.

                Args: 
                    l1 : a list.
                    l2 : a list
                Returns:
                    List of positions of l2 as sublist of l1.
                """
                rep = []
                for i in range(len(l1)-len(l2)):
                    if is_sublist(l1,l2,i):
                        rep.append(i)
                return rep 



**Exercice :** Ecrire une fonction :code:`del_n_return(l:list[Any],i:int)->list[Any]` qui retourne supprime l'élément d'indice :code:`i` dans la liste et le retourne. On n'utilisera pas la méthode :code:`pop`.


.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python
            
            def del_n_return(l:list[Any], i:int)->list[Any]:
                """
                Removes the item at the given index from the list and returns the removed item.

                Args: 
                    l   : a list.
                    i   : an int.
                Returns:
                    l[i] after delete it in l.
                """
                
                rep = l[i]
                l = l[:i] + l[i+1:]
                return rep
                
                
                
**Exercice :** Ecrire une fonction :code:`nth_max(l:list[float], n:int)->float` qui retourne le n-ième plus grand élément de :code:`l`, après avoir testé que :code:`l` contient assez d'éléments. Vous n'utiliserez pas les méthodes :code:`sort` ou :code:`index`, mais vous utiliserez les fonctions :code:`del_n_return` et :code:`maximum` que vous avez codé plus haut.

.. admonition:: Solution
   :class: dropdown; tip

        .. code-block :: python
            
            def nth_max(l:list[float], n:int)->float:
                """
                Determines the n-th largest number of l.

                Args: 
                    l   : a list of float.
                Returns:
                    The n-th largest number of l.
                """
                
                assert n < len(l), "n is too large."
                lmax = []
                while len(lmax) < n:
                    lmax.append(del_n_return(l,maximum(l)[1]))
                return lmax[len(lmax)-1]
                   
                

**Exercice :** Ecrire une fonction :code:`filtre(l:list[int], test:Callable[[int], bool])->list[int]` qui retourne la liste des éléments :code:`elt` de la liste :code:`l` pour lesquels :code:`test(elt)` est :code:`True`.

.. admonition:: Solution
   :class: dropdown; tip
   
    .. code-block:: python
        
        def filtre(l:list[int], test:Callable[[int], bool])->list[int]:
            """
            Selecte element of l which verify test(elt) == True
            
            Args:
                l      : a list of int
                test   : a function 
            Returns:
                The list of elements of l for which test is true.
            """
            rep = []
            for elt in l:
                if test(elt):
                    rep.append(elt)
                    
            return rep

    La bonne alternative en Python3 
    
    .. code-block:: python
    
        [elt in l if test(elt)]
         



Les tuples
----------

.. note :: 
    Un n-uplet ou tuple est une collection ordonnées d’objets séparés par des virgules et encadrée par des parenthèses.
    
    Par exemple :
    
    .. ipython :: python
        
        t1 = ('a',1)
        t2 = (1,'a')
        t1 == t2
        

    Pour obtenir la longueur d'un tuple on utilise la fonction :code:`len`.
    
    .. ipython :: python
        
        t3 = (1,'a',3.14)
        len(t3)
    
    Pour accéder aux éléments d'un tuple on utilise son indice (attention on commence à :math:`0`) comme pour le listes :
    
    .. ipython :: python
        
        t3[0]
        t3[1]
        t3[2]
        
    Les tuples sont itérables, en particulier on peut les parcourir avec une boucle :code:`for`:
    
    .. ipython :: python
    
        for i in range(len(t3)):
            print(t3[i])
            
    On peut obtenir une tranche (un slice) d'un tuple :
    
    .. ipython :: python
    
        t = tuple(range(21))
        t[2:7]
        t[::3]
        t[1:20:5]
        
    Contrairement aux listes, les tuples sont non-mutables :
    
    .. ipython :: python
        :okexcept:
        
        t = (1,2)
        t[0] = 3
        
    On peut tester l'appartenance d'un élément à un tuple :code:`t` grâce à l'expression :code:`x in t`.
    
    .. ipython :: python
    
        t = (1,2,'coucou')
        1 in t
        'coucou' in t
        3 in t

**Exercice :** Ecrire une fonction :code:`copy_tuple(t:tuple)->tuple` qui retourne un tuple copie du tuple :code:`t` en utilisant une liste.

.. admonition:: Solution
   :class: dropdown; tip
   
    .. code-block:: python
        
        def copy_tuple(t:tuple)->tuple:
            """
            Return a copy of the tuple t.
            
            Args:
                t : the tuple to copy
            Returns:
                a copy of the tuple t
            """
            tmp_list = []
            for elt in t:
                tmp_list.append(elt)
                
            return tuple(tmp_list)
                
        




**Exercice :** Ecrire une fonction :code:`indice(elt:Any, t:tuple)->int` qui retourne l'indice de la première occurence de :code:`elt` dans :code:`t`, si elle existe et :code:`-1` sinon.

.. admonition:: Solution
   :class: dropdown; tip
   
    .. code-block:: python
        
        def indice(elt:Any, t:tuple)->int:
            """
            Return the index of elt in tuple.
            
            Args:
                elt : an element
                t   : a tuple
            Returns:
                the index of elt in t if exists, or -1.
            """
            if not elt in t:
                rep = -1
            else:
                rep = 0
                while t[rep] != elt:
                    rep += 1
            return rep
            



**Exercice :** Ecrire une fonction :code:`nb_occurences(elt:Any, t:tuple)->int` qui retourne le nombre d'occurence de l'élément :code:`elt` dans le tuple :code:`tuple`.

.. admonition:: Solution
   :class: dropdown; tip
   
    .. code-block:: python
        
        def nb_occurences(elt:Any, t:tuple)->int:
            """
            Count the number of occurrences of elt in t.
            
            Args:
                elt : an element
                t   : a tuple
            Returns:
                The number of occurrences of elt in t.
            """
            rep = 0
            if elt in t:
                for e in t:
                    if e == elt:
                        rep += 1
            return rep
            

**Exercice :** Ecrire une fonction :code:`mdlast(l:list[tuple[int]],val:int)->list[tuple[int]]` qui prend comme arguments une liste de tuples d'entiers et une valeur, et qui retourne la même liste de tuples après avoir remplacer le dernier élément de chaque tuple par la valeur.



.. admonition:: Solution
   :class: dropdown; tip
   
    .. code-block:: python
        
        def mdlast(l:list[tuple[int]], val:int)->list[tuple[int]]:
            """
            Change the last value of each tuple in list by val.
            
            Args:
                l    : a list of tuple of int
                val  : a int
            Returns:
                The same list where the last value of each tuple is val.
            """
            
  
        
**Petit problème 2 :** 
	Dans cet exercice, on cherche une approximation de :math:`\pi` par une
	méthode de Monte-Carlo qui consiste à:

	* tirer aléatoirement et uniformément un point M de coordonnées :math:`(x,y)` dans le carré unité :math:`(x,y) \in [0,1[^2`

	* déterminer si le point se trouve dans le quart de cercle de rayon
	  unité :math:`x^2 + y^2 \leq 1`

	* lancer cette expérience un grand nombre de fois et évaluer le ratio
	  entre le nombre de points dans le quart de cercle et le nombre total de
	  points. Ce ratio tend vers :math:`\displaystyle\frac{\pi}{4}`.


	Pour cela, on utilisera la fonction :code:`random.random()` qui permet de générer 	pseudo-aléatoirement un nombre
	entre 0 et 1. Elle est accessible après avoir fait :code:`import random`. 


.. admonition:: Solution
   :class: dropdown; tip

    .. ipython :: python

        import random
        import math

        M = 10**3
        echantillons_dans_le_cercle = 0
        for (x,y) in ((random.random(), random.random()) for i in range(M)):
            if x**2+y**2 <= 1:
                echantillons_dans_le_cercle += 1

        print("Estimation de pi/4 ({}) : {}".format(math.pi/4.0,echantillons_dans_le_cercle/M))



.. note:: L'avantage d'un tuple sur une liste est qu'il est `hashable <https://docs.python.org/3/glossary.html#term-hashable>`_ .


Les dictionnaires
-----------------


.. note:: Les dictionnaires sont des tableaux associatifs qui associent à chaque clef une valeur. Les clefs comme les valeurs peuvent être hétérogènes (i.e. de type différents). Seule restriction les clefs doivent être des objets hashables, donc non mutables, en particulier pas des listes ou des ensembles.

    On définit des dictionnaire entre accolades et en déclarant les couples clef-valeur comme suit :

    .. ipython :: python
    
        dict1 = {'bananes': 4, 'citrons': 2.5, 'pamplemousses' : 'beaucoup', 3 : [1,2,3]}
    
    On accède aux différentes valeurs à l'aide de leur clef :
    
    
    .. ipython :: python
        :okexcept:
    
        dict1['bananes']
        dict1['citrons']
        dict1['pamplemousses']
        dict1[3]
    
    Que se passe-til si l'on charche à accéder à une valeur pour une clef qui n'existe pas :
    
    .. ipython :: python
        :okexcept:
        
        dict1['cerises']
        
    On peut éviter cela en utilisant la méthode :code:`get` :
    
    .. ipython :: python
        :okexcept:
        
        # Comme second argument on donne une valeur qui sera retournée si la clef est absente.
        dict1.get('cerises', "Il n'y en a pas")
        
        dict1.get('cerises',0)
        
    On obtient la longueur d'un dictionnaire avec :code:`len`:
    
    .. ipython :: python 
        :okexcept:
        
        len(dict1)
        
        
    Il est possible d'accèder aux clefs et aux valeurs en utilisant les méthodes :code:`keys` et :code:`values` :
    
    .. ipython :: python
        :okexcept:
    
        dict1.keys()
        dict1.values()
        
    Il est possible d'itérer sur les clefs et/ou les valeurs :
    
    .. ipython :: python
        :okexcept:   
        
        for key in dict1.keys(): print(dict1[key])
        for val in dict1.values(): print(val)
        # Plus simplement 
        for val in dict1: print(val)
        for k, v in dict1.items(): print(k, v)
        
    Les dictionnaires sont mutables :
    
    .. ipython :: python
    
        # On peut modifier une valeur :
        dict1['bananes'] = 6
        dict1
        # On peut éliminer un coupl clef-valeur :
        dict1.pop('pamplemousses') # Comme pour la méthode de liste l'entrée est retournée.
        dict1
        # On peut ajouter un couple clef-valeur :
        dict1['pommes'] = 10
        dict1
    
    Il est possible de définir une dictionnaire en compréhension comme pour les listes :
    
    .. ipython :: python
        
        dict2 = { x : x**3 for x in range(5)}
        dict2
    
    Comme pour les tuples et les listes on peut tester l'appartenance d'une clef avec :code:`in` :
    
    .. ipython :: python
        :okexcept:
        
        3 in dict2
        
        
    Parmi les choses intéressantes avec les dictionnaires il y l':code:`unpacking` dont le principe est illustré ci-dessous :
    
    .. ipython :: python 
        :okexcept:
        
        def prod(a,b):
            return a*b
    
    .. ipython :: python
    
        dict3 = {'a' : 2, 'b' : 3}
        # On utilise ** pour "unpacker" le dictionnaire :
        prod(**dict3)
        
    Pour tout savoir sur les dictionnaires c'est `ici <https://docs.python.org/3/tutorial/datastructures.html>`_ .
    

**Exercice :** Ecrire une fonction :code:`find_key(d:dict, val:Any)->Any` qui recherche la ou les clefs associées à la valeur val dans le dictionnaire :code:`d` et en retourne la liste, et :code:`None` si  il n'y a aucune clef.


.. admonition:: Solution
   :class: dropdown; tip
   
    .. code-block:: python
        
        def find_key(d:dict, val:Any)->Any:
            """
            Find keys of value = val.
            
            Args:
                d   : a dict
                val : a value
            Returns:
                The list of keys of d of value = val.
            """
            
            rep = []
            for k, v in d.items():
                if v == val:
                    rep.append(k)
            if len(rep) == 0:
                rep = None
            return rep
            

**Exercice :** Ecrire une fonction :code:`nb_occurences2(s:str)->dict` qui prend une chaine de cractères en argument et qui retourne sous forme d'un dictionnaire le nombre d'occurence de chaque lettre qui apparait dans :code:`s`.

.. admonition:: Solution
   :class: dropdown; tip
   
    .. code-block:: python
        
        def nb_occurences2(s:str)->dict:
            """
            Determine the number of occurencies of each character in string s.
            
            Args:
                s   : a string
            Returns:
                The dict of occurencies of each character in s.
            """
            
            occ = {}
            for c in s:
                occ[c] = occ.get(c,0) + 1
            return occ
            

**Exercice :** Pour la classe de PTSI-B on dispose d'un dictionnaire dont les clefs sont les noms des étudiants et les valeurs des listes de notes (pas nécessairement de même longueur). Ecrire une fonction :code:`average(d:dict)->dict` qui retourne un dictionnaire dont les clefs sont les noms des étudiants et les valeurs leurs moyennes.


.. admonition:: Solution
   :class: dropdown; tip
   
    .. code-block:: python
        
        def average(d:dict)->dict:
            """
            Calculate averages of students.
            
            Args:
                d   : a dict
            Returns:
                The dict of averages.
            """
            
            ave = {}
            for student in d:
                notes = d[student]
                if len(notes) > 0:
                    s = 0
                    for note in notes:
                        s += note
                    m = s/len(notes)
                    ave[student] = m
                else:
                    ave[student] = 'Non noté'
                
            return ave
     

**Exercice :** Ecrire une fonction :code:`matching_score(d1:dict, d2:dict)->int` qui prend comme argument deux dictionnaires :code:`d1` et :code:`d2` et qui comptabilise le score de correspondances entre le premier et le second de la manière suivante : pour chaque clef :code:`key` de :code:`d1`, si :code:`key` est une clef de :code:`d2` on ajoute 3 au score si les valeurs correspondantes sont les mêmes, -2 si elle diffèrent, enfin si la clefs n'est pas présente dans :code:`d2` on ajoute -1.

.. admonition:: Solution
   :class: dropdown; tip
   
    .. code-block:: python
        
        def matching_score(d1:dict, d2:dict)->int:
            """
            Calculate the matching's score of d1 and d2.
            
            Args:
                d1 : a dict
                d2 : a dict to score the matching with d1  
            Returns:
                The matching's score of d2.
            """
            
            score = 0
            for k, v in d1.items():
                if not k in d2:
                    score += -3
                elif v == d2[k]:
                    score += 3
                else:
                    score += -3
                
            return score
  
