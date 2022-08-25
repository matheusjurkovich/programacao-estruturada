import math

def tinta(metros):
    tipoLata = input("Informe o tamanho da lata (G ou P): ").upper()
    if tipoLata == "G":
        lataQuantidade = (round(metros) // 108) + 1
        lataValor = lataQuantidade * 80
        if lataQuantidade == 1:
            print(f"O orçamento é: {lataQuantidade} lata de tinta grande por R${lataValor}")
        else:
            print(f"O orçamento é: {lataQuantidade} latas de tinta grandes por R${lataValor}")
        return lataQuantidade, lataValor
    elif tipoLata == "P":
        lataQuantidade = (round(metros) // 21.6) + 1
        lataValor = lataQuantidade * 25
        if lataQuantidade == 1:
            print(f"O orçamento é: {lataQuantidade} lata de tinta pequena por R${lataValor}")
        else:
            print(f"O orçamento é: {lataQuantidade} latas de tinta pequenas por R${lataValor}")
        return lataQuantidade, lataValor
  

metrosQuadrados = int(input("Quantos metros quadrados deseja pintar: "))
tinta(metrosQuadrados)