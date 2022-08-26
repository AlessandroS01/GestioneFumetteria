class Cliente:

    def __init__(self, nome,
                 cognome, codiceFiscale,
                 telefono, email):
        self.nome = nome
        self.cognome = cognome
        self.codiceFiscale = codiceFiscale
        self.telefono = telefono
        self.email = email

    def toString(self):
        return str(self.getNome() + "-" + self.getCognome() + "-" +
                   self.getCodiceFiscale() + "-" + self.getTelefono() + "-" +
                   self.getEmail())

    def getNome(self):
        return self.nome

    def setNomeBasico(self, nome):
        self.nome = nome

    def setNome(self, nome):
        return str(nome + "-" + self.getCognome() + "-" +
                          self.getCodiceFiscale() + "-" + self.getTelefono() + "-" +
                          self.getEmail())

    def getCognome(self):
        return self.cognome

    def setCognomeBasico(self, cognome):
        self.cognome = cognome

    def setCognome(self, cognome):
        return str(self.getNome() + "-" + cognome + "-" +
                   self.getCodiceFiscale() + "-" + self.getTelefono() + "-" +
                   self.getEmail())

    def getCodiceFiscale(self):
        return self.codiceFiscale

    def setCodiceFiscaleBasico(self, codiceFiscale):
        self.codiceFiscale = codiceFiscale

    def setCodiceFiscale(self, codiceFiscale):
        return str(self.getNome() + "-" + self.getCognome() + "-" +
                   codiceFiscale + "-" + self.getTelefono() + "-" +
                   self.getEmail())

    def getTelefono(self):
        return self.telefono

    def setTelefonoBasico(self, telefono):
        self.telefono = telefono

    def setTelefono(self, telefono):
        return str(self.getNome() + "-" + self.getCognome() + "-" +
                   self.getCodiceFiscale() + "-" + telefono + "-" +
                   self.getEmail())

    def getEmail(self):
        return self.email

    def setEmailBasico(self, email):
        self.email = email
    def setEmail(self, email):
        return str(self.getNome() + "-" + self.getCognome() + "-" +
                   self.getCodiceFiscale() + "-" + self.getTelefono() + "-" +
                   email)

