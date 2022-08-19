from pathlib import Path

from GestioneMagazzino.Magazzino import Magazzino


class Amministratore:

    #credenziali salvate su file per comodità nella gestione delle informazioni
    def __init__(self):

        pathRelativo = Path("CredenzialiAmministratore")
        pathAssoluto = pathRelativo.absolute()

        with open(pathAssoluto, 'r') as f:
            credenzialiLette = f.read()
            f.close()

        credenziali = credenzialiLette.split("\n")
        self.nomeUtente = credenziali[0]
        self.password = credenziali[1]

    def getNomeUtente(self):
        return self.nomeUtente

    def setNomeUtente(self, nomeUtente):
        pathRelativo = Path("CredenzialiAmministratore")
        pathAssoluto = pathRelativo.absolute()

        with open(pathAssoluto, 'r') as file:
            data = file.readlines()
            file.close()

        data[0] = nomeUtente + "\n"

        with open(pathAssoluto, 'w') as file:
            file.writelines(data)
            file.close()


    def getPassword(self):
        return self.password

    def setPassword(self, password):
        pathRelativo = Path("CredenzialiAmministratore")
        pathAssoluto = pathRelativo.absolute()

        with open(pathAssoluto, 'r') as file:
            data = file.readlines()
            file.close()

        data[1] = password + "\n"

        with open(pathAssoluto, 'w') as file:
            file.writelines(data)
            file.close()

    def visualizzaMagazzino(self):

        magazzino = Magazzino()
        return magazzino.getMagazzino()

    def controlloCredenziali(self, utente, password):
        if self.nomeUtente == utente and self.password == password:
            return True
        else:
            return False
