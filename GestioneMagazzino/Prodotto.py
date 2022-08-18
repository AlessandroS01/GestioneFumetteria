class Prodotto:

    def __init__(self, nomeProdotto,
                 quantitaMagazzino, codiceSeriale,
                 prezzo, offerta,
                 tipoOfferta, prezzoOfferta,
                 dataScadenzaOfferta):

        if offerta:
            self.nomeProdotto = nomeProdotto
            self.quantitaMagazzino = quantitaMagazzino
            self.codiceSeriale = codiceSeriale
            self.prezzo = prezzo
            self.offerta = offerta
            self.tipoOfferta = tipoOfferta
            self.prezzoOfferta = prezzoOfferta
            self.dataScadenzaOfferta = dataScadenzaOfferta

        else:
            self.tipoOfferta = None
            self.prezzoOfferta = None
            self.dataScadenzaOfferta = None

    def getNomeProdotto(self):
        return self.nomeProdotto

    def setNomeProdotto(self, nomeProdotto):
        self.nomeProdotto = nomeProdotto

    def getQuantitaMagazzino(self):
        return self.quantitaMagazzino

    def setQuantitaMagazzino(self, quantitaMagazzino):
        self.quantitaMagazzino = quantitaMagazzino

    def getCodiceSeriale(self):
        return self.codiceSeriale

    def setCodiceSeriale(self, codiceSeriale):
        self.codiceSeriale = codiceSeriale

    def getPrezzo(self):
        return self.prezzo

    def setPrezzo(self, prezzo):
        self.prezzo = prezzo

    def getOfferta(self):
        return self.offerta

    def setOfferta(self, offerta):
        self.offerta = offerta

    def getTipoOfferta(self):
        return self.tipoOfferta

    def setTipoOfferta(self, tipoOfferta):
        self.tipoOfferta = tipoOfferta

    def getPrezzoOfferta(self):
        return self.prezzoOfferta

    def setPrezzoOfferta(self, prezzoOfferta):
        self.prezzoOfferta = prezzoOfferta

    def getDataScadenzaOfferta(self):
        return self.dataScadenzaOfferta

    def setDataScadenzaOfferta(self, dataScadenzaOfferta):
        self.dataScadenzaOfferta = dataScadenzaOfferta

