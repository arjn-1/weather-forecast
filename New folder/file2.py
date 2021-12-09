import requests
import random


def word_of_day():
    words_list = ["ambition", "restaurateur", "Disneyfy", "fustian", "celerity", "satori", "enlightenment", "encomium", "spangle", "neophyte"]
    ran = random.choice(words_list)
    return ran


base_url = "https://od-api.oxforddictionaries.com/api/v2/entries/en-us/" + word_of_day()
ids = "write your ids"
key = "write your long and cool key"

result = requests.get(url=base_url, headers={"app_id": ids, "app_key": key})
data = result.json()


def print_word():
    wor = data["id"]
    return wor


def print_meaning():
    meaning = data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
    return meaning

