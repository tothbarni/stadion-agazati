bold_start = "\033[5m"
bold_end = "\033[0m"
kek = "\033[34m"

from datetime import datetime

class Stadion:
    def __init__(self, nev:str="", varos:str="",csapatok_szama:int=0,elso_merk:str="",utolso_merk:str=""):
        self.nev=nev
        self.varos=varos
        self.csapatok_szama=int(csapatok_szama)
        self.elso_merk=datetime.strptime(elso_merk, "%Y-%m-%d")
        self.utolso_merk=datetime.strptime(utolso_merk, "%Y-%m-%d")

    def __str__(self):
        return (f"{bold_start}{kek}Stadion adatok:\n{bold_end}"
                f"Név: {self.nev}\n"
                f"Város: {self.varos}\n"
                f"Csapatok száma: {self.csapatok_szama}\n"
                f"Első mérkőzés dátuma: {self.elso_merk}\n"
                f"Utolsó mérkőzés dátuma: {self.utolso_merk}\n"
                f"*****************************"
                f"\n")