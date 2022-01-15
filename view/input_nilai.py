class data:

    # def __init__(self):
    #     self.nama

    def inputData(self):

        nama = str(input('Masukan Nama:'))
        nim = int(input('Masukan NIM:'))
        nilaiTugas = int(input('Masukan Nilai Tugas:'))
        nilaiUTS = int(input('Masukan Nilai UTS:'))
        nilaiUAS = int(input('Masukan Nilai UAS:'))
        nilaiAkhir = (nilaiTugas * 0.30) + (nilaiUAS * 0.35) + (nilaiUTS *
                                                                0.35)

        return (nama, nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir)

    def nama(self):
        nama = str(input('Masukan Nama:'))

        return nama

    def update():

        nilaiTugas = int(input('Masukan Nilai Tugas:'))
        nilaiUTS = int(input('Masukan Nilai UTS:'))
        nilaiUAS = int(input('Masukan Nilai UAS:'))
        nilaiAkhir = (nilaiTugas * 0.30) + (nilaiUAS * 0.35) + (nilaiUTS *
                                                                0.35)

        return (nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir)
