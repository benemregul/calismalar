liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

yeniliste = []

for birinci in liste:
    if isinstance(birinci, list):
        for ikinci in birinci:
            if isinstance(ikinci, list):
                for ucuncu in ikinci:
                    if isinstance(ucuncu, list):
                        for dorduncu in ucuncu:
                            if isinstance(dorduncu, list):
                                print("yeni veri kalmadı.")
                            else:
                                yeniliste.append(dorduncu)
                    else:
                        yeniliste.append(ucuncu)
            else:
                yeniliste.append(ikinci)    
    else:
        yeniliste.append(birinci)        

print(yeniliste)

ters = [[1, 2], [3, 4], [5, 6, 7]]
yeniters = []

ters.reverse()

for i in range(len(ters)):

    ters[i].reverse()
    yeniters.append(ters[i])

print(yeniters)
