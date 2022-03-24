#devine le nombre

n = int(input("Choisissez un nombre entier entre 0 et 100 : "))
g = 0
d = 100
while True:
    m = (g+d)//2
    v = str(input("si votre nombre est égale à " + str(m) + " écrivez bravo sinon dîtes s'il est plus petit ou plus grand :"))
    if v == "plus petit":
        d = m-1
    elif v == "plus grand":
        g = m+1
    else:
        print(m)
        break
        