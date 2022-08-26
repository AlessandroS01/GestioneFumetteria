from datetime import datetime


class Scontrino:

    def __init__(self, acquisti, codiceScontrino):
        self.codiceScontrino = codiceScontrino
        self.acquisti = acquisti
        self.dataEmissioneScontrino = datetime.now().date()
        self.prezzoTotale = 0

        for acquisto in acquisti:
            self.prezzoTotale += acquisto.getQuantitaAcquistate() * acquisto.getProdottoAcquistato().getPrezzo()

    def getAcquisti(self):

