#homeres_adatok = open("minta_bemenet","r")
#print homeres_adatok.readlines()

with open("minta_bemenet") as fajl: #with be is zarja a fajlt
    homeres_adatok = fajl.read()
    print homeres_adatok