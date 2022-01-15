from tabulate import tabulate
from view.input_nilai import data
from model import daftar_nilai


class tampilkan:

    def menu():
        print('-' * 80, '\n')
        method = daftar_nilai.method

        start = True

        print('Program Data Sederhana'.center(80, ' '))

        while (start):
            print(
                '(T) Tambah Data, (U) Ubah Data, (H) Hapus Data, (S) Tampilkan Data, (F) Cari Data, (E) Exit Program'
            )

            inputUser = str(input('Pilih Menu: '))
            inputs = inputUser.lower()

            if inputs == 't':
                method.tambah('str')

            elif inputs == 'u':
                method.update('str')

            elif inputs == 'h':
                method.hapus('str')

            elif inputs == 's':
                method.show()

            elif inputs == 'f':
                method.cari()

            elif inputs == 'e':
                print("Program dihentikan")
                start = False

            else:
                print('Input Salah!')

    def search(self, datas):
        for i in range(0, len(datas)):
            nama = data.nama(self)

            if datas[i]['nama'] == nama:
                rows = [x.values() for x in datas]
                headers = [
                    'Nama', 'NIM', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS',
                    'Nilai Akhir'
                ]
                print(
                    tabulate(rows,
                             headers=headers,
                             tablefmt='fancy_grid',
                             stralign='center'))

            else:
                print(
                    tabulate('DATA TIDAK DITEMUKAN',
                             tablefmt='fancy_grid',
                             stralign='center'))

    def show(self, datas):

        if datas[0]['nama'] == 'No Data Found!':
            print(tabulate([datas], tablefmt='fancy_grid', stralign='center'))
        else:
            rows = [x.values() for x in datas]
            headers = [
                'Nama', 'NIK', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS',
                'Nilai Akhir'
            ]
            print(
                tabulate(rows,
                         headers=headers,
                         tablefmt='fancy_grid',
                         stralign='center'))
