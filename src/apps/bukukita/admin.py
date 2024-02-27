from django.contrib import admin

from apps.bukukita.models import Books

# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display = (
        'tgl_cari',
        'keyword',
        'url',
        'judul',
        'penulis',
        'penerbit',
        'isbn',
        'tgl_terbit',
        'jumlah_halaman',
        'berat',
        'img_source',
        'rating',
        'cover',
    )

admin.site.register(Books, BooksAdmin)
