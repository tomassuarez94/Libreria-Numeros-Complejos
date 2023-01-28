import math
def suma(c1,c2):
    real = c1[(0)] + c2[(0)]
    img = c1[(1)] + c2[(1)]
    return real,img
def resta(c1,c2):
    real = c1[(0)] - c2[(0)]
    img = c1[(1)] - c2[(1)]
    return real,img
def mult(c1,c2):
    real = ((c1[0]*c2[0])-(c1[1]*c2[1]))
    img = ((c1[0]*c2[1])+(c1[1]*c2[0]))
    return real,img
def div(c1,c2):
    real = (((c1[0]*c2[0])+(c1[1]*c2[1]))/((c2[0]**2)+(c2[1]**2)))
    img = (((c2[0]*c1[1])-(c1[0]*c2[1]))/((c2[0]**2)+(c2[1]**2)))
    return real + img
def mod(c):
    return math.sqrt(c[0]**2+c[1]**2)
def conj(c):
    return c[0],-c[1]
def to_polar(c):
    return mod(c), phase(c)
def to_cart(c):
    return (c[0]*math.cos(c[1])),(c[0]*math.sin(c[1]))
def phase(c):
    return math.atan2(c[1],c[0])
def pretty(c):
    if c[1] < 0:
        return "{} - {}i".format(c[0],-c[1])
    else:
        return "{} + {}i".format(c[0], c[1])

