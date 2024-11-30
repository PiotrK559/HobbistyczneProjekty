Operacje = ("+", "-", "*", "/")

while True:
    Operacja = input("Podaj jaką chcesz dokonać operację(+|-|/|*): ")
    if Operacja in Operacje:
        break
    else:
        print("Proszę podać prawidłową operację!")

while True:
    try:
        Liczba1 = float(input("Proszę podać pierwszą liczbę: "))
    except ValueError: #Sprawdza czy użytkownik podał liczbę
        print("Proszę podać liczbę!")
        continue
    break

while True:
    try:
        Liczba2 = float(input("Proszę podać drugą liczbę: "))
    except ValueError:
        print("Proszę podać liczbę!")
        continue
    break

def Obliczenie():
    match(Operacja): #Sprawdza która operacja została wybrana i na jej bazie dokonuje prawidłowego obliczenia
        case "+":
            return Liczba1 + Liczba2
        case "-":
            return Liczba1 - Liczba2
        case "*":
            return Liczba1 * Liczba2
        case "/":
            try:
                return Liczba1 / Liczba2
            except ZeroDivisionError: #Specjalna wiadomość kiedy użytkownik spróbuje podzielić przez 0
                return "Nie można dzielić przez zero"

wynik = Obliczenie()
print(f"Twój wynik wynosi: {wynik}")

