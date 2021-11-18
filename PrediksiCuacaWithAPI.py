import requests
import datetime
import time
import GetGeoLocation
import haversine as hs
import sys


# Cari Index Wilayah yang paling dekat
def getIdWilayah(location):
    # cari lat & lon lokasi yang diinput
    latitudeNow = GetGeoLocation.getLatitude(location)
    longitudeNow = GetGeoLocation.getLongtitude(location)
    # masukkan ke dalam tuple
    locNow = (latitudeNow, longitudeNow)
    distance = sys.maxsize
    # cari wilayah terdekat
    for i in range(len(x)):
        if(x[i]['lat'] == latitudeNow and x[i]['lon'] == longitudeNow):
            return i
        else:
            loc2 = (float(x[i]["lat"]), float(x[i]["lon"]))
            # lib haversine untuk menacari jarak antara dua geolocation
            distanceTemp = hs.haversine(locNow, loc2)
            if(distanceTemp < distance):
                distance = distanceTemp
                index = i

    return index


def getCuaca(idWilayah):
    tanggal = str(datetime.date.today())
    nowHour = time.strftime(("%H:%M:%S"))
    linkCuacaWilayah = f"https://ibnux.github.io/BMKG-importer/cuaca/{idWilayah}.json"
    response = requests.get(linkCuacaWilayah)
    y = response.json()
    # mengsplit tanggal & waktu
    for i in range(len(y)):
        y[i]['jamCuaca'] = y[i]['jamCuaca'].split()

    for i in range(len(y)):
        if tanggal in y[i]['jamCuaca']:
            # menampilkan prediksi cuaca untuk jam sekarang
            if y[i+1]['jamCuaca'][1] == "00:00:00":
                y[i+1]['jamCuaca'][1] = "24:00:00"
            if y[i]['jamCuaca'][1] <= nowHour <= y[i+1]['jamCuaca'][1]:
                print(f'Tanggal: {tanggal}\nJam Sekarang: {nowHour}')
                print(f'Cuaca: {y[i]["cuaca"]}')
                print(f'Temperature: {y[i]["tempC"]}')
                print(f'Kelembaban: {y[i]["humidity"]}')


# Link API
linkCuaca = "https://ibnux.github.io/BMKG-importer/cuaca/wilayah.json"
response = requests.get(linkCuaca)
x = response.json()

location = input("Masukkan Wilayah Anda: ")
try:
    idWilayah = x[getIdWilayah(location)]['id']
    # print(x[getIdWilayah(location)])
    # print(f'Kota: {x[getIdWilayah(location)]["kota"]}')
    # print(f'Kecamatan: {x[getIdWilayah(location)]["kecamatan"]}')
    getCuaca(idWilayah)

except:
    print("Wilayah anda salah")
