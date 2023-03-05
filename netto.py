def cena_netto(cena_brutto, stawka_podatku):
    """
    Oblicza wartość ceny netto na podstawie przekazanej ceny brutto oraz stawki podatku.

    cena_brutto (float): Wartość ceny brutto.
    stawka_podatku (float): Stawka podatku jako wartość zmiennoprzecinkowa z zakresu 0.0 do 1.0.

    Zwraca wartość ceny netto jako wartość zmiennoprzecinkowa.
    """
    cena_netto = cena_brutto / (1 + stawka_podatku)
    return cena_netto





cena_brutto = 100
stawka_podatku = 0.23
cena_netto = cena_netto(cena_brutto, stawka_podatku)
print(cena_netto)