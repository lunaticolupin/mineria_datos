n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print (n[0:21]) 
print (n[3:10])

print (n[0:21:2])

print("Agrega un elemento")

n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(n)
n.append(21)
print(n)

print("Remueve un elemento")
n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(n)
n.remove(10)
print(n)

n.reverse()
print(n)
