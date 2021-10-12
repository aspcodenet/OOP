
# AAA111 Volvo XC60 Blå
# BBB222 Renault Megane Grön
# CCC111 Renault Megane Vit
# 

# OBJEKT = *EN* sak som kan ha flera egenskaper (fack med namn) 


class Bil:
    def __init__(self, regnr : str, biltyp:str, color:str):
        self._regnr = regnr
        self._biltyp = biltyp
        self._color = color
    
    def getRegnr(self) -> str:
        return self._regnr

    def getBiltyp(self) -> str:
        return self._biltyp

    def getColor(self) -> str:
        return self._color

    def setColor(self, color: str):
        self._color = color

    


# print(nissesBil.getColor())

lisasBil = Bil("BBB222", "Saab V4", "Brun")
# print(lisasBil.getColor())

listaMedBilar = [] # str - dvs regnr

while True:
    print("1. Skapa ny bil")
    print("2. Lista alla bilar")    
    print("3. Lacka om bilen")    
    print("0. Avsluta")    

    sel = input("Vad vill du göra:")
    if sel == "1":
        regnr = input("Ange regnr:")
        biltyp = input("Ange biltyp:") # Volvo XC60
        color = input("Ange färg:")
        bil = Bil(regnr, biltyp,color )       
        listaMedBilar.append(bil)
    if sel == "2":
        for x in listaMedBilar:
            print(f"{x.getRegnr()}, {x.getColor()}")
    if sel == "0":
        break
