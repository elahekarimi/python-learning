# import requests
# from bs4 import BeautifulSoup
#
# URL = "https://www.empireonline.com/movies/features/best-movies-2"
# response = requests.get(URL)
# website_html = response.text
#
# soup = BeautifulSoup(website_html, "html.parser")
#
# all_movies = soup.find_all(name="h3", class_="title")
# move_title = [movie.gettext() for movie in all_movies]
#
# movies = move_title[::-1]
#
# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")

import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://www.empireonline.com/movies/features/best-movies-2/")
response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")
movies_name = soup.find_all(name="h3", class_="title")
movie_titles = [movie.text for movie in movies_name]

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_titles[::-1]:
        file.write(f"{movie}\n")
