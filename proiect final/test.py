from tkinter import *
from tkinter import PhotoImage
from bs4 import BeautifulSoup
import time
import requests
import sqlite3
from datetime import datetime
import schedule


form = Tk()

button_y_pressed = 'false'


def message(message):
    label_info = Label(form,  text="", font=(
        'Patrick Hand', 10, 'bold'), fg='black', bg='yellow', justify='center', height=2, width=40)
    label_info.place(relx=0.04, rely=0.86)
    label_info.config(text=message)


def get_products(input_product_val, input_keywords_val):
    searchUrl = "http://www.emag.ro/search/" + \
        input_product_val + " " + input_keywords_val + "?ref=effective_search"

    print(searchUrl)
    page = requests.get(searchUrl)

    soup = BeautifulSoup(page.text, 'html.parser')

    products = soup.find_all("div", class_='card-item')

    first_four_products = products[:4]

    return first_four_products


def display_product(product_index, product_info, products, button_y, button_n):
    product_index += 1
    if product_index == 4:
        product_info.config(text='Product not found')
        return

    print(product_index)
    date = datetime.now().date()

    print(products[product_index])

    if products[product_index] is None:
        product_info.config(text='Product not found')
        return

    title = products[product_index].find(class_='card-v2-title').get_text()

    price = products[product_index].find(
        class_='product-new-price').get_text()
    url = products[product_index].find(class_='js-product-url').get('href')

    product_info.config(text=title + '\n' + price)
    button_y.config(command=lambda: insert_to_database(
        title, price, date, url))

    if product_index < 4:
        button_n.config(command=lambda: display_product(
            product_index, product_info, products, button_y, button_n))


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

    message("PRODUCT ADDED SUCCESSFULLY")

    button_y_pressed = 'true'

    conn.commit()
    conn.close()


def search(input_product, input_keywords, product_info,  button_y, button_n):

    input_product_val = input_product.get()
    input_keywords_val = input_keywords.get()

    date = datetime.now().date()

    if len(input_product_val) == 0:
        message("Please enter a product name.")
        return
    elif len(input_keywords_val) == 0:
        message("Please enter a product keywords.")
        return

    products = get_products(input_product_val, input_keywords_val)

    product_index = -1

    display_product(product_index, product_info, products, button_y, button_n)


def add_product():
    form.geometry("500x400")
    form.resizable(False, False)
    background_image = PhotoImage(file="test1.png")
    background_label = Label(form, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    form.title("Add new product")

    # Search product
    label = Label(form,  text="Search product", font=(
        'Castellar', 12, 'bold'), fg='white', bg='black', justify='center', height=2, width=15)
    label.place(relx=0.04, rely=0.05)

    label_line = Label(form, fg='white', bg='black',
                       justify='center', height=21, width=-2)
    label_line.place(relx=0.49, rely=0)

    product_name = Label(text="Product name")
    product_name.place(relx=0.04, rely=0.2)
    input_product = Entry(form)
    input_product.place(relx=0.04, rely=0.25, relwidth=0.3,
                        relheight=0.09)

    product_keywords = Label(text="Add keywords")
    product_keywords.place(relx=0.04, rely=0.4)
    input_keywords = Entry(form)
    input_keywords.place(relx=0.04, rely=0.45, relwidth=0.3,
                         relheight=0.09)

    button_search = Button(form, text="Search", font=(
        'Patrick Hand', 9),  relief=FLAT, bg='black', bd=2, fg='white', height=2, width=28, command=lambda: search(input_product, input_keywords, product_info,  button_y, button_n))
    button_search.place(relx=0.04, rely=0.6)

    # Display found product
    label2 = Label(form,  text="Product found", font=(
        'Castellar', 12, 'bold'), fg='white', bg='black', justify='center', height=2, width=15)
    label2.place(relx=0.52, rely=0.05)

    product_info = Label(text="Product name",
                         height=10, width=27, justify=LEFT, wraplength=150)
    product_info.place(relx=0.52, rely=0.2)

    button_y = Button(form, text="Yes", font=(
        'Patrick Hand', ),  relief=FLAT, bg='black', bd=2, fg='white', height=1, width=10)
    button_y.place(relx=0.8, rely=0.71)

    button_n = Button(form, text="No", font=(
        'Patrick Hand',),  relief=FLAT, bg='black', bd=2, fg='white', height=1, width=10)
    button_n.place(relx=0.56, rely=0.71)

    form.mainloop()


def main_form():
    form.geometry("500x400")
    form.resizable(False, False)
    background_image = PhotoImage(file="test1.png")
    background_label = Label(form, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    form.title("Market Study")
    label = Label(form,  text="Market research", font=(
        'Castellar', 26, 'bold'), fg='white', bg='black', relief="flat", justify='center', height=2, width=15)
    label.pack(expand=True)
    # Create the first button
    button1 = Button(form, text="Add new product", font=(
        'Patrick Hand', 15),  relief=FLAT, bg='black', bd=2, fg='white', height=2, width=30, command=add_product)
    button1.pack(side=TOP, padx=5, pady=5, expand=YES)
    button1.pack()

    # Create the second button
    button2 = Button(form, text="Analyze the existing products", font=(
        'Patrick Hand', 15),  relief=FLAT, bg='black', bd=2, fg='white', height=2, width=30)

    button2.pack()
    button2.pack(side=TOP, padx=1, pady=1, expand=YES)
    form.mainloop()


main_form()
