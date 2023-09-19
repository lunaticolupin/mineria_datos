from csv import writer

matriz = [
    ['Jesus', 373, 1970],
    ['Bryan', 124, 1983],
    ['Cristian', 901, 1650],
    ['Ricardo', 300, 2000],
    ['Andres', 75, 1975],
]

with open("datos2.csv", "w") as archivo:
    documento = writer(archivo, delimiter=',', quotechar='"')
    #documento.writerows(matriz)
    #documento.writerow(['Alejandro',986796, 8787807])

    for linea in matriz:
        documento.writerow(linea)

    ultima_linea=['Sergio',986796, 8787807]

    documento.writerow(ultima_linea)
    documento.writerow(['Saul',986796, 8787807])