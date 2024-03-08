# Project pars-HDrezka

Pars-HDrezka is a script for gathering information from the HDrezka website, specifically from the "Latest Releases" section.

## Installing

1. Clone the repository from Git Hub: 
    `git clone https://github.com/Alexandr1123212545/pars-HDrezka.git`
2. Create virtual environment: 
   `python -m venv "your_venv"`
3. Activate virtal enviroment:
    `.\venv\Script\acrivate`
5. Install dependencies:
   `pip install -r requirements.txt`
6.  Determine the list of pages in main.py, specifying the first and last pages in the script:
       ```
    FIRST_PAGE = 'first page'
    LAST_PAGE = 'last page'
    ```
7. Run script!


As a result, you get a "movies.json" file. Each block describes one movie and contains information about its title, release year, country of production, genre, and a link to the movie's page on the website:
```
Example
{
'title': 'Way Home',
'year': '2013',
'country': 'South Korea',
'genre': 'Drama',
'link': 'https://rezka.ag/films/drama/68021-put-domoy-2013.html'
}

{
'title': 'House of Dracula',
'year': '1945',
'country': 'USA',
'genre': 'Science Fiction',
'link': 'https://rezka.ag/films/fiction/68060-dom-drakuly-1945.html'
}
```
