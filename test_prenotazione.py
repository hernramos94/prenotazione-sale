"""Test della classe Prenotazione."""

import unittest
from datetime import date

from prenotazioni import Prenotazione


class TestPrenotazione(unittest.TestCase):
    def setUp(self):
        # giorno valido usato da tutti i test (è un martedì)
        self.giorno = date(2026, 12, 1)

    def test_inizio_non_multiplo_di_30(self):
        with self.assertRaises(ValueError):
            Prenotazione("A1", self.giorno, "09:15", "10:00", "Mario Rossi", 5)

    def test_inizio_prima_dell_apertura(self):
        with self.assertRaises(ValueError):
            Prenotazione("A1", self.giorno, "07:30", "09:00", "Mario Rossi", 5)

    def test_fine_dopo_la_chiusura(self):
        with self.assertRaises(ValueError):
            Prenotazione("A1", self.giorno, "19:00", "20:30", "Mario Rossi", 5)

    def test_fine_non_successiva_all_inizio(self):
        with self.assertRaises(ValueError):
            Prenotazione("A1", self.giorno, "10:00", "10:00", "Mario Rossi", 5)

    def test_giorno_non_date(self):
        # il giorno è una stringa invece di un oggetto date
        with self.assertRaises(TypeError):
            Prenotazione("A1", "2026-12-01", "09:00", "10:00", "Mario Rossi", 5)

    def test_durata_minuti(self):
        # Preparazione
        riunione = Prenotazione("A1", self.giorno, "09:00", "10:30", "Mario Rossi", 5)

        # Azione
        durata = riunione.durata_minuti()

        # Verifica
        self.assertEqual(durata, 90)


if __name__ == "__main__":
    unittest.main()
