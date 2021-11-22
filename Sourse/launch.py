from Parser.Parserlow import YandexImage
import time
import os
import json

print('---------------------------------')
print('python yandex images lister started its work')
print('---------------------------------')


def launch():
    request_words = input("Input search words: ")

    def list_created_check(number):
        if not os.path.exists('./imlinks'):
            os.makedirs('./imlinks')
        directory = os.listdir('./imlinks')
        file = request_words + ("(" + str(number) + ")") * ((number > 0) - (number < 0)) + '.txt'
        if file in directory:
            return list_created_check(number + 1)
        else:
            return './imlinks/' + file

    def options_check():
        if 'options.json' in os.listdir('./'):
            pass
        else:
            print('Error: No options.json')
            print('Restoring to default...')
            with open('./options.json', 'w', encoding='utf-8') as o:
                data = {"black_list": ["narvii", "memestatic.fjcdn.com", "pngkey", "scontent-hel3-1.cdninstagram",
                                       "images-wixmp", "static.zerochan", "images-eds-ssl.xboxlive", "d.furaffinity",
                                       "www.seekpng", "steamuserimages", "artist-oil.ru", "derpicdn.net",
                                       "e7.pngegg.com", "static.vecteezy.com", "yt3.ggpht.com", "wallpaperscraft.ru",
                                       "www.pngkey.com", "mocah.org", "www.kindpng.com", "wallpapersmug.com",
                                       "www.wallpapertip.com", "zerochan.net", "www.pikpng.com", "oir.mobi",
                                       "hdwallsbox.com", "safebooru.org", "catherineasquithgallery.com", "mimer.ru",
                                       "get.pxhere.com", "edyal.ru", "www.anypics.ru", "krasivosti.pro", "nastol.net",
                                       "www.fonstola.ru", "www.zastavki.com", "dogcatdog.ru", "get.wallhere.com",
                                       "furry"], "type_of_search": None, "image_size": "large", "delay": 60}
                json.dump(data, o, indent=4, ensure_ascii=False)

    options_check()
    file = list_created_check(0)
    parser = YandexImage()
    for i in range(50):
        i = i + 1
        try:
            images = []
            for item in parser.search(request_words, num_page=i):
                images.append(item.url)
            with open(file, 'a') as f:
                for image in images:
                    f.write(image + '\n')
            if i != 50:
                print(f'{i}/50 request was complited.')
                with open('./options.json', 'r', encoding='utf-8') as o:
                    options = json.load(o)
                    delay = options["delay"]
                    if delay < 10:
                        print('Warning: Setting delay less than 10 can lead to "captcha block"')
                        time.sleep(4)
                print(f'waiting {delay} seconds to avoid captcha check...')
                time.sleep(delay)
        except Exception as e:
            print(f'Something went wrong during accessing {i} request: ')
            print(f"""Error:
{e}""")
    print('---------------------------------')
    print('Finished')


launch()
while True:
    a = input('One more time? Y/N: ')
    if a == 'Y' or a == 'y' or a == 'yes' or a == 'да' or a == "д":
        print('---------------------------------')
        launch()
    else:
        os._exit(0)
