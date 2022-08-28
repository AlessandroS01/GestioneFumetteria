import os
from datetime import datetime
from unittest import TestCase


class TestVari(TestCase):

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

    # Test utilizzato per capire se le date
    # utilizzate sono le stesse
    def test_lettura_datetime(self):

        today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        dateTest = datetime.strptime("25/8/2022", '%d/%m/%Y').date()

        assert today == dateTest
