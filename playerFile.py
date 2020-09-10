import csv

with open('jogadores.csv', 'w', newline='') as csvfile:
    infoplayers = ['name', 'birth', 'color', 'rank', 'totalpoints', 'lastgamepoints']
    writer = csv.DictWriter(csvfile, fieldnames=infoplayers)

    writer.writeheader()
    writer.writerow({'name': 'Test1', 'birth': [11, 11, 1900], 'totalpoints': 0})


with open('jogadores.csv', newline='') as csvfile:
    a = []
    spamreadernames = csv.reader(csvfile, delimiter=',', quotechar=',')
    for pos, row in enumerate(spamreadernames):
        for posicao, i in enumerate(row):
            print(i)

def arquivoJogadores():
