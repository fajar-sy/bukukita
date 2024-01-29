import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import sqlite3
import pandas

def get_details(book_id, url_det, headers, tgl_cari, cari):

    res = requests.get(url_det, headers=headers)
    # print(res.url_det)

    soup = BeautifulSoup(res.text, 'html.parser')

    bukus = []
    buku = soup.find('div', {'class': 'product-info col-sm-9 col-md-8'})
    items = buku.find_all('div',{'class':'col-xs-5 col-md-3'})

    # Extract the Books
    for item in items:
        val1 = item.find_next()
        val = val1.text.strip()
        val = re.sub(" ","",val)
        # print(item.text + ' : ' + val)

        # bukus.append({
        #     'item':item.text.strip(),
        #     'val': val
        # })
        # bukus.append(val)
        if item.text.strip() == 'Judul':
            judul = val
        if item.text.strip() == 'Penulis':
            penulis = val
        if item.text.strip() == 'No. ISBN':
            no_isbn = val
        if item.text.strip() == 'Penerbit':
            penerbit = val
        if item.text.strip() == 'Tanggal terbit':
            tgl_terbit = val
        if item.text.strip() == 'Jumlah Halaman':
            jml_hal = val
        if item.text.strip() == 'Berat':
            berat = val
        if item.text.strip() == 'Jenis Cover':
            cover = val
        if item.text.strip() == 'Dimensi(L x P)':
            dimensi = val
        if item.text.strip() == 'Kategori':
            kategori = val
        if item.text.strip() == 'Bonus':
            bonus = val
        if item.text.strip() == 'Text Bahasa':
            bahasa = val
        if item.text.strip() == 'Lokasi Stok':
            lokasi = val

    try:
        img_source = soup.find('div', {'class':'product-main-image__item'}).find('img')['src']
    except:
        img_source = '-'

    try:
        rating = soup.find('div',{'itemprop':'aggregateRating'}).find('span', {'itemprop':'reviewCount'}).text
    except:
        rating = '-'

    try:
        harga = soup.find('div', {'class':'price-box product-info__price'}).find('span',{'class':'price-box__new'}).text
    except:
        harga = '-'

    try:
        des = soup.find('div', {'id': 'Tab1'}).find('h2',{'class':'midnight-city'}).find_next('div',{'align':'justify'}).text.strip()
    except:
        des = '-'

    # val = img + ', ' + rating + ', ' + harga + ', ' + des

    # print('Image Source : ' + img)
    # print('Rating : ' + rating)
    # print('Harga : ' + harga)
    # print(' Description ' : ' + val)
    #
    # bukus.append({
    #     'item':des,
    #     'val': val
    # })
    # bukus.append(val)
    # print(bukus)
    # print(book_id, tgl_cari, cari, url_det, judul,  penulis, no_isbn, penerbit, tgl_terbit, jml_hal, berat, cover, dimensi, kategori, bonus, bahasa, lokasi, img_source, rating, harga, des)


    # save to Database bukukita.db and Table books
    conn = sqlite3.connect('bukukita.db')
    c = conn.cursor()
    c.execute('''INSERT INTO books VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
              (book_id, tgl_cari, cari, url_det, judul,  penulis, no_isbn, penerbit, tgl_terbit, jml_hal, berat, cover, dimensi,
               kategori, bonus, bahasa, lokasi, img_source, rating, harga, des))

    conn.commit()
    conn.close()
    print('Save Completed. Book ID: ' + str(book_id))
    # conn.execute('''SELECT * FROM books''')
    # res_db = c.fetchall()
    # print(res_db)

