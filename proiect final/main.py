from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import sqlite3
from datetime import datetime
import schedule

product = ''
keywords = ''


def insert_to_database(title, price, date, url):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    table_name = 'products'
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    if cursor.fetchone():
        print('')
    else:
        cursor.execute(
            '''CREATE TABLE products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER, date, url TEXT)''')

    cursor.execute(
        "INSERT INTO products (name, price , date, url) VALUES (?, ?, ?, ?)", (title, price, date, url))

    conn.commit()
    conn.close()


def search_save_product(product, keywords):

    if product != "":
        date = datetime.now().date()
        searchUrl = "http://www.emag.ro/search/" + \
            product + " " + keywords + "?ref=effective_search"

        page = requests.get(searchUrl)
        soup = BeautifulSoup(page.text, 'html.parser')

        products = soup.find_all("div", class_='card-item')

        first_four_products = products[:4]

        answer = ''
        for s_product in first_four_products:
            title = s_product.find(class_='card-v2-title').get_text()
            price = s_product.find(
                class_='product-new-price').get_text()
            url = s_product.find(class_='js-product-url').get('href')

            answer = input(
                "This is the product are you looking for : " + title + "? [y/n]")

            if answer == 'y':
                print(title + ': ' + price)
                insert_to_database(title, price, date, url)
                break

        if answer == 'n':
            print("No product found.")


def product_market_research():

    decision = input(
        "If you want a market research with the existing products type 1. If you want to add products to the research type 2. ")

    if decision == "1":

        with open('market_study.py', 'r') as file:
            exec(file.read())

    elif decision == "2":
        product = input("What product are you looking for? ")
        keywords = input("Add keywords.. ")
        search_save_product(product, keywords)
    else:
        print('Try again')


product_market_research()
