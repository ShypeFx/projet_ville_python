import geopy.distance
from math import cos, sqrt
import csv




def read_from_file():
    with open('./laposte_hexasmal_mod.csv') as orders_file:
        spamreader = csv.reader(orders_file, delimiter=';')

        p1 = [48.923446118, 2.869532744]
        p2 = [48.776484949,2.296467846]
        distance = qick_distance(p1,p2)
        print(distance,"km")

        ville = "SCEAUX"
        coordonnee = ""
        codepostale = ""
        for row in spamreader:
            list_of_strings = row[5].split(',')
            if row[5] != '':
                list_float = [float(x) for x in list_of_strings]
                distance = qick_distance(p1, list_float)
                print(distance,"km")
            if(row[1].__eq__(ville)):
                print('type : ', type(row[5]))
                print('coordonnee : ',row[5])
                coordonnee = row[5]
                print('codepostale : ', row[2])
                codepostale = (row[2])

def qick_distance(coord1, coord2):
    x = coord2[0] - coord1[0]
    y = (coord2[1] - coord1[1]) * cos((coord2[0] + coord1[0])*0.00872664626)
    return 111.319 * sqrt(x*x + y*y)


def find_coord_city_name(city):
    with open('./laposte_hexasmal_mod.csv') as orders_file:
        spamreader = csv.reader(orders_file, delimiter=';')
        for row in spamreader:
            list_of_strings = row[5].split(',')
            if(row[1].__eq__(city)):
                #print('type : ', type(row[5]))
                #print('ville : ', city)
                #print('coordonnee : ',row[5])
                #print('codepostale : ', row[2])
                list_of_strings = row[5].split(',')
                list_float = [float(x) for x in list_of_strings]
                return list_float


def information_city(coordonates):
    with open('./laposte_hexasmal_mod.csv') as orders_file:
        spamreader = csv.reader(orders_file, delimiter=';')
        for row in spamreader:
            if(row[5].__eq__(coordonates)):
                print('ville : ', row[1])
                print('codepostale : ', row[2])
                print('coordonnee : ', coordonates)
def min_from_city(coordonates):
    with open('./laposte_hexasmal_mod.csv') as orders_file:
        spamreader = csv.reader(orders_file, delimiter=';')
        for row in spamreader:
            if row[5] != '':
                list_of_strings = row[5].split(',')
                list_float = [float(x) for x in list_of_strings]
                res = qick_distance(coordonates,list_float)
                if(res < 10):
                    print(' ville : ',row[1])
                    print(' distance : ', res)



def main():
    city = input(" ENTRER UNE VILLE : ")
    coordonate_var = find_coord_city_name(city)
    min_from_city(coordonate_var)

main()
