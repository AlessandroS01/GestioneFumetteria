from GestioneMagazzino.Prodotto import Prodotto


class Manga(Prodotto):

    def __init__(self, nomeProdotto,
                 quantitaMagazzino, codiceSeriale,
                 prezzo, offerta,
                 tipoOfferta, prezzoOfferta,
                 dataScadenzaOfferta, genere):

        super().__init__(nomeProdotto, quantitaMagazzino,
                         codiceSeriale, prezzo,
                         offerta, tipoOfferta,
                         prezzoOfferta, dataScadenzaOfferta)

        self.genere = genere

    def getGenere(self):
        return self.genere

    def setGenere(self, genere):
        self.genere = genere
