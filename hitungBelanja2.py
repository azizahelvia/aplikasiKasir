dompet_anda = input('Uang anda senilai Rp ' )
uang_anda = int(dompet_anda)

barang2 = {'Mie Ayam': 10000, 'Mie Ayam Bakso': 12000, 'Bakso': 8000}

for nama_barang in barang2:
    print('======================================')
    print('Anda membayar uang dengan Rp ' + str(uang_anda) + ' di dompet anda')
    print('Harga ' + nama_barang + ' Rp ' + str(barang2[nama_barang]))

    hitung_beli = input('Anda membeli ' + nama_barang + '?:')
    print('Anda akan membeli ' + hitung_beli +  ' ' + nama_barang)

    hitung = int(hitung_beli)
    total_harga = barang2[nama_barang] * hitung
    print('Harga total adalah Rp ' + str(total_harga))

    if uang_anda >= total_harga:
        print('Anda telah membeli ' + hitung_beli + ' ' + nama_barang)
        uang_anda -= total_harga

        if uang_anda == 0:
            print('Uang Anda pas tidak ada sisa')
            break

    else:
        print('Uang anda tidak mencukupi')
        print('Anda tidak bisa membeli' + nama_barang)

print('Uang Anda sisa Rp ' + str(uang_anda))    