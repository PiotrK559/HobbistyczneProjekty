import random

while True:
    WylosowanaLiczba = random.randint(1, 100) #Losuje liczbę od 1 do 100
    IloscProb = 0 #Resetuje liczbę prób do 0 na początku każdej gry
    while True:
        try:
            WybranaLiczba = int(input("Proszę wybrać liczbę: "))
        except ValueError: #Test czy użytkownik podał liczbę
            print("Proszę podać liczbę od 1 do 100!") 
            continue
        if(WybranaLiczba > 100 or WybranaLiczba < 1):
            print("Proszę podać liczbę od 1 do 100!")
            continue
        IloscProb += 1
        if WybranaLiczba > WylosowanaLiczba:
            print("Twoja liczba jest większa!")
        elif WybranaLiczba < WylosowanaLiczba:
            print("Twoja liczba jest mniejsza!")
        else:
            print("Brawo, odgadłeś liczbę!")
            print(f"Ilość prób: {IloscProb}")
            break
    PlayAgain = input("Chcesz zagrać ponowanie?(y/n): ")
    if PlayAgain.lower() == "y":
        continue
    else:
        break