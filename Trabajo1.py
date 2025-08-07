import random
def generador():
    long=int(input("de cuantos caracteres quieres tu contraseña"))
    contraseña=""
    letras="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    for i in range(long):
        contraseña += random.choice(letras)
    print(contraseña)
generador()
