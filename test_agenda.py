"""Test della classe Agenda."""

import unittest
from datetime import date

from prenotazioni import (
    Agenda,
    DataNonAmmessa,
    Prenotazione,
    PrenotazioneNonTrovata,
    Sala,
    SalaNonTrovata,
)


class TestSale(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()
        self.agenda.aggiungi_sala(Sala("A1", "Aula Magna", 60))

    def test_aggiungi_sala_codice_duplicato(self):
        with self.assertRaises(ValueError):
            self.agenda.aggiungi_sala(Sala("A1", "Altra aula", 30))

    def test_sala_inesistente(self):
        with self.assertRaises(SalaNonTrovata):
            self.agenda.sala("Z9")


class TestDatePrenotazione(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()
        self.agenda.aggiungi_sala(Sala("A1", "Aula Magna", 60))
        # data di riferimento fissa: lunedì 30 novembre 2026
        self.oggi = date(2026, 11, 30)

    def test_data_passata(self):
        # sabato 28 novembre: due giorni prima di oggi
        giorno = date(2026, 11, 28)
        richiesta = Prenotazione("A1", giorno, "09:00", "10:00", "Mario Rossi", 5)
        with self.assertRaises(DataNonAmmessa):
            self.agenda.prenota(richiesta, oggi=self.oggi)

    def test_domenica(self):
        # domenica 6 dicembre: la sede è chiusa
        giorno = date(2026, 12, 6)
        richiesta = Prenotazione("A1", giorno, "09:00", "10:00", "Mario Rossi", 5)
        with self.assertRaises(DataNonAmmessa):
            self.agenda.prenota(richiesta, oggi=self.oggi)

    def test_oltre_orizzonte(self):
        # 30 gennaio 2027: 61 giorni dopo oggi, il limite è 60
        giorno = date(2027, 1, 30)
        richiesta = Prenotazione("A1", giorno, "09:00", "10:00", "Mario Rossi", 5)
        with self.assertRaises(DataNonAmmessa):
            self.agenda.prenota(richiesta, oggi=self.oggi)

    def test_oggi_accettato(self):
        # Preparazione
        richiesta = Prenotazione("A1", self.oggi, "09:00", "10:00", "Mario Rossi", 5)

        # Azione
        id_richiesta = self.agenda.prenota(richiesta, oggi=self.oggi)

        # Verifica
        self.assertEqual(id_richiesta, 1)


class TestPrenotazioneNonTrovata(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()

    def test_cancella_id_inesistente(self):
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.cancella(99)

    def test_prenotazione_id_inesistente(self):
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.prenotazione(99)


if __name__ == "__main__":
    unittest.main()
