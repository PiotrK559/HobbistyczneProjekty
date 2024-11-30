from math import pi

Figury = ("1 - Koło", "2 - Kwadrat", "3 - Trójkąt", "4 - Prostokąt") #Tuple do późniejszego pokazania opcji

def WprowadzanieDanych(NazwaDanej): #Funkcja by nie przepisywać tego samego 6 razy
    while True:
        try:
            x = float(input(f"Proszę podać {NazwaDanej}: "))
        except ValueError:
            print("Proszę podać prawidłową wartość!")
            continue
        if x <= 0:
            print("Wartośc nie może wynosić 0, ani mniej niż 0!")
            continue
        break
    return x

def Kolo():
    Promien = WprowadzanieDanych("promień koła")
    return pi * Promien ** 2

def Kwadrat():
    DlugoscBoku = WprowadzanieDanych("długość boku kwadratu")
    return DlugoscBoku ** 2

def Trojkat():
    Podstawa = WprowadzanieDanych("podstawę trójkąta")
    Wysokosc = WprowadzanieDanych("wysokość trójkąta")
    return Podstawa * Wysokosc / 2

def Prostokat():
    Bok1 = WprowadzanieDanych("pierwszy bok prostokąta")
    Bok2 = WprowadzanieDanych("drugi bok prostokąta")
    return Bok1 * Bok2

while True:
    for i in Figury:
        print(i) #Pokazuje opcje
    try:
        Wybor = int(input("Proszę wybrać figurę, której chcesz obliczyć pole(1-4): "))
    except ValueError:
        print("Proszę dokonać prawidłowego wyboru(1-4)!")
        continue
    match Wybor:
        case 1:
            Wynik = Kolo()
        case 2:
            Wynik = Kwadrat()
        case 3:
            Wynik = Trojkat()
        case 4:
            Wynik = Prostokat()
        case _:
            print("Proszę dokonać prawidłowego wyboru(1-4)!")
            continue
    print(f"Pole wynosi {Wynik:.2f}") #Wyświetlenie wyniku z maksymalną ilością 2 cyfr po kropce
    Wybor = input("Czy chesz skorzystać w programu jeszcze raz?(y/n): ")
    if(Wybor.lower() == "y"):
        continue
    else:
        break






