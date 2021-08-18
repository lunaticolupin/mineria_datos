age = None

if age is None:
    print("Variable Nula")

age = int(input("¿Cuál es tu edad? "))

if age is not None:
    print("Variable no Nula")

if age < 18:

    if age < 12:
        print("Eres un niño %s " % age)
    
    print("Eres menor de edad " + str(age))

else:
    print("Eres mayor de edad.")
