from bs4 import BeautifulSoup
import requests
import sqlite3
from sys import argv


def parse_value(value, currency='pound'):
    '''Function parse value of footballer from str to float, second argument'''
    # new_value = int(value.strip().replace('£','').replace('k','000').replace('m','000000').replace('.',''))
    if currency == 'pound':
        value = value.replace(',','.')
        new_value = float(value[1:-1])*1000 if value[-1] == 'k' else float(value[1:-1])*1000000
        return int(new_value)
    elif currency == 'euro':
        value = value.replace(',','.')
        new_value = float(value[1:-1])*1000 if value[-1] == 'k' else float(value[1:-1])*1000000
        new_value = new_value*1.11
        return int(new_value)

# print(parse_value('$3.1m','euro'))
# print(parse_value('£10k','euro'))

def parse_table():
    page = requests.get(URL).text
    soup = BeautifulSoup(page, 'html.parser')

    for table in soup.find_all('table', class_='tableizer-table'):
        # print(table.find_all('td'))
        for i, item in enumerate(table.find_all('td')):
            # print(item.text, i)
            no_attr = 7
            item = item.text
            if i % no_attr == 0:
                if item == '1':
                    break
                else:
                    name = item
            elif i % no_attr == 1:
                age = item
            elif i % no_attr == 2:
                club = item
            elif i % no_attr == 3:
                position = item
            elif i % no_attr == 4:
                cr = item
            elif i % no_attr == 5:
                pr = item
            else:
                value = parse_value(item, 'euro')
                print(f'{name}_{age}_{club}_{position}_{cr}_{pr}_{value}')
                cursor.execute('''INSERT INTO young_players_fifa20 VALUES (?,?,?,?,?,?,?)''',
                               (name, age, club, position, cr, pr, value))
                db.commit()
        print('\n\n NEW TABLE')

URL = 'https://www.goal.com/en/news/fifa-20-best-young-players-career-modes-top-strikers-midfielders-/14t4h24w35v3z19593a0xxdh36'

db = sqlite3.connect('fifa20youngplayers.db')
cursor = db.cursor()

if len(argv) > 1 and argv[1] == 'setup':
    cursor.execute('''CREATE TABLE young_players_fifa20 
    (
    NAME TEXT,
    AGE INTEGER ,
    CLUB TEXT,
    POSITION TEXT,
    CR INTEGER,
    PR INTEGER,
    VALUE REAL
    )''')

parse_table()

db.close()