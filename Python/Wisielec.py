import random

ListaSlow = ("arbuz", "aleja", "astma", "beczka", "bajka", "ceyclia", "czarny", "cytryna")
Wisielec = {0: ("   ", #Liczba = ilość błędów
                "   ",
                "   "),
            1: (" o ",
                "   ",
                "   "),
            2: (" o ",
                " | ",
                "  "),
            3: (" o ",
                "/| ",
                "   "),
            4: (" o ",
                "/|\\",
                "   "),
            5: (" o ",
                "/|\\",
                "/  "),
            6: (" o ",
                "/|\\",
                "/ \\")}

def PokazWisielca(IloscBledow):
    for Linia in Wisielec[IloscBledow]:
        print(Linia)

def PokazWskazowki(Wskazowka):
    print(" ".join(Wskazowka))

def PokazOdpowiedz(Odpowiedz):
    print(" ".join(Odpowiedz))

def main():
    Odpowiedz = random.choice(ListaSlow) #Losuje słowo
    Wskazowka = ["_"] * len(Odpowiedz) #Tworzy stringa, gdzie wszystkie litery są zamienione w puste pole
    Bledy = 0
    WybranaLitery = set() #Wykorzystano set ponieważ nie może zawierać dublikatów
    while True:
        PokazWisielca(Bledy)
        PokazWskazowki(Wskazowka)
        WybranaLitera = input("Podaj literę: ").lower()
        if len(WybranaLitera) != 1 or not WybranaLitera.isalpha(): #Sprawdza czy faktycznie podano pojedynczą literę
            print("Nieprawidłowa odpowiedź")
            continue
        if WybranaLitera in WybranaLitery:
            print(f"Litera '{WybranaLitera}' została już wybrana!")
            continue
        WybranaLitery.add(WybranaLitera)
        if WybranaLitera in Odpowiedz:
            for i in range(len(Odpowiedz)):
                if Odpowiedz[i] == WybranaLitera:
                    Wskazowka[i] = WybranaLitera
        else:
            Bledy += 1
        if not "_" in Wskazowka:
            print("Wygrałeś! Gratulacje!")
            break
        elif Bledy == 6:
            PokazWisielca(Bledy)
            print("Przegrałeś! Oto prawidłowa odpowiedź: ")
            PokazOdpowiedz(Odpowiedz)
            break

if __name__ == "__main__":
    main()