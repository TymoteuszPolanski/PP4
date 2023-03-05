def dopisz_do_pliku(nazwa_pliku, ciag_znakow):
    """
    Dopisuje przekazany ciąg znaków jako nową linijkę do pliku o podanej nazwie.

    nazwa_pliku (str): Nazwa pliku, do którego ma być dopisany ciąg znaków.
    ciag_znakow (str): Ciąg znaków, który ma być dopisany jako nowa linijka do pliku.
    """
    with open(nazwa_pliku, 'a') as plik:
        plik.write(ciag_znakow + '\n')



#dopisz_do_pliku('plik.txt', 'To jest nowa linijka tekstu.')
