from django.db import models

# Create your models here.
class Books(models.Model):
    tgl_cari = models.DateTimeField()
    keyword = models.CharField()
    url = models.URLField()
    judul = models.CharField()
    penulis = models.CharField()
    penerbit = models.CharField()
    isbn = models.CharField()
    tgl_terbit = models.DateField()
    jumlah_halaman = models.CharField()
    berat = models.CharField()
    img_source = models.URLField()
    rating = models.CharField()
    cover = models.CharField()


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.judul