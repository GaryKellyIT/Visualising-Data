import csv
import pandas as pd

tournaments = pd.read_csv('C:/Users/garye/Downloads/finaldf.csv')
prize_money = pd.read_csv('C:/Users/garye/Downloads/prize_money.csv', encoding = 'latin1')

#print(tournaments)
#print(prize_money.title)                     
count =0

csv_file = open('tournamentIndex.csv','w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Tournament','title','Type'])


for i,j in tournaments.iterrows():
    for x,y in prize_money.iterrows():
        if j.Tournament in y.Tournament and j.Type in y.Type:
            count += 1
            print(j.Tournament)
            print(j.Type)
            print(y.Tournament)
            print(y.Type)
            print()
            csv_writer.writerow([j.Tournament,y.Tournament,j.Type])


print(count)
csv_file.close()

