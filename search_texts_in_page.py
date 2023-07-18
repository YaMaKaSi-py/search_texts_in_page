import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# URL страницы для сканирования
url = input("Введите ссылку на страницу: \n")

# Настройка браузера
options = Options()
#options.add_argument('--headless') #уберите '#' для отображения браузера
driver = webdriver.Chrome(options=options)

# Получение HTML страницы
driver.get(url)
time.sleep(10)
html = driver.page_source

# Чтение файлов
with open("texts.txt", "r") as f:
    search_texts = [line.strip() for line in f]

found_texts = []

# Поиск текста на странице
for text in search_texts:
    if text in html:
        found_texts.append(text)

# Запись найденного текста в файл
with open("found.txt", "w") as f:
    for text in found_texts:
        f.write(text + "\n")

driver.quit()

input("Программа закончил работу, нажмите Enter чтобы выйти ")