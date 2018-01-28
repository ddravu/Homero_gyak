from homeres import fajl_beolvasas

fajl = fajl_beolvasas("minta_bemenet")
homersekletek = fajl.hasznalando_homersekletek()

for homerseklet in sorted(homersekletek):
    print("Nap:{} Homersekletek:{}".format(homerseklet, homersekletek[homerseklet]))
