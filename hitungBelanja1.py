harga_apel = 3000
punya_uang = input('Anda punya uang berapa:Rp  ')
barang_beli = input('Anda membeli: ')

hitung_beli = int(barang_beli)
uang_beli = int(punya_uang)
total_harga = harga_apel * hitung_beli

print('Anda akan membeli ' + str(hitung_beli) + ' apel')
print('Harga total adalah ' + str(total_harga) + ' Rupiah')

if uang_beli > total_harga:
    print('Anda telah membeli ' + str(hitung_beli) + ' buah apel')
    print('Sisa uang anda ' + str(uang_beli - total_harga) + ' Rupiah')

elif uang_beli == total_harga:
    print('Anda telah membeli ' + str(hitung_beli) + ' buah apel')
    print('Sisa uang anda tidak ada')

else:
    print('Uang Anda tidak mencukupi')
    print('Anda tidak dapat membeli apel')    