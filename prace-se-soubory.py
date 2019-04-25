
def malapismena():
    vstup = input("Jméno tvého vstupního souboru:")
    jmenovstupu = open(vstup, "r")
    vystup = input("Jméno tvého výstupního souboru:")
    jmenovystupu = open(vystup, "w")

    while True:
        radek = jmenovstupu.readline
        if radek == "":
            break
        radek = radek.lower()
        radek.encode("UTF-8")
        jmenovystupu.write(radek)
    jmenovstupu.close()
    jmenovystupu.close()

menu = int(input("Vyber si číslo:"))
if menu == 1:
    malapismena()
