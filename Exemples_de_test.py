from Etudiant import Etudiant
from Cours import Cours
from Note import Note
from BD import BD

from functools import reduce

# Instances d'Etudiant
Etudiant_1 = Etudiant(1, 'William', 'Charles', 'A')
Etudiant_2 = Etudiant(2, 'David', 'Michael', 'B')
Etudiant_3 = Etudiant(3, 'Patricia', 'Smith', 'C')

# Instances de Cours
Cours_1 = Cours('NFA004', 'Architecture des machines', 'A')
Cours_2 = Cours('NFA008', 'Automates', 'B')
Cours_3 = Cours('NFA010', 'Graphes et optimisation', 'C')

# Instances de Notes
Note_1 = Note(1, 'NFA004', 15)
Note_2 = Note(1, 'NFA008', 10)
Note_3 = Note(1, 'NFA010', 8)

Note_4 = Note(2, 'NFA004', 13)
Note_5 = Note(2, 'NFA008', 12)
Note_6 = Note(2, 'NFA010', 17)

Note_7 = Note(3, 'NFA004', 7)
Note_8 = Note(3, 'NFA008', 11)
Note_9 = Note(3, 'NFA010', 14)

# Instance de BD
db = BD()

# Application des méthodes

# Ajouter les étudiants à la BD
db.ajouter_Etudiant(Etudiant_1)
db.ajouter_Etudiant(Etudiant_2)
db.ajouter_Etudiant(Etudiant_3)

# Ajouter les cours à la BD
db.ajouter_Cours(Cours_1)
db.ajouter_Cours(Cours_2)
db.ajouter_Cours(Cours_3)

# Ajouter les notes à la BD
db.ajouter_Note(Note_1)
db.ajouter_Note(Note_2)
db.ajouter_Note(Note_3)

db.ajouter_Note(Note_4)
db.ajouter_Note(Note_5)
db.ajouter_Note(Note_6)

db.ajouter_Note(Note_7)
db.ajouter_Note(Note_8)
db.ajouter_Note(Note_9)

# Editer le prenom de l'Etudiant_1 de la BD
db.editer_Etudiant(Etudiant_1, 'Louis')

# Editer l'intitulé du Cours_2 de la BD
db.editer_Cours(Cours_2, 'Bases de données')

# Editer note de Note_7 de la BD
db.editer_Note(Note_7, 10)

print("Première version: Paradigme impératif")

# Calcul des moyennes
print(db.moyenne_Classe(Cours_3))
print(db.moyenne_Etudiant(Etudiant_1))

# Consulter les notes
print(db.consulter_Notes_Classe(Cours_2))
print(db.consulter_Notes_Etudiant(Etudiant_3))

print("\nSeconde version: Paradigmme filter-map-reduce")

# Calcul des moyennes 
print(db.moyenne_Classe_SV(Cours_3))
print(db.moyenne_Etudiant_SV(Etudiant_1))

# Consulter les notes
print(db.consulter_Notes_Classe_SV(Cours_2))
print(db.consulter_Notes_Etudiant_SV(Etudiant_3))


