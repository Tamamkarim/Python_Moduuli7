def();
kuukausi = int(input("Syötä kuukauden numero: "))

if kuukausi in [3, 4, 5]:
    print("Kevät")
elif kuukausi in [6, 7, 8]:
    print("Kesä")
elif kuukausi in [9, 10, 11]:
    print("Syksy")
elif kuukausi in [12, 1, 2]:
    print("Talvi")
else:
    print("Virheellinen kuukauden numero")