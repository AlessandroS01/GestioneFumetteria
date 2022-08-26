class Acquisto:

    def __init__(self, codiceProdottoAcquistato,
                 quantitaAcquistate):
        self.codiceProdottoAcquistato = codiceProdottoAcquistato
        self.quantitaAcquistate = quantitaAcquistate

    def getCodiceProdottoAcquistato(self):
        return self.codiceProdottoAcquistato.getCodiceSeriale()

    def setCodiceProdottoAcquistato(self):
        return self.quantitaAcquistate

    def setQuantitaAcquistate(self, quantita):
        self.quantitaAcquistate = quantita
