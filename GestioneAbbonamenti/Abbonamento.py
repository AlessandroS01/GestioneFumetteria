from pathlib import Path


class Abbonamento:

    def __init__(self, cliente,
                 dataEmissione, dataScadenza,
                 codiceIdentificativo):
        self.cliente = cliente
        self.dataEmissione = dataEmissione
        self.dataScadenza = dataScadenza
        self.codiceIdentificativo = codiceIdentificativo

    def getAbbonamento(self):
        return str(self.getCliente().toString() + "-" + self.getDataEmissione() + "-"
                   + self.getDataScadenza() + "-" + self.getCodiceIdentificativo())

    def getCliente(self):
        return self.cliente

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

    def modificaNome(self, nome):
        replacement = str(self.getCliente().setNome(nome) + "-" + self.getDataEmissione() + "-"
                          + self.getDataScadenza() + "-" + self.getCodiceIdentificativo())
        data = self.getAbbonamento()

        self.sovrascriviDati(data, replacement)

    def modificaCognome(self, cognome):
        replacement = str(self.getCliente().setCognome(cognome) + "-" + self.getDataEmissione() + "-"
                          + self.getDataScadenza() + "-" + self.getCodiceIdentificativo())
        data = self.getAbbonamento()

        self.sovrascriviDati(data, replacement)

    def modificaCodiceFiscale(self, codiceFiscale):
        replacement = str(self.getCliente().setCodiceFiscale(codiceFiscale) + "-" + self.getDataEmissione() + "-"
                          + self.getDataScadenza() + "-" + self.getCodiceIdentificativo())
        data = self.getAbbonamento()

        self.sovrascriviDati(data, replacement)

    def modificaTelefono(self, telefono):
        replacement = str(self.getCliente().setTelefono(telefono) + "-" + self.getDataEmissione() + "-"
                          + self.getDataScadenza() + "-" + self.getCodiceIdentificativo())
        data = self.getAbbonamento()

        self.sovrascriviDati(data, replacement)

    def modificaEmail(self, email):
        replacement = str(self.getCliente().setEmail(email) + "-" + self.getDataEmissione() + "-"
                          + self.getDataScadenza() + "-" + self.getCodiceIdentificativo())
        data = self.getAbbonamento()

        self.sovrascriviDati(data, replacement)

    # Metodo richiamato se si vuole ad andare a sostituire una
    # linea all'interno del file "Abbonamenti.txt".
    def sovrascriviDati(self, stringaDaCambiare, stringaModificata):
        pathRelativo = Path("Abbonamenti")
        pathAssoluto = pathRelativo.absolute()

        with open(pathAssoluto, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(stringaDaCambiare, stringaModificata)

        # Write the file out again
        with open(pathAssoluto, 'w') as file:
            file.write(filedata)
