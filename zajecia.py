class Zajecia:
    def __init__(self):
        self.lista_studentow = []

    def zapisz_studenta(self, student):
        """
        Metoda umożliwia zapisanie studenta na zajęcia.
        Sprawdza, czy na zajęciach jest już maksymalna liczba studentów.
        """
        if len(self.lista_studentow) >= 10:
            print("Nie można zapisać więcej studentów na tych zajęciach.")
        else:
            self.lista_studentow.append(student)
            print(f"Student {student} został zapisany na zajęcia.")


zajecia = Zajecia()

zajecia.zapisz_studenta('Adam')
zajecia.zapisz_studenta('Barbara')
zajecia.zapisz_studenta('Celina')
zajecia.zapisz_studenta('Daniel')
zajecia.zapisz_studenta('Eliza')
zajecia.zapisz_studenta('Filip')
zajecia.zapisz_studenta('Grażyna')
zajecia.zapisz_studenta('Henryk')
zajecia.zapisz_studenta('Iwona')
zajecia.zapisz_studenta('Janusz')
zajecia.zapisz_studenta('Katarzyna')
