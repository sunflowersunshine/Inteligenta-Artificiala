from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import sqlite3
from datetime import datetime
import schedule


def study_market_research():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    table_name = 'products'
    cursor.execute('SELECT COUNT(*) FROM products')
    result = cursor.fetchone()

    if result[0] < 0:
        print("There are no product for analyze")
    else:
        cursor.execute("SELECT * FROM products")

        records = cursor.fetchall()

        for row in records:
            req = requests.get(row[4])
            soup = BeautifulSoup(req.text, "html.parser")

            price_element = soup.find(
                'p', attrs={'class': 'product-new-price'})
            if price_element:
                price = price_element.text
            else:
                price = None

            if row[2] != price:
                with open('study_market.txt', 'a') as f:
                    f.write('Pretul produsului' +
                            row[1] + 'a fost schimbat \n')
                    f.write('Pretul vechi \n' + row[2])
                    f.write('Pretul nou \n \n' + price)
            else:
                with open('study_market.txt', 'a') as f:
                    f.write('Pretul produsului' +
                            row[1] + 'nu a fost schimbat. \n')
                    f.write('Pretul este' + row[2])


study_market_research()
