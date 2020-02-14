class Etudiant:

    # Instantiation
    def __init__(self, numero, prenom, nom, niveau):
        """
            :param numero: numéro de l'étudiant
            :param prenom: prénom de l'étudiant
            :param nom: nom de l'étudiant
            :param niveau: niveau de l'étudiant (cyle d’inscription A, B ou C)
            :return: None
        """
        assert niveau == 'A' or niveau == 'B' or niveau == 'C', "Niveau de l'étudiant doit être: A, B ou C"
        self.numero_Etud = numero
        self.prenom_Etud = prenom
        self.nom_Etud = nom
        self.niveau_Etud = niveau
        
    def __str__(self):
        return f"{self.nom_Etud} {self.prenom_Etud}\tNuméro: {self.numero_Etud}\tNiveau: {self.niveau_Etud}"
  