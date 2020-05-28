import csv
import requests
import json

parameters = {"page": 0, "pageSize": 100, "excludeLevels":"ITF","from":"2020-01-01","to":"2020-12-30"}

response = requests.get("https://api.wtatennis.com/tennis/tournaments/", params=parameters)

tournament_data = json.loads(response.content)

datalist = tournament_data['content']
print(datalist)

csv_file = open('WTA_prize_money.csv','w', newline='')
csv_writer = csv.writer(csv_file)

count = 0 
for tournament in datalist:
    if count == 0:
        header = tournament.keys()
        csv_writer.writerow(header)
        count+=1
    csv_writer.writerow(tournament.values())
        
csv_file.close()



