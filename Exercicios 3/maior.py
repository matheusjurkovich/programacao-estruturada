def maiorNumero(n1, n2):
    if n1 > n2:
        print(f"{n1} é maior que {n2}")
        return n1
    else:
        print(f"{n2} é maior que {n1}")
        return n2

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
maiorNumero(n1, n2)
