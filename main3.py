import random

#0
print("Egy emberi név generálása")

vNEVEK=["Ádám", "Balogh", "Lakatos", "Tóth" "Rézműves", "Váradi"]
ferfiKVENEK=["András", "Béla", "Géza", "István", "Dominik"]
noikNEVEK=["anita", "Ildikó","Erika","Marian"]

#
neme=input("Kérem az emberek nemét (férfi/nö): ")
if neme.lower()=="férfi":
    teljesNev = random.choice(vNEVEK)+ ' '+random.choice(ferfiKVENEK)
elif neme.lower=="nő":
    teljesNev = random.choice(vNEVEK)+ ' '+random.choice(noikNEVEK)
else:
        print("HIBA: rossz nemet adott meg")
        exit()


#2-3
print(teljesNev)