import requests
import json
import seaborn as sns
from textblob import TextBlob

# Set seaborn theme and context
sns.set_theme()
sns.set_context("paper", rc={"font.size": 10, "axes.titlesize": 10})

def get_projects_from_github(language):
    """Fetches GitHub projects for a given programming language."""
    github_api_url = f'https://api.github.com/search/repositories?q=language:{language}'
    response = requests.get(github_api_url)
    response_dict = response.json()
    print(response_dict.keys())

def create_barplot_projects(projects, language):
    """Creates a barplot for the most popular GitHub projects of a given language."""
    github_api_url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars'
    response = requests.get(github_api_url)
    response_dict = response.json()
    projects = response_dict["items"]
    project_names = [project["name"] for project in projects]
    project_ratings = [project["stargazers_count"] for project in projects]
    barplot = sns.barplot(y=project_names, x=project_ratings)
    plot_title = f'Most Popular {language} Projects on GitHub'
    plot_filename = f'{language}_projects_ratings.png'
    barplot.set_title(plot_title)
    barplot.set_xlabel("Star Rating")
    barplot.figure.savefig(plot_filename, bbox_inches='tight')
    barplot.figure.clf()

# API for getting a random joke about chuck norris 
url_chuck_norris = 'https://api.chucknorris.io/jokes/random'

response_chuck_norris = requests.get(url_chuck_norris)
print(response_chuck_norris)
chuck_norris_dict = response_chuck_norris.json()
random_joke = chuck_norris_dict["value"]
print(chuck_norris_dict.keys())
print(random_joke)

text = TextBlob(random_joke)

text_german = text.translate(from_lang="en", to="de")
print(text_german)

# weather API for getting information about the weather
url_meteo = 'https://geocoding-api.open-meteo.com/v1/search?name=Fiestel&language=de&count=1'

user_input = input("Enter the name of the city: ")

url_meteo_result = f'https://geocoding-api.open-meteo.com/v1/search?name={user_input}&language=de&count=1'

url_meteo_response = requests.get(url_meteo_result)
meteo_dict = url_meteo_response.json()

lat = meteo_dict["results"][0]["latitude"]
lon = meteo_dict["results"][0]["longitude"]
print(f'The city {user_input} has latitude {lat} and longitude {lon}.')

url_meteo_temperature = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_min,temperature_2m_max&timezone=Europe/Berlin'
url_meteo_temperature_response = requests.get(url_meteo_temperature)
meteo_temperature_dict = url_meteo_temperature_response.json()

print(meteo_temperature_dict)

with open("meteo_temperature_dict.json", "w") as fh:
    json.dump(meteo_temperature_dict, fh, indent=4)

# get the min and max temperature for the day after tomorrow
day = meteo_temperature_dict["daily"]["time"][2]
min_temperature = meteo_temperature_dict["daily"]["temperature_2m_min"][2]
max_temperature = meteo_temperature_dict["daily"]["temperature_2m_max"][2]

print(f'On ({day}), the day after tomorrow, the temperature will range between {min_temperature}°C and {max_temperature}°C')