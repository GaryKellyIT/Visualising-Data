'''
Author: Gary Kelly
Description: Program to scrape ATP Tournament website for list of tournament names,
             dates and prize moneys
'''
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.atptour.com/en/tournaments/').text
soup = BeautifulSoup(source,'lxml')

csv_file = open('ATP_prize_money.csv','w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Tournament','startDate','endDate','prizeMoney','prizeMoneyCurrency'])

for post in soup.find_all('tr', class_='tourney-result'):
    title = post.find('td', class_='title-content')
    name = title.find('a', class_='tourney-title').text
    location = title.find('span', class_='tourney-location').text
    dates = title.find('span', class_='tourney-dates').text
    tourney_details = post.find('td', class_='tourney-details-table-wrapper')
    financial_com = tourney_details.find('td', class_='tourney-details fin-commit')

    try:
        prize_money = financial_com.find('span', class_='item-value').text
    except Exception as e:
        prize_money = "$0"

    location = location.strip()
    
    dates = dates.strip()
    dates = dates.replace(".","/")
    dates = list(dates)
    start_date = dates[:10]
    end_date = dates[13:]
    start_date = ''.join(start_date)
    end_date = ''.join(end_date)
    
    name = name.strip()
    
    prize_money = prize_money.strip()
    prize_money = list(prize_money)
    if prize_money[0] == "$":
        currency = "USD"
        prize_money = prize_money[1:]
    elif prize_money[0] == "A":
        currency = "AUD"
        prize_money = prize_money[2:]
    else:    
        currency = "EUR"
        prize_money = prize_money[1:]
    
    prize_money = ''.join(prize_money)
    
    csv_writer.writerow([name,start_date,end_date,prize_money,currency])
    print(location)
    print(start_date)
    print(end_date)
    print(name)
    print(prize_money)
    print(currency)
    print()
    

csv_file.close()

    
    
          
