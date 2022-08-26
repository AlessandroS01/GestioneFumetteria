import os
from datetime import datetime
from pathlib import Path

from cffi.backend_ctypes import long

from GestioneAbbonamenti.Abbonamento import Abbonamento
from GestioneAbbonamenti.Cliente import Cliente
from GestioneMagazzino.Magazzino import Magazzino

# Classe necessaria per andare a leggere dal file "Abbonamenti.txt"
# e popolare la lista degli abbonamenti con la lettura.
class GestioneAbbonamenti:

    def __init__(self):

        pathRelativoPrezzo = Path("PrezzoAbbonamenti")
        pathAssolutoPrezzo = pathRelativoPrezzo.absolute()

        with open(pathAssolutoPrezzo, 'r') as f:
            self.prezzoAbbonamento = f.read()
            f.close()

        pathRelativoAbbonamenti = Path("Abbonamenti")
        pathAssolutoAbbonamenti = pathRelativoAbbonamenti.absolute()

        with open(pathAssolutoAbbonamenti, 'r') as f:
            storage = f.read()
            f.close()

        if os.stat(pathAssolutoAbbonamenti).st_size == 0:
            self.listaAbbonamenti = []
        else:

            abbonamento = storage.split("\n")
            self.abbonamentiDaFile = abbonamento
            self.listaAbbonamenti = []

            for index, element in enumerate(self.abbonamentiDaFile):
                stringaSplittata = str(self.abbonamentiDaFile[index]).split('-')

                clienteAppoggio = Cliente(None, None, None, None, None)
                clienteAppoggio.setNomeBasico(stringaSplittata[0])
                clienteAppoggio.setCognomeBasico(stringaSplittata[1])
                clienteAppoggio.setCodiceFiscaleBasico(stringaSplittata[2])
                clienteAppoggio.setTelefonoBasico(stringaSplittata[3])
                clienteAppoggio.setEmailBasico(stringaSplittata[4])

                abbonamentoAppoggio = Abbonamento(None, None, None, None)
                abbonamentoAppoggio.setCliente(clienteAppoggio)
                abbonamentoAppoggio.setDataEmissione(stringaSplittata[5])
                abbonamentoAppoggio.setDataScadenza(stringaSplittata[6])
                abbonamentoAppoggio.setCodiceIdentificativo(stringaSplittata[7])

                self.listaAbbonamenti.append(abbonamentoAppoggio)

    def getPrezzoAbbonamento(self):
        return float(self.prezzoAbbonamento)

    def setPrezzoAbbonamento(self, prezzoAbbonamento):

        pathRelativoPrezzo = Path("PrezzoAbbonamenti")
        pathAssolutoPrezzo = pathRelativoPrezzo.absolute()

        with open(pathAssolutoPrezzo, 'w') as f:
            f.write(prezzoAbbonamento)
            f.close()

    # Metodo che ritorna una lista di abbonamenti che è stata
    # popolata grazie al costruttore.
    def getAbbonamenti(self):
        return self.listaAbbonamenti

    # Metodo che ritorna una lista di prodotti salvati all'interno
    # del file di testo "Magazzino.txt" con un'offerta esclusiva
    # per gli abbonati.
    def getProdottiOffertaAbbonati(self):

        magazzino = Magazzino()
        listaProdottiTotale = magazzino.getMagazzino()

        listaProdottiOffertaAbbonati = []

        for prodotto in listaProdottiTotale:

            if prodotto.getTipoOfferta() == "Abbonati":
                listaProdottiOffertaAbbonati.append(prodotto)

        return listaProdottiOffertaAbbonati

    # Metodo che ritorna una lista degli abbonamenti attivi salvati all'interno
    # del file di testo "Abbonamenti.txt".
    def getAbbonamentiAttivi(self):

        listaAbbonamentiAttivi = []
        dataOdierna = datetime.now().date()

        for abbonamento in self.getAbbonamenti():

            dataScadenzaAbbonamento = datetime.strptime(abbonamento.getDataScadenza(), '%d/%m/%Y').date()

            if dataScadenzaAbbonamento >= dataOdierna:
                listaAbbonamentiAttivi.append(abbonamento)

        return listaAbbonamentiAttivi

    # Metodo che ritorna una lista degli abbonamenti emessi durante
    # una giornata salvati all'interno del file di testo "Abbonamenti.txt".
    def getAbbonamentiEmessi(self, dataEmissione):

        listaAbbonamentiEmessi = []
        dataImmessa = datetime.strptime(dataEmissione, '%d/%m/%Y').date()

        for index in range(0, len(self.getAbbonamenti())):
            date = datetime.strptime(self.getAbbonamenti()[index].getDataEmissione(), '%d/%m/%Y').date()

            if dataImmessa == date:
                listaAbbonamentiEmessi.append(self.getAbbonamenti()[index])

        return listaAbbonamentiEmessi

    # Metodo che serve per ricercare un abbonamento tramite il suo codice seriale.
    def ricercaAbbonamentoCodice(self, codiceIdentificativoAbbonamento):
        for index, element in enumerate(self.listaAbbonamenti):

            if element != "":
                codiceIdentificativoEsistente = self.listaAbbonamenti[index].getCodiceIdentificativo()

                if codiceIdentificativoEsistente == codiceIdentificativoAbbonamento:
                    return True, self.listaAbbonamenti[index]

        return False, ""

    # Metodo che serve per ricercare un abbonamento tramite l'email.
    def ricercaEmail(self, email):
        for index, element in enumerate(self.listaAbbonamenti):

            if element != "":
                emailEsistente = self.listaAbbonamenti[index].getCliente().getEmail()

                if emailEsistente == email:
                    return True, self.listaAbbonamenti[index]

        return False, ""

    # Metodo che serve per ricercare un abbonamento tramite il telefono.
    def ricercaTelefono(self, telefono):
        for index, element in enumerate(self.listaAbbonamenti):

            if element != "":
                telefonoEsistente = self.listaAbbonamenti[index].getCliente().getTelefono()

                if telefonoEsistente == telefono:
                    return True, self.listaAbbonamenti[index]

        return False, ""

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
