import fileinput
from pathlib import Path


class Prodotto:

    # Il costruttore di Prodotto permette ad ogni oggetto di
    # prodotto di settare i propri attributi iniziali.
    def __init__(self, nomeProdotto,
                 quantitaMagazzino, prezzo,
                 codiceSeriale, offerta,
                 tipoOfferta, prezzoOfferta,
                 dataScadenzaOfferta):

        self.nomeProdotto = nomeProdotto
        self.quantitaMagazzino = quantitaMagazzino
        self.prezzo = prezzo
        self.codiceSeriale = codiceSeriale
        self.offerta = offerta
        self.tipoOfferta = tipoOfferta
        self.prezzoOfferta = prezzoOfferta
        self.dataScadenzaOfferta = dataScadenzaOfferta

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

    # Il metodo ritorna come stringa i vari attributi del prodotto in successione
    # nello stesso modo in cui vengono salvati all'interno del file di
    # testo "Magazzino.txt".
    def getProdotto(self):
        return str(self.getNomeProdotto() + "-" + self.getQuantitaMagazzino()
                   + "-" + self.getPrezzo() + "-" + self.getCodiceSeriale()
                   + "-" + self.getOfferta() + "-" + self.getTipoOfferta()
                   + "-" + self.getPrezzoOfferta() + "-" + self.getDataScadenzaOfferta())

    # Metodo che va a settare un'offerta a un prodotto.
    # Per settare l'offerta, questo metodo richiama il metodo
    # "sovrascriviDati".
    # I vari attributi relativi al campo dell'offerta sono inseriti tramite
    # l'interfaccia ModificaOfferta.
    def setNuovaOfferta(self, tipoOfferta,
                        prezzoOfferta, dataScadenzaOfferta):

        nomeProdotto = self.getNomeProdotto()
        quantitaProdotto = self.getQuantitaMagazzino()
        prezzoProdotto = self.getPrezzo()
        codiceSeriale = self.getCodiceSeriale()

        replacement = str(nomeProdotto + "-" + quantitaProdotto + "-"
                          + prezzoProdotto + "-" + codiceSeriale + "-True-"
                          + tipoOfferta + "-" + prezzoOfferta + "-" + dataScadenzaOfferta)
        data = self.getProdotto()
        self.sovrascriviDati(data, replacement)

    # Metodo che va a eliminare l'offerta al prodotto.
    # Per eliminare l'offerta, questo metodo richiama il metodo
    # "sovrascriviDati".
    # I vari attributi relativi al campo dell'offerta sono settati tutti a "None"
    def eliminaOfferta(self):

        nomeProdotto = self.getNomeProdotto()
        quantitaProdotto = self.getQuantitaMagazzino()
        prezzoProdotto = self.getPrezzo()
        codiceSeriale = self.getCodiceSeriale()

        replacement = str(nomeProdotto + "-" + quantitaProdotto + "-"
                          + prezzoProdotto + "-" + codiceSeriale + "-None-None-None-None")
        data = self.getProdotto()
        self.sovrascriviDati(data, replacement)

    # Metodo richiamato se si vuole ad andare a sostituire una
    # linea all'interno del file "Magazzino.txt".
    def sovrascriviDati(self, stringaDaCambiare, stringaModificata):
        pathRelativo = Path("Magazzino")
        pathAssoluto = pathRelativo.absolute()

        with open(pathAssoluto, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(stringaDaCambiare, stringaModificata)

        # Write the file out again
        with open(pathAssoluto, 'w') as file:
            file.write(filedata)
