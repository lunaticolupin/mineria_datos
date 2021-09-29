#from csv import reader

import csv

# c:\\Users\\Tu usuario\\archivo.csv
with open("/home/lunatico/code/mineria/0_introduccion/archivo.csv", "r") as archivo:
    documento = csv.reader(archivo, delimiter=';', quotechar='"')

    for fila in documento:
        # ' '.join(fila)
        # print(fila)
        # print(' '.join(fila))
        print(fila[0]+ " " + fila[1])

    archivo.close()