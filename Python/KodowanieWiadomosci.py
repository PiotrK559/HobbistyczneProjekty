import string
import random

znaki = " " + string.ascii_letters + string.digits + string.punctuation
znaki = list(znaki) #Tworzy listę ze wszystkimi literami(bez polskich znaków), liczbami i znakami specjalnymi
klucz = znaki.copy() #Tworzy kopię listy ze znakami
random.shuffle(klucz) #Totalnie miesza listę

tekst = input("Podaj tekst do zakodowania: ")
zakodowanytekst = ""

for znak in tekst:
    index = znaki.index(znak)
    zakodowanytekst += klucz[index]

print(f"Oto zakodowana wiadomość: {zakodowanytekst}")