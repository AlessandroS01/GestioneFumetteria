from pathlib import Path

from GestioneMagazzino.Magazzino import Magazzino


class Amministratore:

    # credenziali salvate su file per comodità nella gestione delle informazioni
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

    # metodo che serve a cambiare il nome utente dell'amministratore per il login
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

    # metodo che serve a cambiare la password dell'amministratore per il login
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

    # metodo che richiama il getMagazzino all'interno dell'istanza magazzino
    def visualizzaMagazzino(self):

        magazzino = Magazzino()
        return magazzino.getMagazzino()

    # metodo che viene utilizzato per confrontare le credenziali immesse per il login
    # e quelle all'interno del file
    def controlloCredenziali(self, utente, password):
        if self.nomeUtente == utente and self.password == password:
            return True
        else:
            return False

    # metodo che viene utilizzato per generare un'offerta relativa ad un prodotto ricercato
    # e cambiare i valori all'interno del file per salvare la modifica
    def aggiungiOffertaProdotto(self, codiceSerialeProdotto,
                                tipoOfferta, prezzoOfferta,
                                dataScadenzaOfferta):
        magazzino = Magazzino()
        resultRicerca = magazzino.ricercaProdotto(codiceSerialeProdotto)

        # resultRicerca[2] indice
        # resultRicerca[1] prodotto
        if resultRicerca[0] is True:
            resultRicerca[1].setOffertaTotale(tipoOfferta, prezzoOfferta,
                                              dataScadenzaOfferta, resultRicerca[1])
            # aggiungere una parte che mi permette di modificare i dati relativi all'offerta
            # all'interno del file del prodotto ritrovato

            return True

        else:
            return False

    # metodo che viene utilizzato per cercare all'interno del magazzino tutti i prodotti che hanno
    # un'offerta
    def visualizzaProdottiConOfferta(self):
        magazzino = Magazzino()
        listaProdotti = magazzino.getMagazzino()
        listaProdottiConOfferta = []

        for prodotto in listaProdotti:
            if prodotto.getOfferta() is True:
                listaProdottiConOfferta.append(prodotto)

        return listaProdottiConOfferta
