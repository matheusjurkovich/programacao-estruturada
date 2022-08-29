def download(fileSize, speed):
    downloadTime = fileSize / speed
    return downloadTime

fileSize = int(input("Digite o tamanho do arquivo em MB: "))
speed = int(input("Digite a velocidade de download em Mbps: "))
print ("O tempo de download é de %.2f segundos" % download(fileSize, speed))