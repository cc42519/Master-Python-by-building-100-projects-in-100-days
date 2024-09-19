import requests
from bs4 import BeautifulSoup

combined_movies = []

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
all_movies_year = soup.find_all(name="strong")
print(all_movies)
print(all_movies_year)


for count in range(len(all_movies_year)):
    D = {'title': all_movies[count].getText(),
         'year': all_movies_year[count].getText()}
    combined_movies.append(D)

print(combined_movies)

with open("movies.txt", mode="w") as file:
    for movie in combined_movies:
      file.write(f"{movie}\n")
