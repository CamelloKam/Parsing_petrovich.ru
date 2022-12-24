import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import xlsxwriter

book = xlsxwriter.Workbook(r"C:\Users\Марат\Desktop\Камиль\PY\data.xlsx")
page = book.add_worksheet("товар1")

row = 0
column = 0

page.set_column("A:A", 50)
page.set_column("B:B", 20)


for count in range(0, 8):
    url = f"https://petrovich.ru/catalog/12100/?p={count}"
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, "lxml")

    # тут находится для одной карточки
    data = soup.find("div", class_="main_container")
    kok = data.findAll("div", class_="fade-in-list")

    for i in kok:
        lol3 = i.find("a", class_="pt-link___JRuYu pt-link-primary___Am9vu pt-link-md___Yhrk7").text
        coin = i.find("p", class_="pt-price___c9u6v").text
        print(lol3)
        print(coin)
        page.write(row, column, lol3)
        page.write(row, column+1, coin)
        row += 1

book.close()














