from django.shortcuts import render
from administrator.models import Guru, Detail_gaji, Piket, Tahun_pelajaran, Jam_pelajaran, Setting_gaji
from django.contrib.auth.decorators import login_required
from administrator.decorators import ijinkan_pengguna
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth
from django.db.models import Sum

@login_required(login_url='halamanlogin')
@ijinkan_pengguna(yang_diizinkan=['guru'])
def berandaguru(request):
   
    context = {
        'judul': 'Halaman Guru',
        'menu': 'Guru',
      
    }
    return render(request, 'berandaguru.html', context)
def get_month_name(month_number):
    months = [
        "Januari", "Februari", "Maret", "April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ]
    return months[month_number - 1] if 1 <= month_number <= 12 else ""
@login_required(login_url='halamanlogin')
@ijinkan_pengguna(yang_diizinkan=['guru'])
def gajiguru(request):


    queryset = Detail_gaji.objects.all()
    
    

    queryset = queryset.values(
        'tahun_pelajaran__nama',
        'tahun_pelajaran__id',
        'guru__nama_guru',
        'guru__id',
        'tanggal__month',
    ).annotate(
        month=ExtractMonth('tanggal'),
        total_nominal=Sum('nominal')
    ).order_by(
        'tahun_pelajaran__nama',
        'guru__nama_guru',
        'month'
    )

    for entry in queryset:
        entry['month_name'] = get_month_name(entry['month'])
        
    context = {
        'data': queryset,
        'tahun_pelajarans': Tahun_pelajaran.objects.all(),
        'gurus': Guru.objects.all(),
        
        'bulan_choices': [(str(i), get_month_name(i)) for i in range(1, 13)],
        'judul': 'Halaman Data Gaji',
        'menu': 'Gaji',
    }
    return render(request, 'gajiguru.html', context)


@login_required(login_url='halamanlogin')
@ijinkan_pengguna(yang_diizinkan=['guru'])
def detailgajiguru(request, th, guru, bulan):
   
    idtahun = Tahun_pelajaran.objects.get(id=th)
    idguru = Guru.objects.get(id=guru)
    namabulan = get_month_name(int(bulan))
   
    data = Detail_gaji.objects.filter(tahun_pelajaran=th, guru=guru,tanggal__month=bulan)
    context = {
        'judul': 'Detail Gaji Guru',
        'menu': 'Rincian Gaji Guru',
        'data':data,
        'idtahun':idtahun,
        'idguru':idguru,
        'namabulan':namabulan
        
      
    }
    return render(request, 'tampildetailgajiguru.html', context)
