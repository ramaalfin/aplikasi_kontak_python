daftar_kontak = []
def daftarMenu():
    print(30*('-'))
    print('Aplikasi Daftar Kontak')
    print(30*('-'))

    print('1. Lihat Kontak')
    print('2. Tambah Kontak')
    print('3. Hapus Kontak')
    print('4. Cari Kontak')
    print('0. Exit')

    menu = str(input('Pilih Menu : '))
    while True:
        if menu == '0':
            exit()
        elif menu == '1':
            lihatKontak(daftar_kontak)
            backMenu()
            break
        elif menu == '2':
            kontak = tambahKontak()
            daftar_kontak.append(kontak)
            backMenu()
            break
        elif menu == '3':
            hapusKontak(daftar_kontak)
            backMenu()
            break
        elif menu == '4':
            cariKontak(daftar_kontak)
            backMenu()
            break


def lihatKontak(daftar_kontak):
    if len(daftar_kontak) > 0:
        for kontak in daftar_kontak:
            print('\n')
            print(30*('-'))
            print(f"Nama : {kontak['nama']}")
            print(f"Telepon : {kontak['telepon']}")
            print(30*('-'))
    else:
        print('Belum Ada Kontak')


def tambahKontak():
    nama = str(input('Nama : '))
    telepon = int(input('Telepon : '))
    kontak = {
        "nama":nama,
        "telepon":telepon
    }
    print('Berhasil Menambahkan Kontak')
    return kontak


def hapusKontak(daftar_kontak):
    nama = str(input('Nama yang Akan Dihapus : '))
    isi = -1

    for index in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[index]
        if nama == kontak['nama']:
            isi = index
            break
    if isi == -1:
        print('Kontak Tidak Ditemukan')
    else:
        del daftar_kontak[isi]
        print('Berhasil Menghapus Kontak')


def cariKontak(daftar_kontak):
    cariNama = str(input('Nama : '))
    for kontak in daftar_kontak:
        nama = kontak['nama']
        if nama.find(cariNama) != -1:
            print('\n')
            print("Kontak Ditemukan")
            print(30*('-'))
            print(f"Nama : {kontak['nama']}")
            print(f"Telepon : {kontak['telepon']}")
            print(30*('-'))
            break
        elif nama.find(cariNama) == -1:
            print('Tidak Ada Kontak')


def backMenu():
    back = str(input('Balik ke Menu ? Ya/Tidak : '))
    if back == 'Ya' or back == 'ya':
        daftarMenu()
    elif back == 'Tidak' or back == 'tidak':
        print('Terima Kasih')

daftarMenu()