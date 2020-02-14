class Note:

    # Instantiation
    def __init__(self, numero, code, note):
        """
            :param numero: numéro de l’étudiant
            :param code: code du cours
            :param note: note de l'étudiant dans ce cours
            :return: None
        """
        self.numero_Etud = numero
        self.code_Cours = code
        self.note = note

    def __str__(self):
        return f"Note de l'étudiant {self.numero_Etud} dans le cours {self.code_Cours} est: {self.note}"
