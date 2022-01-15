from view.input_nilai import data
from view.view_nilai import tampilkan

# update = data.update()
datas = [{'nama': 'No Data Found!'}]


class method:

    def tambah(self):
        if datas[0]['nama'] == 'No Data Found!':
            del datas[0]
        input = data.inputData(self)
        dataAppend = {
            'nama': input[0],
            'nim': input[1],
            'nTugas': input[2],
            'nUTS': input[3],
            'nUAS': input[4],
            'nAkhir': input[5]
        }
        datas.append(dataAppend)
        print('Data Telah Terinput')

        #Log
        # print(datas)

    def update(self):

        for i in range(0, len(datas)):
            nama = data.nama(self)
            if datas[i]['nama'] == nama:
                update = data.update()
                print(update[0])
                datas[i]['nTugas'] = update[0]
                datas[i]['nUTS'] = update[1]
                datas[i]['nUAS'] = update[2]
                datas[i]['nAkhir'] = update[3]
                # print(datas)
                print('Data Telah Terupdate')
            else:
                print("DATA TIDAK DI TEMUKAN!")

    def hapus(self):

        for i in range(0, len(datas)):
            nama = data.nama(self)

            if datas[i]['nama'] == nama:
                del datas[i]['nama']
                del datas[i]['nim']
                del datas[i]['nTugas']
                del datas[i]['nUTS']
                del datas[i]['nUAS']
                del datas[i]['nAkhir']
                print('Data Telah Dihapus')
                # datas[0] = {'nama': 'No Data Found!'}
                # print(datas)

    def cari():
        tampilkan.search('self', datas)

    def show():
        tampilkan.show('self', datas)
