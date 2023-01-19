def encoder(*args):
    import string
    import re
    sayii = input("sayi gir: ")
    """sayilar=(23, 5, 12, 12, 27, 20, 8, 5, 27, 6, 12, 1, 7, 27, 9, 19, 27, 8, 9, 4, 4, 5, 14, 27, 8, 5, 18, 5, 27, 2, 21, 20, 27, 6, 9, 18, 19, 20, 27, 23, 5, 27, 8, 1, 22, 5, 27, 19, 15, 13, 5, 27, 20, 5, 24, 20, 27, 20, 15, 27, 3, 15, 14, 6, 21, 19, 5, 27, 25, 15, 21, 27, 14, 15, 23, 27, 20, 8, 5, 27, 6, 12, 1, 7, 27, 9, 19, 27, 9, 14, 27, 6, 1, 3, 20, 27, 19, 5, 3, 18, 5, 20, 19, 28, 1, 18, 5, 28, 8, 9, 4, 4, 5, 14, 28, 9, 14, 28, 20, 8, 9, 19, 28, 12, 9, 19, 20, 27, 4, 15, 14, 20, 27, 9, 14, 3, 12, 21, 4, 5, 27, 20, 8, 5, 27, 16, 1, 18, 20, 19, 27, 20, 8, 1, 20, 27, 1, 18, 5, 27, 19, 5, 16, 5, 18, 1, 20, 5, 4, 27, 23, 9, 20, 8, 27, 19, 16, 1, 3, 5, 19)"""
    alphabet = list(string.ascii_lowercase + " " + "_")
    last = {}
    thelast=[]
    sayii = str(sayii)
    a = 1
    c=(int(s) for s in re.findall(r'\b\d+\b', sayii))
    while True:
        for i in alphabet:
            last.update({a:i})
            a+=1
        break
    print(last)
    for v in re.findall(r'\d+', c):
        print(v)
        thelast.append(last[v])
    flag=" ".join(thelast)
    print(thelast)
    print(type(flag))
encoder()