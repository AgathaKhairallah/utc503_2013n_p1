class Cours:

    # Instantiation
    def __init__(self, code, intitule, niveau):
        """
            :param code: code du cours
            :param intitule: intitulé du cours
            :param niveau: niveau du cours (A, B ou C)
            :return: None
        """
        assert niveau == 'A' or niveau == 'B' or niveau == 'C', "Niveau du cours doit être: A, B ou C"
        self.code_Cours = code
        self.intitule_Cours = intitule
        self.niveau_Cours = niveau

    def __str__(self):
        return f"{self.intitule_Cours}\t Code: {self.code_Cours}\tNiveau: {self.niveau_Cours}"