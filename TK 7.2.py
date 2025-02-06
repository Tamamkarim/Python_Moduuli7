def 
    tulosta_vuodenaika(kuukausi_numero):
    vuodenajat = {
        (12, 1, 2): "Talvi",
        (3, 4, 5): "Kevät",
        (6, 7, 8): "Kesä",
        (9, 10, 11): "Syksy"
    }

    for kuukaudet, vuodenaika in vuodenajat.items():
        if kuukausi_numero in kuukaudet:
            print(f"Kuukausi {kuukausi_numero} on {vuodenaika}.")
            return

    print("Virheellinen kuukausi numero.")

if __name__ == "__main__":
    while True:
        try:
            kuukausi_numero = int(input("Anna kuukauden numero (1-12): "))
            if 1 <= kuukausi_numero <= 12:
                break
            else:
                print("Kuukausi numeron on oltava välillä 1-12.")
        except ValueError:
            print("Virheellinen syöte. Anna numero.")

    tulosta_vuodenaika(kuukausi_numero)
