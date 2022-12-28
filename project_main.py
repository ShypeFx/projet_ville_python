import geopy.distance
import csv



def read_from_file():
    with open('./laposte_hexasmal.csv') as orders_file:
        spamreader, spamreader1 = csv.reader(orders_file, delimiter=',')


    ville = "SCEAUX"
    coordonnee = ""
    codepostale = ""
    for row in spamreader:
        if(row[1].__eq__(ville)):
            print('coordonnee : ',row[5])
            coordonnee = row[5]
            print('codepostale : ', row[2])
            codepostale = row[2]

    for row in spamreader1:
        print(geopy.distance.geodesic(row[5], coordonnee).km)



def find_gps_city(name):
    for row in spamreader:
        if(row[1].__eq__(name)):
            print('coordonnee : ',row[5])

def find_postal_code(name):
    for row in spamreader:
        if (row[1].__eq__(name)):
            print('codepostale : ', row[2])


read_from_file()