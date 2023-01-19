def fibonacci(n):
    a = 1
    fibo = [1]
    last = []
    b = 0
    emp = []
    while a < 51:
        fibo.append(sum(fibo[-2:]))
        last.append(fibo[:a])
        a += 1
    for i in last:
        emp.append("".join(map(str, i)))
    print(emp)
    thelast = emp[n - 1]
    fibbbo=thelast[-9:]
    print(fibbbo)
    print(len(thelast))
    print(thelast)
fibonacci(34)