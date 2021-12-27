# ngram
Получение данных xml API Яндекса (топ 10 юрл из выдачи), парсинг статей с топа и получение ngram<br>

Демонстрация работы с API XML яндекса https://xml.yandex.ru/<br>
Для работы скрипта нужны лимиты XML<br>
В https://xml.yandex.ru/settings/  находим строку вида https://yandex.ru/search/xml?user=login&key=03.39566772:381454f4e1e690d25288aca7<br>
Редактируем файл ini.txt<br>
Первая строка = login<br>
Вторая key вида = 03.39566772:381454f4e1e690d25288aca7<br>
Третья = нужный нам запрос.<br>
Рекомендация = для редактирования использовать UTF-8 (Notepad++ например)<br><br>

После получения топ 10 выдачи скрипт удаляет стоп  url и парсит статьи из оставшихся (только основной текст статей).<br>
После парсинга лематизирует с помощью Mystem https://yandex.ru/dev/mystem/ (для этого скачайте файл mystem.exe и добавьте в папку с проектом)<br>
И вычисляет топ ngram и записывает в файл название-запроса.csv (в UTF-8).<br>

