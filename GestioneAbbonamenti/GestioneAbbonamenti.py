import os
from datetime import datetime
from pathlib import Path

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
                clienteAppoggio.setNome(stringaSplittata[0])
                clienteAppoggio.setCognome(stringaSplittata[1])
                clienteAppoggio.setCodiceFiscale(stringaSplittata[2])
                clienteAppoggio.setTelefono(stringaSplittata[3])
                clienteAppoggio.setEmail(stringaSplittata[4])

                abbonamentoAppoggio = Abbonamento(None, None, None, None)
                abbonamentoAppoggio.setCliente(clienteAppoggio)
                abbonamentoAppoggio.setDataEmissione(stringaSplittata[5])
                abbonamentoAppoggio.setDataScadenza(stringaSplittata[6])
                abbonamentoAppoggio.setCodiceIdentificativo(stringaSplittata[7])

                self.listaAbbonamenti.append(abbonamentoAppoggio)

    def getPrezzoAbbonamento(self):
        return self.prezzoAbbonamento

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

    # Metodo che serve per ricercare un abbonamento tramite il suo codice seriale.
    def ricercaAbbonamentoCodice(self, codiceIdentificativoAbbonamento):

        for index, element in enumerate(self.listaAbbonamenti):

            if element != "":
                codiceIdentificativoEsistente = self.listaAbbonamenti[index].getCodiceIdentificativo()

                if codiceIdentificativoEsistente == codiceIdentificativoAbbonamento:
                    return True, self.listaAbbonamenti[index]

        return False, ""

