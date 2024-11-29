class Pracownik():
    def __init__(self, Imie, Nazwisko, Wiek, Stanowsiko):
        self.Imie = Imie
        self.Nazwisko = Nazwisko
        self.Wiek = Wiek
        self.Stanowisko = Stanowsiko
    def PokazDane(self):
        print(f"Pracownik nazywa się {Imie} {Naziwsko}, ma {Wiek} lat i pracuje jako {Stanowisko}")

ListaStanowisk = ("Woźny", "Mechanik", "Recepcja", "Menedżer")

while True:
    Imie = input("Proszę podać imię pracownika: ")
    if Imie.isalpha(): #Sprawdza czy nie podano cyfr/znaków specjalnych
        break
    else:
        print("Proszę prawidłowo podać imię!")
        continue

while True:
    Naziwsko = input("Proszę podać nazwisko pracownika: ")
    if Naziwsko.isalpha():
        break
    else:
        print("Proszę prawidłowo podać naziwsko!")
        continue

while True:
    try:
        Wiek = int(input(f"Proszę podać ile lat ma {Imie} {Naziwsko}: "))
    except ValueError: #Sprawdza czy nie ma błędu(Użytkownik nie podał liczby)
        print("Proszę podać prawidłowy wiek!")
        continue
    if(Wiek < 18):
        print("pracownik jest za młody!")
        continue
    break
    
while True:
    Stanowisko = input(f"Proszę podać na jakim stanowisku pracuje {Imie} {Naziwsko}: ")
    if Stanowisko.capitalize() in ListaStanowisk: #Sprawdza czy podane stanowisko należy do listy
        break
    else:
        print("Nie ma takiego stanowiska!")
        continue
Pracownik1 = Pracownik(Imie.capitalize(), Naziwsko.capitalize(), Wiek, Stanowisko.capitalize())
Pracownik1.PokazDane()
