def zvetsi_obrazek(zprava, N, sirka, vyska, zvetseni):
    """
    Fce zvětšuje obrázek o zadaném zvětšení.
    """
    zvetsena_zprava = []
    for i in range(0, N, sirka):
        radek = zprava[i:i + sirka]
        zvetseny_radek = "".join(znak * zvetseni for znak in radek)
        for _ in range(zvetseni):
            zvetsena_zprava.append(zvetseny_radek)
    return zvetsena_zprava, sirka * zvetseni, vyska * zvetseni

# Hlavní program
with open("message.txt", "r") as soubor:
    zprava = soubor.read().strip()

N = len(zprava)
sirka, vyska = 23, 73
zvetseni = 10

# Zvětšení obrázku
zvetsena_zprava, zvetsena_sirka, zvetsena_vyska = zvetsi_obrazek(zprava, N, sirka, vyska, zvetseni)

# Uložení PBM souboru
with open("arecibo10.pbm", "w", encoding="UTF-8") as pbm:
    pbm.write("P1\n")
    pbm.write(f"{zvetsena_sirka} {zvetsena_vyska}\n")
    for radek in zvetsena_zprava:
        pbm.write(" ".join(radek) + "\n")

# Uložení PPM souboru
with open("arecibo.ppm", "w", encoding="UTF-8") as ppm:
    ppm.write("P3\n")
    ppm.write(f"{zvetsena_sirka} {zvetsena_vyska}\n")
    ppm.write("255\n")
    
    for radek in zvetsena_zprava:
        for znak in radek:
            if znak == "1":
                ppm.write("0 255 0 ")  # Zelená
            else:
                ppm.write("255 255 255 ")  # Bílá (pozadí)
        ppm.write("\n")

