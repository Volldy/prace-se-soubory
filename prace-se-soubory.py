
def malapismena():
    soubor1 = input("Jméno soubur:")
    soubor1_jmeno = open(soubor1, "r")
    soubor2 = input("Kam to chceš uložit?:")
    soubor2_jmeno = open(soubor2, "w")

    while True:
        radek = soubor1_jmeno.readline()
        if radek == "":
            break                   #znamená to ,že jsme došli na konec souboru
        radek = radek.lower()
        soubor2_jmeno.write(radek)
    soubor1_jmeno.close()
    soubor2_jmeno.close()


def nahrada():
    soubor1 = input("Jméno souboru:")
    soubor1_jmeno = open(soubor1, "r")
    soubor2 = input("Jméno tvého výstupního souboru:")
    soubor2_jmeno = open(soubor2, "w")
    STARYznak = ord(input("Jaký znak chceš nahradit?:"))
    NOVYznak = ord(input("Čím ho chceš nahradit?:"))

    while True:
        znak = soubor1_jmeno.read()
        if znak == "":
            break
        if znak == STARYznak:
            soubor2_jmeno.write(NOVYznak)
        else:
            soubor2_jmeno.write(znak)

    soubor1_jmeno.close()
    soubor2_jmeno.close()


        
def statistika():
    soubor = input("Jméno souboru:")

    radky=0
    slova=0
    znaky=0

    with open(soubor, "r") as f:
        for radek in f:
            x=radek.split()

            radky+=1
            slova+=len(x)
            znaky+=len(radek)
    print("Počet řádků:", radky)
    print("Počet znaků:",znaky)
    print("Počet slov:",slova)
     

menu = int(input("<---MENU--->\n1)Změna velkých písmen na malá písmena\n2)Náhrada jednoho znaku jiným znakem\n3)Statistika souboru\nJaké čísilko sis vybral?"))
if menu == 1:
    malapismena()
elif menu == 2:
    nahrada()
elif menu == 3:
    statistika()



