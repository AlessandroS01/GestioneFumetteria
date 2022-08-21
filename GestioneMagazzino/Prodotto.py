import fileinput
from pathlib import Path


class Prodotto:

    def __init__(self, nomeProdotto,
                 quantitaMagazzino, prezzo,
                 codiceSeriale, offerta,
                 tipoOfferta, prezzoOfferta,
                 dataScadenzaOfferta):

        if offerta:
            self.nomeProdotto = nomeProdotto
            self.quantitaMagazzino = quantitaMagazzino
            self.prezzo = prezzo
            self.codiceSeriale = codiceSeriale
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

    # ritorna tutti gli attributi del prodotto specifico come una stringa
    def getProdotto(self):
        return str(self.getNomeProdotto() + " " + self.getQuantitaMagazzino()
                   + " " + self.getPrezzo() + " " + self.getCodiceSeriale()
                   + " " + self.getOfferta() + " " + self.getTipoOfferta()
                   + " " + self.getPrezzoOfferta() + " " + self.getDataScadenzaOfferta())

    # metodo che serve a settare totalmente un'offerta al prodotto
    def setOffertaTotale(self, tipoOfferta,
                         prezzoOfferta, dataScadenzaOfferta,
                         prodotto):

        pathRelativo = Path("Magazzino")
        pathAssoluto = pathRelativo.absolute()

        nomeProdotto = prodotto.getNomeProdotto()
        quantitaProdotto = prodotto.getQuantitaMagazzino()
        prezzoProdotto = prodotto.getPrezzo()
        codiceSeriale = prodotto.getCodiceSeriale()

        replacement = str(nomeProdotto + "-" + quantitaProdotto + "-" + prezzoProdotto + "-" + codiceSeriale + "-" + tipoOfferta + "-" + prezzoOfferta + "-" + dataScadenzaOfferta + "-")
        data = str(nomeProdotto + "-" + quantitaProdotto + "-" + prezzoProdotto + "-" + codiceSeriale + "----")

        with open(pathAssoluto, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(data, replacement)

        # Write the file out again
        with open(pathAssoluto, 'w') as file:
            file.write(filedata)


