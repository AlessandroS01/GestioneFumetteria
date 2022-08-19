from GestioneMagazzino.Prodotto import Prodotto
from pathlib import Path


class Magazzino:

    def __init__(self):

        pathRelativo = Path("Magazzino")
        pathAssoluto = pathRelativo.absolute()

        with open(pathAssoluto, 'r') as f:
            storage = f.read()
            f.close()

        prodotto = storage.split("\n")
        self.storage = prodotto

    # stampa tutti i prodotti che sono stati salvati all'interno dello storage
    def getMagazzino(self):
        return self.storage

    # metodo che serve per ricercare un prodotto all'interno del magazzino tramite
    # l'utilizzo del suo codice seriale
    def ricercaProdotto(self, codiceSerialeProdotto):

        for prodotto in self.storage:
            if prodotto.__contains__(codiceSerialeProdotto): #ripensare perhcè il contains può dare problemi
                return prodotto

        return self.invioMessaggioErroreRicerca()

    def invioMessaggioErroreRicerca(self):
        return "Il prodotto cercato non si trova all'interno del magazzino"

    def invioMessaggioErroreOfferta(self):
        return "Il prodotto cercato non si trova all'interno del magazzino"

    def invioMessaggioInserimentoProdotto(self):
        return "Non è possibile aggiungere il prodotto al magazzino perchè il codice seriale è già stato utilizzato"
