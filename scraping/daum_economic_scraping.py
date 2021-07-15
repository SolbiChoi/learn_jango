from bs4 import BeautifulSoup
import requests

res = requests.get('http://media.daum.net/economic/')

import sqlite3

if res.status_code == 200:
    soup = BeautifulSoup(res.content, 'html.parser')
    links = soup.find_all('a', class_='link_txt')
    connect = sqlite3.connect('../db.sqlite3')
    cursor = connect.cursor()
    for link in links:
        title = str.strip(link.get_text())
        href = str.strip(link.get('href'))
        try:
            cursor.execute(
                "insert into polls_economics(create_date, href, title) values(datetime('now'), ?, ?)",(href,title))
            print(title,' : ', href)
        except:
            pass


    connect.commit()