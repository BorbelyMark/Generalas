import random

#0
print("Egy osztály tanulóinak generálása")

vNEVEK=["Ádám", "Balogh", "Lakatos", "Tóth" "Rézműves", "Váradi"]
ferfiKVENEK=["András", "Béla", "Géza", "István", "Dominik"]
noikNEVEK=["anita", "Ildikó","Erika","Marian"]

db=int(input("kérem a tanulók számnát: "))
tanulok = []
for i in range(db):
    #tanuló neve
    neme=input("Kérem az emberek nemét (férfi/nö): ")
    neme=random.randint(1,2)
    if neme==1:
        teljesNev = random.choice(vNEVEK)+ ' '+random.choice(ferfiKVENEK)
        neme="ferfi"
else:
    teljesNev = random.choice(vNEVEK)+ ' '+random.choice(noikNEVEK)
    neme="nő"
    #tanuló születési ideje
    ev= random.randint(2000, 2005)
    honap=random.randint(1, 12)
    nap= random.randint(1, 28)
#dátum összeállitása
datum= f"{ev}.{honap:0>2d}.{nap:0>2d}"
#magasság
magassag= random.randint(155, 190)

#tanuló összeállitása
tanulo = (teljesNev, datum, neme, magassag)
#felvétel a tanulókhoz
tanulok.append(tanulok)


#2-3
for item in tanulok:
    print(item)