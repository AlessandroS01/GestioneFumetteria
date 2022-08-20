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
    # all'interno di una singola lista.
    # Per trovare un prodotto si immette l'indice all'interno di []
    def getMagazzino(self):
        return self.storage

    def aggiungereProdottoSuFile(self, nomeProdotto,
                                 quantitaProdotto, prezzoProdotto,
                                 codiceSeriale):

        pathRelativo = Path("Magazzino")
        pathAssoluto = pathRelativo.absolute()

        with open(pathAssoluto, 'a') as f:
            f.write("\n")
            f.write(nomeProdotto + "-" + quantitaProdotto + "-"
                    + prezzoProdotto + "-" + codiceSeriale)
            f.close()

    # metodo che serve per ricercare un prodotto all'interno del magazzino tramite
    # l'utilizzo del suo codice seriale
    def ricercaProdotto(self, codiceSerialeProdotto):

        for index, element in enumerate(self.storage):
            if element != "":
                codiceProdottoEsistente = str(self.storage[index]).split('-')
                if codiceProdottoEsistente[3] == codiceSerialeProdotto:
                    return True, element

        return False, self.invioMessaggioErroreRicerca()

    def aggiungiProdotto(self, nomeProdotto,
                         quantitaProdotto, prezzoProdotto,
                         codiceSeriale):

        result = self.ricercaProdotto(codiceSeriale)

        if result[0] is False:
            self.aggiungereProdottoSuFile(nomeProdotto,
                                          quantitaProdotto, prezzoProdotto,
                                          codiceSeriale)
            return True
        else:
            self.invioMessaggioErroreInserimentoProdotto()
            return False

    def invioMessaggioErroreRicerca(self):
        return "Il prodotto cercato non si trova all'interno del magazzino"

    def invioMessaggioErroreOfferta(self):
        return "Il prodotto cercato non si trova all'interno del magazzino"

    def invioMessaggioErroreInserimentoProdotto(self):
        return "Non è possibile aggiungere il prodotto al magazzino perchè il codice seriale è già stato utilizzato"
