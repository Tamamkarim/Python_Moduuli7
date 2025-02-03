def pääohjelma():
    vuodenaika = (
        ('talvi', 'talvi', 'talvi'),  # joulukuu, tammikuu, helmikuu
        ('kevät', 'kevät', 'kevät'),  # maaliskuu, huhtikuu, toukokuu
        ('kesä', 'kesä', 'kesä'),    # kesäkuu, heinäkuu, elokuu
        ('syksy', 'syksy', 'syksy')  # syyskuu, lokakuu, marraskuu
    )
    kuukausi = int(input("Syötä kuukauden numero (1-12): "))

    if 1 <= kuukausi <= 12:

        vuodenaika_indeksi = (kuukausi - 1) // 3

        vuodenajan_nimi = vuodenaika[vuodenaika_indeksi][0]
        print(f"Kuukauden {kuukausi} vuoden aika on {vuodenajan_nimi}.")
    else:
        print("Virheellinen kuukauden numero. Syötä luku välillä 1-12.")

if __name__ == "__main__":
    pääohjelma()
