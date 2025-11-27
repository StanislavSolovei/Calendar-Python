rok = int(input("Wprowadź rok: "))

if rok % 4 == 0:
    print("Rok przestępny")
else: 
    print("Zwykły rok")

if rok % 100 == 0:
    print("Rok przestępny")
else:
    print("Zwykły rok")

if rok % 400 == 0:
    print("Zwykły rok")