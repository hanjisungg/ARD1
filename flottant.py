#prend un argument qui prend en tableau de 0 et de 1 de taille 32 et qui renvoie  le nombre corresponsdant

#definir 2 fonctions:

#def mantisse qui prend en argument un tableau de 0 et de 1 de taille 23 et renvoie la mantisse (nombre flottant en python)

#def exposant qui prend en ragument un tableau de 0 et de 1 de taille 8 et renvoie l'exposant (un entier en -126 et +127)


#fonction finale = def flottant


def exposant(t8):
    global e
    e = 0
    for i in range(8):
        if t8[i] == 1:
            e = e+2**(7-i)
    e = e-127
    return e

def mantisse(t23):
    global m
    m = 1
    acc = 1/2
    for i in range(23):
        if t23[i] == 1:
            m = m + acc
        acc = acc/2
    return m

def flottant(t32):
    t8 = t32[1:9]
    t23 = t32[9:32]
    exposant(t8)
    mantisse(t23)
    if t32[0] == 1:
        x = -(m*2**e)
    else:
        x = m*2**e
    return x
        
        
    
