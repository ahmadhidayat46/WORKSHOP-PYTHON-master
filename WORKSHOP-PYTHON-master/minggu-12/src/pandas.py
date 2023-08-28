##Object creation##
# Import library yang diperlukan
import numpy as np
import pandas as pd
s = pd.Series([1, 3, 5, np.nan, 6, 8])# Membuat Pandas Series
s # Menampilkan Pandas Series

# Membuat range tanggal dengan frekuensi harian (daily) selama 6 periode, dimulai dari "2013-01-01"
dates = pd.date_range("20130101", periods=6)
# Menampilkan range tanggal yang telah dibuat
dates
# Membuat DataFrame dengan data acak dari distribusi normal (6 baris, 4 kolom)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
# Menampilkan DataFrame yang telah dibuat
df

# Membuat DataFrame dengan data yang berbeda di setiap kolom
df2 = pd.DataFrame(
    {
        "A": 1.0,  # Kolom "A" dengan nilai float 1.0
        "B": pd.Timestamp("20130102"),  # Kolom "B" dengan nilai tanggal (timestamp)
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),  # Kolom "C" dengan Series yang berisi nilai 1 (tipe data float32)
        "D": np.array([3] * 4, dtype="int32"),  # Kolom "D" dengan array numpy berisi 4 bilangan bulat 3 (tipe data int32)
        "E": pd.Categorical(["test", "train", "test", "train"]),  # Kolom "E" dengan kategori "test" dan "train" (tipe data Categorical)
        "F": "foo",  # Kolom "F" dengan nilai string "foo" untuk setiap baris
    }
)
# Menampilkan DataFrame yang telah dibuat
df2
# Menampilkan tipe data dari setiap kolom dalam DataFrame df2
df2.dtypes
# Menggunakan metode 'all()' untuk memeriksa apakah semua elemen di setiap kolom bernilai True
result = df2.all()


##Viewing data##
df.head()  #digunakan untuk melihat 5 baris pertama secara default
df.tail(3) # Menampilkan 3 baris terakhir dari DataFrame df
df.index # Menampilkan indeks dari DataFrame df
df.columns # Menampilkan nama-nama kolom dari DataFrame df
df.to_numpy() # Menampilkan array NumPy yang dihasilkan
df2.to_numpy() # Menampilkan array NumPy yang dihasilkan dalam DataFrame df2
df.describe() # Memberikan ringkasan statistik dari DataFrame df
df.T # Mengubah DataFrame df menjadi hasil transpose
df.sort_index(axis=1, ascending=False) #mengurutkan baris-baris DataFrame berdasarkan label indeks baris secara menurun.
df.sort_values(by="B") # baris-baris DataFrame akan diurutkan berdasarkan nilai pada kolom "B" secara menurun, dari nilai terbesar hingga nilai terkecil pada kolom tersebut.


##Selection##
df["A"] # Memilih kolom "A" dari DataFrame df
df[0:3] # Memilih baris dari indeks 0 hingga 2 
df["20130102":"20130104"] # Memilih baris dari tanggal "2013-01-02" hingga "2013-01-04" berdasarkan label indeks tanggal
df.loc[dates[0]]# Memilih baris berdasarkan label indeks tanggal pertama (dates[0])
df.loc[:, ["A", "B"]] # Memilih kolom "A" dan "B" dari DataFrame df
df.loc["20130102":"20130104", ["A", "B"]] # Memilih baris dari tanggal "2013-01-02" hingga "2013-01-04" dan kolom "A" dan "B"
df.loc["20130102", ["A", "B"]] # Memilih baris dengan label indeks tanggal "2013-01-02" dan kolom "A" dan "B"
df.loc[dates[0], "A"] # Memilih nilai dari kolom "A" pada baris dengan label indeks tanggal pertama (dates[0])
df.at[dates[0], "A"] # Memilih  nilai tunggal dari kolom "A" pada baris dengan label indeks tanggal pertama (dates[0])
df.iloc[3] # Memilih baris dengan indeks numerik 3 dari DataFrame df
df.iloc[3:5, 0:2] # Memilih dua baris dan dua kolom dari DataFrame df menggunakan indeks numerik
df.iloc[[1, 2, 4], [0, 2]] #Memilih baris dengan indeks numerik 1, 2, dan 4, serta kolom dengan indeks numerik 0 dan 2 dari DataFrame df.
df.iloc[1:3, :] #Memilih baris dengan indeks numerik 1 dan 2, serta semua kolom dari DataFrame df.
df.iloc[:, 1:3] #Memilih semua baris dan kolom dengan indeks numerik 1 dan 2 dari DataFrame df.
df.iloc[1, 1] # Memilih nilai dari baris dengan indeks numerik 1 dan kolom dengan indeks numerik 1.
df.iat[1, 1] # Memilih nilai dari baris dengan indeks numerik 1 dan kolom dengan indeks numerik 1 (alternatif untuk memilih nilai tunggal).
df[df["A"] > 0] #  Memilih baris-baris dari DataFrame df di mana nilai kolom "A" lebih besar dari 0.
df[df > 0] # Memilih seluruh DataFrame df di mana nilai-nilai yang lebih besar dari 0. Nilai-nilai negatif dan nilai NaN akan menjadi bagian dari hasil ini.
df2 = df.copy() #Menduplikasi DataFrame df menjadi DataFrame df2.
df2["E"] = ["one", "one", "two", "three", "four", "three"]
df2
df2[df2["E"].isin(["two", "four"])] # Memilih baris-baris dari DataFrame df2 di mana nilai kolom "E" adalah "two" atau "four".
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6)) # Membuat objek Pandas Series s1 dengan nilai dan indeks tertentu.
s1
df["F"] = s1 #Menambahkan kolom "F" ke DataFrame df dengan menggunakan nilai dari Pandas Series s1.
df.at[dates[0], "A"] = 0 # Mengubah nilai di baris dengan label indeks tanggal pertama pada kolom "A" menjadi 0.
df.iat[0, 1] = 0 #Mengubah nilai di baris dengan indeks numerik 0 pada kolom dengan indeks numerik 1 menjadi 0.
df.loc[:, "D"] = np.array([5] * len(df)) #Mengubah seluruh nilai kolom "D" dalam DataFrame df menjadi 5.
df
df2 = df.copy()
df2[df2 > 0] = -df2 #Mengganti semua nilai positif dalam DataFrame df2 menjadi negatif (diubah menjadi negatif nilainya).
df2



##Missing data##
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])#Membuat DataFrame baru df1 berdasarkan DataFrame df (empat tanggal pertama) dan kolom yang ditambahkan dengan kolom "E".
df1.loc[dates[0] : dates[1], "E"] = 1
df1

df1.dropna(how="any") # Menghapus baris-baris yang memiliki nilai yang hilang (NaN) dalam DataFrame df1. how="any"
df1.fillna(value=5) # Mengisi nilai-nilai yang hilang (NaN) dalam DataFrame df1 dengan nilai 5.
pd.isna(df1) #Membuat DataFrame baru dengan ukuran yang sama dengan df1.


##Operations##
df.mean() # Menghitung nilai rata-rata dari setiap kolom dalam DataFrame df
df.mean(1) # Menghitung nilai rata-rata dari setiap baris dalam DataFrame df

# Membuat objek Pandas Series dengan nilai-nilai dan indeks tertentu, lalu melakukan shift(2)
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
s

df.sub(s, axis="index")# Pengurangan antara DataFrame df dengan Series s berdasarkan indeks (axis="index")
df.apply(np.cumsum) # Menghitung kumulatif penjumlahan untuk setiap kolom dalam DataFrame df
df.apply(lambda x: x.max() - x.min())# Menghitung selisih nilai maksimum dan minimum untuk setiap kolom dalam DataFrame df

# Menghasilkan 10 bilangan bulat acak dari 0 hingga 6 dan mengubahnya menjadi Pandas Series
s = pd.Series(np.random.randint(0, 7, size=10))
s

s.value_counts()# Menghitung jumlah kemunculan setiap nilai unik dalam Series s

# Mengonversi setiap elemen string dalam Series s menjadi huruf kecil (lowercase)
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
s.str.lower()