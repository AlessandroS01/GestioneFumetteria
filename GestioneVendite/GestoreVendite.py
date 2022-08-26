from pathlib import Path

from GestioneVendite.Scontrino import Scontrino


class GestoreVendite:

    def __init__(self):

        pathRelativo = Path("ScontriniProdotti")
        pathAbsolute = pathRelativo.absolute()

        with open(pathAbsolute, 'r') as f:
            self.content = f.read()
            f.close()

    def creaScontrino(self):

        numeroScontrini = len(self.content)

        scontrinoNuovo = Scontrino( , int(numeroScontrini+1))