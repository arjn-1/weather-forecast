import requests


res = requests.get("http://api.weatherapi.com/v1/current.json?key=writeyourlongandcoolkey&q=" + "delhi")
data = res.json()


def print_region():
    return data["location"]["region"]


def print_country():
    return data["location"]["country"]


def print_tz_id():
    return data["location"]["tz_id"]


def print_day():
    return data["current"]["condition"]["text"]


def print_tempinc():
    return data["current"]["temp_c"]


def print_tempinf():
    return data["current"]["temp_f"]


def print_windkph():
    return data["current"]["wind_kph"]


def print_windmph():
    return data["current"]["wind_mph"]


def direc_deg():
    return data["current"]["wind_dir"], data["current"]["wind_degree"]


