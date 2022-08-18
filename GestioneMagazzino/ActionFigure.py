from GestioneMagazzino.Prodotto import Prodotto


class ActionFigure(Prodotto):

    def __init__(self, nomeProdotto,
                 quantitaMagazzino, codiceSeriale,
                 prezzo, offerta,
                 tipoOfferta, prezzoOfferta,
                 dataScadenzaOfferta, altezza,
                 larghezza, profondita):

        super().__init__(nomeProdotto, quantitaMagazzino,
                         codiceSeriale, prezzo,
                         offerta, tipoOfferta,
                         prezzoOfferta, dataScadenzaOfferta)

        self.altezza = altezza
        self.larghezza = larghezza
        self.profondita = profondita

    def getAltezza(self):
        return self.altezza

    def setAltezza(self, altezza):
        self.altezza = altezza

    def getLarghezza(self):
        return self.larghezza

    def setLarghezza(self, larghezza):
        self.larghezza = larghezza

    def getProfondita(self):
        return self.profondita

    def setProfondita(self, profondita):
        self.profondita = profondita
