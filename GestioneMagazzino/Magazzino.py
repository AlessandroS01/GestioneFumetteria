from GestioneMagazzino.Prodotto import Prodotto
from pathlib import Path

class Magazzino:

    def __init__(self):

        pathRelativo = Path("proveLetturaFile/A")
        pathAssoluto = pathRelativo.absolute()

        with open(pathAssoluto, 'r') as f:
            storage = f.read()
            f.close()

        prodotto = storage.split("\n")
        self.storage = prodotto

    def getMagazzino(self):
        return self.storage


    def invioMessaggioErroreRicerca(self):
        return "Il prodotto cercato non si trova all'interno del magazzino"

    def invioMessaggioErroreOfferta(self):
        return "Il prodotto cercato non si trova all'interno del magazzino"

    def invioMessaggioInserimentoProdotto(self):
        return "Non è possibile aggiungere il prodotto al magazzino perchè il codice seriale è già stato utilizzato"
