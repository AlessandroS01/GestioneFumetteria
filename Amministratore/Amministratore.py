from GestioneMagazzino.Magazzino import Magazzino


class Amministratore:

    def __init__(self):
        self.nomeUtente = "utente"
        self.password = "password"

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
        return magazzino

    def aggiungiOffertaProdotto(self, codiceSeriale):

        return None
