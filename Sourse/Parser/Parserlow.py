import requests
import json
from bs4 import BeautifulSoup as bs4

class Result:
    def __init__(self,
                 url: str):
        self.url = url


class YandexImage:
    def __init__(self):
        self.version = '1.0-modified'
        self.about = 'YandexImageSearcherLow'
        with open('./options.json', 'r') as o:
            self.options = json.load(o)
        self.black_list = self.options["black_list"]
        self.size = self.options["image_size"]
        self.search_type = self.options["type_of_search"]

    def check(self, image):
        for domen in self.black_list:
            if domen in image:
                return False
        if self.search_type is not None and self.search_type not in image:
            return False
        return True

    def search(self, query: str, num_page=1) -> list:
        next_page = requests.get('https://yandex.ru/images/search',
                                 params={"text": query,
                                         "isize": self.size,
                                         "p": num_page
                                         },
                                 headers={'Accept': '*/*', 'Connection': 'keep-alive',
                                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683 Safari/537.36',
                                          'Accept-Encoding': 'gzip, deflate, br', 'Cache-Control': 'max-age=0',
                                          'DNT': '1', 'Referer': 'https://google.com'})
        soup = bs4(next_page.text, 'html.parser')
        items_place = soup.find('div', {"class": "serp-list"})
        output = list()
        try:
            items = items_place.find_all("div", {"class": "serp-item"})
        except AttributeError:
            return output

        for item in items:
            data = json.loads(item.get("data-bem"))
            image = data['serp-item']['img_href']
            if self.check(image):
                output.append(Result(image))

        return output
