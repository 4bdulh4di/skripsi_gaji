from django.db import models
from django.contrib.auth.models import User


class Piket(models.Model):
    Jk=(
        ('Laki-laki','Laki-laki'),
        ('Perempuan','Perempuan')
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama_piket = models.CharField(max_length=200, blank=True, null=True)
    jenis_kelamin = models.CharField(max_length=200, blank=True, null=True, choices=Jk)
    alamat = models.TextField (blank=True, null=True)
    no_hp =  models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nama_piket
    class Meta:
        verbose_name_plural ="Piket"

class Tahun_pelajaran(models.Model):
    nama = models.CharField(max_length=200, blank=False, null=True)
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural ="Tahun Pelajaran"


class Guru(models.Model):
    Jk=(
        ('Laki-laki','Laki-laki'),
        ('Perempuan','Perempuan')
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama_guru = models.CharField(max_length=200, blank=True, null=True)
    jenis_kelamin = models.CharField(max_length=200, blank=True, null=True, choices=Jk)
    alamat = models.TextField (blank=True, null=True)
    no_hp =  models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.nama_guru
    class Meta:
        verbose_name_plural ="guru"
        
        
class Jam_pelajaran(models.Model):
    jam_ke = models.CharField(max_length=200, blank=False, null=True)
    jam_pelajaran_dari_ke= models.CharField(max_length=200, blank=False, null=True)
   
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.jam_pelajaran_dari_ke
    class Meta:
        verbose_name_plural ="Jam Pelajaran"
        
class Setting_gaji(models.Model):
    tahun_pelajaran = models.ForeignKey(Tahun_pelajaran, null=True, blank=True, on_delete=models.SET_NULL)
    nominal = models.PositiveIntegerField(blank=False, null=True)
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.tahun_pelajaran.nama
    class Meta:
         verbose_name_plural ="Setting Gaji"



     
class Detail_gaji(models.Model):
    tahun_pelajaran = models.ForeignKey(Tahun_pelajaran, null=True, blank=True, on_delete=models.SET_NULL)
    jam_pelajaran = models.ForeignKey(Jam_pelajaran, null=True, blank=True, on_delete=models.SET_NULL)
    guru = models.ForeignKey(Guru, null=True, blank=True, on_delete=models.SET_NULL)
    tanggal = models.DateField(max_length=200, blank=False, null=True)
    nominal = models.PositiveIntegerField(blank=False, null=True)
   
    def __str__(self):
        return self.guru.nama_guru
    class Meta:
         verbose_name_plural ="Detail Gaji"