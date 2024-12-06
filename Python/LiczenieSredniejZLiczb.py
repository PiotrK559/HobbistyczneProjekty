Liczby = [] #Lista dla liczb

while True:
    Liczba = input("Proszę podać liczbę(q, aby zakończyć wpisywanie liczb): ")
    if Liczba.lower() == "q":
        break
    else:
        try:
            Liczba = float(Liczba)
        except ValueError: #W przypadku kiedy nie wpisano "q" jest sprawdzane, czy wartość może być zamieniona na Floata
            print("Proszę podać prawidłową liczbę!")
            continue
        Liczby.append(Liczba)

IloscLiczb = len(Liczby)
if(IloscLiczb < 2):
    print("Podano mniej niż 2 liczby, wyłączanie programu")
    exit()
SumaLiczb = 0
for Liczba in Liczby:
    SumaLiczb += Liczba

Srednia = SumaLiczb / IloscLiczb

print(f"Średnia tych liczb wynosi: {Srednia:.2f}")

