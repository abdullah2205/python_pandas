import pandas as pd

#nomor 1
data = pd.read_csv(r"~/Downloads/topik_khusus/tk_uts.csv", sep=";")
#nomor 2
sort = data.sort_values(by=['Nip'])
#nomor 3
sort['Rata'] = sort.apply(lambda x: (x['Nilai_Ipa'] + x['Nilai_Bahasa']) / 2, axis=1)
print(sort)
#nomor 4
update=sort.replace(to_replace={'Nilai_Ipa' : {81: 100}},value=None)
print( '\n\n==================== Ubah Nilai =====================\n', update)
#nomor 5
data2=sort[sort['Rata']>62]
print('\n\n============= Rata-rata diatas 62 ===================\n', data2)
