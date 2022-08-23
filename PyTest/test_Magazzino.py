import os
import pathlib
from unittest import TestCase

from GestioneMagazzino.Magazzino import Magazzino


class TestMagazzino(TestCase):

    # Il test viene superato se alla fine si riesce
    # a leggere il contenuto del file.
    def test_lettura_file(self):

        stringa = os.getcwd().split("\\")
        path = ""
        for index in range(0, len(stringa) - 1):
            if index == 0:
                path = stringa[index]
            else:
                path += "\\" + stringa[index]

        pathMagazzino = path + "\\Magazzino"
        with open(pathMagazzino) as f:
            fileContent = f.read()

        assert fileContent != ""
