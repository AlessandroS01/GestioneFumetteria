from pathlib import Path

from GestioneMagazzino.Magazzino import Magazzino


class Amministratore:

    # Il costruttore di amministratore serve a leggere all'interno del
    # file apposito (CredenzialiAmministratore.txt) quali sono le credenziali
    # dell'amministratore.
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

    # Metodo che serve a cambiare il nome utente dell'amministratore per il login.
    # Il nome utente viene poi salvato direttamente su file nella prima riga.
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

    # Metodo che serve a cambiare la password dell'amministratore per il login.
    # La password viene poi salvata direttamente su file nella seconda riga.
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

    # Metodo che richiama il getMagazzino all'interno dell'oggetto magazzino, che
    # grazie al costruttore viene popolato.
    def visualizzaMagazzino(self):

        magazzino = Magazzino()
        return magazzino.getMagazzino()

    # Metodo che viene utilizzato per confrontare le credenziali immesse per il login
    # tramite interfaccia e quelle all'interno del file.
    def controlloCredenziali(self, utente, password):
        if self.nomeUtente == utente and self.password == password:
            return True
        else:
            return False

    # Metodo che viene utilizzato per generare un'offerta relativa a un
    # prodotto prima sprovvisto di offerta.
    # Per fare ciò vengono cambiati gli attributi di quel determinato
    # prodotto attraverso il metodo che viene richiamato all'interno dell if
    # e che è descritto dentro la classe Prodotto.
    def aggiungiOffertaProdotto(self, codiceSerialeProdotto,
                                tipoOfferta, prezzoOfferta,
                                dataScadenzaOfferta):
        magazzino = Magazzino()
        resultRicerca = magazzino.ricercaProdottoCodice(codiceSerialeProdotto)

        if resultRicerca[0] is True:
            resultRicerca[1].setNuovaOfferta(tipoOfferta, prezzoOfferta,
                                             dataScadenzaOfferta, resultRicerca[1])
            return True
        else:
            return False

    # Metodo che va a ricercare quali sono i prodotti all'interno
    # del file ai quali è presente un'offerta.
    # Una volta trovato un prodotto con l'offerta, questo viene aggiunto
    # a una nuova lista al cui interno si troveranno tutti i prodotti con
    # un'offerta abbinata.
    # Alla fine viene fatto il return della lista.
    def visualizzaProdottiConOfferta(self):
        magazzino = Magazzino()
        listaProdotti = magazzino.getMagazzino()
        listaProdottiConOfferta = []

        for index in range(0, len(listaProdotti)):
            if listaProdotti[index].getOfferta() == "True":
                listaProdottiConOfferta.append(listaProdotti[index])

        return listaProdottiConOfferta
