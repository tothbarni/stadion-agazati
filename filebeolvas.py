from Stadion import Stadion 
def beolvas(fajlnev, stadionok_lista=[]):
    fajlom = open(fajlnev, "r", encoding="UTF-8")
    elso_sor = fajlom.readline()
    tobbi_sor = fajlom.readlines()
    print(elso_sor)
    print(tobbi_sor)
    # lista feldolgozása \ sorok splittelése
    for i in range(1, len(tobbi_sor), 1):
        sor = tobbi_sor[i].strip()
        sor_lista = sor.split(";")
        stadion=Stadion(sor_lista[0], sor_lista[1], int(sor_lista[2]), sor_lista[3], sor_lista[4])
        stadionok_lista.append(stadion)
    fajlom.close()
    return stadionok_lista