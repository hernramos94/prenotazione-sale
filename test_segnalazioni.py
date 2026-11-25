"""Test dei difetti segnalati dagli utenti."""

import unittest
from datetime import date

from prenotazioni import Agenda, Prenotazione, Sala


class TestPrenotazioniContigue(unittest.TestCase):
    def test_prenotazioni_contigue_accettate(self):
        # Preparazione
        agenda = Agenda()
        agenda.aggiungi_sala(Sala("A2", "Aula 2", 25))
        # oggi è lunedì, il giorno dopo è martedì: data valida e non domenica
        oggi = date(2026, 11, 30)
        martedi = date(2026, 12, 1)
        prima = Prenotazione("A2", martedi, "09:00", "10:00", "Mario Rossi", 10)
        agenda.prenota(prima, oggi=oggi)

        # Azione
        seconda = Prenotazione("A2", martedi, "10:00", "11:00", "Mario Rossi", 10)
        id_seconda = agenda.prenota(seconda, oggi=oggi)

        # Verifica
        # se la seconda viene accettata riceve l'id 2 (la prima ha l'id 1)
        self.assertEqual(id_seconda, 2)


class TestCapienzaEsatta(unittest.TestCase):
    def test_capienza_esatta_accettata(self):
        # Preparazione
        agenda = Agenda()
        agenda.aggiungi_sala(Sala("R1", "Sala riunioni", 10))
        # oggi è lunedì, il giorno dopo è martedì: data valida e non domenica
        oggi = date(2026, 11, 30)
        martedi = date(2026, 12, 1)
        riunione = Prenotazione("R1", martedi, "09:00", "10:00", "Mario Rossi", 10)

        # Azione
        id_riunione = agenda.prenota(riunione, oggi=oggi)

        # Verifica
        # 10 persone in una sala da 10 posti devono essere accettate (id 1)
        self.assertEqual(id_riunione, 1)


if __name__ == "__main__":
    unittest.main()
