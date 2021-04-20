import csv

archivo = open("appstore_games.csv", "r")
csvreader = csv.reader(archivo, delimiter=',')

#Imprimir los juegos gratis ( precio 0) y en español
show = filter(lambda x: x[7] == "0" and "ES" in x[12], csvreader)
for elem in show:
    print(elem[2])

#imprimir 10 juegos con mayor user rating
filtro = filter(lambda x: x[6] > '98', csvreader)
i = 0
while i <= 10:
    for elem in filtro:
        print("Juego:",elem[2])
        print("Icon url:",elem[4])
    i += 1

archivo.close()