from datetime import datetime


class Scontrino:

    def __init__(self, acquisti, codiceScontrino):
        self.codiceScontrino = codiceScontrino
        self.acquisti = acquisti
        self.dataEmissioneScontrino = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.prezzoTotale = 0

        for index in range(len(acquisti)):

            self.prezzoTotale += float(float(acquisti[index].getQuantitaAcquistate()) * float(acquisti[index].getAcquisto().getPrezzo()))

    def getAcquisti(self):
        return self.acquisti

    def getPrezzoTotale(self):
        return self.prezzoTotale

    def getDataEmissione(self):
        return self.dataEmissioneScontrino
