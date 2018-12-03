#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy_orm.py
from uczniowie_model import* 

def kw01(): # zapytania na jedynym modelu
    #SELECT * FROM uczen WHERE imie LIKE;
    #query = Uczen.select().where(Uczen.imie.startswith('G'))
    #query = Uczen.select().where(Uczen.imie == 'Rafał')
    #SELECT * FROM uczen WHERE imie = 'Rafał';
    #query = Uczen.select().where(Uczen.imie == 'Rafał').count() #ile jest 'Rafał'
    #query = Uczen.select().where(Uczen.egz_mat > 40 )
    query = (Uczen 
        .select()
        .where(Uczen.egz_mat.between(30,35)) 
        .order_by(Uczen.egz_mat.asc())  
    )
    for obj in query:
        print(obj.nazwisko, obj.imie, obj.egz_mat)


def kw02():
    #SELECT nazwisko, klasa FROM uczen INNER JOIN klasa ON uczen.id_klasa = klasa.id 
    query = (Uczen
        .select(Uczen.nazwisko, Uczen.klasa.klasa)
        .join(Klasa)
        .where(Uczen.klasa.klasa.startswith('3')) #wybrana klasa
        .order_by(Uczen.klasa.klasa.asc())
    )
    for obj in query:
        print(obj.nazwisko, obj.klasa.klasa)


def kw03():
    #SELECT nazwisko, klasa FROM uczen INNER JOIN klasa ON uczen.id_klasa = klasa.id 
    query = (Ocena
        .select(Ocena.uczen.nazwisko, Ocena.ocena)
        .join(Uczen)
        .where(Ocena.uczen.imie.startswith('B'))
    )
    for obj in query:
        print( obj.uczen.nazwisko, obj.ocena)



def kw04():
    query = (Ocena
        .select(Ocena.uczen.nazwisko, fn.Count(Ocena.ocena).alias('ile'))
        .join(Uczen)
        .where(Ocena.ocena == 1)
        .group_by(Ocena.uczen.nazwisko)
        .order_by(SQL('ile').asc())
    )
    for obj in query:
        print( obj.uczen.nazwisko, obj.ile)



def kw05():
    #po ile uczniow w klasach 
    query = (Uczen
        .select(Uczen.klasa.klasa, fn.Count(Uczen.id).alias('ile'))
        .join(Klasa)
        .group_by(Uczen.klasa.klasa)
        .order_by(SQL('ile').asc())
    )
    for obj in query:
        print( obj.klasa.klasa, obj.ile)

def kw06():
    #srednia ocen
    query = (Ocena
        .select(Ocena.przedmiot.przedmiot, fn.AVG(Ocena.ocena).alias('srednia'))
        .join(Przedmiot)
        .group_by(Ocena.przedmiot.przedmiot)
        .order_by(SQL('srednia').asc())
    )
    for obj in query:
        print(obj.przedmiot.przedmiot, obj.srednia)

def kw07():
    #srenia uczniow
    query = (Ocena
        .select(Ocena.uczen.nazwisko, fn.AVG(Ocena.ocena).alias('srednia'))
        .join(Uczen)
        .group_by(Ocena.uczen.nazwisko)
        .order_by(SQL('srednia').asc())
    )
    for obj in query:
        print(obj.uczen.nazwisko, obj.srednia)

def kw08():
    #oceny ucznia Szymczak z poszczegolnych przedmiotow
    query = (Uczen
        .select(Uczen.ocena.ocena, fn.AVG(Ocena.ocena).alias('ile'))
        .join(Uczewn)
        .group_by(Uczen.uczen.ocena)
        .order_by(SQL('ile').asc())
    )
    for obj in query:
        print(obj.uczen.ocena, obj.oceny)

def main(args):
    baza.connect()
    
    kw08()
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
