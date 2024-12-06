ListaZakupów = {} #Użyto dictionary, ponieważ tak najłatwiej ogarnąć strukturę którą potrzebuję, czyli -> Nazwa produktu: Cena
Suma = 0

def WprowadzenieProduktu():
    while True:
        x = input("Proszę wprowadzić nazwę produktu: ")
        if not x.isalpha(): #Sprawdza czy nazwa produktu zawiera cyfry
            print("Proszę wprowadzić prawidłową nazwę produktu!")
            continue
        break
    return x

def WprowadzenieCeny():
    while True:
        try:
            x = float(input("Proszę podać cenę produktu: "))
        except ValueError:
            print("Proszę podać prawidłową wartość!")
            continue
        break
    return x

while True:
    Produkt = WprowadzenieProduktu()
    Cena = WprowadzenieCeny()
    ListaZakupów[Produkt] = Cena
    Wybor = input("Czy chcesz coś jeszcze dodać?(y/n): ")
    if Wybor.lower() == "y":
        continue
    else:
        break
print("Oto twój koszyk: ")
for Produkt, CenaProduktu in ListaZakupów.items():
    Suma += CenaProduktu
    print(f"{Produkt}: {CenaProduktu}zł")
print(f"Suma kosztów zakupów: {Suma}zł")
