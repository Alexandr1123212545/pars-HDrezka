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
6.  Determine the list of pages, specifying the first and last pages in the script:
       ```
    FIRST_PAGE = 'first page'
    LAST_PAGE = 'last page'
    ```
7. Run script!


As a result, you get a JSON file. Each block describes one movie and contains information about its title, release year, country of production, genre, and a link to the movie's page on the website.
