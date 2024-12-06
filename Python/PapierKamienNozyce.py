import random

Opcje = ("Papier", "Kamień", "Nożyce")

def ZdobycieWyniku(x, y): # x - Wybór Gracz, y - Wybór Komputera
    if x == y:
        return "Remis"
    elif x == 1 and y == 2:
        return "Wygrałeś!"
    elif x == 1 and y == 3:
        return "Przegrałeś!"
    elif x == 2 and y == 1:
        return "Przegrałeś!"
    elif x == 2 and y == 3:
        return "Wygrałeś!"
    elif x == 3 and y == 1:
        return "Wygrałeś!"
    elif x == 3 and y == 2:
        return "Przegrałeś!"

while True:
    try:
        Opcja = int(input("Wybierz 1(Papier), 2(Kamień), albo 3(Nożyce): "))
    except ValueError:
        print("Proszę dokonać prawidłowego wyboru!")
        continue
    if Opcja > 3 or Opcja < 1:
        print("Proszę dokonać prawidłowego wyboru!")
        continue
    WyborGracza = Opcja
    WyborKomputera = random.randint(0, 2)
    print(f"Komputer wybrał: {Opcje[WyborKomputera]}")
    # Dodano jeden do wyboru komputera, ponieważ indexy zaczynają się od 0, a wybór gracza zaczyna się od 1.
    # Rzecz głównie dla czytelności kodu
    WyborKomputera += 1
    print(ZdobycieWyniku(WyborGracza, WyborKomputera))
    JeszczeRaz = input("Chcesz zagrać jeszcze raz?(y/n): ")
    if(JeszczeRaz.lower() != "y"):
        break