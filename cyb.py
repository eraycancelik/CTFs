import re
sayilar=input("sayi gir: ")
liste=[]
for i in re.findall(r'\d+', sayilar):
    liste.append(i)
liste=str(liste)
