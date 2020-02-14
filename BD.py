from Etudiant import Etudiant
from Cours import Cours
from Note import Note

from functools import reduce

class BD:

    # Instantiation
    def __init__(self):
        self.liste_Etudiants = []
        self.liste_Cours = []
        self.liste_Notes = []
    
    def ajouter_Etudiant(self, etudiant):
        """
            :param etudiant: ajoute cet étudiant dans la liste des étudiants
            :return: None
        """
        assert isinstance(etudiant, Etudiant), "etudiant doit être un Etudiant !"
        self.liste_Etudiants.append(etudiant)

    def supprimer_Etudiant(self, etudiant):
        """
            :param etudiant: supprime cet étudiant de la liste des étudiants 
            :return: None
        """
        assert etudiant in self.liste_Etudiants, "etudiant doit être dans la BD !"
        self.liste_Etudiants.remove(etudiant)
    
    def editer_Etudiant(self, etudiant, prenom=None, nom=None, niveau=None):
        """
            Il suffit de supprimer etudiant, éditer ses valeurs puis l'ajouter de nouveau à la BD
            :param etudiant: Etudiant à éditer
            :param prenom: nouveau prénom de l'étudiant
            :param nom: nouveau nom de l'étudiant
            :param niveau: nouveau niveau de l'étudiant
            :return: None
        """
        self.supprimer_Etudiant(etudiant)
        if prenom is not None:
            etudiant.prenom_Etud = prenom
        if nom is not None:
            etudiant.nom_Etud = nom
        if niveau is not None:
            etudiant.niveau_Etud = niveau
        self.ajouter_Etudiant(etudiant)
    
    def ajouter_Cours(self, cours):
        """
            :param cours: ajoute ce cours dans la liste des cours
            :return: None
        """
        assert isinstance(cours, Cours), "cours doit être un Cours !"
        self.liste_Cours.append(cours)
    
    def supprimer_Cours(self, cours):
        """
            :param cours: supprime ce cours de la liste des cours
            :return: None
        """
        assert cours in self.liste_Cours, "cours doit être dans la BD !"
        self.liste_Cours.remove(cours)
    
    def editer_Cours(self, cours, intitule=None, niveau=None):
        """
            Il suffit de supprimer cours, éditer ses valeurs puis l'ajouter de nouveau à la BD
            :param cours: Cours à éditer
            :param intitule: nouveau intitulé du cours
            :param niveau: nouveau niveau du cours
            :return: None
        """
        self.supprimer_Cours(cours)
        if intitule is not None:
            cours.intitule_Cours = intitule
        if niveau is not None:
            cours.niveau_Cours = niveau
        self.ajouter_Cours(cours)

    def ajouter_Note(self, note):
        """
            :param note: ajoute cette note dans la liste des notes
            :return: None
        """
        assert isinstance(note, Note), "note doit être une Note !"
        assert self.verifier_Numero(note.numero_Etud) and self.verifier_Code(note.code_Cours), "numero_Etud et/ou code_Cours n'exite pas dans la BD !"
        self.liste_Notes.append(note)

    def verifier_Numero(self, numero_Etud):
        """
            :param numero_Etud: identifiant de l'étudiant à chercher
            :return: True si l'identifiant de l'étudiant est trouvé, False sinon
        """
        for obj in self.liste_Etudiants:
            if(obj.numero_Etud == numero_Etud):
                return True
        return False

    def verifier_Code(self, code_Cours):
        """
            :param code_Cours: code du cours à chercher
            :return: True si le code du cours est trouvé, False sinon
        """
        for obj in self.liste_Cours:
            if(obj.code_Cours == code_Cours):
                return True
        return False

    def supprimer_Note(self, note):
        """
            :param note: supprime cette note de la liste des notes
            :return: None
        """
        assert note in self.liste_Notes, "note doit être dans la BD !"
        self.liste_Notes.remove(note)

    def editer_Note(self, note, val_Note=None):
        """
            Il suffit de supprimer note, éditer ses valeurs puis l'ajouter de nouveau à la BD
            :param note: Note à éditer
            :param val_Note: nouvelle note
            :return: None
        """
        self.supprimer_Note(note)
        if val_Note is not None:
            note.note = val_Note
        self.ajouter_Note(note)

    # Première version: Paradigme impératif

    def moyenne_Classe(self, cours):
        """
            Il s'agit de trouver la moyenne des notes dans un cours donné
            :param: cours: Cours à chercher sa moyenne des notes
            :return: la moyenne des notes dans le cours
        """
        somme_Notes = []
        for notes in self.liste_Notes:
            if (notes.code_Cours == cours.code_Cours):
                somme_Notes.append(notes.note)
        if somme_Notes:
            return sum(somme_Notes) / len(somme_Notes)
        else:
            return 0

    def moyenne_Etudiant(self, etudiant):
        """
            :param: etudiant: Etudiant à chercher sa moyenne des notes
            :return: la moyenne des notes de l'étudiant
        """
        somme_Notes = []
        for notes in self.liste_Notes:
            if (notes.numero_Etud == etudiant.numero_Etud):
                somme_Notes.append(notes.note)
        if somme_Notes:
            return sum(somme_Notes) / len(somme_Notes)
        else:
            return 0

    def consulter_Notes_Classe(self, cours):
        """
            Il s'agit de consulter les notes dans un cours donné
            :param cours: Cours à consulter ses notes
            :return: toutes les notes dans ce cours
        """
        notes_Classes = "Les notes dans le cours " + str(cours.intitule_Cours) + ": "
        for notes in self.liste_Notes:
            if(notes.code_Cours == cours.code_Cours):
                notes_Classes = notes_Classes + "\nNuméro de l'étudiant: " + str(notes.numero_Etud) + "\tNote: " + str(notes.note)
        return notes_Classes
    
    def consulter_Notes_Etudiant(self, etudiant):
        """
            :param etudiant: Etudiant à consulter ses notes
            :return: toutes les notes de l'étudiant
        """
        notes_Etudiant = "Les notes de " + etudiant.nom_Etud + " " + etudiant.prenom_Etud + ":"
        for notes in self.liste_Notes:
            if(notes.numero_Etud == etudiant.numero_Etud):
                notes_Etudiant = notes_Etudiant + "\nCode du cours: " + str(notes.code_Cours) + "\tNote: " + str(notes.note)
        return notes_Etudiant

    # Seconde version: Paradigmme filter-map-reduce

    def moyenne_Classe_SV(self, cours):
        """
            filter est utilisée pour extraire les Notes des étudiants dans le cours en paramètre
            map est utilisée pour séléctionner les valeurs des Notes
            reduce est utilisée pour calculer la sommes des notes
            filter et map sont des Lazy evaluations
             
            :param: cours: Cours à chercher sa moyenne des notes
            :return: la moyenne des notes dans le cours
        """
        Notes_Cours = list(filter(lambda notes: notes.code_Cours == cours.code_Cours, self.liste_Notes))
        valeurs = list(map(lambda Note: Note.note, Notes_Cours))
        return (reduce(lambda note1, note2: note1 + note2, valeurs) / len (valeurs)) if valeurs else 0

    def moyenne_Etudiant_SV(self, etudiant):
        """
            filter est utilisée pour extraire les Notes de l'étudiant en paramètre
            map est utilisée pour séléctionner les valeurs des Notes
            reduce est utilisée pour calculer la sommes des notes
            filter et map sont des Lazy evaluations

            :param: etudiant: Etudiant à chercher sa moyenne des notes
            :return: la moyenne des notes de l'étudiant
        """
        Notes_Etudiant = list(filter(lambda notes: notes.numero_Etud == etudiant.numero_Etud, self.liste_Notes))
        valeurs = list(map(lambda Note: Note.note, Notes_Etudiant))
        return (reduce(lambda note1, note2: note1 + note2, valeurs) / len (valeurs)) if valeurs else 0

    def consulter_Notes_Classe_SV(self, cours):
        """
            filter est utilisée pour extraire les Notes du cours en paramètre
            reduce est utilisée pour concatener les valeurs des notes

            Il s'agit de consulter les notes dans un cours donné
            :param cours: Cours à consulter ses notes
            :return: les notes dans ce cours
        """
        def notes_Classes(Notes):
            """
                :param Notes: Notes du cours en paramètre
                :return: les notes dans ce cours
            """
            return reduce(lambda x, y: f"{x}\nNuméro de l'étudiant: {y.numero_Etud}\tNote: {y.note}", Notes, "Les notes dans le cours " + str(cours.intitule_Cours) + ":")

        Notes_Cours = list(filter(lambda notes: notes.code_Cours == cours.code_Cours, self.liste_Notes))
        return f"""{notes_Classes(Notes_Cours)}"""

    def consulter_Notes_Etudiant_SV(self, etudiant):
        """
            filter est utilisée pour extraire les Notes de l'étudiant en paramètre
            reduce est utilisée pour concatener les valeurs des notes

            :param etudiant: Etudiant à consulter ses notes
            :return: toutes les notes de l'étudiant
        """
        def notes_Etudiants(Notes):
            """
                :param Notes: Notes de l'étudiant en paramètre
                :return: les notes de cet étudiant
            """
            return reduce(lambda x, y: f"{x}\nCode du cours: {y.code_Cours}\tNote: {y.note}", Notes, "Les notes de " + etudiant.nom_Etud + " " + etudiant.prenom_Etud + ":")

        Notes_Etudiants = list(filter(lambda notes: notes.numero_Etud == etudiant.numero_Etud, self.liste_Notes))
        return f"""{notes_Etudiants(Notes_Etudiants)}"""