#Dictoniary jest dla mnie najwygodniejszy do dania produktu i ceny w jednym miejscu
ListaProduktów = {"Woda": 3.99, "Pizza": 13.99, "Ketchup": 9.99, "Czekolada": 7.99, "Masło": 4.99, "Lody": 12.99}
Suma = 0

def WprowadzenieProduktu():
    while True:
        x = input("Proszę wprowadzić nazwę produktów: ")
        if x not in ListaProduktów:
            print("Nie ma takiego produktu!")
            continue
        break
    return x
def WprowadzenieIlosci():
    while True:
        try:
            x = int(input("Proszę podać ilość: "))
        except ValueError:
            print("Nieprawidłowa wartość! Spróbuj ponownie!")
            continue
        break
    return x

print("Oto lista produktów:")
for P in ListaProduktów.keys():
    print(P, end=" ")
print()
while True:
    Produkt = WprowadzenieProduktu()
    Ilosc = WprowadzenieIlosci()
    Suma += ListaProduktów[Produkt] * Ilosc
    print(f"Obecna suma wynosi: {Suma:.2f}zł")
    Wybor = input("Coś jeszcze?(y/n): ")
    if Wybor.lower() == "y":
        continue
    else:
        print(f"Koszt wszystkich zakupów: {Suma:.2f}zł")
        break