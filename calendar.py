def czy_przestepny(rok):
    if rok < 1582:
        return None
    if rok % 4 != 0:
        return False
    elif rok % 100 != 0:
        return True
    elif rok % 400 != 0:
        return False
    else:
        return True

def dni_w_miesiacu(rok, miesiac):
    if rok < 1582 or miesiac < 1 or miesiac > 12:
        return None
    dni_w_miesiacach = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if miesiac == 2 and czy_przestepny(rok):
        return 29
    else:
        return dni_w_miesiacach[miesiac - 1]

# Interaktywne wprowadzanie danych
rok = int(input("Wprowadź rok: "))
miesiac = int(input("Wprowadź miesiąc (1-12): "))

# Sprawdzenie czy rok jest przestępny
czy_przest = czy_przestepny(rok)
if czy_przest is None:
    print("Nie w kalendarzu gregoriańskim")
elif czy_przest:
    print(f"Rok {rok} jest przestępny")
else:
    print(f"Rok {rok} jest zwykły")

# Sprawdzenie liczby dni w miesiącu
dni = dni_w_miesiacu(rok, miesiac)
if dni is None:
    print("Nieprawidłowy rok lub miesiąc")
else:
    print(f"Liczba dni w miesiącu {miesiac} roku {rok}: {dni}")