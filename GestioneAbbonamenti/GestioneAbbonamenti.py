import os
from pathlib import Path

from GestioneAbbonamenti.Abbonamento import Abbonamento
from GestioneAbbonamenti.Cliente import Cliente


# Classe necessaria per andare a leggere dal file "Abbonamenti.txt"
# e popolare la lista degli abbonamenti con la lettura.
from GestioneMagazzino.Magazzino import Magazzino


class GestioneAbbonamenti:

    def __init__(self):

        pathRelativo = Path("Abbonamenti")
        pathAssoluto = pathRelativo.absolute()

        with open(pathAssoluto, 'r') as f:
            storage = f.read()
            f.close()

        if os.stat(pathAssoluto).st_size == 0:
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

                abbonamentoAppoggio = Abbonamento(None, None, None, None, None)
                abbonamentoAppoggio.setCliente(clienteAppoggio)
                abbonamentoAppoggio.setDataEmissione(stringaSplittata[5])
                abbonamentoAppoggio.setDataScadenza(stringaSplittata[6])
                abbonamentoAppoggio.setCodiceIdentificativo(stringaSplittata[7])
                abbonamentoAppoggio.setPrezzoAbbonamento(stringaSplittata[8])

                self.listaAbbonamenti.append(abbonamentoAppoggio)

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

