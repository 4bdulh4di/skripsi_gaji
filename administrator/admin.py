from django.contrib import admin
from .models import Guru, Detail_gaji, Piket, Tahun_pelajaran, Jam_pelajaran, Setting_gaji
admin.site.register(Guru)
admin.site.register(Detail_gaji)
admin.site.register(Piket)
admin.site.register(Tahun_pelajaran)
admin.site.register(Jam_pelajaran)
admin.site.register(Setting_gaji)
