class Abbonamento:

    def __init__(self, cliente,
                 dataEmissione, dataScadenza,
                 codiceIdentificativo, prezzoAbbonamento):

        self.cliente = cliente
        self.dataEmissione = dataEmissione
        self.dataScadenza = dataScadenza
        self.codiceIdentificativo = codiceIdentificativo
        self.prezzoAbbonamento = prezzoAbbonamento

    def getCliente(self):
        return self.cliente.getCliente()

    def setCliente(self, cliente):
        self.cliente = cliente

    def getDataEmissione(self):
        return self.dataEmissione

    def setDataEmissione(self, dataEmissione):
        self.dataEmissione = dataEmissione

    def getDataScadenza(self):
        return self.dataScadenza

    def setDataScadenza(self, dataScadenza):
        self.dataScadenza = dataScadenza

    def getCodiceIdentificativo(self):
        return self.codiceIdentificativo

    def setCodiceIdentificativo(self, codiceIdentificativo):
        self.codiceIdentificativo = codiceIdentificativo

    def getPrezzoAbbonamento(self):
        return self.prezzoAbbonamento

    def setPrezzoAbbonamento(self, prezzoAbbonamento):
        self.prezzoAbbonamento = prezzoAbbonamento


