from Stadion import Stadion
from datetime import datetime
#1
def NewYork(stadionok):
    db:int = 0
    for i in range(0, len(stadionok), 1):
        if (stadionok[i].varos == "New York"):
            db += 1
    return db
#2
def csapat_szam(stadionok):
    csp_db:int = 0
    for i in range(0, len(stadionok), 1):
        csp_db += stadionok[i].csapatok_szama
    return csp_db
#3
def elso_merkozes(stadionok):
    lista = []
    for i in range(0, len(stadionok), 1):
        if (stadionok[i].elso_merk < datetime.strptime("1900-01-01", "%Y-%m-%d")):
            lista.append(stadionok[i].nev)
    return lista
#4
def semmi(stadionok):
    db:int = 0
    for i in range(0, len(stadionok), 1):
        if (stadionok[i].utolso_merk < datetime.strptime("2000", "%Y")):
            db += 1
    return db
#5
def buffalo(stadionok):
    cs_szam:int = 0
    for i in range(0, len(stadionok), 1):
        if (stadionok[i].varos == "Buffalo"):
            cs_szam += stadionok[i].csapatok_szama
    return cs_szam