import requests
from bs4 import BeautifulSoup
from datetime import datetime

file_path = datetime.strftime(datetime.now(),"./scrap%Y-%m-%d_%H:%M:%S.txt" )

url = "http://okky.kr/articles/questions"

response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')
lists = soup.select('li.list-group-item')

f = open('file_path', 'w',encoding='utf-8')
data = ' '
for li in lists:
    a = li.find('h5').select_one('a')
    link =  a['href']
    list_id = link.split('/')[-1]
    title = a.text.strip()

    print(link,list_id,title)
    data += 'link : %s,id : %s,title : %s\n' % (link,list_id,title)
f.write(data)
f.close()