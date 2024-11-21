from Stadion import Stadion
import filebeolvas
import feladatok

kek = "\033[34m"
piros = "\033[31m"
zold = "\033[32m"
kek_end = "\033[0m"
char = "*"

stadionok = filebeolvas.beolvas("stadionok.txt", [])
for stadion in stadionok:
    print(stadion)

print(f"{kek}{char * 50}{kek_end}")
db = feladatok.NewYork(stadionok)
print(f"{zold}New Yorkban {db} stadion található.{kek_end}")
print(f"{kek}{char * 50}{kek_end}")

csp_db = feladatok.csapat_szam(stadionok)
print(f"{zold}Az össz csapatszám: {csp_db} db.{kek_end}")
print(f"{kek}{char * 50}{kek_end}")

lista = feladatok.elso_merkozes(stadionok)
print(f"{zold}1900 előtt {piros}{len(lista)} stadionban{zold} volt mérkőzés:{kek_end}\n{lista}")
print(f"{kek}{char * 50}{kek_end}")

db = feladatok.semmi(stadionok)
print(f"{zold}{db} stadionban 2000 óta nem volt mérkőzés.{kek_end}")
print(f"{kek}{char * 50}{kek_end}")

cs_szama = feladatok.buffalo(stadionok)
print(f"{zold}Buffalo-ban összesen {cs_szama} csapat játszott.{kek_end}")
print(f"{kek}{char * 50}{kek_end}")
