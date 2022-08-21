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
        self.listaProdotti = []
        for index, element in enumerate(self.storage):
            stringaSplittata = str(self.storage[index]).split('-')
            prodottoAppoggio = Prodotto(None, None, None, None, None, None, None, None)
            prodottoAppoggio.setNomeProdotto(stringaSplittata[0])
            prodottoAppoggio.setQuantitaMagazzino(stringaSplittata[1])
            prodottoAppoggio.setPrezzo(stringaSplittata[2])
            prodottoAppoggio.setCodiceSeriale(stringaSplittata[3])
            prodottoAppoggio.setOfferta(stringaSplittata[4])
            prodottoAppoggio.setTipoOfferta(stringaSplittata[5])
            prodottoAppoggio.setPrezzoOfferta(stringaSplittata[6])
            prodottoAppoggio.setDataScadenzaOfferta(stringaSplittata[7])
            self.listaProdotti.append(prodottoAppoggio)

    # stampa tutti i prodotti che sono stati salvati all'interno dello storage
    # all'interno di una singola lista.
    # Per trovare un prodotto si immette l'indice all'interno di []
    def getMagazzino(self):
        return self.listaProdotti

    # metodo richiamato da aggiungiProdotto per andare a
    # scrivere i dati del prodotto su file
    def aggiungereProdottoSuFile(self, nomeProdotto,
                                 quantitaProdotto, prezzoProdotto,
                                 codiceSeriale):

        pathRelativo = Path("Magazzino")
        pathAssoluto = pathRelativo.absolute()

        with open(pathAssoluto, 'a') as f:
            f.write("\n")
            f.write(nomeProdotto + "-" + quantitaProdotto + "-"
                    + prezzoProdotto + "-" + codiceSeriale
                    + "-None-None-None-None")
            f.close()

    # metodo che serve a capire se un prodotto è possibile aggiungerlo al
    # file Magazzino a seguito della ricerca
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

    # metodo che serve per ricercare un prodotto all'interno del magazzino tramite
    # l'utilizzo del suo codice seriale
    def ricercaProdotto(self, codiceSerialeProdotto):

        for index, element in enumerate(self.listaProdotti):
            if element != "":
                codiceProdottoEsistente = self.listaProdotti[index].getCodiceSeriale()
                if codiceProdottoEsistente == codiceSerialeProdotto:
                    return True, self.listaProdotti[index]

        return False, self.invioMessaggioErroreRicerca()

    def invioMessaggioErroreRicerca(self):
        return "Il prodotto cercato non si trova all'interno del magazzino"

    def invioMessaggioErroreOfferta(self):
        return "Il prodotto cercato non si trova all'interno del magazzino"

    def invioMessaggioErroreInserimentoProdotto(self):
        return "Non è possibile aggiungere il prodotto al magazzino perchè il codice seriale è già stato utilizzato"
