numero = int(input())
num = str(numero)
divisores = 0
i = 0

while i < len(num):
    digito = int(num[i])
    if digito != 0 and numero % digito == 0:
        divisores += 1
    i += 1

print(divisores)