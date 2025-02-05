def main():
    lentoasemat = {}

    while True:
        print("\nValitse toiminto:")
        print("1 - Lisää uusi lentoasema")
        print("2 - Hae lentoaseman tiedot")
        print("3 - Lopeta")
        valinta = input("Anna valintasi (1/2/3): ")

        if valinta == "1":
            icao = input("Anna lentoaseman ICAO-koodi: ").strip().upper()
            nimi = input("Anna lentoaseman nimi: ").strip()
            lentoasemat[icao] = nimi
            print(f"Lentoasema {nimi} (ICAO: {icao}) lisätty.")

        elif valinta == "2":
            icao = input("Anna haettava ICAO-koodi: ").strip().upper()
            if icao in lentoasemat:
                print(f"Lentoasema: {lentoasemat[icao]}")
            else:
                print("Lentoasemaa ei löydy.")

        elif valinta == "3":
            print("Ohjelma lopetetaan.")
            break

        else:
            print("Virheellinen valinta, yritä uudelleen.")


if __name__ == "__main__":
    main()
