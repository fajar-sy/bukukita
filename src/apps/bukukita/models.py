from django.db import models

# Create your models here.
class Books(models.Model):
    tgl_cari = models.DateTimeField()
    keyword = models.CharField(max_length=200)
    url = models.URLField()
    judul = models.CharField(max_length=200)
    penulis = models.CharField(max_length=200)
    penerbit = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    tgl_terbit = models.DateField()
    jumlah_halaman = models.CharField(max_length=200)
    berat = models.CharField(max_length=200)
    img_source = models.URLField()
    rating = models.CharField(max_length=200)
    cover = models.CharField(max_length=200)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.judul