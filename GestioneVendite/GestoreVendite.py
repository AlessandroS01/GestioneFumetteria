from pathlib import Path

from GestioneVendite.Scontrino import Scontrino


class GestoreVendite:

    def __init__(self):

        self.pathRelativo = Path("ScontriniProdotti")
        self.pathAbsolute = self.pathRelativo.absolute()

        with open(self.pathAbsolute, 'r') as f:
            self.content = f.read()
            f.close()

        self.listaScontrini = []
        self.listaScontrini.append(self.content.split("\n"))

        self.listaAcquistiNuovoScontrino = []

    def aggiungiAcquisto(self, acquisto):
        self.listaAcquistiNuovoScontrino.append(acquisto)

    def getListaAcquisti(self):
        return self.listaAcquistiNuovoScontrino

    # Metodo utilizzato per salvare all'interno del file
    # "ScontriniProdotti.txt" un nuovo acquisto a seguito
    # della creazione dello scontrino.
    def creaScontrino(self):
        scontrinoNuovo = ""

        for index in range(len(self.getListaAcquisti())):

            acquisto = self.getListaAcquisti()[index].getAcquisto()
            if index == 0:
                scontrinoNuovo = str(acquisto.getNomeProdotto() + "|" + acquisto.getCodiceSeriale() + "|"
                                     + self.getListaAcquisti()[index].getQuantitaAcquistate() + "|" + acquisto.getPrezzo())
            else:
                scontrinoNuovo += str("-" + acquisto.getNomeProdotto() + "|" + acquisto.getCodiceSeriale() + "|"
                                      + self.getListaAcquisti()[index].getQuantitaAcquistate() + "|" + acquisto.getPrezzo())

        numeroScontrino = len(self.getListaAcquisti())
        scontrinoCreato = Scontrino(self.listaAcquistiNuovoScontrino, numeroScontrino + 1)
        prezzoTotale = scontrinoCreato.getPrezzoTotale()
        dataEmissioneScontrino = scontrinoCreato.getDataEmissione()

        scontrinoNuovo += str(";" + str(prezzoTotale) + ";"
                              + str(dataEmissioneScontrino)
                              + ";" + str(numeroScontrino+1)
                              + "\n")

        with open(self.pathAbsolute, 'a') as f:
            f.write(scontrinoNuovo)
            f.close()
