
import urllib.request
from PIL import Image
import requests


def print_all_icons():
    """function that print all the icon's name"""
    response = requests.get('https://api.github.com/emojis')
    try:
        if response.status_code == 200:
            emojis = response.json()
            for emoji_name, emoji_url in emojis.items():
                print(f'{emoji_name}')
        else:
            raise requests.HTTPError('Failed to retrieve emojis:', response.status_code)
    except requests.HTTPError as e:
        print("HTTPError:",e)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


def search_icons_by_keyword(str):
    """this func search all the icons that match your keyword the func return list of search results"""
    try:
        response = requests.get('https://api.github.com/emojis')
        response.raise_for_status()
        emojis = response.json()
        emojis_filter = list(filter(lambda x: x.startswith(str), emojis))
        if len(emojis_filter) == 0:
            print('No results were found for your search.....')
        else:
            print('Icons matching your search:')
            print([x for x in emojis_filter])
            return emojis_filter
    except requests.exceptions.RequestException as e:
        print("Error:", e)


def display_icon(icon_name,arr):
    """Displays the icon according to the name sent"""
    if icon_name not in arr:
        raise ValueError('The entry does not match your search list')
    icon_url = find_url(icon_name)
    urllib.request.urlretrieve(
        f'{icon_url}',
        f"{icon_name}")
    img = Image.open(f"{icon_name}")
    img.show()


def find_url(icon_name):
    """The function returns the URL of the icon name"""
    response = requests.get('https://api.github.com/emojis')
    if response.status_code == 200:
        emojis = response.json()
        for emoji_name, emoji_url in emojis.items():
            if emoji_name == icon_name:
                    return emoji_url
    else:
        raise requests.HTTPError('Failed to retrieve emojis:', response.status_code)