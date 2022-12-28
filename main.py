import csv
import panda as pd

def read_from_file():
    csv_file = './laposte_hexasmal.csv'
    col_list = ["Code_commune_INSEE","Nom_commune","Code_postal","Ligne_5","Libellé_d_acheminement","coordonnees_gps"]
    df = pd.read_csv(csv_file, usecols=col_list)
    print(df["Nom_commune"])


read_from_file()