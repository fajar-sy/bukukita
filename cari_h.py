import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sqlite3
import pandas as pd
from cari_details import get_details


def cari_buku(url,headers,cari):

    driver = webdriver.Chrome()
    driver.get(url)

    # Input Text to Search bar
    driver.find_element(By.NAME,'key').send_keys(cari)
    driver.find_element(By.NAME,'key').send_keys(Keys.ENTER)

    # wait 3s while the page loading
    time.sleep(3)

    # get search pages
    curr_url = driver.current_url + '?page=1&id=1&key=' + cari + '&match=2'
    driver.get(curr_url)
    res = requests.get(curr_url)
    # print(curr_url)
    options = Options()
    options.add_argument("--enable-javascript")
    options.add_argument(f'user-agent={headers}')
    book_id = 0
    tgl_cari = datetime.datetime.now()

    while True:
       current_page_number = int(driver.find_element(By.CSS_SELECTOR, 'li.active').text)
       # print(f"Processing page {current_page_number}")
       # print(curr_url)

        # access the search page for those keywords and accessing each page
       try:
           soup = BeautifulSoup(res.text, 'html.parser')
           items = soup.findAll('div', {'class': 'product-preview-wrapper'})
           books_data = []
           url_det = ''

           # extract link of each books from every pages
           for item in items:
               link_books = item.find('div', {'class': 'ellipsis'})
               link_books1 = link_books.find('a')
               links_book = url + link_books1['href']

               url_det = links_book
               book_id = book_id + 1
               # print('Book ID : ' + str(book_id) + ', Link Detail : ' + links_book)
               get_details(book_id, url_det, headers, tgl_cari, cari)

           next_page = str(current_page_number + 1)
           next_page_link = driver.find_element(By.LINK_TEXT, next_page).send_keys(Keys.ENTER)
           curr_url = driver.current_url + '?page=' + str(current_page_number) + '&id=1&key=' + cari + '&match=2'
           driver.get(curr_url)
           res = requests.get(curr_url)
           # print(curr_url)

           print('Save Completed.')

       except NoSuchElementException:
            print(f"Exiting. Last page: {current_page_number}.")
            break


if __name__ == '__main__':

    url = 'https://www.bukukita.com/'
    cari = 'Python'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    cari_buku(url, headers, cari)

    conn = sqlite3.connect('bukukita.db')
    c = conn.cursor()
    df = pd.read_sql_query("SELECT * FROM books",conn)
    print(df)
    conn.close()
