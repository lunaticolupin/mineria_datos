numero = 10
contador = 0

#for i in range(numero):
for i in range(1, numero+1):
    if (i==0):
        continue

    if (numero%i)==0:
        contador = contador + 1

print (contador)