from datetime import datetime
from pathlib import Path


class GestoreVendite:

    def __init__(self):

        self.pathRelativo = Path("ScontriniProdotti")
        self.pathAbsolute = self.pathRelativo.absolute()

        with open(self.pathAbsolute, 'r') as f:
            self.content = f.read()
            f.close()

        self.listaScontrini = []
        self.listaScontrini.append(self.content.split("\n"))
        self.numeroScontrino = 0

        self.listaAcquistiNuovoScontrino = []
        self.listaPrezziProdotti = []

    # Metodo utilizzato per settare il numero dello scontrino
    # leggendo le righe del file "ScontriniProdotti.txt".
    def getNumeroScontrino(self):
        with open(self.pathAbsolute, 'r') as f:
            self.content = f.read()
            f.close()

        numeroScontriniEsistenti = 0
        for index in range(len(str(self.content).split("\n"))):
            numeroScontriniEsistenti = index

        return numeroScontriniEsistenti

    # Serve a popolare una lista di acquisti ogni
    # volta che viene poi utilizzata per creare uno scontrino
    # e salvare l'acquisto nel file di testo "ScontriniProdotti.txt"
    def aggiungiAcquisto(self, acquisto):
        self.listaAcquistiNuovoScontrino.append(acquisto)

    def listaAcquisti(self):
        return self.listaAcquistiNuovoScontrino

    # Metodo utilizzato per salvare all'interno del file
    # "ScontriniProdotti.txt" un nuovo acquisto a seguito
    # della creazione dello scontrino.
    def creaScontrino(self, listaPrezzi):
        scontrinoNuovo = ""
        numeroScontrino = self.getNumeroScontrino() + 1
        listaAcquisti = self.listaAcquistiNuovoScontrino
        prezzoTotale = 0

        for index in range(len(listaAcquisti)):
            prezzo = listaPrezzi[index]
            prezzoTotale += float(prezzo)
            prodottoAcquistato = listaAcquisti[index].getAcquisto()
            if index == 0:
                scontrinoNuovo = str(
                    prodottoAcquistato.getNomeProdotto() + "|" + prodottoAcquistato.getCodiceSeriale() + "|"
                    + listaAcquisti[index].getQuantitaAcquistate() + "|" + str(prezzo) + "€")
            else:
                scontrinoNuovo += str(
                    "-" + prodottoAcquistato.getNomeProdotto() + "|" + prodottoAcquistato.getCodiceSeriale() + "|"
                    + listaAcquisti[index].getQuantitaAcquistate() + "|" + str(prezzo) + "€")

        giorno = datetime.now().day
        mese = datetime.now().month
        anno = datetime.now().year

        dataEmissioneScontrino = str(str(giorno) + "/" +
                                     str(mese) + "/" +
                                     str(anno))

        scontrinoNuovo += str(";" + str(prezzoTotale) + "€" + ";"
                              + str(dataEmissioneScontrino)
                              + ";" + str(numeroScontrino)
                              + "\n")

        with open(self.pathAbsolute, 'a') as f:
            f.write(scontrinoNuovo)
            f.close()

    # Metodo utilizzato per ritrovare quali sono le vendite
    # effettuata durante una giornata immessa da interfaccia.
    def getVenditeGiornata(self, data):
        prezzoTotale = 0
        listaVenditeGiornata = []

        with open(self.pathAbsolute, 'r') as f:
            contenutoFile = f.read().split("\n")
            f.close()

        for index in range(len(contenutoFile)):
            splitData = contenutoFile[index].split(";")
            dataTotale = splitData[len(splitData) - 2].split(" ")
            dataScontrino = dataTotale[0]

            if dataScontrino == data:
                vendite = splitData[len(splitData) - 4]
                # Utilizzato per eliminare l'ultimo carattere (€) all'interno
                # della stringa
                prezzo = splitData[len(splitData) - 3][:-1]
                prezzoTotale += float(prezzo)
                listaVenditeGiornata.append(vendite)

        return listaVenditeGiornata, prezzoTotale

    def aggiungiPrezzoProdotto(self, prezzi):
        self.listaPrezziProdotti.append(prezzi)

    def getListaPrezziProdotti(self):
        return self.listaPrezziProdotti
