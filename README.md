# Navigation
- [Ru](https://github.com/Berlkot/Image-Lister#ru)
  - [Установка](https://github.com/Berlkot/Image-Lister#установка)
  - [Настройка](https://github.com/Berlkot/Image-Lister#настройка)
  - [Использование программы](https://github.com/Berlkot/Image-Lister#использование-программы)
  - [Ресурсы](https://github.com/Berlkot/Image-Lister#ресурсы)
- [En](https://github.com/Berlkot/Image-Lister#en)
  - [Installation](https://github.com/Berlkot/Image-Lister#installation)
  - [Setting](https://github.com/Berlkot/Image-Lister#setting)
  - [Using the program](https://github.com/Berlkot/Image-Lister#using-the-program)
  - [Resources used](https://github.com/Berlkot/Image-Lister#resources-used)
## Ru
Программка, создающая .txt с ссылками на картинки.

### Установка:
1. Устанавливаете нужную версию программы из [Релизов](https://github.com/Berlkot/Image-Lister/releases/)
2. Распакуйте архив куда вам удобно.

### Настройка:
Вся настройка происходит через options.json. Есть несколько пунктов настройки:
1. "black_list" - лист тех доменов или ссылок, которые игнорятся программой
2. "type_of_search" - настройка по пойску поределённых расширений файлов(изначально null)
3. "image_size" - размер искомых картинок
4. "delay" - задержка между запросами, неодходимая для предотвращения проверки капчи (гораздо проще подождать 10 секунд после каждого запроса, чем после пяти запросов получить капчу в лицо на 30 минут :smirk:)

### Использование программы:
После открытия исполняемого файла, вам будет предложено ввести поисковый запрос (те картинки, которые в итоге надо получить). Программа работает достаточно долго, так что советую запастись терпением.

На выходе вы получите папку, которая будет находится рядом с исполняемым файлом. В ней будет находится весь выход программы (.txt файлы с ~1200 ссылками)

### Использованые ресурсы:
- Официальный сайт [ЯндексКартинок](https://yandex.ru/images/)
- Библиотека с [Оригинальным Парсером](https://github.com/Ulbwaa/YandexImagesParser)

## En
A program that creates a .txt with links to pictures.

### Installation:
1. Install the required version of the program from [Releases](https://github.com/Berlkot/Image-Lister/releases/)
2. Unpack the archive wherever you like.

### Setting:
All customization happens through options.json. There are several configuration items:
1. 'black_list' - a list of those domains or links that are ignored by the program
2. 'type_of_search' - setting for searching for specific file extensions (null by default)
3. 'image_size' - the size of the desired images
4. 'delay' - the delay between requests, which is necessary to prevent captcha checking (it is much easier to wait 10 seconds after each request than after five requests get captcha into face for 30 minutes :smirk:)

### Using the program:
After opening the executable file, you will be needed to enter a search query (those pictures that you want to get in the end). The program works long enough, so I advise you to be patient.

As a result, you will get a folder that will be located next to the executable file. It will contain the entire output of the program (.txt files with ~1200 links)

### Resources used:
- Official site of [Yandex Pictures](https://yandex.ru/images/)
- Original Parser [library](https://github.com/Ulbwaa/YandexImagesParser)
