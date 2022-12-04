import csv

with open('note.csv') as fichier:
     lire = csv.reader(fichier)
     for ligne in lire:
          print(ligne)
