from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register (Siswa)
admin.site.register (Guru)
admin.site.register (Karyawan)
