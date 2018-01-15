#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rekurencja_ćw6.py



def wz_rek(a, b):
        if b == 0:
            return a
        
    return nwd_rek(b,a%b)

def main(args):
    a = int(input('Podaj liczbę naturalną'))
    b = int(input('Podaj liczbę naturalną '))
    assert nwd_v2(5, 10) == 5
    assert nwd_v2(3, 9) == 3
    assert nwd_v2(4, 8) == 4
    print("NWD({:d}, {:d}) = {:d}".format(a, b, nwd_rek(a, b)))
    print('Największy wspolny dzielnik', nwd_rek(a, b))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
