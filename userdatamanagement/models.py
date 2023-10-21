from django.db import models
from django.core.validators import RegexValidator

import os
from uuid import uuid4

def rename_uploaded_image (instance, filename):
    ext = filename.split ('.')[-1]
    new_filename = f'{uuid4()}.{ext}'
    return os.path.join ('/images', new_filename)


alphabeth = RegexValidator (r'^[a-zA-Z]*$')
numeric = RegexValidator (r'^[0-9]*$')

JENIS_KELAMIN = [("L","Laki-Laki"),("P","Perempuan")]

class Siswa (models.Model):
    import datetime
    year = datetime.datetime.now().year

    nama = models.CharField(max_length = 50, validators = [alphabeth])
    jenis_kelamin = models.CharField (max_length = 2, choices = JENIS_KELAMIN, default = JENIS_KELAMIN[0])
    NIK = models.CharField(max_length = 30, validators = [numeric], unique = True)
    NIS = models.CharField(max_length = 30, validators = [numeric], unique = True)
    NISN = models.CharField(max_length = 30, validators = [numeric], unique = True)
    alamat = models.CharField(max_length = 200)
    tempat_lahir = models.CharField(max_length = 100)
    tanggal_lahir = models.DateField("tanggal lahir")
    email = models.CharField(max_length = 50, unique = True)
    no_telepon = models.CharField(max_length = 15, validators = [numeric])
    nama_ayah_kandung = models.CharField(max_length = 50, validators = [alphabeth])
    nama_ibu_kandung = models.CharField(max_length = 50, validators = [alphabeth])
    tahun_masuk = models.PositiveIntegerField(default = year)
    tahun_keluar = models.PositiveIntegerField(blank = True, null = True)
    foto = models.ImageField (upload_to = rename_uploaded_image, null = True)
    print ("========", rename_uploaded_image)
    nama_wali = models.CharField (max_length = 50, validators = [alphabeth])
    jenis_kelamin_wali = models.CharField (max_length = 2, choices = JENIS_KELAMIN, default = JENIS_KELAMIN[0])
    NIK_wali = models.CharField(max_length = 30, validators = [numeric])
    alamat_wali = models.CharField(max_length = 200)
    tempat_lahir_wali = models.CharField(max_length = 100)
    tanggal_lahir_wali = models.DateField("tanggal lahir wali")
    email_wali = models.CharField(max_length = 50, unique = True)
    no_telepon_wali = models.CharField(max_length = 15, validators = [numeric])

    class Meta:
        ordering = ('nama',)

    def __str__(self):
        return "Siswa"

class Guru (models.Model):
    import datetime
    year = datetime.datetime.now().year

    nama = models.CharField(max_length = 50, validators = [alphabeth])
    jenis_kelamin = models.CharField (max_length = 2, choices = JENIS_KELAMIN, default = JENIS_KELAMIN[0])
    NIK = models.CharField(max_length = 30, validators = [numeric])
    alamat = models.CharField(max_length = 200)
    tempat_lahir = models.CharField(max_length = 100)
    tanggal_lahir = models.DateField("tanggal lahir")
    email = models.CharField(max_length = 50, unique = True)
    no_telepon = models.CharField(max_length = 15, validators = [numeric])
    tahun_masuk = models.PositiveIntegerField(default = year)

    class Meta:
        ordering = ('nama',)

    def __str__(self):
        return "Guru"

class Karyawan (models.Model):
    import datetime
    year = datetime.datetime.now().year

    nama = models.CharField(max_length = 50, validators = [alphabeth])
    jenis_kelamin = models.CharField (max_length = 2, choices = JENIS_KELAMIN, default = JENIS_KELAMIN[0])
    NIK = models.CharField(max_length = 30, validators = [numeric])
    alamat = models.CharField(max_length = 200)
    tempat_lahir = models.CharField(max_length = 100)
    tanggal_lahir = models.DateField("tanggal lahir")
    email = models.CharField(max_length = 50, unique = True)
    no_telepon = models.CharField(max_length = 15, validators = [numeric])
    tahun_masuk = models.PositiveIntegerField(default = year)

    class Meta:
        ordering = ('nama',)

    def __str__(self):
        return "Siswa"
