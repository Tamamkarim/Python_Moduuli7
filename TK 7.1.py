def pääohjelma():
    vuodenajat = {
        12: 'talvi', 1: 'talvi', 2: 'talvi',
        3: 'kevät', 4: 'kevät', 5: 'kevät',
        6: 'kesä', 7: 'kesä', 8: 'kesä',
        9: 'syksy', 10: 'syksy', 11: 'syksy'
    }

    try:
        kuukausi = int(input("Syötä kuukauden numero (1-12): "))
        if 1 <= kuukausi <= 12:
            vuodenaika = vuodenajat.get(kuukausi)
            print(f"Kuukauden {kuukausi} vuoden aika on {vuodenaika}.")
        else:
            print("Virheellinen kuukauden numero. Syötä luku välillä 1-12.")
    except ValueError:
        print("Virheellinen syöte. Syötä kokonaisluku.")

if __name__ == "__main__":
    pääohjelma()
