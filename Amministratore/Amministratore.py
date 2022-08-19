from GestioneMagazzino.Magazzino import Magazzino


class Amministratore:

    # le credenziali è meglio farle su file
    def __init__(self):
        self.nomeUtente = "f"
        self.password = "f"

    def getNomeUtente(self):
        return self.nomeUtente

    def setNomeUtente(self, nomeUtente):
        self.nomeUtente = nomeUtente

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def visualizzaMagazzino(self):

        magazzino = Magazzino()
        return magazzino.getMagazzino()

    def controlloCredenziali(self, utente, password):
        if self.nomeUtente == utente and self.password == password:
            return True
        else:
            return False
