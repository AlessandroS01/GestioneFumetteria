class Cliente:

    def __init__(self, nome,
                 cognome, codiceFiscale,
                 telefono, email):

        self.nome = nome
        self.cognome = cognome
        self.codiceFiscale = codiceFiscale
        self.telefono = telefono
        self.email = email

    def getCliente(self):
        return str(self.getNome() + "-" + self.getCognome() + "-" +
                   self.getCodiceFiscale() + "-" + self.getTelefono() + "-" +
                   self.getEmail())

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getCognome(self):
        return self.cognome

    def setCognome(self, cognome):
        self.cognome = cognome

    def getCodiceFiscale(self):
        return self.codiceFiscale

    def setCodiceFiscale(self, codiceFiscale):
        self.codiceFiscale = codiceFiscale

    def getTelefono(self):
        return self.telefono

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email
