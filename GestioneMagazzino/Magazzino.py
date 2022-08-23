import os

from GestioneMagazzino.Prodotto import Prodotto
from pathlib import Path


class Magazzino:

    # Il costruttore di magazzino ha il compito di popolare una lista
    # formata solamente da oggetti di Prodotto. Per popolare la lista
    # il costruttore richiama l'apertura del file Magazzino.txt per far
    # sì che si possa leggere ogni prodotto che si trova all'interno del
    # file stesso.
    # Per leggere le singole righe però non devo avere righe nulle (sia all'inizio,
    # sia nel mezzo, sia alla fine del file) altrimenti il programma smette
    # di funzionare.
    # L'If serve a far sì che se il file inizialmente è nullo, il programma non vada
    # in crash e setta la lista dei prodotti a una lista vuota.
    def __init__(self):

        pathRelativo = Path("Magazzino")
        pathAssoluto = pathRelativo.absolute()

        with open(pathAssoluto, 'r') as f:
            storage = f.read()
            f.close()

        if os.stat(pathAssoluto).st_size == 0:
            self.listaProdotti = []
        else:
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

    # Ritorna tutti i prodotti che sono stati salvati all'interno della lista
    # popolata grazie al costruttore.
    def getMagazzino(self):
        return self.listaProdotti

    # Metodo richiamato da aggiungiProdotto per andare a
    # scrivere i dati del prodotto da aggiungere su file a seguito
    # di un controllo effettuato dal metodo richiamante.
    # Per non incorrere nel problema della lettura delle righe nulle, il
    # quale è responsabile del crash del programma, la scrittura del prodotto
    # avviene in modo diverso in base al file di testo.
    # Infatti se il file è vuoto, il metodo scrive nella prima riga il prodotto
    # da aggiungere, altrimenti, grazie all' "append" e un "\n", il metodo scrive
    # il nuovo prodotto sulla linea successiva rispetto all'ultimo prodotto salvato.
    def aggiungereProdottoSuFile(self, nomeProdotto,
                                 quantitaProdotto, prezzoProdotto,
                                 codiceSeriale):

        pathRelativo = Path("Magazzino")
        pathAssoluto = pathRelativo.absolute()

        with open(pathAssoluto, 'a') as f:
            if os.stat(pathAssoluto).st_size == 0:
                f.write(nomeProdotto + "-" + quantitaProdotto + "-"
                        + prezzoProdotto + "-" + codiceSeriale
                        + "-None-None-None-None")
                f.close()
            else:
                f.write("\n")
                f.write(nomeProdotto + "-" + quantitaProdotto + "-"
                        + prezzoProdotto + "-" + codiceSeriale
                        + "-None-None-None-None")
                f.close()

    # Metodo che va a richiamare il metodo sopra solo se è
    # possibile aggiungere un nuovo prodotto i cui attributi vengono
    # istanziati a seguito dell'inserimento di questi ultimi all'interno
    # dell'interfaccia rispettiva (AggiungiProdotto.py).
    # Il controllo viene fatto rispetto al nome e al codice seriale.
    # In caso il controllo viene passato, il metodo richiama il metodo
    # sopra scritto.
    def aggiungiProdotto(self, nomeProdotto,
                         quantitaProdotto, prezzoProdotto,
                         codiceSeriale):

        resultCodice = self.ricercaProdottoCodice(codiceSeriale)
        resultNome = self.ricercaProdottoNome(nomeProdotto)

        if resultCodice[0] is False and resultNome[0] is False:
            self.aggiungereProdottoSuFile(nomeProdotto, quantitaProdotto,
                                          prezzoProdotto, codiceSeriale)
            return True
        else:
            self.invioMessaggioErroreInserimentoProdotto()
            return False

    # Metodo che serve per ricercare un prodotto all'interno del
    # magazzino tramite l'utilizzo del suo codice seriale.
    def ricercaProdottoCodice(self, codiceSerialeProdotto):
        for index, element in enumerate(self.listaProdotti):
            if element != "":
                codiceProdottoEsistente = self.listaProdotti[index].getCodiceSeriale()
                if codiceProdottoEsistente == codiceSerialeProdotto:
                    return True, self.listaProdotti[index]

        return False, self.invioMessaggioErroreRicerca()

    # Metodo che serve per ricercare un prodotto all'interno
    # del magazzino tramite l'utilizzo del suo nome.
    def ricercaProdottoNome(self, nomeProdotto):
        for index, element in enumerate(self.listaProdotti):
            if element != "":
                nomeProdottoEsistente = self.listaProdotti[index].getNomeProdotto()
                if nomeProdottoEsistente == nomeProdotto:
                    return True, self.listaProdotti[index]

        return False, self.invioMessaggioErroreRicerca()

    def invioMessaggioErroreRicerca(self):
        return "Il prodotto cercato non si trova all'interno del magazzino"

    def invioMessaggioErroreOfferta(self):
        return "Il prodotto cercato non si trova all'interno del magazzino"

    def invioMessaggioErroreInserimentoProdotto(self):
        return "Non è possibile aggiungere il prodotto al magazzino perchè il codice seriale è già stato utilizzato"
