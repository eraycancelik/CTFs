def encoder(*args):
    import string
    alphabet_list = list(string.ascii_lowercase + " " + "_")
    dic={}
    one_to_end=[]
    a=0
    last=[]
    hidden_list=[]
    for i in range(1,29):
        one_to_end.append(i)

    for c in one_to_end:
        dic.update({c: alphabet_list[a]})
        a += 1
    for z in args:
        z=int(z)
        last.append(dic.get(z))
    flag_sentence="".join(last)
    print(flag_sentence)

encoder(23, 5, 12, 12)
