import Lib as c
import math


def test_suma():
    assert c.suma((5,2),(-8,3)) == (-3, 5) , c.pretty(c.suma((5,2), (-8, 3)))
    assert c.suma((0,5),(4,3)) == (4, 8), c.pretty(c.mult((0,5), (4, 3)))

def test_resta():
    assert c.resta((5,2),(4,-2)) == (1,4), c.pretty(c.resta((5,2), (4, -2)))
    assert c.resta((7,12), (7, -2)) == (0, 14), c.pretty(c.resta((7,12), (7, -2)))


def test_multiplicacion():
    assert c.mult((5, 2), (4, -2)) == (24, -2), c.pretty(c.mult((5,2), (4, -2)))
    assert c.mult((7, 12), (7, -2)) == (73, 70), c.pretty(c.mult((7, 12), (7, -2)))

def test_division():
    assert c.div((5, 2), (4, -2)) == (1.7000000000000002), c.div((5, 2), (4, -2))
    assert c.div((7, 12), (7, -2)) == (2.3207547169811322), c.div((7, 12), (7, -2))


def test_conjugado():
    assert c.conj((5, 2)) == (5,-2), c.pretty(c.conj((5, 2)))
    assert c.conj((7, 12)) == (7,-12), c.pretty(c.conj((7, 12)))


def test_modulo():
    assert c.mod((4, -2)) == (math.sqrt(20)), (c.mod((4, -2)))
    assert c.mod((7, -2)) == (math.sqrt(53)), (c.mod((7, -2)))


def test_fase():
    assert c.phase((5, 2)) == (0.3805063771123649), (c.phase((5, 2)))
    assert c.phase((7, 12)) == (1.042721878368537), (c.phase((7, 12)))

def test_coor_cart_pola():
    assert c.to_polar((5, 2)) == (5.385164807134504, 0.3805063771123649), (c.to_polar((5, 2)))
    assert c.to_polar((7, 12)) == (13.892443989449804, 1.042721878368537), (c.to_polar((7, 12)))

def test_coor_pol_car():
    assert c.to_cart((5, 2)) == (-2.080734182735712, 4.546487134128409), (c.to_cart((5, 2)))
    assert c.to_cart((7, 12)) == (5.906977711127445, -3.7560104260030447), (c.to_cart((7, 12)))

if __name__ == '__main__':
    test_suma()
    test_resta()
    test_multiplicacion()
    test_division()
    test_conjugado()
    test_modulo()
    test_coor_cart_pola()
    test_coor_pol_car()
    print("Prueba exitosa")
