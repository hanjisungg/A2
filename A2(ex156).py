#devine le nombre mais triche



g = 0
d = 100
print("Devinez mon nombre entre 0 et 100.")
while g <= d:
    v = int(input("Quelle est votre proposition ? ") )
    m = (d+g)//2
    if g == d:
        print("Bravo!")
        break
    elif v < g:
        print("valeur plus grande")
    elif v > d:
        print("valeur plus petite")
    elif v >= m:
        print("valeur plus petite")
        d = v-1
    else:
        print("valeur plus grande")
        g = v+1
   
    

    