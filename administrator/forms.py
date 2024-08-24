from django import forms
from django.forms import ModelForm
from .models import Guru, Detail_gaji, Piket, Tahun_pelajaran, Jam_pelajaran, Setting_gaji
from django.contrib.auth.models import User

class DetailForm(ModelForm):
    class Meta:
        model = Detail_gaji
        fields=['tanggal','nominal']
        widgets = {
            'tanggal': forms.TextInput(attrs={'class': 'form-control','type':'date'}),
            'nominal': forms.TextInput(attrs={'class': 'form-control','placeholder':'Isi Nominal','type':'number'}),
        }
        
        
class SettingForm(ModelForm):
    class Meta:
        model = Setting_gaji
        fields=['tahun_pelajaran','nominal','aktif']
        widgets = {
            'tahun_pelajaran': forms.Select(attrs={'class': 'form-control'}),
            'nominal': forms.TextInput(attrs={'class': 'form-control','placeholder':'Isi Nominal','type':'number'}),
        }
class TahunForm(ModelForm):
    class Meta:
        model = Tahun_pelajaran
        fields=['nama','aktif']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control','placeholder':'Tahun Pelajaran'}),
        }
class JamForm(ModelForm):
    class Meta:
        model = Jam_pelajaran
        fields=['jam_ke','jam_pelajaran_dari_ke','aktif']
        widgets = {
            'jam_ke': forms.TextInput(attrs={'class': 'form-control','placeholder':'Jam Ke','type':'number'}),
            'jam_pelajaran_dari_ke': forms.TextInput(attrs={'class': 'form-control','placeholder':'Jam dari dan Ke'}),
            }
       
        
class GuruForm(ModelForm):
    class Meta:
        model = Guru
        fields=['nama_guru','jenis_kelamin','alamat','no_hp']
        widgets = {
            'nama_guru': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama Bendahara'}),
            'jenis_kelamin': forms.Select(attrs={'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control','placeholder':'Alamat'}),
            'no_hp': forms.TextInput(attrs={'class': 'form-control','type':'number','placeholder':'628xxxxxxxxxx'}),
    
        }
class PiketForm(ModelForm):
    class Meta:
        model = Piket
        fields=['nama_piket','jenis_kelamin','alamat','no_hp']
        widgets = {
            'nama_piket': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nama Piket'}),
            'jenis_kelamin': forms.Select(attrs={'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control','placeholder':'Alamat'}),
            'no_hp': forms.TextInput(attrs={'class': 'form-control','type':'number','placeholder':'628xxxxxxxxxx'}),
            
        }
        
class UserForm(ModelForm):
    class Meta:
        model= User
        fields =['username']
        help_texts ={
            'username':''
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','required':'required'}),
        }
        labels = {
            'username': 'Username*',
        }
        