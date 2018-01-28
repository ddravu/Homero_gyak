import re #import regex

#homeres_adatok = open("minta_bemenet","r")
#print homeres_adatok.readlines()

class fajl_beolvasas:

    def __init__(self,fajlnev):
        self.fajlnev = fajlnev
        self.homersekletek = self.napi_adatok_beolv(fajlnev)

    def napi_adatok_beolv(self,fajlnev):
        with open("minta_bemenet",'r') as fajl: #with be is zarja a fajlt
            homeres_adatok = re.findall('(\d{4}-\d{2}-\d{2})\W+(\[.*\])', fajl.read())

            napi_adatok = {}
            for adatok in homeres_adatok:
                nap = adatok[0]
                homersekletek = self.homersekletek_a_fajlbol(adatok[1])
                napi_adatok[nap] = homersekletek
        return napi_adatok

    def homersekletek_a_fajlbol(self, homersekletek):
        homersekletek_tagolasa = homersekletek
        karakterek_elhgyasa = ['[', ']', ' ']
        for karakter in karakterek_elhgyasa:
            homersekletek_tagolasa = homersekletek_tagolasa.replace(karakter, '')
        homersekletek_tagolasa = homersekletek_tagolasa.split(',')
        return homersekletek_tagolasa

    def hasznalando_homersekletek(self):
        return self.homersekletek