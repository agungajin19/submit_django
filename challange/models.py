from django.db import models

# Create your models here.
class Mentee(models.Model):
    nama = models.CharField(max_length=200, default='')
    foto = models.CharField(max_length=300)
    quote = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.nama


class Mentor(models.Model):
    nama = models.CharField(max_length=200)
    foto = models.CharField(max_length=300)
    quote = models.CharField(max_length=300, default='')
    experience = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.nama

class Blog(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.CharField(max_length=400, default='')
    foto = models.CharField(max_length=200)
    tanggal = models.DateField('Tanggal', auto_now=True)
    comment = models.IntegerField(default=0)

    def __str__(self):
        return self.judul