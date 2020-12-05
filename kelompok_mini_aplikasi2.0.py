## Tugas Mini Aplikasi
## JCAH Data Science
## Karina Anggraeni - Mega Alam

# Data
data = ['bayam', 'kangkung', 'bawang', 'kangkung', 'sawi', 'wortel', 'bayam', 'terong', 'wortel', 'kentang', 'terong', 'selada']

#---------------------------------------------------------------------------------------------------#
# Welcome
print('Selamat datang di aplikasi Sayur-Mayur! Silahkan login terlebih dahulu.\n')

# Login
password = 'hai'
login = ''
trial = 1
limit = 4

while login != password and trial <= limit:
    if trial <= limit:
        login = input('Masukkan password: ')
        if login != password and trial < limit:
            print('Password salah. Sisa kesempatan: {} kali.'.format(limit - trial))
            trial += 1
        elif login != password and trial == limit:
            print('Password salah. Kesempatan habis.')
            trial += 1
            exit()
        else:
            print("Password benar.\n")

#---------------------------------------------------------------------------------------------------#
# Mini Menu
def mini_menu():
    print('\nAda lagi yang bisa Sayur-Mayur lakukan untuk Anda?')
    print('1. Kembali ke menu utama')
    print('2. Kembali ke menu sebelumnya')

#---------------------------------------------------------------------------------------------------#
# Menu Utama
user_input = ''

def menu_utama():
    print('\nApa yang bisa Sayur-Mayur lakukan untuk Anda? Sayur-Mayur dapat membantu Anda dalam: ')
    print('1. Mencetak data persediaan barang')
    print('2. Menambahkan data persediaan barang')
    print('3. Memperbaharui data persediaan barang')
    print('4. Menghapus data persediaan barang')
    print('5. Keluar')

    menu_input = input('Silahkan ketik nomor pilihan menu yang Anda inginkan. ')
    
    if menu_input == '1':
        # Read
        def read():
            if len(data) != 0:
                print('Persediaan barang di Sayur-Mayur:')
                for i in data:
                    print(str('- ') + i)
            else:
                print('Daftar persediaan masih kosong.')

            # Mini Menu
            mini_menu()
            mini_input = ''
            while mini_input != '1' and mini_input != '2':
                mini_input = input('Silahkan ketik nomor pilihan menu yang Anda inginkan. ')
                if mini_input == '1' or mini_input == '2':
                    if mini_input == '1':
                        menu_utama()
                    elif mini_input == '2':
                        read()       
        read()
            
    elif menu_input == '2':
        # Create
        def create():
            tambah = ''

            def tambah_data():
                if tambah in data:
                    print('\nJenis barang ini sudah tersedia, apakah akan tetap disimpan?')
                    pilihan = ''
                    while pilihan != 'ya' and pilihan != 'tidak':
                        pilihan = input('(Ya/ Tidak) ').lower()
                        if pilihan == 'ya':
                            data.append(tambah)
                            print('\nBarang berhasil ditambahkan ke dalam persediaan.')
                        elif pilihan == 'tidak':
                                print('\nBarang tidak ditambahkan ke dalam persediaan.')
                else:
                    data.append(tambah)  
                    print('\nBarang berhasil ditambahkan ke dalam persediaan.')
            
            while tambah.isalpha() == False:                          
                tambah = input('Masukkan jenis barang yang akan ditambahkan ke dalam persediaan: ').lower()
                if tambah.isalpha() == True:
                    tambah_data()  
                else:
                    print('Jenis barang yang Anda masukkan salah.\n')
        
            # Mini Menu
            mini_menu()
            mini_input = ''
            while mini_input != '1' and mini_input != '2':
                mini_input = input('Silahkan ketik nomor pilihan menu yang Anda inginkan. ').lower()
                if mini_input == '1' or mini_input == '2':
                    if mini_input == '1':
                        menu_utama()
                    elif mini_input == '2':
                        create()
        create()

    elif menu_input == '3':
        # Update
        def update():
            barang = ''
            ubah = ''

            def ubah_data():
                if barang in data:
                    if barang != ubah:
                        barang_index = data.index(barang)
                        try:
                            while barang_index <= len(data):
                                data.remove(barang)
                                data.insert(barang_index, ubah)
                                barang_index = data.index(barang)
                        except:
                            print('\nData persediaan barang berhasil diperbaharui.')
                    else:
                        print('\nMasukkan jenis barang lain.')
                else: 
                    print('\n{} tidak ada dalam daftar persediaan.'.format(barang.capitalize()))

            while barang.isalpha() == False and ubah.isalpha() == False:
                barang = input('Masukkan jenis barang yang ingin diperbaharui: ').lower()
                ubah = input('Masukkan jenis barang baru: ').lower()
                if barang.isalpha() == True and ubah.isalpha() == True:
                    ubah_data()
                elif barang.isalpha() == True and ubah.isalpha() == False:
                    while ubah.isalpha() == False:
                        print('Jenis barang yang Anda masukkan salah.\n')
                        ubah = input('Masukkan jenis barang baru: ').lower()
                        if ubah.isalpha() == True:
                            ubah_data()
                elif barang.isalpha() == False and ubah.isalpha() == True:
                    while barang.isalpha() == False:
                        print('Jenis barang yang Anda masukkan salah.\n')
                        barang = input('Masukkan jenis barang yang ingin diperbaharui: ').lower()
                        if barang.isalpha() == True:
                            ubah_data()
                else:
                    print('Jenis barang yang Anda masukkan salah.\n')

            # Mini Menu
            mini_menu()
            mini_input = ''
            while mini_input != '1' and mini_input != '2':
                mini_input = input('Silahkan ketik nomor pilihan menu yang Anda inginkan. ').lower()
                if mini_input == '1' or mini_input == '2':
                    if mini_input == '1':
                        menu_utama()
                    elif mini_input == '2':
                        update()
        update()            

    elif menu_input == '4':
        # Delete
        def delete():
            hapus = ''

            def hapus_data():
                if hapus in data:
                    hapus_index = data.index(hapus)
                    try:
                        while hapus_index <= len(data):
                            data.remove(hapus)
                    except:
                        print('\nBarang berhasil dihapus dari persediaan.')
                else: 
                    print('\nMaaf, persediaan {} kami sudah habis.'.format(hapus))
        
            while hapus.isalpha() == False:
                hapus = input("Masukkan jenis barang yang akan dihapus dari persediaan: ").lower()
                if hapus.isalpha() == True:
                    hapus_data()    
                else:
                    print('Jenis barang yang Anda masukkan salah.\n')
    
            # Mini Menu
            mini_menu()
            mini_input = ''
            while mini_input != '1' and mini_input != '2':
                mini_input = input('Silahkan ketik nomor pilihan menu yang Anda inginkan. ').lower()
                if mini_input == '1' or mini_input == '2':
                    if mini_input == '1':
                        menu_utama()
                    elif mini_input == '2':
                        delete()
        delete()

    elif menu_input == '5':
        exit()
    else:
        print('\nPilihan menu tidak tersedia.')
        
while user_input != 'menu':
    user_input = input("Silahkan ketik 'menu' untuk melihat menu utama. ").lower()
    if user_input == 'menu':
        menu_utama()

#---------------------------------------------------------------------------------------------------#
