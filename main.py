
listaMedBilar = []

while True:
    print("1. Skapa ny bil")
    print("2. Lista alla bilar")    
    print("0. Avsluta")    

    sel = input("Vad vill du göra:")
    if sel == "1":
        regnr = input("Ange regnr:")
        listaMedBilar.append(regnr)
    if sel == "2":
        for x in listaMedBilar:
            print(x)
    if sel == "0":
        break
