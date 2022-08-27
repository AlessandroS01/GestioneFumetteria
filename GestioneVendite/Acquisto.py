class Acquisto:

    def __init__(self, prodotto,
                 quantitaAcquistate):
        self.prodottoAcquistato = prodotto
        self.quantitaAcquistate = quantitaAcquistate

    def getAcquisto(self):
        return self.prodottoAcquistato

    def getQuantitaAcquistate(self):
        return self.quantitaAcquistate

    def setQuantitaAcquistate(self, quantita):
        self.quantitaAcquistate = quantita
