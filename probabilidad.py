espacio_muestral = [1, 2, 3, 4, 5, 6]

n = len(espacio_muestral)

probabilidad = 1.0 / n

numeros_pares = [i for i in espacio_muestral if i % 2 is 0]

h = len(numeros_pares)
probabilidad = float(h) / n

pssme = lambda e: 1.0 / len(e)

def pscme(e, sc):
	n = len(e)
	return len(sc) / float(n)

