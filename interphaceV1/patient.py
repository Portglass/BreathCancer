class Patient():

    def __init__(self,info):
        global conn,cur
        self.nom = info[0]
        self.prenom = info[1]

    def logInfo(self):
        print("prenom,nom = "+self.prenom+", " + self.nom)
