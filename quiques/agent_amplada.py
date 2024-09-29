""" Fitxer que conté l'agent barca en amplada.

S'ha d'implementar el mètode:
    actua()
"""

from quiques.agent import Barca
from quiques.estat import Estat
from quiques.joc import AccionsBarca


class BarcaAmplada(Barca):
    def __init__(self):
        super(BarcaAmplada, self).__init__()

    def actua(self, percepcio: dict) -> AccionsBarca | (AccionsBarca, (int, int)):
        pass