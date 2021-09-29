from csv import writer

matriz = [
    ['Juan', 373, 1970],
    ['Ana', 124, 1983],
    ['Pedro', 901, 1650],
    ['Rosa', 300, 2000],
    ['Juana', 75, 1975],
]

with open("/home/lunatico/Desktop/datos1.csv", "w") as archivo:
    documento = writer(archivo, delimiter=';', quotechar='"')
    #documento.writerows(matriz)
    #documento.writerow(['Alejandro',986796, 8787807])

    for linea in matriz:
        documento.writerow(linea)

    ultima_linea=['Alejandro',986796, 8787807]

    documento.writerow(ultima_linea)