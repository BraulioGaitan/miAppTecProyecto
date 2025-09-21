def rectangulo(base, altura):
    a = base * altura
    p = 2 * (base + altura)
    return a, p

def triangulo(base, altura):
    a = (base * altura) / 2
    l = (base**2 + altura**2) ** 0.5
    p = l + base + altura
    return a, p

def circulo(radio):
    a = 3.1416 * (radio**2)
    p = 2 * 3.1416 * radio
    return a, p

