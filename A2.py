#A2

def recherche_dichotomique(t, v):
    g = 0
    d = len(t)-1
    while g <= d:
        m = (g+d)//2
        if t[m] < v:
            g = m+1
        elif t[m] > v:
            d = m-1
        else:
            return m
    return None


#exercice 152


def recherche_dichotomique2(t, v):
    g = 0
    d = len(t)-1
    tours = 0
    while g <= d:
        tours = tours+1
        m = (g+d)//2
        if t[m] < v:
            g = m+1
        elif t[m] > v:
            d = m-1
        else:
            return m, tours
    return None, tours
