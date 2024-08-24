from django.shortcuts import render,redirect
from administrator.models import Guru, Detail_gaji, Piket, Tahun_pelajaran, Jam_pelajaran, Setting_gaji
from administrator.forms import DetailForm
from django.contrib.auth.decorators import login_required
from administrator.decorators import ijinkan_pengguna
from django.db.models import Sum
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth

@login_required(login_url='halamanlogin')
@ijinkan_pengguna(yang_diizinkan=['piket'])
def berandapiket(request):
   
    context = {
        'judul': 'Halaman Piket',
        'menu': 'Piket',
      
    }
    return render(request, 'berandapiket.html', context)

@login_required(login_url='halamanlogin')
@ijinkan_pengguna(yang_diizinkan=['piket'])
def kelolagaji(request):
    jam = Jam_pelajaran.objects.filter(aktif=True).order_by('jam_ke')
    guru = Guru.objects.order_by('-id')
    tahun = Tahun_pelajaran.objects.order_by('-id')
    context = {
        'judul': 'Halaman Kelola Gaji',
        'menu': 'Kelola Gaji',
        'data':jam,
        'guru':guru,
        'tahun':tahun
      
    }
    return render(request, 'kelolagaji.html', context)

def get_month_name(month_number):
    months = [
        "Januari", "Februari", "Maret", "April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ]
    return months[month_number - 1] if 1 <= month_number <= 12 else ""
@login_required(login_url='halamanlogin')
@ijinkan_pengguna(yang_diizinkan=['piket'])
def simpankelolagaji(request):
    if request.method == "POST":
        idjam = request.POST.getlist('id[]')
        guru = request.POST.get('guru')
        tanggal = request.POST.get('tanggal')
        tahun = request.POST.get('tahun')
        
        
        idguru= Guru.objects.get(pk=guru)
        idtahun= Tahun_pelajaran.objects.get(pk=tahun)
        gajijam= Setting_gaji.objects.get(tahun_pelajaran__id=idtahun.id)
       
       
        for row in idjam:
            iddetailjam= Jam_pelajaran.objects.get(pk=row)
            simpan = Detail_gaji.objects.create(tahun_pelajaran=idtahun)
            simpan.guru = idguru
            simpan.jam_pelajaran = iddetailjam
            simpan.tanggal = tanggal
            simpan.nominal = gajijam.nominal
            simpan.save()
        return JsonResponse({'status': 'Save' })
    else:
        return JsonResponse({'status' : 0})

@login_required(login_url='halamanlogin')
@ijinkan_pengguna(yang_diizinkan=['piket'])
def gajipiket(request):
    tahun_pelajaran_id = request.GET.get('tahun_pelajaran')
    guru_id = request.GET.get('guru')
    bulan = request.GET.get('bulan')

    queryset = Detail_gaji.objects.all()
    
    if tahun_pelajaran_id:
        queryset = queryset.filter(tahun_pelajaran_id=tahun_pelajaran_id)
    
    if guru_id:
        queryset = queryset.filter(guru_id=guru_id)
    
    if bulan:
        queryset = queryset.filter(tanggal__month=bulan)

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
        'selected_tahun_pelajaran': tahun_pelajaran_id,
        'selected_guru': guru_id,
        'selected_bulan': bulan,
        'bulan_choices': [(str(i), get_month_name(i)) for i in range(1, 13)],
        'judul': 'Halaman Data Gaji',
        'menu': 'Gaji',
    }
    return render(request, 'gajipiket.html', context)


@login_required(login_url='halamanlogin')
@ijinkan_pengguna(yang_diizinkan=['piket'])
def detailgajipiket(request, th, guru, bulan):
   
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
    return render(request, 'tampildetailgajipiket.html', context)


@login_required(login_url='halamanlogin')
@ijinkan_pengguna(yang_diizinkan=['piket'])
def editdetailgajipiket(request, pk):
    detail = Detail_gaji.objects.get(id=pk)
    form = DetailForm(instance=detail)
    if request.method == 'POST':
        formsimpan = DetailForm(request.POST, instance=detail)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('detailgajipiket', detail.tahun_pelajaran.id, detail.guru.id, detail.tanggal.month)
    context = {
        'judul': 'Edit Gaji Guru',
        'menu': 'Rincian Gaji Guru',
        'form':form,
        'detail':detail
    }
    return render(request, 'editdetailgajipiket.html', context)


@login_required(login_url='halamanlogin')
@ijinkan_pengguna(yang_diizinkan=['piket'])
def deletedetailgajipiket(request, pk):
    hapus = Detail_gaji.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('detailgajipiket', hapus.tahun_pelajaran.id, hapus.guru.id, hapus.tanggal.month)

    context = {
         'judul': 'Hapus Gaji Guru',
        'menu': 'Rincian Gaji Guru',
        'hapus':hapus  
    }
    return render(request, 'deletedetailgajipiket.html', context)




