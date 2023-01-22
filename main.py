import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/chart/top/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

list_film=[]

all_movies = soup.find_all(class_="titleColumn")
for tag in all_movies:
    a = tag.text
    a = a.replace("\n"," " )
    a = a.replace("       "," ")
    list_film.append(a)

with open("movies.txt", mode="w") as file:
    for movie in list_film:
        file.write(f"{movie}\n")
