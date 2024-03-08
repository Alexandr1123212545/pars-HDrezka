import requests
from bs4 import BeautifulSoup
from time import sleep
import json


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
FIRST_PAGE = 1
LAST_PAGE = 5

for page in range(FIRST_PAGE, LAST_PAGE):
    url = f'https://rezka.ag/films/page/{page}/'
    r = requests.get(url, headers=headers)
    sleep(3)

    soup = BeautifulSoup(r.text, 'lxml')
    films = soup.findAll('div', class_='b-content__inline_item-link')

    for film in films:
        ycg = film.find('div').text.split(',') # Year Country Genre

        data = {
                'title': film.find('a').text,
                'year': ycg[0],
                'country': ycg[1].lstrip(),
                'genre': ycg[2].lstrip(),
                'link': film.find('a').get('href'),
            }
            
        with open('movies.json', 'a', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            json_file.write('\n')

    print(f'Page {page} ready!')
print('Done!')

